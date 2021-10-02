#!/usr/bin/env python3

import json
import logging
import os
import platform
import sys
from itertools import chain
from json.decoder import JSONDecodeError
from pathlib import Path
from types import FrameType
from typing import Dict, Union

from . import config
from .__init__ import package_name
from .config import BRIGHT, CYAN, DIM, GREEN, NORMAL, RED, RESET_ALL, YELLOW

#region logging and resource access

def get_config_dir() -> Path:
    """
    Return a platform-specific root directory for user configuration settings.
    """
    return {
        'Windows': Path(os.path.expandvars('%LOCALAPPDATA%')),
        'Darwin': Path.home().joinpath('Library').joinpath('Application Support'),
        'Linux': Path.home().joinpath('.config')
    }[platform.system()].joinpath(package_name)

def get_resource_path(filename: Union[str, Path]) -> Path:
    """
    Return a platform-specific log file path.
    """
    config_dir = get_config_dir()
    config_dir.mkdir(parents=True, exist_ok=True)
    resource = config_dir.joinpath(filename)
    resource.touch(exist_ok=True)
    return resource

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s::%(levelname)s::%(lineno)d::%(name)s::%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler = logging.FileHandler(get_resource_path(config.LOGFILE))
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def read_json_file(filename: Union[str, Path]) -> Dict:
    """
    Read `filename` and, if this file is empty, return an empty dictionary in its place.
    """
    with open(get_resource_path(filename), mode='r', encoding='utf-8') as file_handler:
        try:
            return json.load(file_handler)
        except JSONDecodeError:
            return dict()

def write_json_file(filename: Union[str, Path], params: dict) -> None:
    """
    Save the data in `params` as a JSON file by creating an union of pre-existing data (if any).
    """
    config = read_json_file(filename)
    with open(get_resource_path(filename), mode='w', encoding='utf-8') as file_handler:
        json.dump({**config, **params}, file_handler)
        file_handler.write('\n')

def reset_file(filename: Union[str, Path]) -> None:
    open(get_resource_path(filename), mode='w', encoding='utf-8').close()

#endregion logging and resource access

#region development utilities

def print_dict(title_left: str, title_right: str, table: dict) -> None:
    """
    Print a flat dictionary as table with two column titles.
    """
    table = {str(key): str(value) for key, value in table.items()}
    invert = lambda x: -x + (1 + len(max(chain(table.keys(), [title_left]), key=len)) // 8)
    tabs = lambda string: invert(len(string) // 8) * '\t'
    print('\n' + BRIGHT + GREEN + title_left + tabs(title_left) + title_right + RESET_ALL)
    print((len(title_left) * '-') + tabs(title_left) + (len(title_right) * '-'))
    for key, value in table.items():
        print(key + tabs(key) + value)
    print()

def print_on_success(message: str, verbose: bool=True) -> None:
    """
    Print a formatted success message if verbose is enabled.
    """
    if verbose:
        print(BRIGHT + GREEN + "[  OK  ]".ljust(12, ' ') + RESET_ALL + message)

def print_on_warning(message: str, verbose: bool=True) -> None:
    """
    Print a formatted warning message if verbose is enabled.
    """
    if verbose:
        print(BRIGHT + YELLOW + "[ WARNING ]".ljust(12, ' ') + RESET_ALL + message)

def print_on_error(message: str, verbose: bool=True) -> None:
    """
    Print a formatted error message if verbose is enabled.
    """
    if verbose:
        print(BRIGHT + RED + "[ ERROR ]".ljust(12, ' ') + RESET_ALL + message, file=sys.stderr)

def debug(msg: str, frame: FrameType) -> None:
    """
    Helper function for slightly better print debugging. Prints the current line
    of invocation, a custom `msg` and the source file name as color-formatted string.
    Set `frame` to `inspect.currentframe()` when you invoke this function.
    Example
    -------
    ```
    import inspect
    # some code
    debug('Validate incoming data stream.', frame=inspect.currentframe())
    # ...
    debug('Enter recursive function.', frame=inspect.currentframe())
    ```
    Note
    ----
    Consider using an IDE with a debugger whenever possible.
    """
    print(BRIGHT + YELLOW + '[' + str(frame.f_lineno).zfill(4) + ']' + RESET_ALL + '\t' + msg + " (in '%s').", Path(frame.f_code.co_filename).name)

def clear():
    """
    Reset terminal screen.
    """
    os.system('cls' if platform.system() == 'Windows' else 'clear')

#endregion development utilities
