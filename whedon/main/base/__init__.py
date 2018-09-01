# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/whedon-python

from whedon.logger import bot

import json
import sys
import os
import re

from .command import ( generate_bind_list, init_command, run_command )
from .flags import parse_verbosity
from .sutils import ( get_uri, load, setenv, get_filename )
from .logger import ( println,  init_level )
from .generate import RobotNamer

class Client:

    def __str__(self):
        return "[whedon-python]"

    def __repr__(self):
        return self.__str__()

    def version(self):
        '''return the version of singularity
        '''

        if not check_install():
            bot.warning("Singularity version not found, so it's likely not installed.")
        else:
            cmd = ['singularity','--version']
            version = self._run_command(cmd).strip('\n')
            bot.debug("Singularity %s being used." % version)  
            return version


    def _check_install(self):
        '''ensure that singularity is installed, and exit if not.
        '''
        if check_install() is not True:
            bot.error("Cannot find Singularity! Is it installed?")
            sys.exit(1)



# Image Utils
Client.load = load
Client._get_filename = get_filename
Client._get_uri = get_uri
Client.setenv = setenv

# Commands
Client._generate_bind_list = generate_bind_list
Client._init_command = init_command
Client._run_command = run_command

# Flags and Logger
Client._parse_verbosity = parse_verbosity
Client._println = println
Client._init_level = init_level
Client.RobotNamer = RobotNamer()
