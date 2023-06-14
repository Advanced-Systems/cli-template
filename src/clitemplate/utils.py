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
file_handler = logging.FileHandler(get_resource_path(config.LOG_FILE))
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
