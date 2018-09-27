# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

from openbases.logger import bot

def main(args, options=None):

    from openbases.main import Client

    params = None
    if args.repo is not None:
        if os.path.exists(args.repo):
            params = {'repo', args.repo}
        else:
            bot.warning('%s does not exist.' % args.repo)

    if args.basic is True:
        validator = Client.BasicValidator(infile=args.infile)
    else:
        validator = Client.PaperValidator(infile=args.infile,
                                          params=params)
    validator.validate_criteria(criteria=args.criteria)
