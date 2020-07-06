# Copyright (c) 2018-2020, Vanessa Sochat All rights reserved.
# This code was originally written *by same author* for openschemas and shared
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

from openbases.logger import bot
from openbases.main.validate.helpers import (
    validate_loads,
    validate_criteria,
    load_criteria
)

import os
import sys

here = os.path.abspath(os.path.dirname(__file__))


################################################################################
# Validator Classes ############################################################
################################################################################

class BasicValidator:
    '''the basic validator doesn't care about the input file extensions,
       and gives the user more freedom to write custom validators using it. 
       We only validate that the file exists.
    '''
    default_criteria = '%s/criteria/dummy.yml' % here
    params = {}

    def __str__(self):
        return '[basic-validator:%s]' % self.name

    def __repr__(self):
        return self.__str__()

    def __init__(self, infile):

        from openbases.main.base import RobotNamer
        self.load(infile)
        self.robot = RobotNamer()

# Loading

    def load(self, infile):
        '''load an input file, meaning checking for the file's existence.
           It's up to the user (if desired) to load the file in their 
           validation functions, or write a custom _load() function.

           Parameters
           ==========
           infile: the input file to load
        '''
        # Step 0. of validation checks exist and load of file
        self.infile = self.validate_exists(infile)
        if self.infile is not None:

            # If the fie exists, we can store metadata about it
            self.name = os.path.basename(self.infile)
            self.folder = os.path.dirname(self.infile)
            print('Input file provided under attribute "infile"')


# Validation

    def validate_exists(self, infile):
        '''determine filename of infile, validate that exists. 

           Parameters
           ==========
           infile: the name of the specification / yaml file
           extensions: a list of valid extensions
        '''
        if os.path.exists(infile):
            print('Found %s, valid name' % infile)
            return os.path.abspath(infile)

    
class PaperValidator:
    '''the spec validator can "sniff" a file based on extension, and validate
       the file based on the extension, or have one of the specific type 
       validators (html, yaml) called directly. There are two steps.

       Step 0. validates the file itself. Does it exist? Load without error?
       Step 1. validates the file against a criteria.yml, default is provided
    '''

    default_criteria = '%s/criteria/paper.yml' % here
    params = {}
    folder = None
    name = None

    def __str__(self):
        return '[paper-validator:%s]' % self.name

    def __repr__(self):
        return self.__str__()

    def __init__(self, infile, bibfile=None):
        from openbases.main.base import RobotNamer
        self.load(infile)
        self.robot = RobotNamer()

        # If there is an error or file not found, is None
        self.bib = self.load_bib(bibfile)
        
# Loading

    def load(self, infile):
        '''load an input file, meaning checking for the file's existence,
           that it has a default extension, and loading it into the "spec"
           via the YamlManager (that can handle frontmatter in a html or
           standard yml/yaml

           Parameters
           ==========
           infile: the input file to load
        '''
        # Step 0. of validation checks exist and load of file
        self.infile = self.validate_exists(infile)
        if self.infile is not None:

            # If the fie exists, we can store metadata about it
            self.name = os.path.basename(self.infile)
            self.folder = os.path.dirname(self.infile)

            # We only return a manager if the file loads cleanly.
            self.spec =  validate_loads(infile) # returns YamlManager
            if self.spec is not None:
                return self.spec.load()

    def load_bib(self, bibfile, envar="OPENBASESENV_BIBFILE"):
        '''load the bibfile, and derive from the paper file if it was loaded
           first. This means checking for the file's existence,
           that it has a default extension, and loading it into the "spec"
           
           Parameters
           ==========
           infile: the input file to load
        '''
        # If the bibfile is None, then we try deriving based on paper.md
        if bibfile is None:
            if self.folder is not None:
                bibfile = os.path.join(self.folder, 'paper.bib')
    
        self.bibfile = self.validate_exists(bibfile, extensions=['bib'])
        if self.bibfile is not None:

            # If we have a bibfile, export to environment for tests
            os.putenv(envar, self.bibfile)
            os.environ[envar] = self.bibfile
            self.params.update({'bibfile': self.bibfile})

            # We show error to user, but don't exit here
            from openbases.utils import read_bibtex
            return read_bibtex(self.bibfile)

# Validation

    def validate_exists(self, infile, extensions=None):
        '''determine filename of infile 
           based on Specification Name (and extension). If the extension
           doesn't end in yml/yaml or html, it's not valid (and note
           we will need to add support for reading json). If valid,
           return the filename. If not, return None.

           Parameters
           ==========
           infile: the name of the specification / yaml file
           extensions: a list of valid extensions
        '''
        if extensions == None:
            extensions = ['yaml', 'yml', 'html', 'md', 'markdown']

        if not isinstance(extensions, (list,tuple)):
            extensions = [extensions]

        for ext in extensions:
            if infile.endswith(ext) and os.path.exists(infile):
                print('Found %s, valid name' % infile)
                return os.path.abspath(infile)

        # Tell the user doesn't have valid, show which are
        valids = ','.join(extensions)
        print('%s does not have a valid extension (%s)' % (infile, valids))


BasicValidator.load_criteria = load_criteria
BasicValidator.validate_criteria = validate_criteria
PaperValidator.load_criteria = load_criteria
PaperValidator.validate_criteria = validate_criteria
