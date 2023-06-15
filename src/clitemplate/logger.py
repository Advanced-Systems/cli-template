#!/usr/bin/env python3

import logging
from pathlib import Path
from typing import Union


class Logger:
    def __init__(self, path: Union[Path, str], level: int) -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)
        self.formatter = logging.Formatter('%(asctime)s [%(levelname)s]::%(name)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        self.file_handler = logging.FileHandler(path)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

    def log(self, msg: str, level: int, *args) -> None:
        if level > 50 or not all(map(lambda x: x % 10 == 0, range(0, 51, 10))):
            docs = "https://docs.python.org/3/howto/logging.html#logging-levels"
            raise ValueError(f"{level} is an invalid logging level, see also: {docs}")

        self.logger.log(level, msg, *args)
