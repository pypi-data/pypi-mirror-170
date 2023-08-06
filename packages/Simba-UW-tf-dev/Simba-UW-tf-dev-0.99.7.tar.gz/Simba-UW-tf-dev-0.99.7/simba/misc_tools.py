__author__ = "Simon Nilsson", "JJ Choong"

import configparser

from simba.drop_bp_cords import get_fn_ext, get_workflow_file_format
from simba.rw_dfs import read_df, save_df
import cv2
from pylab import *
import os, glob
from copy import deepcopy
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from scipy.signal import savgol_filter
from PIL import Image
from pathlib import Path
import io
import PIL
import imutils
from numba import jit
from configparser import ConfigParser, MissingSectionHeaderError
import multiprocessing
from simba.read_config_unit_tests import (check_file_exist_and_readable,
                                          read_config_entry,
                                          check_int)
import shutil
import platform
import pickle
import subprocess
from datetime import datetime
import simba

def get_video_meta_data(video_path: str):
    """
    Helper to read video meta data (fps, resolution, frame cnt etc.) from video file.

    Parameters
    ----------
    video_path: str
        Path to video file.

    Returns
    -------
    vdata: dict
        Python dictionary holding video meta data

    Notes
    ----------

    Examples
    >>>  get_video_meta_data('tests/test_data/mouse_open_field/project_folder/videos/SI_DAY3_308_CD1_PRESENT.mp4')
    {'video_name': 'SI_DAY3_308_CD1_PRESENT', 'fps': 15, 'width': 1500, 'height': 1350, 'frame_count': 900, 'resolution_str': '1500 x 1350'}

    """

    video_data = {}
    cap = cv2.VideoCapture(video_path)
    _, video_data['video_name'], _ = get_fn_ext(video_path)
    video_data['fps'] = int(cap.get(cv2.CAP_PROP_FPS))
    video_data['width'] = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_data['height'] = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_data['frame_count'] = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    video_data['video_length_s'] = int(video_data['frame_count'] / video_data['fps'])
    for k, v in video_data.items():
        if v == 0:
            print('SIMBA WARNING: Video {} has {} of {}.'.format(video_data['video_name'], k, str(v)))
            raise ValueError('SIMBA WARNING: Video {} has {} of {}.'.format(video_data['video_name'], k, str(v)))
    video_data['resolution_str'] = str('{} x {}'.format(video_data['width'], video_data['height']))

    return video_data

def check_directionality_viable(animal_bp_dict: dict):
    """
    Helper to check if its possible to calculate ``directionality`` statistics (i.e., nose, and ear coordinates from
    pose estimation has to be present)

    Parameters
    ----------
    animal_bp_dict: dict
        Animal body-part dictionary created by :meth:`~simba.drop_bp_cords.create_body_part_dictionary`

    Returns
    -------
    directionalitySetting: bool
    NoseCoords: list
    EarLeftCoords: list
    EarRightCoords: list
    """
    directionalitySetting = True
    NoseCoords = []
    EarLeftCoords = []
    EarRightCoords = []
    for animal in animal_bp_dict:
        for bp_cord in ['X_bps', 'Y_bps']:
            bp_list = animal_bp_dict[animal][bp_cord]
            for bp_name in bp_list:
                bp_name_components = bp_name.split('_')
                bp_name_components = [x.lower() for x in bp_name_components]
                if ('nose' in bp_name_components):
                    NoseCoords.append(bp_name)
                if ('ear' in bp_name_components) and ('left' in bp_name_components):
                    EarLeftCoords.append(bp_name)
                if ('ear' in bp_name_components) and ('right' in bp_name_components):
                    EarRightCoords.append(bp_name)

    for cord in [NoseCoords, EarLeftCoords, EarRightCoords]:
        if len(cord) != len(animal_bp_dict.keys()) * 2:
            directionalitySetting = False

    if directionalitySetting:
        NoseCoords = [NoseCoords[i * 2:(i + 1) * 2] for i in range((len(NoseCoords) + 2 - 1) // 2)]
        EarLeftCoords = [EarLeftCoords[i * 2:(i + 1) * 2] for i in range((len(EarLeftCoords) + 2 - 1) // 2)]
        EarRightCoords = [EarRightCoords[i * 2:(i + 1) * 2] for i in range((len(EarRightCoords) + 2 - 1) // 2)]

    return directionalitySetting, NoseCoords, EarLeftCoords, EarRightCoords


def check_multi_animal_status(config: configparser.ConfigParser,
                              no_animals: int):
    """
    Helper to check if the project is a multi-animal SimBA project.

    Parameters
    ----------
    config: configparser.ConfigParser
        Parsed SimBA project_config.ini file.
    no_animals: int
        Number of animals in the SimBA project

    Returns
    -------
    multi_animal_status: bool
    multi_animal_id_lst: list
    """
    multi_animal_id_lst = []
    if not config.has_section('Multi animal IDs'):
        for animal in range(no_animals):
            multi_animal_id_lst.append('Animal_' + str(animal + 1))
        multi_animal_status = False

    else:
        multi_animal_id_str = read_config_entry(config=config, section='Multi animal IDs',option='id_list',data_type='str')
        multi_animal_id_lst = [x.lstrip() for x in multi_animal_id_str.split(",")]
        multi_animal_id_lst = [x for x in multi_animal_id_lst if x != 'None']
        if (no_animals > 1) and (len(multi_animal_id_lst) > 1):
            multi_animal_status = True
        else:
            for animal in range(no_animals):
                multi_animal_id_lst.append('Animal_{}'.format(str(animal + 1)))
            multi_animal_status = False

    return multi_animal_status, multi_animal_id_lst


def line_length(p: list,
                q: list,
                n: list,
                M: list,
                coord: list):
    """
    Helper to calculate if an animal is directing towards a coordinate.

    Parameters
    ----------
    p: list
        left ear coordinates of observing animal.
    q: list
        right ear coordinates of observing animal.
    n: list
        nose coordinates of observing animal.
    M: list
        The location of the target coordinates.
    coord: list
        empty list to store the eye coordinate of the observing animal.

    Returns
    -------
    bool
    coord: list
    """

    Px = np.abs(p[0] - M[0])
    Py = np.abs(p[1] - M[1])
    Qx = np.abs(q[0] - M[0])
    Qy = np.abs(q[1] - M[1])
    Nx = np.abs(n[0] - M[0])
    Ny = np.abs(n[1] - M[1])
    Ph = np.sqrt(Px*Px + Py*Py)
    Qh = np.sqrt(Qx*Qx + Qy*Qy)
    Nh = np.sqrt(Nx*Nx + Ny*Ny)
    if (Nh < Ph and Nh < Qh and Qh < Ph):
        coord.extend((q[0], q[1]))
        return True, coord
    elif (Nh < Ph and Nh < Qh and Ph < Qh):
        coord.extend((p[0], p[1]))
        return True, coord
    else:
        return False, coord

@jit(nopython=True)
def line_length_numba(left_ear_array: np.array,
                      right_ear_array: np.array,
                      nose_array: np.array,
                      target_array: np.array):
    """
    Jitted helper to calculate if an animal is directing towards another animals body-part coordinate.

    Parameters
    ----------
    left_ear_array: np.array
        left ear coordinates of observing animal.
    right_ear_array: np.array
        right ear coordinates of observing animal.
    nose_array: np.array
        nose coordinates of observing animal.
    target_array: np.array
        The location of the target coordinates.

    Returns
    -------
    results_array: np.array
    """

    results_array = np.zeros((left_ear_array.shape[0], 4))
    for frame_no in range(results_array.shape[0]):
        Px = np.abs(left_ear_array[frame_no][0] - target_array[frame_no][0])
        Py = np.abs(left_ear_array[frame_no][1] - target_array[frame_no][1])
        Qx = np.abs(right_ear_array[frame_no][0] - target_array[frame_no][0])
        Qy = np.abs(right_ear_array[frame_no][1] - target_array[frame_no][1])
        Nx = np.abs(nose_array[frame_no][0] - target_array[frame_no][0])
        Ny = np.abs(nose_array[frame_no][1] - target_array[frame_no][1])
        Ph = np.sqrt(Px * Px + Py * Py)
        Qh = np.sqrt(Qx * Qx + Qy * Qy)
        Nh = np.sqrt(Nx * Nx + Ny * Ny)
        if (Nh < Ph and Nh < Qh and Qh < Ph):
            results_array[frame_no] = [0, right_ear_array[frame_no][0], right_ear_array[frame_no][1], True]
        elif (Nh < Ph and Nh < Qh and Ph < Qh):
            results_array[frame_no] = [1, left_ear_array[frame_no][0],  left_ear_array[frame_no][1], True]
        else:
            results_array[frame_no] = [2, -1, -1, False]
    return results_array


@jit(nopython=True)
def line_length_numba_to_static_location(left_ear_array: np.array,
                                         right_ear_array: np.array,
                                         nose_array: np.array,
                                         target_array: np.array):
    """
    Jitted helper to calculate if an animal is directing towards a static coordinate
    (e.g., the center of a user-defined ROI)

    Parameters
    ----------
    left_ear_array: np.array
        left ear coordinates of observing animal.
    right_ear_array: np.array
        right ear coordinates of observing animal.
    nose_array: np.array
        nose coordinates of observing animal.
    target_array: np.array
        The location of the target coordinates.

    Returns
    -------
    results_array: np.array
    """

    results_array =  np.zeros((left_ear_array.shape[0], 4))
    for frame_no in range(results_array.shape[0]):
        Px = np.abs(left_ear_array[frame_no][0] - target_array[0])
        Py = np.abs(left_ear_array[frame_no][1] - target_array[1])
        Qx = np.abs(right_ear_array[frame_no][0] - target_array[0])
        Qy = np.abs(right_ear_array[frame_no][1] - target_array[1])
        Nx = np.abs(nose_array[frame_no][0] - target_array[0])
        Ny = np.abs(nose_array[frame_no][1] - target_array[1])
        Ph = np.sqrt(Px * Px + Py * Py)
        Qh = np.sqrt(Qx * Qx + Qy * Qy)
        Nh = np.sqrt(Nx * Nx + Ny * Ny)
        if (Nh < Ph and Nh < Qh and Qh < Ph):
            results_array[frame_no] = [0, right_ear_array[frame_no][0], right_ear_array[frame_no][1], True]
        elif (Nh < Ph and Nh < Qh and Ph < Qh):
            results_array[frame_no] = [1, left_ear_array[frame_no][0],  left_ear_array[frame_no][1], True]
        else:
            results_array[frame_no] = [2, -1, -1, False]

    return results_array


def find_video_of_file(video_dir: str,
                       filename: str):
    """
    Helper to find the video file that represents a data file.

    Parameters
    ----------
    video_dir: str
        Directory holding putative video file
    filename: str
        Data file name, e.g., ``Video_1``.

    Returns
    -------
    return_path: str

    """

    all_files_in_video_folder = [f for f in next(os.walk(video_dir))[2] if not f[0] == '.']
    all_files_in_video_folder = [os.path.join(video_dir, x) for x in all_files_in_video_folder]
    return_path = ''
    for file_path in all_files_in_video_folder:
        _, video_filename, ext = get_fn_ext(file_path)
        if ((video_filename == filename) and ((ext.lower() == '.mp4') or (ext.lower() == '.avi'))):
            return_path = file_path

    if return_path == '':
        print('FAILED: SimBA could not find a video file resenting {} in the project_folder/videos directory'.format(str(filename)))
    else:
        return return_path


def smooth_data_gaussian(config: configparser.ConfigParser,
                         file_path: str,
                         time_window_parameter: int):
    """
    Helper to perform Gaussian smoothing of pose-estimation data. Overwrites the input data with smoothened data.

    Parameters
    ----------
    config: configparser.ConfigParser
        Parsed SimBA project_config.ini file
    file_path: str
        Path to pose estimation data.
    time_window_parameter: int
        Gaussian rolling window size in milliseconds.

    Returns
    -------
    None
    """

    try:
        time_window_parameter = int(time_window_parameter)
    except:
        print('Gaussian smoothing failed for video {}. Time window parameter {} can not be interpreted as an integer.'.format(str(os.path.basename(file_path)), str(time_window_parameter)))
    _, filename, _ = get_fn_ext(file_path)
    project_dir = config.get('General settings', 'project_path')
    video_dir = os.path.join(project_dir, 'videos')
    video_file_path = find_video_of_file(video_dir, filename)
    file_format = get_workflow_file_format(config)
    cap = cv2.VideoCapture(video_file_path)
    video_fps = int(cap.get(cv2.CAP_PROP_FPS))
    if file_format == 'csv':
        pose_df = pd.read_csv(file_path, header=[0, 1, 2], index_col=0)
    elif file_format == 'parquet':
        pose_df = pd.read_parquet(file_path)
    else:
        print('SIMBA ERROR: Workflow file format {} is not recognized (OPTIONS: csv or parquet)'.format(str(file_format)))
        raise ValueError('SIMBA ERROR: Workflow file format {} is not recognized (OPTIONS: csv or parquet)'.format(str(file_format)))
    frames_in_time_window = int(time_window_parameter / (1000 / video_fps))
    new_df = deepcopy(pose_df)
    new_df.columns.names = ['scorer', 'bodyparts', 'coords']

    for c in new_df:
        new_df[c] = new_df[c].rolling(window=int(frames_in_time_window), win_type='gaussian', center=True).mean(std=5).fillna(new_df[c])
        new_df[c] = new_df[c].abs()

    if file_format == 'csv':
        save_df(new_df,file_format, file_path)
    elif file_format == 'parquet':
        table = pa.Table.from_pandas(new_df)
        pq.write_table(table, file_path)

    print('Gaussian smoothing complete for file {}'.format(filename), '...')


def smooth_data_savitzky_golay(config: configparser.ConfigParser,
                               file_path: str,
                               time_window_parameter=int):
    """
    Helper to perform Savitzky-Golay smoothing of pose-estimation data. Overwrites the input data with smoothened data.

    Parameters
    ----------
    config: configparser.ConfigParser
        Parsed SimBA project_config.ini file
    file_path: str
        Path to pose estimation data.
    time_window_parameter: int
        Savitzky-Golay rolling window size in milliseconds.

    Returns
    -------
    None
    """

    try:
        time_window_parameter = int(time_window_parameter)
    except:
        print(
            'Savitzky-Golay smoothing failed for video {}. Time window parameter {} can not be interpreted as an integer.'.format(
                str(os.path.basename(file_path)), str(time_window_parameter)))
    _, filename, _ = get_fn_ext(file_path)
    project_dir = config.get('General settings', 'project_path')
    video_dir = os.path.join(project_dir, 'videos')
    video_file_path = find_video_of_file(video_dir, filename)
    file_format = get_workflow_file_format(config)
    cap = cv2.VideoCapture(video_file_path)
    video_fps = int(cap.get(cv2.CAP_PROP_FPS))
    if file_format == 'csv':
        pose_df = pd.read_csv(file_path, header=[0, 1, 2], index_col=0)
    elif file_format == 'parquet':
        pose_df = pd.read_parquet(file_path)
    else:
        print('SIMBA ERROR: Workflow file format {} is not recognized (OPTIONS: csv or parquet)'.format(str(file_format)))
        raise ValueError('SIMBA ERROR: Workflow file format {} is not recognized (OPTIONS: csv or parquet)'.format(str(file_format)))
    frames_in_time_window = int(time_window_parameter / (1000 / video_fps))
    if (frames_in_time_window % 2) == 0:
        frames_in_time_window = frames_in_time_window - 1
    if (frames_in_time_window % 2) <= 3:
        frames_in_time_window = 5
    new_df = deepcopy(pose_df)
    new_df.columns.names = ['scorer', 'bodyparts', 'coords']

    for c in new_df:
        new_df[c] = savgol_filter(x=new_df[c].to_numpy(), window_length=frames_in_time_window, polyorder=3, mode='nearest')
        new_df[c] = new_df[c].abs()

    if file_format == 'csv':
        save_df(new_df,file_format, file_path)
    elif file_format == 'parquet':
        table = pa.Table.from_pandas(new_df)
        pq.write_table(table, file_path)

    print('Savitzky-Golay smoothing complete for file {}'.format(filename), '...')

def add_missing_ROI_cols(shape_df: pd.DataFrame):
    """
    Helper to add missing ROI definitions in ROI info dataframes created by the first version of the SimBA ROI
    user-interface but analyzed using newer versions of SimBA.

    Parameters
    ----------
    shape_df: pd.DataFrame
        Dataframe holding ROI definitions.

    Returns
    -------
    shape_df: pd.DataFrame
    """

    if not 'Color BGR' in shape_df.columns:
        shape_df['Color BGR'] = [(255, 255, 255)] * len(shape_df)
    if not 'Thickness' in shape_df.columns:
        shape_df['Thickness'] = [5] * len(shape_df)
    if not 'Color name' in shape_df.columns:
        shape_df['Color name'] = 'White'

    return shape_df

def get_file_path_parts(file_path: str):
    """
    Helper to split file path into three components: (i) directory, (ii) file name, and (iii) file extension.

    Parameters
    ----------
    filepath: str
        Path to file.

    Returns
    -------
    file_directory: str
    file_name: str
    extension: str

    """
    file_name = Path(file_path).stem
    file_directory = Path(file_path).parents[0]
    extension = Path(file_path).suffix
    return file_directory, file_name, extension

def create_gantt_img(bouts_df: pd.DataFrame,
                     clf_name: str,
                     image_index: int,
                     fps: int,
                     gantt_img_title: str):
    """
    Helper to create a single gantt plot based on the data preceeding the input image.

    Parameters
    ----------
    bouts_df: pd.DataFrame
        Pandas dataframe holding information on individual bouts created by ``simba.misc_tools.get_bouts_for_gantt``.
    clf_name: str
        Name of the classifier.
    image_index: int
        The count of the image.
    fps: int
        The fps of the input video.
    gantt_img_title: str
        Title of the output image

    Returns
    -------
    open_cv_image: np.array

    """


    fig, ax = plt.subplots()
    fig.suptitle(gantt_img_title, fontsize=24)
    relRows = bouts_df.loc[bouts_df['End_frame'] <= image_index]
    for i, event in enumerate(relRows.groupby("Event")):
        data_event = event[1][["Start_time", "Bout_time"]]
        ax.broken_barh(data_event.values, (4, 4), facecolors='red')
    xLength = (round(image_index / fps)) + 1
    if xLength < 10:
        xLength = 10
    ax.set_xlim(0, xLength)
    ax.set_ylim([0, 12])
    plt.ylabel(clf_name, fontsize=12)
    plt.yticks([])
    plt.xlabel('time(s)', fontsize=12)
    ax.yaxis.set_ticklabels([])
    ax.grid(True)
    buffer_ = io.BytesIO()
    plt.savefig(buffer_, format="png")
    buffer_.seek(0)
    image = PIL.Image.open(buffer_)
    ar = np.asarray(image)
    open_cv_image = ar[:, :, ::-1]
    open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
    open_cv_image = cv2.resize(open_cv_image, (640, 480))
    open_cv_image = np.uint8(open_cv_image)
    buffer_.close()
    plt.close(fig)

    return open_cv_image

def resize_gantt(gantt_img: np.array,
                 img_height: int):
    """
    Helper to resize a image in np.array format.
    """

    return imutils.resize(gantt_img, height=img_height)


def plug_holes_shortest_bout(data_df: pd.DataFrame,
                             clf_name: str,
                             fps: int,
                             shortest_bout: int):
    """

    Parameters
    ----------
    data_df: pd.DataFrame
        Pandas Dataframe with classifier prediction data.
    clf_name: str
        Name of the classifier
    fps: int
        The fps of the input video
    shortest_bout: int
        The shortest valid behavior boat in milliseconds

    Returns
    -------
    data_df: pd.DataFrame
        Dataframe where behavior bouts with invalid lengths have been removed (< shortest_bout).
    """


    frames_to_plug = int(int(fps) * int(shortest_bout) / 1000)
    frames_to_plug_lst = list(range(1, frames_to_plug + 1))
    frames_to_plug_lst.reverse()
    patternListofLists, negPatternListofList = [], []
    for k in frames_to_plug_lst:
        zerosInList, oneInlist = [0] * k, [1] * k
        currList = [1]
        currList.extend(zerosInList)
        currList.extend([1])
        currListNeg = [0]
        currListNeg.extend(oneInlist)
        currListNeg.extend([0])
        patternListofLists.append(currList)
        negPatternListofList.append(currListNeg)
    fill_patterns = np.asarray(patternListofLists)
    remove_patterns = np.asarray(negPatternListofList)

    for currPattern in fill_patterns:
        n_obs = len(currPattern)
        data_df['rolling_match'] = (data_df[clf_name].rolling(window=n_obs, min_periods=n_obs)
                                     .apply(lambda x: (x == currPattern).all())
                                     .mask(lambda x: x == 0)
                                     .bfill(limit=n_obs - 1)
                                     .fillna(0)
                                     .astype(bool)
                                     )
        data_df.loc[data_df['rolling_match'] == True, clf_name] = 1
        data_df = data_df.drop(['rolling_match'], axis=1)

    for currPattern in remove_patterns:
        n_obs = len(currPattern)
        data_df['rolling_match'] = (data_df[clf_name].rolling(window=n_obs, min_periods=n_obs)
                                     .apply(lambda x: (x == currPattern).all())
                                     .mask(lambda x: x == 0)
                                     .bfill(limit=n_obs - 1)
                                     .fillna(0)
                                     .astype(bool)
                                     )
        data_df.loc[data_df['rolling_match'] == True, clf_name] = 0
        data_df = data_df.drop(['rolling_match'], axis=1)

    return data_df


def get_bouts_for_gantt(data_df: pd.DataFrame,
                        clf_name: str,
                        fps: int):
    """
    Helper to detect all behavior bouts for a specific classifier.

    Parameters
    ----------
    data_df: pd.DataFrame
        Pandas Dataframe with classifier prediction data.
    clf_name: str
        Name of the classifier
    fps: int
        The fps of the input video.

    Returns
    -------
    pd.DataFrame:
        Holding the start time, end time, end frame, bout time etc of each classified bout.
    """



    boutsList, nameList, startTimeList, endTimeList, endFrameList = [], [], [], [], []
    groupDf = pd.DataFrame()
    v = (data_df[clf_name] != data_df[clf_name].shift()).cumsum()
    u = data_df.groupby(v)[clf_name].agg(['all', 'count'])
    m = u['all'] & u['count'].ge(1)
    groupDf['groups'] = data_df.groupby(v).apply(lambda x: (x.index[0], x.index[-1]))[m]
    for indexes, rows in groupDf.iterrows():
        currBout = list(rows['groups'])
        boutTime = ((currBout[-1] - currBout[0]) + 1) / fps
        startTime = (currBout[0] + 1) / fps
        endTime = (currBout[1]) / fps
        endFrame = (currBout[1])
        endTimeList.append(endTime)
        startTimeList.append(startTime)
        boutsList.append(boutTime)
        nameList.append(clf_name)
        endFrameList.append(endFrame)

    return pd.DataFrame(list(zip(nameList, startTimeList, endTimeList, endFrameList, boutsList)), columns=['Event', 'Start_time', 'End Time', 'End_frame', 'Bout_time'])

def read_config_file(ini_path: str):
    """ Helper to read SimBA project config ini file"""
    config = ConfigParser()
    try:
        config.read(str(ini_path))
    except MissingSectionHeaderError:
        raise MissingSectionHeaderError('ERROR:  Not a valid project_config file. Please check the project_config.ini path.')
    return config

def create_single_color_lst(pallete_name: str,
                            increments: int):
    """
    Helper to create a color palette of bgr colors in a list.
    Parameters
    ----------
    pallete_name: str
        Palette name (e.g., 'jet')
    increments: int
        Numbers of colors in the color palette to create.

    Returns
    -------
    color_lst: list

    """

    cmap = cm.get_cmap(pallete_name, increments + 1)
    color_lst = []
    for i in range(cmap.N):
        rgb = list((cmap(i)[:3]))
        rgb = [i * 255 for i in rgb]
        rgb.reverse()
        color_lst.append(rgb)
    return color_lst

def detect_bouts(data_df: pd.DataFrame,
                 target_lst: list,
                 fps: int):
    """
    Helper to detect all behavior bouts for a list of classifiers

    Parameters
    ----------
    data_df: pd.DataFrame
        Pandas Dataframe with classifier prediction data.
    target_lst: list
        List of classifier names. E.g., ['Attack', 'Sniffing', 'Grooming']
    fps: int
        The fps of the input video.

    Returns
    -------
    pd.DataFrame:
        Holding the start time, end time, end frame, bout time etc of each classified bout.
    """

    boutsList, nameList, startTimeList, endTimeList, startFrameLst, endFrameList = [], [], [], [], [], []
    for target_name in target_lst:
        groupDf = pd.DataFrame()
        v = (data_df[target_name] != data_df[target_name].shift()).cumsum()
        u = data_df.groupby(v)[target_name].agg(['all', 'count'])
        m = u['all'] & u['count'].ge(1)
        groupDf['groups'] = data_df.groupby(v).apply(lambda x: (x.index[0], x.index[-1]))[m]
        for _, row in groupDf.iterrows():
            bout = list(row['groups'])
            bout_time = ((bout[-1] - bout[0]) + 1) / fps
            bout_start = (bout[0] + 1) / fps
            bout_end = (bout[1]) / fps
            bout_start_frm = bout[0] + 1
            endFrame = (bout[1])
            endTimeList.append(bout_end)
            startTimeList.append(bout_start)
            boutsList.append(bout_time)
            nameList.append(target_name)
            endFrameList.append(endFrame)
            startFrameLst.append(bout_start_frm)

    return pd.DataFrame(list(zip(nameList, startTimeList, endTimeList, startFrameLst, endFrameList, boutsList)), columns=['Event', 'Start_time', 'End Time', 'Start_frame', 'End_frame', 'Bout_time'])

def find_core_cnt():
    """
    Helper to find the local cpu count and half of the cpu counts.

    Returns
    -------
    cpu_cnt: int
    cpu_cnt_to_use: int
    """
    cpu_cnt = multiprocessing.cpu_count()
    cpu_cnt_to_use = int(cpu_cnt / 2)
    return cpu_cnt, cpu_cnt_to_use

def remove_a_folder(folder_dir: str):
    """Helper to remove a directory"""
    shutil.rmtree(folder_dir, ignore_errors=True)

def determine_chunksize_for_imap(data_df_len: int=None,
                                 percent: float = 0.025):
    if data_df_len < 100:
        return 10
    else:
        ratio = int(data_df_len *  percent)
        if ratio > 200:
            ratio = 200
        return ratio

def tabulate_clf_info(clf_path: str):
    """
    Helper to print the hyperparameters and creation date of a pickled classifier.

    Parameters
    ----------
    clf_path: str
        Path to classifier

    Returns
    -------
    None

    """

    _, clf_name, _ = get_fn_ext(clf_path)
    check_file_exist_and_readable(file_path=clf_path)
    try:
        clf_obj = pickle.load(open(clf_path, 'rb'))
    except:
        print('SIMBA ERROR: The {} file is not a pickle file'.format(clf_path))
        raise AttributeError('SIMBA ERROR: The {} file is not a pickle file'.format(clf_path))
    try:
        clf_features_no = clf_obj.n_features_
        clf_criterion = clf_obj.criterion
        clf_estimators = clf_obj.n_estimators
        clf_min_samples_leaf = clf_obj.min_samples_split
        clf_n_jobs = clf_obj.n_jobs
        clf_verbose = clf_obj.verbose
        if clf_verbose == 1: clf_verbose = True
        if clf_verbose == 0: clf_verbose = False
    except:
        print('SIMBA ERROR: The {} file is not an scikit-learn RF classifier'.format(clf_path))
        raise AttributeError('SIMBA ERROR: The {} file is not an scikit-learn RF classifier'.format(clf_path))
    creation_time = 'Unknown'
    try:
        if platform.system() == 'Windows':
            creation_time = os.path.getctime(clf_path)
        elif platform.system() == 'Darwin':
            creation_time = os.stat(clf_path)
            creation_time = creation_time.st_birthtime
    except AttributeError:
        pass
    if creation_time != 'Unknown':
        creation_time = str(datetime.utcfromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S'))


    print(str(clf_name), "CLASSIFIER INFORMATION")
    for (name, val) in zip(['NUMBER OF FEATURES', 'NUMBER OF TREES', 'CLASSIFIER CRITERION', 'CLASSIFIER_MIN_SAMPLE_LEAF',
              'CLASSIFIER_N_JOBS', 'CLASSIFIER VERBOSE SETTING', 'CLASSIFIER PATH', 'CLASSIFIER CREATION TIME'], [clf_features_no, clf_estimators, clf_criterion, clf_min_samples_leaf,
                                                                   clf_n_jobs, clf_verbose, clf_path, str(creation_time)]):
        print(name + ': ' + str(val))


def split_file_path(path: str):
    """
    Split file path into a list of the path directory components.
    """
    path_parts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            path_parts.insert(0, parts[0])
            break
        elif parts[1] == path:  # sentinel for relative paths
            path_parts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            path_parts.insert(0, parts[1])
    return path_parts


def convert_parquet_to_csv(directory: str):
    """
    Helper to convert all parquet files in a folder to csv format.

    Parameters
    ----------
    directory: str
        Path to directory holding parquet files

    Returns
    -------
    None
    """

    if not os.path.isdir(directory):
        print('SIMBA ERROR: {} is not a valid directory'.format(directory))
        raise NotADirectoryError
    files_found = glob.glob(directory + '/*.parquet')
    if len(files_found) < 1:
        print('SIMBA ERROR: No parquet files (with .parquet file ending) found in the {} directory'.format(directory))
        raise ValueError
    for file_cnt, file_path in enumerate(files_found):
        print('Reading in {} ...'.format(os.path.basename(file_path)))
        df = pd.read_parquet(file_path)
        new_file_path = os.path.join(directory, os.path.basename(file_path).replace('.parquet', '.csv'))
        if 'scorer' in df.columns:
            df = df.set_index('scorer')
        df.to_csv(new_file_path)
        print('Saved {}...'.format(new_file_path))
    print('SIMBA COMPLETE: {} parquet files in {} converted to csv'.format(str(len(files_found)), directory))

def convert_csv_to_parquet(directory: str):
    """
    Helper to convert all csv files in a folder to parquet format.

    Parameters
    ----------
    directory: str
        Path to directory holding csv files

    Returns
    -------
    None
    """
    if not os.path.isdir(directory):
        print('SIMBA ERROR: {} is not a valid directory'.format(directory))
        raise NotADirectoryError
    files_found = glob.glob(directory + '/*.csv')
    if len(files_found) < 1:
        print('SIMBA ERROR: No parquet files (with .csv file ending) found in the {} directory'.format(directory))
        raise ValueError
    print('Converting {} files...'.format(str(len(files_found))))
    for file_cnt, file_path in enumerate(files_found):
        print('Reading in {} ...'.format(os.path.basename(file_path)))
        df = pd.read_csv(file_path)
        new_file_path = os.path.join(directory, os.path.basename(file_path).replace('.csv', '.parquet'))
        df.to_parquet(new_file_path)
        print('Saved {}...'.format(new_file_path))
    print('SIMBA COMPLETE: {} csv files in {} converted to parquet'.format(str(len(files_found)), directory))

def change_img_format(directory: str,
                      file_type_in: str,
                      file_type_out: str):
    """
    Helper to convert file type of all image files in a folder.

    Parameters
    ----------
    directory: str
        Path to directory holding csv files
    file_type_in: str
        Input file type
    file_type_out: str
        Output file type

    Returns
    -------
    None
    """
    if not os.path.isdir(directory):
        print('SIMBA ERROR: {} is not a valid directory'.format(directory))
        raise NotADirectoryError
    files_found = glob.glob(directory + '/*.{}'.format(file_type_in))
    if len(files_found) < 1:
        print('SIMBA ERROR: No {} files (with .{} file ending) found in the {} directory'.format(file_type_in, file_type_in, directory))
        raise ValueError
    print('{} image files found in {}...'.format(str(len(files_found)), directory))
    for file_path in files_found:
        im = Image.open(file_path)
        save_name = file_path.replace('.' + str(file_type_in), '.' + str(file_type_out))
        im.save(save_name)
        os.remove(file_path)
    print('SIMBA COMPLETE: Files in {} directory converted to {}'.format(directory, file_type_out))


def clahe_enhance_video(file_path: str):
    """
    Helper to convert a single video file to clahe-enhanced greyscale .avi file. The result is saved with prefix
    ``CLAHE_`` in the same directory as in the input file.

    Parameters
    ----------
    file_path: str
        Path to video file.

    Returns
    -------
    None
    """

    check_file_exist_and_readable(file_path=file_path)
    dir, file_name, file_ext = get_fn_ext(filepath=file_path)
    save_path = os.path.join(dir, 'CLAHE_{}.avi'.format(file_name))
    video_meta_data = get_video_meta_data(file_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    print('Applying CLAHE on video {}, this might take awhile...'.format(file_name))
    cap = cv2.VideoCapture(file_path)
    writer = cv2.VideoWriter(save_path, fourcc, video_meta_data['fps'], (video_meta_data['height'], video_meta_data['width']), 0)
    clahe_filter = cv2.createCLAHE(clipLimit=2, tileGridSize=(16, 16))
    try:
        frm_cnt = 0
        while True:
            ret, img = cap.read()
            if ret:
                frm_cnt += 1
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                clahe_frm = clahe_filter.apply(img)
                writer.write(clahe_frm)
                print('CLAHE converted frame {}/{}'.format(str(frm_cnt), str(video_meta_data['frame_count'])))
    except Exception as se:
        print(se.args)
        print('CLAHE conversion failed for video {}'.format(file_name))
        raise ValueError


def extract_frame_range(file_path: str,
                        start_frame: int,
                        end_frame: int):
    """
    Helper to extract a user-defined range of frames from a video file and save those in png format. Images
    are saved in a folder with the suffix `_frames` within the same directory as the video file.

    Parameters
    ----------
    file_path: str
        Path to video file.
    start_frame: int
        First frame in range to extract.
    end_frame: int
        Last frame in range to extract.

    Returns
    -------
    None
    """

    check_file_exist_and_readable(file_path=file_path)
    video_meta_data = get_video_meta_data(file_path)
    check_int(name='start frame', value=start_frame, min_value=0)
    file_dir, file_name, file_ext = get_fn_ext(filepath=file_path)
    check_int(name='end frame', value=end_frame, max_value=video_meta_data['frame_count'])
    frame_range = list(range(int(start_frame), int(end_frame) + 1))
    save_dir = os.path.join(file_dir, file_name + '_frames')
    cap = cv2.VideoCapture(file_path)
    if not os.path.exists(save_dir): os.makedirs(save_dir)
    for frm_cnt, frm_number in enumerate(frame_range):
        cap.set(1, frm_number)
        ret, frame = cap.read()
        frm_save_path = os.path.join(save_dir, '{}.{}'.format(str(frm_number), 'png'))
        cv2.imwrite(frm_save_path,frame)
        print('Frame {} saved (Frame {}/{})'.format(str(frm_number), str(frm_cnt), str(len(frame_range))))
    print('SIMBA COMPLETE: {} frames extracted for video {}'.format(str(len(frame_range)), file_name))




def change_single_video_fps(file_path: str,
                            fps: int):
    """
    Helper to change the fps of a single video file. Results are stored in the same directory as in the input file with
    the suffix ``_fps_new_fps``.

    Parameters
    ----------
    file_path: str
        Path to video file.
    fps: int
        Fps of the new video file
    """

    check_file_exist_and_readable(file_path=file_path)
    check_int(name='New fps', value=fps)
    video_meta_data = get_video_meta_data(video_path=file_path)
    dir_name, file_name, ext = get_fn_ext(filepath=file_path)
    if int(fps) == int(video_meta_data['fps']):
        print('SIMBA WARNING: The new fps is the same as the input fps for video {}'.format(file_name))
    save_path = os.path.join(dir_name, file_name + '_fps_{}{}'.format(str(fps), str(ext)))
    if os.path.isfile(save_path):
        print('SIMBA WARNING: Overwriting existing file at {}'.format(save_path))
    command = str('ffmpeg -i ') + '"' + str(file_path) + '"' + ' -filter:v fps=fps=' + str(fps) + ' ' + '"' + save_path + '"'
    subprocess.call(command, shell=True)
    print('SIMBA COMPLETE: FPS of video {} changed from {} to {} and saved in directory {}'.format(file_name, str(video_meta_data['fps']), str(fps), save_path))


def change_fps_of_multiple_videos(directory: str,
                                  fps: int):
    """
    Helper to change the fps of video files in a folder. Results are stored in the same directory as in the input files with
    the suffix ``_fps_new_fps``.

    Parameters
    ----------
    file_path: str
        Path to video file.
    fps: int
        Fps of the new video file
    """

    if not os.path.isdir(directory):
        print('SIMBA ERROR: {} is not a valid directory'.format(directory))
        raise NotADirectoryError()
    check_int(name='New fps', value=fps)
    video_paths = []
    file_paths_in_folder = [f for f in glob.glob(directory + '/*') if os.path.isfile(f)]
    for file_path in file_paths_in_folder:
        _, _, ext = get_fn_ext(filepath=file_path)
        if ext.lower() in ['.avi', '.mp4', '.mov', '.flv']:
            video_paths.append(file_path)
    if len(video_paths) < 1:
        print('SIMBA ERROR: No files with .mp4, .avi, .mov, .flv file ending found in the {} directory'.format(directory))
        raise ValueError()
    for file_cnt, file_path in enumerate(video_paths):
        dir_name, file_name, ext = get_fn_ext(filepath=file_path)
        save_path = os.path.join(dir_name, file_name + '_fps_{}{}'.format(str(fps), str(ext)))
        command = str('ffmpeg -i ') + str(file_path) + ' -filter:v fps=fps=' + str(fps) + ' ' + '"' + save_path + '"'
        subprocess.call(command, shell=True)
        print('Video {} complete...'.format(file_name))
    print('SIMBA COMPLETE: FPS of {} videos changed to {}'.format(str(len(video_paths)), str(fps)))


def convert_video_powerpoint_compatible_format(file_path: str):
    """
    Helper to make a powerpoint compatible copy of a video file. The results is stored in the same directory as the
    input file with the ``_powerpointready`` suffix.

    Parameters
    ----------
    file_path: str
        Path to video file.

    """


    check_file_exist_and_readable(file_path=file_path)
    dir, file_name, ext = get_fn_ext(filepath=file_path)
    save_name = os.path.join(dir, file_name + '_powerpointready.mp4')
    if os.path.isfile(save_name):
        print('SIMBA ERROR: The outfile file already exist: {}.'.format(save_name))
        raise FileExistsError()
    command = (str('ffmpeg -i ') + '"' + str(file_path) + '"' + ' -c:v libx264 -preset slow  -profile:v high -level:v 4.0 -pix_fmt yuv420p -crf 22 -codec:a aac ' + '"' + save_name + '"')
    print('Creating video in powerpoint compatible format... ')
    subprocess.call(command, shell=True, stdout=subprocess.PIPE)
    print('SIMBA COMPLETE: Video converted! {} generated!'.format(save_name))

def convert_to_mp4(file_path: str):
    """
    Helper to convert a video file to mp4 format. The results is stored in the same directory as the
    input file with the ``_converted.mp4`` suffix.

    Parameters
    ----------
    file_path: str
        Path to video file.

    """

    check_file_exist_and_readable(file_path=file_path)
    dir, file_name, ext = get_fn_ext(filepath=file_path)
    save_name = os.path.join(dir, file_name + '_converted.mp4')
    if os.path.isfile(save_name):
        print('SIMBA ERROR: The outfile file already exist: {}.'.format(save_name))
        raise FileExistsError()
    command = (str('ffmpeg -i ') + '"' + str(file_path) + '"' + ' ' + '"' + save_name + '"')
    print('Converting to mp4... ')
    subprocess.call(command, shell=True, stdout=subprocess.PIPE)
    print('SIMBA COMPLETE: Video converted! {} generated!'.format(save_name))


def video_to_greyscale(file_path: str):
    """
    Helper to convert a video file to greyscale mp4 format. The results is stored in the same directory as the
    input file with the ``_grayscale.mp4`` suffix.

    Parameters
    ----------
    file_path: str
        Path to video file.

    """

    check_file_exist_and_readable(file_path=file_path)
    dir, file_name, ext = get_fn_ext(filepath=file_path)
    save_name = os.path.join(dir, file_name + '_grayscale.mp4')
    if os.path.isfile(save_name):
        print('SIMBA ERROR: The outfile file already exist: {}.'.format(save_name))
        raise FileExistsError()
    command = (str('ffmpeg -i ') + '"' + str(file_path) + '"' + ' -vf format=gray ' + '"' + save_name + '"')
    print('Converting to greyscale... ')
    subprocess.call(command, shell=True, stdout=subprocess.PIPE)
    print('SIMBA COMPLETE: Video converted! {} generated!'.format(save_name))


def superimpose_frame_count(file_path: str):
    """
    Helper to superimpose frame count on a video file. The results is stored in the same directory as the
    input file with the ``_frame_no.mp4`` suffix.

    Parameters
    ----------
    file_path: str
        Path to video file.

    """


    check_file_exist_and_readable(file_path=file_path)
    dir, file_name, ext = get_fn_ext(filepath=file_path)
    save_name = os.path.join(dir, file_name + '_frame_no.mp4')
    print('Superimposing frame numbers...... ')
    try:
        command = (str('ffmpeg -y -i ') + '"' + file_path + '"' + ' -vf "drawtext=fontfile=Arial.ttf: text=\'%{frame_num}\': start_number=0: x=(w-tw)/2: y=h-(2*lh): fontcolor=black: fontsize=20: box=1: boxcolor=white: boxborderw=5" -c:a copy ' + '"' + save_name + '"')
        subprocess.check_output(command, shell=True)
        subprocess.call(command, shell=True, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        simba_cw = os.path.dirname(simba.__file__)
        simba_font_path = Path(simba_cw, 'assets', 'UbuntuMono-Regular.ttf')
        command = 'ffmpeg -y -i ' + file_path + ' -vf "drawtext=fontfile={}:'.format(simba_font_path) + "text='%{frame_num}': start_number=1: x=(w-tw)/2: y=h-(2*lh): fontcolor=black: fontsize=20: box=1: boxcolor=white: boxborderw=5" + '" ' + "-c:a copy " + save_name
        subprocess.call(command, shell=True, stdout=subprocess.PIPE)
    print('SIMBA COMPLETE: Video converted! {} generated!'.format(save_name))



def remove_beginning_of_video(file_path: str,
                              time: int):
    """
    Helper to remove N seconds from the beginning of a video file. The results is stored in the same directory as the
    input file with the ``_shorten.mp4`` suffix.

    Parameters
    ----------
    file_path: str
        Path to video file.
    """

    check_file_exist_and_readable(file_path=file_path)
    check_int(name='Cut time', value=time)
    dir, file_name, ext = get_fn_ext(filepath=file_path)
    save_name = os.path.join(dir, file_name + '_shorten.mp4')
    if os.path.isfile(save_name):
        print('SIMBA ERROR: The outfile file already exist: {}.'.format(save_name))
        raise FileExistsError()
    command = (str('ffmpeg -ss ') + str(int(time)) + ' -i ' + '"' + str(file_path) + '"' + ' -c:v libx264 -c:a aac ' + '"' + save_name + '"')
    print('Shortening video... ')
    subprocess.call(command, shell=True, stdout=subprocess.PIPE)
    print('SIMBA COMPLETE: Video converted! {} generated!'.format(save_name))



def clip_video_in_range(file_path: str,
                        start_time: str,
                        end_time: str):
    """
    Helper to clip video in a specific range. The results is stored in the same directory as the
    input file with the ``_clipped.mp4`` suffix.

    Parameters
    ----------
    file_path: str
        Path to video file.
    start_time: str
        Start time of clip in HH:MM:SS format.
    end_time: str
        End time of clip in HH:MM:SS format.
    """

    check_file_exist_and_readable(file_path=file_path)
    dir, file_name, ext = get_fn_ext(filepath=file_path)
    save_name = os.path.join(dir, file_name + '_clipped.mp4')
    if os.path.isfile(save_name):
        print('SIMBA ERROR: The outfile file already exist: {}.'.format(save_name))
        raise FileExistsError()
    command = (str('ffmpeg -i ') + '"' + str(file_path) + '"' + ' -ss ' + str(start_time) + ' -to ' + str(end_time) + ' -async 1 ' + '"' + save_name + '"')
    print('Clipping video... ')
    subprocess.call(command, shell=True, stdout=subprocess.PIPE)
    print('SIMBA COMPLETE: Video converted! {} generated!'.format(save_name))

