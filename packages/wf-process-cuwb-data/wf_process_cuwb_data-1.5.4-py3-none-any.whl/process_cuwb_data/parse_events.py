import honeycomb_io
import cv_utils
import pandas as pd
import numpy as np
import datetime
import uuid
import functools

from process_cuwb_data.utils.log import logger


def parse_tray_events(
    tray_events,
    environment_id=None,
    environment_name=None,
    camera_device_ids=None,
    camera_names=None,
    default_camera_device_id=None,
    default_camera_name=None,
    camera_calibrations=None,
    position_window_seconds=4,
    imputed_z_position=1.0,
    time_zone='US/Central',
    lead_in_seconds=3,
    scheme='https',
    netloc='honeycomb-ground-truth.api.wildflower-tech.org',
    endpoint='classrooms',
    chunk_size=100,
    client=None,
    uri=None,
    token_uri=None,
    audience=None,
    client_id=None,
    client_secret=None
):
    if environment_id is None and environment_name is None:
        raise ValueError('Must specify either environment ID or environment name')
    camera_info = honeycomb_io.fetch_devices(
        device_types=honeycomb_io.DEFAULT_CAMERA_DEVICE_TYPES,
        device_ids=camera_device_ids,
        names=camera_names,
        environment_id=environment_id,
        environment_name=environment_name,
        start=tray_events['start'].min(),
        end=tray_events['end'].max(),
        output_format='dataframe',
        chunk_size=chunk_size,
        client=client,
        uri=uri,
        token_uri=token_uri,
        audience=audience,
        client_id=client_id,
        client_secret=client_secret
    )
    camera_dict = camera_info['device_name'].to_dict()
    camera_device_ids = list(camera_dict.keys())
    if camera_calibrations is None:
        camera_calibrations = honeycomb_io.fetch_camera_calibrations(
            camera_ids=camera_device_ids,
            start=tray_events['start'].min(),
            end=tray_events['end'].max(),
            chunk_size=chunk_size,
            client=client,
            uri=uri,
            token_uri=token_uri,
            audience=audience,
            client_id=client_id,
            client_secret=client_secret
        )
    if default_camera_device_id is None:
        if default_camera_name is None:
            raise ValueError('Must specify default camera device ID or name')
        default_cameras = camera_info.loc[camera_info['device_name'] == default_camera_name]
        if len(default_cameras) == 0:
            raise ValueError('Default camera name {} not found'.format(
                default_camera_name
            ))
        if len(default_cameras) > 1:
            raise ValueError('More than one camera with default camera name {} found'.format(
                default_camera_name
            ))
        default_camera_device_id = default_cameras.index[0]
    person_ids = tray_events['person_id'].dropna().unique().tolist()
    person_info = honeycomb_io.fetch_persons(
        person_ids=person_ids,
        output_format='dataframe',
        chunk_size=chunk_size,
        client=client,
        uri=uri,
        token_uri=token_uri,
        audience=audience,
        client_id=client_id,
        client_secret=client_secret
    )
    person_info = (
        person_info
        .rename(columns={
            column_name: (
                ('person_' + column_name) if not column_name.startswith('person_')
                else column_name
            )
            for column_name in person_info.columns
        })
        .astype('object')
    )
    person_info = person_info.where(pd.notnull(person_info), None)
    tray_events = tray_events.copy()
    tray_events['id'] = [str(uuid.uuid4()) for _ in range(len(tray_events))]
    tray_events['date'] = tray_events['start'].dt.tz_convert(time_zone).apply(lambda x: x.date())
    tray_events['timestamp'] = tray_events['start']
    tray_events = (
        tray_events
        .drop(columns=person_info.columns, errors='ignore')
        .join(
            person_info,
            how='left',
            on='person_id'
        )
    )
    best_camera_partial = functools.partial(
        best_camera,
        default_camera_device_id=default_camera_device_id,
        environment_id=environment_id,
        environment_name=environment_name,
        camera_device_ids=camera_device_ids,
        camera_calibrations=camera_calibrations,
        position_window_seconds=position_window_seconds,
        imputed_z_position=imputed_z_position,
        chunk_size=chunk_size,
        client=client,
        uri=uri,
        token_uri=token_uri,
        audience=audience,
        client_id=client_id,
        client_secret=client_secret

    )
    tray_events['best_camera_device_id'] = tray_events.apply(
        lambda event: best_camera_partial(
            timestamp=event['start'],
            tray_device_id=event['tray_device_id'],
        ),
        axis=1
    )
    tray_events['best_camera_name'] = tray_events['best_camera_device_id'].apply(
        lambda camera_device_id: camera_dict.get(camera_device_id)
    )
    tray_events['duration_seconds'] = (tray_events['end'] - tray_events['start']).dt.total_seconds()
    tray_events['description'] = tray_events.apply(
        lambda event: describe_tray_event(
            timestamp=event['timestamp'],
            material_name=event['material_name'],
            start=event['start'],
            end=event['end'],
            person_name=event['person_name'],
            duration_seconds=event['duration_seconds'],
            interaction_type=event['interaction_type'],
            time_zone=time_zone
        ),
        axis=1
    )
    tray_events['anonymized_description'] = tray_events.apply(
        lambda event: describe_tray_event(
            timestamp=event['timestamp'],
            material_name=event['material_name'],
            start=event['start'],
            end=event['end'],
            person_name=event['person_anonymized_name'],
            duration_seconds=event['duration_seconds'],
            interaction_type=event['interaction_type'],
            time_zone=time_zone
        ),
        axis=1
    )
    tray_events = tray_events.reindex(columns=[
        'id',
        'date',
        'timestamp',
        'interaction_type',
        'tray_device_id',
        'material_id',
        'material_name',
        'duration_seconds',
        'person_device_id',
        'person_id',
        'person_type',
        'person_name',
        'person_first_name',
        'person_last_name',
        'person_nickname',
        'person_short_name',
        'person_anonymized_name',
        'person_anonymized_first_name',
        'person_anonymized_last_name',
        'person_anonymized_nickname',
        'person_anonymized_short_name',
        'person_transparent_classroom_id',
        'start',
        'end',
        'best_camera_device_id',
        'best_camera_name',
        'description',
        'anonymized_description'
    ])
    tray_events.sort_values('timestamp', inplace=True)
    return tray_events


def describe_tray_event(
    timestamp,
    material_name,
    start,
    end,
    person_name,
    duration_seconds,
    interaction_type,
    time_zone
):
    time_string = timestamp.tz_convert(time_zone).strftime('%I:%M %p')
    person_string = person_name if pd.notnull(person_name) else 'An unknown person'
    if interaction_type == 'CARRYING_FROM_SHELF':
        description_text = '{} took the {} tray from shelf'.format(
            person_string,
            material_name
        )
    elif interaction_type == 'CARRYING_TO_SHELF':
        description_text = '{} put the {} tray back on the shelf'.format(
            person_string,
            material_name
        )
    elif interaction_type == 'CARRYING_BETWEEN_NON_SHELF_LOCATIONS':
        description_text = '{} moved the {} tray'.format(
            person_string,
            material_name
        )
    elif interaction_type == 'CARRYING_FROM_AND_TO_SHELF':
        description_text = '{} took the {} tray from the shelf and immediately put it back'.format(
            person_string,
            material_name
        )
    else:
        raise ValueError('Unexpected interaction type: \'{}\''.format(
            interaction_type
        ))
        raise ValueError('Unexpected state: both start and end of material event are null')
    description = '{}: {}'.format(
        time_string,
        description_text
    )
    return description


def generate_material_events(
    parsed_tray_events,
    environment_id,
    time_zone='US/Central',
    lead_in_seconds=3,
    scheme='https',
    netloc='honeycomb-ground-truth.api.wildflower-tech.org',
    endpoint='classrooms',
):
    parsed_tray_events = parsed_tray_events.copy()
    material_events_list = list()
    for (date, tray_device_id), parsed_tray_events_date_tray in parsed_tray_events.groupby(['date', 'tray_device_id']):
        material_events_list.extend(generate_material_events_date_tray(parsed_tray_events_date_tray))
    material_events = pd.DataFrame(material_events_list)
    material_events['id'] = [str(uuid.uuid4()) for _ in range(len(material_events))]
    material_events['timestamp'] = material_events.apply(
        lambda row: row['start'] if pd.notnull(row['start']) else row['end'],
        axis=1
    )
    material_events['duration_seconds'] = (material_events['end'] - material_events['start']).dt.total_seconds()
    material_events['description'] = material_events.apply(
        lambda event: describe_material_event(
            timestamp=event['timestamp'],
            material_name=event['material_name'],
            start=event['start'],
            person_name_from_shelf=event['person_name_from_shelf'],
            end=event['end'],
            person_name_to_shelf=event['person_name_to_shelf'],
            duration_seconds=event['duration_seconds'],
            time_zone=time_zone
        ),
        axis=1
    )
    material_events['anonymized_description'] = material_events.apply(
        lambda event: describe_material_event(
            timestamp=event['timestamp'],
            material_name=event['material_name'],
            start=event['start'],
            person_name_from_shelf=event['person_anonymized_name_from_shelf'],
            end=event['end'],
            person_name_to_shelf=event['person_anonymized_name_to_shelf'],
            duration_seconds=event['duration_seconds'],
            time_zone=time_zone
        ),
        axis=1
    )
    material_events = material_events.reindex(columns=[
        'id',
        'date',
        'timestamp',
        'tray_device_id',
        'material_id',
        'material_name',
        'duration_seconds',
        'start',
        'id_from_shelf',
        'person_device_id_from_shelf',
        'person_id_from_shelf',
        'person_name_from_shelf',
        'person_anonymized_name_from_shelf',
        'person_type_from_shelf',
        'best_camera_device_id_from_shelf',
        'best_camera_name_from_shelf',
        'end',
        'id_to_shelf',
        'person_device_id_to_shelf',
        'person_id_to_shelf',
        'person_name_to_shelf',
        'person_anonymized_name_to_shelf',
        'person_type_to_shelf',
        'best_camera_device_id_to_shelf',
        'best_camera_name_to_shelf',
        'description',
        'anonymized_description'
    ])
    material_events.sort_values('timestamp', inplace=True)
    return material_events


def generate_material_events_date_tray(parsed_tray_events_date_tray):
    parsed_tray_events_date_tray_filtered = (
        parsed_tray_events_date_tray
        .loc[parsed_tray_events_date_tray['interaction_type'].isin(['CARRYING_FROM_SHELF', 'CARRYING_TO_SHELF'])]
        .sort_values('start')
    )
    in_use = False
    material_events_list = list()
    for index, event in parsed_tray_events_date_tray_filtered.iterrows():
        interaction_type = event['interaction_type']
        if interaction_type == 'CARRYING_FROM_SHELF':
            material_events_list.append({
                'date': event['date'],
                'tray_device_id': event['tray_device_id'],
                'material_id': event['material_id'],
                'material_name': event['material_name'],
                'start': event['start'],
                'id_from_shelf': event['id'],
                'person_device_id_from_shelf': event['person_device_id'],
                'person_id_from_shelf': event['person_id'],
                'person_name_from_shelf': event['person_name'],
                'person_anonymized_name_from_shelf': event['person_anonymized_name'],
                'person_type_from_shelf': event['person_type'],
                'best_camera_device_id_from_shelf': event['best_camera_device_id'],
                'best_camera_name_from_shelf': event['best_camera_name'],
                'end': None,
                'person_device_id_to_shelf': None,
                'person_id_to_shelf': None,
                'person_name_to_shelf': None,
                'person_anonymized_name_to_shelf': None,
                'best_camera_device_id_to_shelf': None,
                'best_camera_name_to_shelf': None
            })
            in_use = True
        elif interaction_type == 'CARRYING_TO_SHELF' and in_use:
            material_events_list[-1]['end'] = event['end']
            material_events_list[-1]['id_to_shelf'] = event['id']
            material_events_list[-1]['person_device_id_to_shelf'] = event['person_device_id']
            material_events_list[-1]['person_id_to_shelf'] = event['person_id']
            material_events_list[-1]['person_name_to_shelf'] = event['person_name']
            material_events_list[-1]['person_anonymized_name_to_shelf'] = event['person_anonymized_name']
            material_events_list[-1]['person_type_to_shelf'] = event['person_type']
            material_events_list[-1]['best_camera_device_id_to_shelf'] = event['best_camera_device_id']
            material_events_list[-1]['best_camera_name_to_shelf'] = event['best_camera_name']
            in_use = False
        elif interaction_type == 'CARRYING_TO_SHELF' and not in_use:
            material_events_list.append({
                'date': event['date'],
                'tray_device_id': event['tray_device_id'],
                'material_id': event['material_id'],
                'material_name': event['material_name'],
                'start': None,
                'person_device_id_from_shelf': None,
                'person_id_from_shelf': None,
                'person_name_from_shelf': None,
                'person_anonymized_name_from_shelf': None,
                'person_type_from_shelf': None,
                'best_camera_device_id_from_shelf': None,
                'best_camera_name_from_shelf': None,
                'end': event['end'],
                'id_to_shelf': event['id'],
                'person_device_id_to_shelf': event['person_device_id'],
                'person_id_to_shelf': event['person_id'],
                'person_name_to_shelf': event['person_name'],
                'person_anonymized_name_to_shelf': event['person_anonymized_name'],
                'person_type_to_shelf': event['person_type'],
                'best_camera_device_id_to_shelf': event['best_camera_device_id'],
                'best_camera_name_to_shelf': event['best_camera_name']
            })
            in_use = False
        else:
            raise ValueError('Encountered unexpected state: interaction type is \'{}\' and in_use is {}'.format(
                interaction_type,
                in_use
            ))
    return material_events_list


def describe_material_event(
    timestamp,
    material_name,
    start,
    person_name_from_shelf,
    end,
    person_name_to_shelf,
    duration_seconds,
    time_zone
):
    time_string = timestamp.tz_convert(time_zone).strftime('%I:%M %p')
    from_shelf_person_string = person_name_from_shelf if pd.notnull(person_name_from_shelf) else 'An unknown person'
    to_shelf_person_string = person_name_to_shelf if pd.notnull(person_name_to_shelf) else 'an unknown person'
    if pd.notnull(start) and pd.notnull(end):
        if duration_seconds > 90:
            duration_string = '{} minutes'.format(round(duration_seconds / 60))
        elif duration_seconds > 30:
            duration_string = '1 minute'
        else:
            duration_string = '{} seconds'.format(round(duration_seconds))
        if person_name_from_shelf == person_name_to_shelf:
            description_text = '{} took {} from shelf and put it back {} later'.format(
                from_shelf_person_string,
                material_name,
                duration_string
            )
        else:
            description_text = '{} took {} from shelf and {} put it back {} later'.format(
                from_shelf_person_string,
                material_name,
                to_shelf_person_string,
                duration_string
            )
    elif pd.notnull(start):
        description_text = '{} took {} from shelf but never put it back'.format(
            from_shelf_person_string,
            material_name
        )
    elif pd.notnull(end):
        if to_shelf_person_string == 'an unknown person':
            to_shelf_person_string = to_shelf_person_string.capitalize()
        description_text = '{} put {} back on shelf but it wasn\'t taken out previously'.format(
            to_shelf_person_string,
            material_name
        )
    else:
        raise ValueError('Unexpected state: both start and end of material event are null')
    description = '{}: {}'.format(
        time_string,
        description_text
    )
    return description


def best_camera(
    timestamp,
    tray_device_id,
    default_camera_device_id,
    environment_id=None,
    environment_name=None,
    camera_device_ids=None,
    camera_calibrations=None,
    position_window_seconds=4,
    imputed_z_position=1.0,
    chunk_size=100,
    client=None,
    uri=None,
    token_uri=None,
    audience=None,
    client_id=None,
    client_secret=None
):
    if camera_calibrations is None:
        if environment_id is None and environment_name is None and camera_device_ids is None:
            raise ValueError(
                'If camera calibration info is not specified, must specify either camera device IDs or environment ID or environment name')
        if camera_device_ids is None:
            camera_info = honeycomb_io.fetch_devices(
                device_types=honeycomb_io.DEFAULT_CAMERA_DEVICE_TYPES,
                environment_id=environment_id,
                environment_name=environment_name,
                start=timestamp,
                end=timestamp,
                output_format='dataframe',
                chunk_size=chunk_size,
                client=client,
                uri=uri,
                token_uri=token_uri,
                audience=audience,
                client_id=client_id,
                client_secret=client_secret
            )
            camera_device_ids = camera_info.index.unique().tolist()
        camera_calibrations = honeycomb_io.fetch_camera_calibrations(
            camera_ids=camera_device_ids,
            start=timestamp,
            end=timestamp,
            chunk_size=chunk_size,
            client=client,
            uri=uri,
            token_uri=token_uri,
            audience=audience,
            client_id=client_id,
            client_secret=client_secret
        )
    position_window_start = timestamp - datetime.timedelta(seconds=position_window_seconds / 2)
    position_window_end = timestamp + datetime.timedelta(seconds=position_window_seconds / 2)
    position_data = honeycomb_io.fetch_cuwb_position_data(
        start=position_window_start,
        end=position_window_end,
        device_ids=[tray_device_id],
        environment_id=None,
        environment_name=None,
        device_types=['UWBTAG'],
        output_format='dataframe',
        sort_arguments=None,
        chunk_size=1000,
        client=client,
        uri=uri,
        token_uri=token_uri,
        audience=audience,
        client_id=client_id,
        client_secret=client_secret
    )
    position = np.nanmedian(position_data.loc[:, ['x', 'y', 'z']].values, axis=0)
    if imputed_z_position is not None:
        position[2] = imputed_z_position
    view_data_list = list()
    for camera_device_id, camera_calibration in camera_calibrations.items():
        camera_position = cv_utils.extract_camera_position(
            rotation_vector=camera_calibration['rotation_vector'],
            translation_vector=camera_calibration['translation_vector']
        )
        distance_from_camera = np.linalg.norm(np.subtract(
            position,
            camera_position
        ))
        image_position = cv_utils.project_points(
            object_points=position,
            rotation_vector=camera_calibration['rotation_vector'],
            translation_vector=camera_calibration['translation_vector'],
            camera_matrix=camera_calibration['camera_matrix'],
            distortion_coefficients=camera_calibration['distortion_coefficients'],
            remove_behind_camera=True,
            remove_outside_frame=True,
            image_corners=np.asarray([
                [0.0, 0.0],
                [camera_calibration['image_width'], camera_calibration['image_height']]
            ])
        )
        image_position = np.squeeze(image_position)
        if np.all(np.isfinite(image_position)):
            in_frame = True
            distance_from_image_center = np.linalg.norm(np.subtract(
                image_position,
                [camera_calibration['image_width'] / 2, camera_calibration['image_height'] / 2]
            ))
            in_middle = (
                image_position[0] > camera_calibration['image_width'] * (1.0 / 10.0) and
                image_position[0] < camera_calibration['image_width'] * (9.0 / 10.0) and
                image_position[1] > camera_calibration['image_height'] * (1.0 / 10.0) and
                image_position[1] < camera_calibration['image_height'] * (9.0 / 10.0)
            )
        else:
            in_frame = False
            distance_from_image_center = None
            in_middle = False
        view_data_list.append({
            'camera_device_id': camera_device_id,
            'position': position,
            'distance_from_camera': distance_from_camera,
            'image_position': image_position,
            'distance_from_image_center': distance_from_image_center,
            'in_frame': in_frame,
            'in_middle': in_middle,
        })
    view_data = pd.DataFrame(view_data_list).set_index('camera_device_id')
    if not view_data['in_frame'].any():
        best_camera_device_id = default_camera_device_id
    elif not view_data['in_middle'].any():
        best_camera_device_id = view_data.sort_values('distance_from_image_center').index[0]
    else:
        best_camera_device_id = view_data.loc[view_data['in_middle']].sort_values('distance_from_camera').index[0]
    return best_camera_device_id
