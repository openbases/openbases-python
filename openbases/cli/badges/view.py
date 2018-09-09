# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

from openbases.main.defaults import (
    BADGE_BASE,
    BADGE_LABELS,
    BADGE_STYLES
)

def main(args, options):
    
    if "label" in args.choice[0].lower():
        print(' '.join(BADGE_LABELS))
    elif "style" in args.choice[0].lower():
        print(' '.join(BADGE_STYLES))
    else:
        print(BADGE_BASE)
