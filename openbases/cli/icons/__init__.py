# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

import requests
import argparse
import sys
import os

def get_parser():

    parser = argparse.ArgumentParser(description="OpenBases Python Icons",
                                formatter_class=argparse.RawTextHelpFormatter,
                                add_help=False)

    # Global Options
    parser.add_argument('--version', dest="version", 
                        help="show openbases python version", 
                        default=False, action='store_true')

    parser.add_argument("--regexp", dest="regexp", default=None,
                        help="regular expression filter for icon name", 
                        type=str)

    parser.add_argument('--help', dest="help", 
                        help="show openbases icons help", 
                        default=False, action='store_true')

    parser.add_argument("--url", dest="url", 
                        default="https://openbases.github.io/openbases-icons/icons.json",
                        help="complete url for json list of icons",
                        type=str)

    parser.add_argument("--n",'--N', dest="N", default=1,
                        help="number of icons to return", 
                        type=int)

    parser.add_argument("--sep", dest="sep", default='\n',
                        help="separator to print icons to screen (default newline)", 
                        type=str)

    return parser


    # Import logger to set
    from openbases.logger import bot
    bot.debug('Logging level %s' %level)
    import openbases

    bot.debug("OpenBases Python Version: %s" % openbases.__version__)

def version():
    '''version prints the version, both for the user and help output
    '''
    import openbases
    return openbases.__version__
    

def main(main=None):

    parser = get_parser()

    def help(return_code=0):
        '''print help, including the software version and exit
        '''
        v = version()
        print("\nOpen Bases Icons [v%s]\n" %(v))
        parser.print_help()
        sys.exit(return_code)
    
    try:
        # We capture all primary arguments, and take secondary to pass on
        args, options = parser.parse_known_args()
    except:
        sys.exit(0)

    # Does the user just want help?
    if args.help:
        help()
        sys.exit(0)

    # If the user wants the version
    if args.version is True:
        print(version())
        sys.exit(0)

    # Get the icons with provided function
    from openbases.main.icons import get_icons
    icons = get_icons(url=args.url, N=args.N, regexp=args.regexp)
    print(args.sep.join(icons))

if __name__ == '__main__':
    main()
