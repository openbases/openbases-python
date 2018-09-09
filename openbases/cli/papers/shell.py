# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

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
    import openbases
    from IPython import embed
    embed()

def bpython(image):
    import bpython
    import openbases
    bpython.embed(locals_={'openbases': openbases})

def python(image):
    import code
    import openbases
    code.interact(local={"openbases":openbases})
