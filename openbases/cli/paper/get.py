# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

import sys
from openbases.main import get_client
from openbases.logger import bot

def main(args, options, parser, sep=","):
    
    command = args.cmd
    cli = get_client()
    quiet = not args.debug or args.silent

    
    # Minimum required is <action> paper.md
    if len(command) < 1:
        bot.exit('''Please provide the paper.md file after an action 
                    ob-paper get paper.md)''')

    # If no arguments, show all fields and exit
    if len(command) <=1:
        paper = cli.paper(command[0], quiet=False)

    else:
        paper = cli.paper(command[0], quiet=quiet)

        # For remainder of arguments, get key
        for arg in command[1:]:

            # If the arg is of format arg:field will return field from list
            paper.get(arg, sep=sep)
