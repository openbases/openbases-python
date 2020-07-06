# Copyright (c) 2018-2020, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

# Validation functions for openbases papers.

# The format of this file is based on levels, messages, and functions.
# It is intended to be run against a single yml file loaded as json. The
# intention is to make it easy to write and understand these criteria. The
# format is the following:

# SECTION DEFINITIONS
# - the version of the criteria format is under version
# - checks: is the group that is run for validation
# - the first field under checks is for a group of checks. You can name it
#   whatever is appropriate for your need (e.g., titles)
# - name: corresponds to the name of the subsection (a check)
# - function: is the python module --> function that is run
# - level: is the python logger level to emit.
# - the subsuections underneath are also different named (individual) checks
# - args: should be a list of named (or not named) arguments.

# It's helpful to look at the example below and then reference the above!

# WRITING FUNCTIONS

# Each function should have the first variable be the file being checked, or
# the loaded specification as a json-derivative (python dictionary). If 
# running from the command line, you would need to provide the path to this
# criteria and the file. If you want to save the redundant loads, you can run
# the validations from within python (and provide the data structure as 
# variable.

# Each of the checks (the functions that you write and provide) should return
# True (passed) or False (failed). You can print output to help the user to
# your heart's content.

from openbases.logger import bot
from openbases.utils import ( find_files, read_file )
import re
import os

def test_length(spec, **kwargs):
    '''the paper should be betwee 250 and 1000 characters.

        length:
          - name: Check that the paper is between 250-1000 characters
          - level: warning
          - function: openbases.main.papers.tests.test_length
    ''' 
    paper = spec.content

    min_length = int(kwargs.get('min_length', 250))
    max_length = int(kwargs.get('max_length', 1000))

    # This currently includes all markdown, additional text, etc.
    bot.warning('Length of paper is approximately %s chars.' % len(paper))
    if len(paper) < min_length:
        bot.warning("Paper (including markdown) is < %s chars" % min_length)

    elif len(paper) > max_length:
        bot.warning("Paper estimated > %s characters" % max_length)

    return True


def test_authors(spec, **kwargs):
    '''the paper header should have a list of authors, each with affiliation,
       name, and orcid.

        authors:
          - name: Submission must include a list of authors, well formatted
          - level: error
          - function: openbases.main.papers.tests.test_authors
    ''' 
    header = spec.loaded

    if "authors" not in header:
        bot.exit('authors missing in front end paper matter.')    
    if not isinstance(header['authors'], list):
        bot.exit('authors in front end paper matter should be a list') 

    # Regular expression for orcid
    regexp = "[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}"

                       # key           type has_regexp  regexp 
    required_fields = ('affiliation', 'orcid', 'name')
    for field in required_fields:
        for author in header['authors']:
            if field not in author:
                bot.exit('Paper is missing a required author field %s' % field)
                print(author)
            if field == 'orcid':
                if not re.search(regexp, author[field]):
                    bot.error('Orcid regular expression failed %s' % author[field])
                    print(author)
    return True


def test_license(spec, envar='OPENBASESENV_REPO_BASE', **kwargs):
    '''required_structure looks for a schema's required fields, and issues
       an exit if doesn't exist. To implement this in a criteria.yml:

        license:
          - name: An OSI license is included in the repository
          - level: error
          - function: openbases.main.papers.tests.test_license
          - environment:
             - OPENBASESENV_REPO_BASE: null

    Templates taken from https://github.com/licenses/license-templates
    '''
    # By default, not found.
    found = False

    # A list of terms to indicate open source licenses
    LICENSE_FLAGS = ["GNU Affero General Public License",
                     "MIT License",
                     "Apache",
                     "Creative Commons",
                     "CC0", # Creative Commans 1.0
                     "CC1",
                     "General Public License",
                     "The GNU General Public License",
                     "GPL-2.0",
                     "Free Software Foundation",
                     "GNU LESSER GENERAL PUBLIC",
                     "GPL-3.0",
                     "Mozilla Public License",
                     "free and unencumbered software released into the public",
                     "www.gnu.org",
                     "This program is free software",
                     "www.wtfpl.net",
                     "COMMON DEVELOPMENT AND DISTRIBUTION",  # CCDL
                     '"AS IS"', # bsd 22
                     'as-is'] # zlib

    repo_base = os.environ.get(envar)
    if repo_base is not None:
        if os.path.exists(repo_base):
            licenses = find_files(repo_base, 'LICENSE')
            for license in licenses:
                content = read_file(license, readlines=False)
                matches = [x for x in LICENSE_FLAGS 
                           if re.search(x.lower(), content.lower())]
                if len(matches) > 0:
                    message = 'Found Open Source license flags! %s'
                    bot.info(message %','.join(matches))
                    print(content)
                    found = True
        else:
            bot.error('%s does not exist! Skipping test.' % repo_base)

    else:
        bot.error('''Did not find %s export for repository base! 
                     Skipping license check''' %envar)

    return found



def test_contributing(spec, envar='OPENBASESENV_REPO_BASE', **kwargs):
    '''look for CONTRIBUTING.md or similar


        contributing:
          - name: Software has CONTRIBUTING.md
          - level: error
          - function: openbases.main.papers.tests.test_contributing
          - environment:
             - OPENBASESENV_REPO_BASE: null

    Templates taken from https://github.com/licenses/license-templates
    '''
    # By default, not found.
    found = False

    repo_base = os.environ.get(envar)
    if repo_base is not None:
        if os.path.exists(repo_base):
            contenders = find_files(repo_base, 'LICENSE|license|License')
            if len(contenders) > 0:
                bot.info('Found CONTRIBUTING file(s) in repository!')
                found = True
    return found


def test_references(spec, envar="OPENBASESENV_BIBFILE", **kwargs):
    '''required_structure looks for a schema's required fields, and issues
       an exit if doesn't exist. To implement this in a criteria.yml:
 
        references:
          - name: References are included and complete
          - level: warning
          - function: openbases.main.papers.tests.test_references

    Templates taken from https://github.com/licenses/license-templates
    '''
    from openbases.utils import read_bibtex

    complete = True
    bibfile = os.environ.get(envar)

    # We must have a bibfile
    if not "bibfile" and "bibfile" not in kwargs:
        bot.warning('Bibfile not provided as argument, skipping test')
        return complete

    required_fields = ['title', 'month', 'year']

    bib = read_bibtex(bibfile)
    for entryid, entry in bib.items():
        bot.info('Testing bibliography entry %s' % entryid)
        bot.info('  type: %s' % entry.type)
        for field in entry.fields:
            if field not in entry.fields:
                bot.error('  %s is missing field %s' % (entryid, field))
                complete = False
            if entry.fields[field] in [None, '']:
                bot.error('  %s has empty field %s' % (entryid, field))
                complete = False
        bot.info('  title: %s' % entry.fields['title'])

    return complete
