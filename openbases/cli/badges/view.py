# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

from openbases.main.defaults import (
    BADGE_BASE,
    BADGE_COLORS,
    BADGE_LABELS,
    BADGE_STYLES
)

def main(args, options):

    if args.choice.lower() == "colors":
        print('\n'.join(BADGE_COLORS))    
    if args.choice.lower() == "labels":
        print(' '.join(BADGE_LABELS))
    elif args.choice.lower() == "styles":
        print(' '.join(BADGE_STYLES))
