#!/usr/bin/env python3

import click
from click import style

try:
    import pretty_errors
except ImportError:
    pass

from . import core, utils
from .__init__ import __version__, package_name

CONTEXT_SETTINGS = dict(max_content_width=120)

@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS, help=style("A modern CLI template for python scripts.", fg='bright_magenta'))
@click.version_option(version=__version__, prog_name=package_name, help=style("Show the version and exit.", fg='yellow'))
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj['CONFIG'] = utils.read_resource('clitemplate.data', 'config.json')

@cli.command(help=style("Perform log file operations.", fg='bright_green'), context_settings=CONTEXT_SETTINGS)
@click.option('--read', is_flag=True, default=False, help=style("Read the log file.", fg='yellow'))
@click.option('--reset', is_flag=True, default=False, help=style("Reset all log file entries", fg='yellow'))
@click.option('--path', is_flag=True, default=False, help=style("Get the log file path.", fg='yellow'))
def log(read, reset, path):
    if read:
        utils.read_log()
        return

    if reset:
        open(utils.log_file_path(target_dir=package_name), mode='w', encoding='utf-8').close()
        return

    if path:
        click.echo(utils.log_file_path(target_dir=package_name))
        return

@cli.command(context_settings=CONTEXT_SETTINGS, help=style("Configure default application settings.", fg='bright_green'))
@click.option('--message', type=click.STRING, help=style("Store a new message in configuration file.", fg='yellow'))
@click.option('--list', is_flag=True, help=style("List all app settings.", fg='yellow'))
@click.option('--reset', is_flag=True, help=style("Discard all application settings.", fg='yellow'))
@click.pass_context
def config(ctx, message, list, reset):
    config = ctx.obj['CONFIG']

    if message:
        config['Message'] = message
        utils.write_resource('clitemplate.data', 'config.json', config)

    if list:
        click.secho("\nApplication Settings", fg='bright_magenta')
        utils.print_dict('Name', 'Value', config)
        return

    if reset:
        utils.reset_resource('clitemplate.data', 'config.json')
        return

@cli.command(context_settings=CONTEXT_SETTINGS, help=style("Simple test command.", fg='bright_green'))
def test():    
    click.secho("\nFirst Ten Powers of 2", fg='bright_magenta')
    start, end = 1, 11
    utils.print_dict('X Values', 'Y Values', dict(zip(range(start, end), core.square_function(start, end))))
