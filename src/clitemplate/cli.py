#!/usr/bin/env python3

import logging

import click
from click import Context

from .__init__ import __version__, package_name
from .commands import square_function
from .constants import Config
from .logger import Logger
from .utils import Utils


@click.group()
@click.help_option()
@click.version_option(version=__version__, package_name=package_name)
@click.pass_context
def cli(ctx: Context):
    log_path = Utils.get_resource_path(Config.LOG_FILE)
    ctx.obj = Logger(path=log_path, level=logging.DEBUG)

@cli.command(help="return the image of [xmin, xmax] under the square function")
@click.option("--xmin", type=int, help="Start value")
@click.option("--xmax", type=int, help="Stop value")
@click.pass_obj
def square(logger: Logger, xmin: int, xmax: int):
    logger.log("test", level=logging.DEBUG)
    for y in square_function(xmin, xmax):
        click.echo(y)
