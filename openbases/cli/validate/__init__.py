#!/usr/bin/env python3

# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# This code was originally written *by same author* for openschemas and shared
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

import argparse
import sys
import os

def get_parser():

    parser = argparse.ArgumentParser(description="OpenBases Python Validator",
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

    paper = subparsers.add_parser("paper",
                                   help="validate a paper.md")

    paper.add_argument('--criteria', nargs='?',
                        help="define custom entry criteria (critera.yml)", 
                        default=None, type=str)

    paper.add_argument('--infile', nargs='?',
                        help="input file to validate", 
                        default=None, type=str)

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
        print("\nOpen Bases Validator Python [v%s]\n" %(v))
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
    if args.command == 'paper': from .paper import main 
    else: help()

    # Pass on to the correct parser
    if args.command is not None:
        main(args=args, options=options)


if __name__ == '__main__':
    main()
