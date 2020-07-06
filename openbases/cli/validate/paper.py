# Copyright (c) 2018-2020, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

from openbases.logger import bot
import os

def main(args, options=None):

    from openbases.main import Client

    params = None
    repo = args.repo
    if repo is None:
        repo = os.getcwd()
    repo = os.path.abspath(repo)

    if os.path.exists(repo):
        bot.info("repo: %s" % repo)
        os.environ['OPENBASESENV_REPO_BASE'] = repo
        os.putenv('OPENBASESENV_REPO_BASE', repo)
    else:
        bot.warning('%s does not exist.' % repo)

    # Ensure that paper exists
    paper = args.infile
    if not paper:
        bot.exit('You must specify a paper with --infile')
    if not os.path.exists(paper):
        bot.exit('%s does not exist.' % paper)
    paper = os.path.abspath(paper)     

    if args.basic is True:
        validator = Client.BasicValidator(infile=paper)
    else:
        validator = Client.PaperValidator(infile=paper)
    validator.validate_criteria(criteria=args.criteria, 
                                params=params)
