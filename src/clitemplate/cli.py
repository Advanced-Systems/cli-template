#!/usr/bin/env python3

import argparse
import errno
import sys

try:
    import pretty_errors
except ImportError:
    pass

from . import core, utils
from .__init__ import __version__, package_name

CONFIG = utils.read_resource('clitemplate.data', 'config.json')

def on_parsing_error():
    utils.logger.error("an error occurred while trying to parse this command: %s", " ".join(sys.argv))
    raise NotImplementedError("aborting operation: failed to parse this option")

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=f"%(prog)s {__version__}")
    parser.add_argument('--verbose', default=True, action=argparse.BooleanOptionalAction, help='increase output verbosity')

    subparser = parser.add_subparsers(dest='command')

    log_parser = subparser.add_parser('log', help="read the log file")
    log_parser.add_argument('--reset', action='store_true', help="reset all log file entries")
    log_parser.add_argument('--path', action='store_true', help="return the log file path")
    log_parser.add_argument('--read', action='store_true', help='read the log file')

    config_parser = subparser.add_parser('config', help="read the config file")
    config_parser.add_argument('--message', type=str, nargs='?', help="store a message in the configuration file")
    config_parser.add_argument('--list', action='store_true', help="list all app settingspath")
    config_parser.add_argument('--reset', action='store_true', help='discard all application settings')

    test_parser = subparser.add_parser('test', help="simple test command")

    args = parser.parse_args()

    if args.command == 'log':
        if args.reset:
            open(utils.LOGFILEPATH, mode='w', encoding='utf-8').close()
        elif args.path:
            print(utils.LOGFILEPATH)
        elif args.read:
            utils.read_log()
        else:
            on_parsing_error()

    if args.command == 'config':
        if args.message:
            print(sys.argv)
            CONFIG['Message'] = args.message
            utils.write_resource('clitemplate.data', 'config.json', CONFIG)
        elif args.list:
            print("Application Settings")
            utils.print_dict('Name', 'Value', CONFIG)
        elif args.reset:
            utils.reset_resource('clitemplate.data', 'config.json')
        else:
            on_parsing_error()

    if args.command == 'test':
        print("First Ten Powers of 2")
        start, end = 1, 11
        utils.print_dict('X Values', 'Y Values', dict(zip(range(start, end), core.square_function(start, end))))
