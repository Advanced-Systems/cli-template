#!/usr/bin/env python3

import logging

import click
from rich.console import Console
from rich.table import Table

from .__init__ import __version__, package_name
from .commands import square_function
from .internals.config import Config
from .internals.constants import Files
from .internals.logger import Logger
from .internals.utils import Utils


class ContextConfig:
    def __init__(self) -> None:
        self.verbose = False
        self.console = Console()
        self.__default_level = logging.DEBUG
        self.logger = Logger(path=Utils.get_resource_path(Files.LOG_FILE.value), level=self.__default_level)
        self.config = Config(Utils.get_resource_path(Files.CONFIG_FILE.value))

        if (self.config.path.exists()): self.config.read(); return
        self.config.add_section("configuration", {
            "level": self.__default_level
        })
        self.config.save()


pass_config = click.make_pass_decorator(ContextConfig, ensure=True)

@click.group()
@click.help_option()
@click.version_option(version=__version__, package_name=package_name)
@click.option("--verbose", is_flag=True, help="Print log messages to console")
@pass_config
def cli(ctx_cfg: ContextConfig, verbose: bool):
    ctx_cfg.verbose = verbose

@cli.command(help="return the image of [xmin, xmax] under the square function")
@click.option("--xmin", type=int, help="Start value")
@click.option("--xmax", type=int, help="Stop value")
@pass_config
def square(ctx_cfg: ContextConfig, xmin: int, xmax: int):
    level = int(ctx_cfg.config.get("configuration", "level"))
    ctx_cfg.logger.log(f"Calling square with values {xmin=},{xmax=}", level, console=ctx_cfg.verbose)

    table = Table(title=f"y=x^2")
    table.add_column("x", justify="right", style="yellow")
    table.add_column("y", justify="right", style="yellow")

    x = iter(range(xmin, xmax+1))

    for y in square_function(xmin, xmax):
        table.add_row(str(next(x)), str(y))

    ctx_cfg.console.print(table)
