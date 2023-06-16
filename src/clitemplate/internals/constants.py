#!/usr/bin/env python3

from enum import Enum, unique

@unique
class Files(Enum):
    LOG_FILE = "cli-template.log"
    CONFIG_FILE = "cli-template.ini"
