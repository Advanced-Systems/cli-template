#!/usr/bin/env python3

import json
import logging
import os
import platform
from collections import namedtuple
from importlib.resources import path as resource_path
from itertools import chain
from pathlib import Path
from types import FrameType

from .__init__ import package_name

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

def get_logfile_path() -> Path:
    """
    Return a platform-specific log file path.
    """
    config_dir = get_config_dir()
    config_dir.mkdir(parents=True, exist_ok=True)
    log_file = config_dir.joinpath("error.log")
    log_file.touch(exist_ok=True)
    return log_file

LOGFILEPATH = get_logfile_path()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s::%(levelname)s::%(lineno)d::%(name)s::%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler = logging.FileHandler(get_logfile_path())
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def read_log() -> None:
    """
    Return the content of the log file from the lolicon module.
    """
    with open(LOGFILEPATH, mode='r', encoding='utf-8') as file_handler:
        log = file_handler.readlines()

        if not log:
            print_on_warning("Operation suspended: nothing to read because the log file is empty")
            return

        parse = lambda line: line.strip('\n').split('::')
        Entry = namedtuple('Entry', 'timestamp levelname lineno name message')

        tabulate = "{:<7} {:<8} {:<30} {:<30}".format

        print(f"\033[32m{tabulate('Line', 'Level', 'File Name', 'Message')}\033[0m")

        for line in log:
            entry = Entry(parse(line)[0], parse(line)[1], parse(line)[2], parse(line)[3], parse(line)[4])
            print(tabulate(entry.lineno.zfill(4), entry.levelname, entry.name, entry.message))

def get_resource_path(package: str, resource: str) -> Path:
    """
    Get the path to a `resource` located in `package`.
    """
    with resource_path(package, resource) as resource_handler:
        return Path(resource_handler)

def read_resource(package: str, resource: str) -> dict:
    """
    Return the content of `package` (a JSON file located in `resource`) as dictionary.
    """
    with open(get_resource_path(package, resource), mode='r', encoding='utf-8') as file_handler:
        return json.load(file_handler)

def write_resource(package: str, resource: str, params: dict) -> None:
    """
    Merge `params` with the content of `package` (located in `resource`) and write
    the result of this operation to disk.
    """
    config = read_resource(package, resource)
    with open(get_resource_path(package, resource), mode='w', encoding='utf-8') as file_handler:
        json.dump({**config, **params}, file_handler)

def reset_resource(package: str, resource) -> None:
    """
    Reset the content of `package` (a JSON file located in `resource`).
    """
    with open(get_resource_path(package, resource), mode='w', encoding='utf-8') as file_handler:
        json.dump({}, file_handler)

#endregion logging and resource access

#region development utilities

def print_dict(title_left: str, title_right: str, table: dict) -> None:
    """
    Print a flat dictionary as table with two column titles.
    """
    table = {str(key): str(value) for key, value in table.items()}
    invert = lambda x: -x + (1 + len(max(chain(table.keys(), [title_left]), key=len)) // 8)
    tabs = lambda string: invert(len(string) // 8) * '\t'
    print(f"\n\033[32m{title_left}{tabs(title_left)}{title_right}\033[0m")
    print(f"{len(title_left) * '-'}{tabs(title_left)}{len(title_right) * '-'}")
    for key, value in table.items():
        print(f"{key}{tabs(key)}{value}")
    print()

def print_on_success(message: str, verbose: bool=True) -> None:
    """
    Print a formatted success message if verbose is enabled.
    """
    if verbose:
        print(f"\033[32m{'[  OK  ]'.ljust(12, ' ')}\033[0m{message}")

def print_on_warning(message: str, verbose: bool=True) -> None:
    """
    Print a formatted warning message if verbose is enabled.
    """
    if verbose:
        print(f"\033[33m{'[ WARNING ]'.ljust(12, ' ')}\033[0m{message}")

def print_on_error(message: str, verbose: bool=True) -> None:
    """
    Print a formatted error message if verbose is enabled.
    """
    if verbose:
        print(f"\033[31m{'[ ERROR ]'.ljust(12, ' ')}\033[0m{message}", err=True)

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
    print(f"\033[93m[{str(frame.f_lineno).zfill(4)}]\033[0m\t\033[92m{msg}\033[0m (in {Path(frame.f_code.co_filename).name}).")

def clear():
    """
    Reset terminal screen.
    """
    os.system('cls' if platform.system() == 'Windows' else 'clear')

#endregion development utilities
