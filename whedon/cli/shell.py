# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/whedon-python

import sys

def main(args, options, parser):

    lookup = { 'ipython': ipython,
               'python': python,
               'bpython': bpython }

    shells = ['ipython', 'python', 'bpython']

    for shell in shells:
        try:
            return lookup[shell]
        except ImportError:
            pass
    

def ipython(image):
    import whedon
    from IPython import embed
    embed()

def bpython(image):
    import bpython
    import whedon
    bpython.embed(locals_={'whedon': whedon})

def python(image):
    import code
    import whedon
    code.interact(local={"whedon":whedon})
