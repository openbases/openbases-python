# Copyright (c) 2018-2020, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

from openbases.logger import bot

import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

      
################################################################################
# Supporting (shared) functions ################################################
################################################################################

def update_environment(params=None, prefix='OPENBASESENV_'):
    '''update environment will put any environment variables found in the 
       params (dictionary) into the environment, expected to be found by
       the various functions. The variables must start with OPENBASESENV_
    '''
    if params is not None:
        for key,value in params.items():
            if key.startswith(prefix):
                if value:
                    bot.debug('Exporting %s=%s' %(key, value))
                    os.putenv(key, value)
                    os.environ[key] = value
            else:
                bot.warning('Skipping parameter %s for environment' % key)


def validate_loads(infile):
    '''determine if a file can load without error. If yes, return manager.
       If not, return None.
           
       Parameters
       ==========
       infile: the input file to attempt loading with the YamlManager,
       can be yaml or front end matter in html.
    '''
    from openbases.utils.managers import YamlManager

    manager = YamlManager(infile)
    try:
        manager.load()
        return manager
    except:
        bot.warning('Load of %s not successfully, using default' % infile)


def load_criteria(self, criteria=None):
    '''load a criteria.yml file. If not specified, load (or reload)
       default provided by package.

       Parameters
       ==========
       criteria: a yml specification for criteria. If not provided, use
        default at criteria/specification.yml. If you need help creating
       a new criteria (that might be added to defaults) please open an issue
    '''
    # First pass - criteria file defined, and exists
    if criteria is not None:
        if os.path.exists(criteria):
            criteria = self.validate_exists(criteria)
            
    # Second pass, use default provided by library
    if criteria is None:
         criteria = self.default_criteria

    # Attempt to load (and validate) the criteria (returns YamlManager)
    self.criteria = validate_loads(criteria)

    # Again fall back to default if error loading user-provided
    if self.criteria is None:
        self.criteria = validate_loads(default_criteria)

    basename = os.path.basename(self.criteria.infile)

    bot.info('[criteria:%s]' % basename)
    return self.criteria.load()


def validate_criteria(self, criteria=None, infile=None, params=None):
    '''validate an infile (or already loaded one) against criteria.

       Parameters
       ==========
       infile: an input specification file
       criteria: a loaded (json/dict) or criteria, or html/yml file
    '''   
    from openbases.utils import load_module

    # If criteria not set, use default
    if criteria is None:
        self.load_criteria()

    # Update environment with params for validation
    if params is not None:
        bot.info('Updating custom params with %s' % params)
        self.params.update(params)

    # Update the environment
    update_environment(params=self.params, prefix='OPENBASESENV_')

    # Read in the criteria - any errors will fall back to default
    if not isinstance(criteria, dict):
        criteria = self.load_criteria(criteria)

    # Case 1: input file provided at runtime
    if infile is not None:
        self.load(infile)
 
    # Case 2: Didn't successfully load, fall back to previously loaded
    if not hasattr(self, 'spec'): # infile didn't load successfully
        if hasattr(self, 'infile'):
            self.load(infile)

    # Case 3: Still no infile! Exit
    if not hasattr(self, 'spec'):
        bot.error('Please provide an infile to function, or load()')

    if "checks" not in criteria:
        bot.error('criteria is missing "checks" section, exiting.')

    # Default missing function
    missing_function = 'openbases.main.validate.criteria.base.missing'

    # Turn status into meaningful message for user
    lookup = {True: 'pass', False: 'fail', None: 'null'}         

    # Loop through checks, run against specification file
    for group, checks in criteria['checks'].items():

        print('[group|start:%s]' % group)
        values = dict()
        [values.update(dict(check)) for check in checks]
            
        # Obtain values, the only required is the function
        name = values.get('name', self.robot.generate())  
        level = values.get('level', 'warning').upper()
        function = values.get('function', missing_function)
        kwargs = values.get('kwargs')
        envars_list = values.get('environment')
        envars = dict()

        # If we have environment vars from criteria, export them
        if envars_list is not None:
            [update_environment(e) for e in envars_list]

        # If we have a function provided in the configuration yaml
        function_name = function
        function = load_module(function)

        if kwargs is None:
            valid = function(self.spec)
        else:
            values = dict()
            [values.update(dict(kwarg)) for kwarg in kwargs]
            valid = function(self.spec, **values)

        print('[check:%s]' % name)
        print(' test:function %s' % function_name)
        print(' test:result %s' % lookup[valid])

        if valid:
            bot.test("PASSED %s" % function_name)
        else:
            print(' test:level %s' % level)
            bot.named(level, function_name)
            if not valid:
                sys.exit(1)

        print('[group|end:%s]' % group)

    print('ALL TESTS PASSING')
