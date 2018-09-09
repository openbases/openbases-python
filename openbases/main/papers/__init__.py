# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

from openbases.logger import bot
from openbases.utils import read_yaml
import os
import re
import sys
  
class Journal:
    joss = 'joss'
    rse = 'rse'

class Author:
    '''an Author holds a name, orcid id, and affiliation'''
    def __init__(self, 
                 name, 
                 orcid, 
                 affiliation):
        self.name = name
        self.orcid = orcid
        self.affiliation = affiliation


class Paper:

    def __init__(self, filename, quiet=False):

        self._check_inputs(filename)
        self.metadata = read_yaml(filename, quiet=quiet)

    def __str__(self):
        return "<paper.md: %s>" % self.filename

    def __repr__(self):
        return self.__str__()

    def __contains__(self, value):
        return value in self.metadata

    def _check_inputs(self, filename):
        '''check to make sure that filename exists
           Parameters
           ==========
           filename: the markdown file to parse
        '''
        if not os.path.exists(filename):
            bot.exit('Cannot find %s' % filename)
        self.filename = os.path.abspath(os.path.realpath(filename))


    def get(self, key, quiet=True, sep=',', field=None):
        '''return a key from the yaml, default is silent (no print) if doesn't
           exist. If the yaml item is a list with different subfields, then
           field must also be defined.
        '''
        # If the arg is of format arg:field will return field from list
        key = key.split(':')
        if len(key) > 1:
            field = key[1]

        key=key[0]

        if key in self.metadata:
    
            value = self.metadata[key]

            if isinstance(value, (tuple, list)):

                # If the first entry is a dict
                if isinstance(value[0], dict):
                    values = []

                    for entry in value:
                        if field in entry and field is not None:
                            if entry[field]:
                                values.append(entry[field])
                    value = values

                print(sep.join(value))
            else:
                print(self.metadata[key])
