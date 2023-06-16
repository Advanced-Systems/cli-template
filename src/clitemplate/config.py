#!/usr/bin/env python3

from configparser import ConfigParser
from pathlib import Path
from typing import Union


class Config:
    def __init__(self, path: Union[str, Path]) -> None:
        self.config = ConfigParser()

