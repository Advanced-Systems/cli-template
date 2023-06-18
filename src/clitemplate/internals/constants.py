#!/usr/bin/env python3

from enum import Enum, unique

from ..__init__ import package_name

@unique
class Files(Enum):
    LOG_FILE = f"{package_name}.log"
    CONFIG_FILE = f"{package_name}.ini"
