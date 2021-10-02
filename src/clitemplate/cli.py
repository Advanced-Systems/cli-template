#!/usr/bin/env python3

import argparse
import errno
import sys
from collections import namedtuple

from . import core, utils
from .__init__ import __version__, package_name
from .config import CONFIGFILE, LOGFILE, GREEN, RESET_ALL


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=f"%(prog)s {__version__}")
    parser.add_argument('--verbose', default=False, action='store_true', help="increase output verbosity")

    subparser = parser.add_subparsers(dest='command')

    log_parser = subparser.add_parser('log', help="interact with the application log")
    log_parser.add_argument('--path', action='store_true', help="return the log file path")
    log_parser.add_argument('--reset', action='store_true', help="purge the log file")
    log_parser.add_argument('--list', action='store_true', help='read the log file')

    config_parser = subparser.add_parser('config', help="configure default application settings")
    config_parser.add_argument('--message', type=str, nargs='?', help="store a message in the configuration file")
    config_parser.add_argument('--path', action='store_true', help="return the config file path")
    config_parser.add_argument('--reset', action='store_true', help='purge the config file')
    config_parser.add_argument('--list', action='store_true', help="list all user configuration")

    test_parser = subparser.add_parser('test', help="simple test command")

    args = parser.parse_args()
    config_data = utils.read_json_file(CONFIGFILE)

    if args.command == 'log':
        logfile = utils.get_resource_path(LOGFILE)

        if args.path:
            return logfile
        if args.reset:
            utils.reset_file(logfile)
            return
        if args.list:
            with open(logfile, mode='r', encoding='utf-8') as file_handler:
                log = file_handler.readlines()

                if not log:
                    utils.print_on_warning("Nothing to read because the log file is empty")
                    return

                parse = lambda line: line.strip('\n').split('::')
                Entry = namedtuple('Entry', 'timestamp levelname lineno name message')

                tabulate = "{:<20} {:<5} {:<6} {:<22} {:<20}".format

                print('\n' + GREEN + tabulate('Timestamp', 'Line', 'Level', 'File Name', 'Message') + RESET_ALL)

                for line in log:
                    entry = Entry(parse(line)[0], parse(line)[1], parse(line)[2], parse(line)[3], parse(line)[4])
                    print(tabulate(entry.timestamp, entry.lineno.zfill(4), entry.levelname, entry.name, entry.message))

    if args.command == 'config':
        config_file = utils.get_resource_path(CONFIGFILE)

        if args.message:
            config_data['UnitSystem'] = args.message
            utils.write_json_file(config_file, config_data)
        if args.path:
            return config_file
        if args.reset:
            utils.reset_file(config_file)
            return
        if args.list:
            utils.print_dict('Name', 'Value', config_data)
            return

    if args.command == 'test':
        print("\nFirst Ten Powers of 2")
        start, end = 1, 11
        utils.print_dict('X Values', 'Y Values', dict(zip(range(start, end), core.square_function(start, end))))
