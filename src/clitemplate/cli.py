#!/usr/bin/env python3

import click
from click import style

try:
    import pretty_errors
except ImportError:
    pass

from . import core, utils
from .__init__ import __version__, package_name


@click.group(invoke_without_command=True)
@click.version_option(version=__version__, prog_name=package_name)
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj['CONFIG'] = utils.read_configuration('clitemplate.data', 'config.json')

@cli.command(help=style("Configure default application settings.", fg='bright_green'))
@click.option('--message', type=click.STRING, help=style("Store a new message in configuration file.", fg='yellow'))
@click.option('--list', is_flag=True, help=style("List all app settings.", fg='yellow'))
@click.option('--reset', is_flag=True, help=style("Discard all application settings.", fg='yellow'))
@click.pass_context
def config(ctx, message, list, reset):
    config = ctx.obj['CONFIG']

    if message:
        config['Message'] = message
        utils.write_configuration('clitemplate.data', 'config.json', config)

    if list:
        click.secho("\nApplication Settings", fg='bright_magenta')
        utils.print_dict('Name', 'Value', config)
        return

    if reset:
        utils.reset_configuration('clitemplate.data', 'config.json')
        return

@cli.command(help=style("Simple test command.", fg='bright_green'))
def test():    
    click.secho("\nFirst Ten Powers of 2", fg='bright_magenta')
    start, end = 1, 11
    utils.print_dict('X Values', 'Y Values', dict(zip(range(start, end), core.square_function(start, end))))
