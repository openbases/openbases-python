# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

import requests
import argparse
import sys
import os

def get_parser():

    from openbases.main.defaults import BADGE_STYLES, BADGE_COLORS

    parser = argparse.ArgumentParser(description="OpenBases Python Badges",
                                formatter_class=argparse.RawTextHelpFormatter,
                                add_help=False)

    # Global Options
    parser.add_argument('--version', dest="version", 
                        help="show openbases python version", 
                        default=False, action='store_true')


    subparsers = parser.add_subparsers(help='description',
                                       title='actions',
                                       description='actions for openbases',
                                       dest="command", metavar='general usage')

    view = subparsers.add_parser("view",
                                 help="view options for style, labels, etc.")

    view.add_argument('choice', nargs="?",
                      default="labels",
                      choices=['labels', 'styles', 'colors'])

    create = subparsers.add_parser("create",
                                    help="extract values from a paper.md")

    create.add_argument('--cache', dest="longCache", 
                        help="enable long cache for badge. Default False", 
                        default=False, action='store_true')

    create.add_argument('names', nargs="*", 
                        help="label followed by name")

    create.add_argument("--link", dest="link", 
                        default=None, type=str,
                        help='badge link, defaults to openbases.github.io')

    create.add_argument('--style',
                        default="flat",
                        choices=BADGE_STYLES, dest="style")

    create.add_argument('--color',
                        default=None,
                        choices=BADGE_COLORS, dest="color")

    create.add_argument('--fmt',
                        default="markdown",
                        choices=["markdown", "svg"], dest="format")

    return parser


def get_subparsers(parser):
    '''get_subparser will get a dictionary of subparsers, to help with printing help
    '''

    actions = [action for action in parser._actions 
               if isinstance(action, argparse._SubParsersAction)]

    subparsers = dict()
    for action in actions:
        # get all subparsers and print help
        for choice, subparser in action.choices.items():
            subparsers[choice] = subparser

    return subparsers


def version():
    '''version prints the version, both for the user and help output
    '''
    import openbases
    return openbases.__version__
    

def main(main=None):

    parser = get_parser()
    subparsers = get_subparsers(parser)

    def help(return_code=0):
        '''print help, including the software version and exit
        '''
        v = version()
        print("\nOpen Bases Badges Python [v%s]\n" %(v))
        parser.print_help()
        sys.exit(return_code)
    
    try:
        # We capture all primary arguments, and take secondary to pass on
        args, options = parser.parse_known_args()
    except:
        sys.exit(0)

    # If the user wants the version
    if args.version is True:
        print(version())
        sys.exit(0)

    # Does the user want help for a subcommand?
    if args.command == 'create': from .create import main 
    elif args.command == 'view': from .view import main 
    else: help()

    # Pass on to the correct parser
    if args.command is not None:
        main(args=args, options=options)


if __name__ == '__main__':
    main()
