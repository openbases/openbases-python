# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

def main(args, options=None):

    from openbases.main import Client

    if args.basic is True:
        validator = Client.BasicValidator(infile=args.infile)
    else:
        validator = Client.SpecValidator(infile=args.infile)
    validator.validate_criteria(criteria=args.criteria)
