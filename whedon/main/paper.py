# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/whedon-python

from whedon.logger import bot
from typing import List
from enum import Enum
import os
import re
import sys
  
class Journal(Enum):
    joss = 'joss'
    rse = 'rse'

class Author:
    '''an Author holds a name, orcid id, and affiliation'''
    def __init__(self, 
                 name: str, 
                 orcid: str, 
                 affiliation: str):

        self.name = name

class Paper:
    def __init__(self, 
                 filename: str):

        # Read in paper
        self._filename: str = filename

        # TODO write parser here
