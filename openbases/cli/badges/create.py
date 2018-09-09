# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

import sys
from openbases.main.badges import Badge
from openbases.logger import bot

def main(args, options):
    
    if len(args.names) < 2:
        bot.error('Must provide a label and name, e.g., experiment labjs')

    badge = Badge(label=args.names[0], 
                  name=args.names[1],
                  longCache=args.longCache,
                  link=args.link,
                  style=args.style)

    # Return the desired format to the user
    if args.format == "svg":
        print(badge.get_svg())
    else:
        print(badge.get_markdown())
