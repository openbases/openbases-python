# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/whedon-python

import sys
from whedon.main import get_client
from whedon.logger import bot

def main(args, options, parser):
    
    command = args.cmd
    cli = get_client()

    if command[0] == 'pdf':

        # Minimum required is paper.md
        if len(command) < 2:
            bot.exit('Please provide the paper.md file after pdf.')
        paper = cli.paper(command[1])
        
        # For remainder of arguments, get key
        for arg in command[1:]:
            print(arg)
