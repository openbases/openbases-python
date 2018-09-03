# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/whedon-python

import argparse
import sys
import os


def get_parser():

    parser = argparse.ArgumentParser(description="Whedon Python",
                                formatter_class=argparse.RawTextHelpFormatter,
                                add_help=False)

    # Global Options
    parser.add_argument('--debug','-d', dest="debug", 
                        help="use verbose logging to debug.", 
                        default=False, action='store_true')

    parser.add_argument('--quiet','-q', dest="quiet", 
                        help="suppress all normal output", 
                        default=False, action='store_true')

    parser.add_argument('--version', dest="version", 
                        help="show whedon python version", 
                        default=False, action='store_true')

    subparsers = parser.add_subparsers(help='description',
                                       title='actions',
                                       description='actions for py-whedon',
                                       dest="command", metavar='general usage')

          
    # Paper Parsing

    paper = subparsers.add_parser("paper",
                                   help="extract values from a paper.md")

    paper.add_argument("cmd", nargs="*",
                        help="paper markdown file to parse", 
                        type=str)


    shell = subparsers.add_parser("shell",
                                   help="start an interactive shell with whedon")
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

    # Import logger to set
    from whedon.logger import bot
    bot.debug('Logging level %s' %level)
    import whedon

    bot.debug("Whedon Python Version: %s" % whedon.__version__)

def version():
    '''version prints the version, both for the user and help output
    '''
    import whedon
    return whedon.__version__
    

def main(main=None):

    parser = get_parser()
    subparsers = get_subparsers(parser)

    def help(return_code=0):
        '''print help, including the software version and exit
        '''
        v = version()
        print("\nWhedon Python [v%s]\n" %(v))
        parser.print_help()
        sys.exit(return_code)
    
    if len(sys.argv) == 1:
        help()
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
    elif args.command == 'shell': from .shell import main 
    else: help()

    # Pass on to the correct parser
    if args.command is not None:
        main(args=args, options=options, parser=parser)


if __name__ == '__main__':
    main()
