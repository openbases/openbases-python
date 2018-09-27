# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

from openbases.logger import bot
import os

def main(args, options=None):

    from openbases.main import Client

    params = None
    if args.repo is not None:
        if os.path.exists(args.repo):
            params = {'repo', args.repo}
        else:
            bot.warning('%s does not exist.' % args.repo)

    # Ensure that paper exists
    paper = args.infile
    if not os.path.exists(paper):
        bot.warning('%s does not exist.' % paper)
    paper = os.path.abspath(paper)     

    if args.basic is True:
        validator = Client.BasicValidator(infile=paper)
    else:
        validator = Client.PaperValidator(infile=paper)
    validator.validate_criteria(criteria=args.criteria, 
                                params=params)
