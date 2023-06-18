#!/usr/bin/env python3

import logging
from pathlib import Path
from typing import Union

import click
from rich.logging import RichHandler


class Logger:
    def __init__(self, path: Union[Path, str], level: int) -> None:
        self.path = path
        self.level = level
        self.logger = logging.getLogger(__name__)

        self.logger.setLevel(self.level)
        self.formatter = logging.Formatter("%(asctime)s [%(levelname)s]::%(name)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

        self.file_handler = logging.FileHandler(self.path)
        self.file_handler.setFormatter(self.formatter)
        self.rich_handler = RichHandler(rich_tracebacks=True, tracebacks_suppress=[click])

        self.logger.addHandler(self.file_handler)

    def log(self, msg: str, level: int=None, console: bool=False, *args) -> None:
        level = level or self.level

        if level > 50 or level % 10 != 0:
            docs = "https://docs.python.org/3/howto/logging.html#logging-levels"
            raise ValueError(f"{level} is an invalid logging level, see also: {docs}")

        if console and self.rich_handler not in self.logger.handlers:
            self.logger.addHandler(self.rich_handler)

        self.logger.log(level, msg, *args)
