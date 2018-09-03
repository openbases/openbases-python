# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/whedon-python

import sys
from whedon.main import get_client
from whedon.logger import bot

def main(args, options, parser, sep=","):
    
    command = args.cmd
    cli = get_client()
    quiet = not args.debug or args.silent

    # Minimum required is <action> paper.md
    if len(command) < 2:
        bot.exit('''Please provide the paper.md file after an action 
                    py-whedon <action> paper.md)''')

    # If no arguments, show all fields and exit
    if len(command) <=2:
        paper = cli.paper(command[1], quiet=False)

    else:
        action = command[0]
        paper = cli.paper(command[1], quiet=quiet)

        if action == 'pdf':
            print('render pdf here')
        
        elif action == 'get':

            # For remainder of arguments, get key
            for arg in command[1:]:

                # If the arg is of format arg:field will return field from list
                paper.get(arg, sep=sep)
