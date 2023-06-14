#!/usr/bin/env python3


from .__init__ import __version__, package_name
from .constants import Config
from .commands import square_function

import click

@click.group()
@click.help_option()
@click.version_option(version=__version__, package_name=package_name)
def cli():
    pass

@cli.command(help="return the image of [xmin, xmax] under the square function")
@click.option("--xmin", type=int, help="Start value")
@click.option("--xmax", type=int, help="Stop value")
def square(xmin, xmax):
    for y in square_function(xmin, xmax):
        click.echo(y)
