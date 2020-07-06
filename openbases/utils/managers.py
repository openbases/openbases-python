# Copyright (c) 2018-2020, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

from openbases.logger import bot
from openbases.utils import (
    read_file, 
    read_frontmatter,
    read_markdown,
    read_yaml,
    write_yaml
)
import os
import sys
import re

class YamlManager:
    '''a YamlManager will read in markdown with Yaml, or pure yaml, and 
       also save the "rest" of the content, if applicable. We have
       removed the python-frontmatter dependencies along with ruamel in 
       favor of just using pyaml for a cleaner installation.
    '''
    infile = None

    def __init__(self, infile=None):
        ''' on init, if a path is provided we want to tell the user quickly
            if it doesn't exist. If the path exists, we also load.

            Parameters
            ==========
            infile: can be a yml file, a markdown file, or html (with frontmatter)
        '''
        self.loaded = {}
        self.content = ''

        # Did the user provide a path to load?
        if infile is not None:
            self.set_infile(infile)

    def set_infile(self, file_path):
        if self._validate_exists(file_path):
            self.infile = file_path
        else:
            bot.warning("%s does not exist." % infile)

    def _validate_exists(self, infile=None):
        '''first determine if the infile is defined, with preference
           to a potentially new file set by the user at runtime. If not set,
           use previously loaded file. In both cases, first check if the
           file exists. Return False if not defined or doesn't exist

           Parameters
           ==========
           infile: a yaml, html, or markdown file
        '''
        if not infile:
            infile = self.infile

        if infile not in ['', None]:
            if os.path.exists(infile):
                return True
            else:
                bot.warning("%s does not exist." % infile)
        else:
            bot.warning("Input (yml/md/html) file is not defined.")
        return False

    def load(self, file_path=None):
        '''load the input file depending on its extension

           Parameters
           ==========
           file_path: a yaml/html file path, if desired, to override previous
        '''

        if not file_path:
            file_path = self.infile

        # Read in raw content
        if self._validate_exists(file_path):

            # Read in standard yaml
            if re.search('[.](yml|yaml)$', file_path):
                self._load_yaml(file_path)

            # Read in html or markdown
            else:
                self._load_frontmatter(file_path)
                self.content = read_markdown(file_path)
            return self.loaded

# Loading

    def _load_yaml(self, file_path, quiet=True):
        '''load the yaml file

           Parameters
           ==========
           file_path: the yaml file path to read
        '''
        self.loaded = read_yaml(file_path, quiet=quiet)

        
    def _load_frontmatter(self, file_path, quiet=True):
        '''load the yaml as frontend matter from an html file

           Parameters
           ==========
           file_path: an html or markdown file path to read
        '''
        self.loaded = read_frontmatter(file_path, quiet=quiet)


# Saving

    def save_yml(self, output_file, content=None, mode = 'w', ext='yml'):
        '''save a yml file, either provided by the client (content)
           or if not provided, the loaded content.
         
           Parameters
           ==========
           output_file: the output file to save to. Should end in yml or yaml
           content: the content to parse to yaml, can be str or dict
           mode: the mode to use (default is w, write)

        '''
        # If content isn't provided, use client loaded content (must be dict)
        if not content:
            content = self.loaded
        
        # Remove any derivation (won'account for compressed e.g., .tar.gz)
        output_file, _ = os.path.splitext(output_file)

        # Ensure ends with a yml derivative extension
        if not re.search('(%s$)' % ext, output_file):
            output_file = "%s.%s" % (output_file, ext)

        # Write the yaml to file
        write_yaml(output_file, content, mode) 
       
# Reading

    def get_key(self, key='specifications'):
        '''return a portion of the yml file based on key

           Parameters
           ==========
           key: defaults to specifications
        '''
        # If not yet loaded, load it based on extension
        if not hasattr(self, 'loaded'):
            self.load(self.infile)
        return self.loaded[key]
