#!/usr/bin/env python3

from configparser import ConfigParser
from pathlib import Path
from typing import Dict, List, Union

from .constants import Files
from .utils import Utils

class Config:
    def __init__(self, path: Union[str, Path], settings: Dict=None, encoding="utf-8") -> None:
        self.path = Utils.get_resource_path(Files.CONFIG_FILE.value)
        self.encoding = encoding
        self.__config = ConfigParser()
        if settings: self.__config.read_dict(settings)

    def add_section(self, section: str, settings: Dict=None) -> None:
        if settings is None: self.__config.add_section(section)
        self.__config[section] = settings

    def save(self) -> None:
        with open(self.path, mode='w', encoding=self.encoding) as file_handler:
            self.__config.write(file_handler)

    def get(self,section: str, option: str):
        return self.__config.get(section, option)
