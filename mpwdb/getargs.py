import argparse
from collections import namedtuple
import os
import sys


Colors = namedtuple(
    'Colors',
    (
        'header',
        'okblue',
        'okgreen',
        'warning',
        'fail',
        'endc',
        'bold',
        'underline',
    ))


colors = Colors(
    header='\033[95m',
    okblue='\033[94m',
    okgreen='\033[92m',
    warning='\033[93m',
    fail='\033[91m',
    endc='\033[0m',
    bold='\033[1m',
    underline='\033[4m',
)


def greenify(text):
    return f'{colors.okgreen}{text}{colors.endc}'


def blueify(text):
    return f'{colors.okblue}{text}{colors.endc}'


def redify(text):
    return f'{colors.fail}{text}{colors.endc}'


# Declare the supported subcommands and their arguments/options
Opt = namedtuple('Opt', ['name', 'metavar', 'help', 'default', 'type'])
Arg = namedtuple('Arg', ['name', 'help', 'type'])
SubCommand = namedtuple('SubCommand', ['name', 'help', 'args', 'opts'])


# KEY_OPT = Opt(
#     name='key',
#     metavar='KEY',
#     help='The key value of a thing.',
#     default=None,
#     type=str)

# ID = Arg(
#     name='id',
#     help='The id of a specific thingy.',
#     type=int)


SUBCOMMANDS = (

    SubCommand(
        name='french-adj',
        help='Ingest French adjective data.',
        args=(),
        opts=(),
    ),

)


def get_args():
    """Return the command-line arguments as a dict. Supports subcommands as
    defined in ``SUBCOMMANDS``.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--url',
                        type=str,
                        dest='url',
                        default=os.environ.get('OLD_URL', ''),
                        help='The URL of the OLD instance that should receive'
                             ' the data')
    parser.add_argument('--username',
                        type=str,
                        dest='username',
                        default=os.environ.get('OLD_USERNAME'),
                        help='The OLD username to authenticate with')
    parser.add_argument('--password',
                        type=str,
                        dest='password',
                        default=os.environ.get('OLD_PASSWORD'),
                        help='The OLD password to authenticate with')
    subparsers = parser.add_subparsers(help='sub-command help',
                                       dest='subcommand', metavar="<command>")
    for subcommand in SUBCOMMANDS:
        subparser = subparsers.add_parser(subcommand.name,
                                          help=subcommand.help)
        for arg in subcommand.args:
            subparser.add_argument(
                arg.name, help=arg.help, type=arg.type)
        for opt in subcommand.opts:
            subparser.add_argument(
                '--' + opt.name, metavar=opt.metavar, help=opt.help,
                default=opt.default, type=opt.type)
    ret = vars(parser.parse_args())
    ret['url'] = ret['url'].rstrip('/') + '/'
    if not ret['subcommand']:
        parser.print_help()
        sys.exit(0)
    return ret
