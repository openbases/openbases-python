# Copyright (c) 2018-2020, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

import os
import sys
from .spinner import Spinner

ABORT = -5
CRITICAL = -4
ERROR = -3
WARNING = -2
LOG = -1
INFO = 1
CUSTOM = 1
QUIET = 0
TEST = 2
VERBOSE = VERBOSE1 = 2
VERBOSE2 = 3
VERBOSE3 = 4
DEBUG = 5

PURPLE = "\033[95m"
YELLOW = "\033[93m"
RED = "\033[91m"
DARKRED = "\033[31m"
CYAN = "\033[36m"

class OpenBasesMessage:

    def __init__(self, MESSAGELEVEL=None):
        self.level = get_logging_level()
        self.history = []
        self.errorStream = sys.stderr
        self.outputStream = sys.stdout
        self.colorize = self.useColor()
        self.colors = {ABORT: DARKRED,
                       CRITICAL: RED,
                       ERROR: RED,    
                       WARNING: YELLOW,  
                       TEST: YELLOW,
                       LOG: PURPLE,      
                       CUSTOM: PURPLE,       
                       DEBUG: CYAN,      
                       'OFF': "\033[0m", # end sequence
                       'CYAN':CYAN,
                       'PURPLE':PURPLE,
                       'RED':RED,
                       'DARKRED':DARKRED,
                       'YELLOW':YELLOW}
                       

    # Colors --------------------------------------------

    def useColor(self):
        '''useColor will determine if color should be added
        to a print. Will check if being run in a terminal, and
        if has support for asci'''
        COLORIZE = get_user_color_preference()
        if COLORIZE is not None:
            return COLORIZE
        streams = [self.errorStream, self.outputStream]
        for stream in streams:
            if not hasattr(stream, 'isatty'):
                return False
            if not stream.isatty():
                return False
        return True

    def addColor(self, level, text):
        '''addColor to the prompt (usually prefix) if terminal
        supports, and specified to do so'''
        if self.colorize:
            if level in self.colors:
                text = "%s%s%s" % (self.colors[level],
                                   text,
                                   self.colors["OFF"])
        return text

    def emitError(self, level):
        '''determine if a level should print to
        stderr, includes all levels but INFO and QUIET'''
        if level in [ABORT,
                     ERROR,
                     WARNING,
                     VERBOSE,
                     VERBOSE1,
                     VERBOSE2,
                     VERBOSE3,
                     DEBUG]:
            return True
        return False

    def emitOutput(self, level):
        '''determine if a level should print to stdout
        only includes INFO'''
        if level in [LOG,
                     INFO]:
            return True
        return False

    def isEnabledFor(self, messageLevel):
        '''check if a messageLevel is enabled to emit a level
        '''
        if messageLevel <= self.level:
            return True
        return False

    def emit(self, level, message, prefix=None, color=None):
        '''emit is the main function to print the message
        optionally with a prefix
        :param level: the level of the message
        :param message: the message to print
        :param prefix: a prefix for the message
        '''
        if color is None:
            color = level

        if prefix is not None:
            prefix = self.addColor(color, "%s " % (prefix))
        else:
            prefix = ""
            message = self.addColor(color, message)

        # Add the prefix
        message = "%s%s" % (prefix, message)

        if not message.endswith('\n'):
            message = "%s\n" % message

        # If the level is quiet, only print to error
        if self.level == QUIET:
            pass

        # Otherwise if in range print to stdout and stderr
        elif self.isEnabledFor(level):
            if self.emitError(level):
                self.write(self.errorStream, message)
            else:
                self.write(self.outputStream, message)

        # Add all log messages to history
        self.history.append(message)

    def write(self, stream, message):
        '''write will write a message to a stream,
        first checking the encoding
        '''
        if isinstance(message, bytes):
            message = message.decode('utf-8')
        stream.write(message)

    def get_logs(self, join_newline=True):
        ''''get_logs will return the complete history, joined by newline
        (default) or as is.
        '''
        if join_newline:
            return '\n'.join(self.history)
        return self.history


    def show_progress(
            self,
            iteration,
            total,
            length=40,
            min_level=0,
            prefix=None,
            carriage_return=True,
            suffix=None,
            symbol=None):
        '''create a terminal progress bar, default bar shows for verbose+
        :param iteration: current iteration (Int)
        :param total: total iterations (Int)
        :param length: character length of bar (Int)
        '''
        percent = 100 * (iteration / float(total))
        progress = int(length * iteration // total)

        if suffix is None:
            suffix = ''

        if prefix is None:
            prefix = 'Progress'

        # Download sizes can be imperfect, setting carriage_return to False
        # and writing newline with caller cleans up the UI
        if percent >= 100:
            percent = 100
            progress = length

        if symbol is None:
            symbol = "="

        if progress < length:
            bar = symbol * progress + '|' + '-' * (length - progress - 1)
        else:
            bar = symbol * progress + '-' * (length - progress)

        # Only show progress bar for level > min_level
        if self.level > min_level:
            percent = "%5s" % ("{0:.1f}").format(percent)
            output = '\r' + prefix + \
                " |%s| %s%s %s" % (bar, percent, '%', suffix)
            sys.stdout.write(output),
            if iteration == total and carriage_return:
                sys.stdout.write('\n')
            sys.stdout.flush()

    # Logging ------------------------------------------

    def named(self, level, message, return_code=-1):
        '''exits if -3 or lower (error or below)'''
        level_int = get_logging_level(level)
        self.emit(level_int, message, level.upper())
        if level_int <= -3:
            sys.exit(return_code)

    def abort(self, message):
        self.emit(ABORT, message, 'ABORT')

    def critical(self, message):
        self.emit(CRITICAL, message, 'CRITICAL')

    def error(self, message):
        self.emit(ERROR, message, 'ERROR')

    def exit(self, message, return_code=1):
        self.emit(ERROR, message, 'ERROR')
        sys.exit(return_code)

    def warning(self, message):
        self.emit(WARNING, message, 'WARNING')

    def log(self, message):
        self.emit(LOG, message, 'LOG')

    def custom(self, prefix, message, color=PURPLE):
        self.emit(CUSTOM, message, prefix, color)

    def info(self, message):
        self.emit(INFO, message)

    def newline(self):
        return self.info("")

    def test(self, message):
        self.emit(TEST, message, "TEST")

    def verbose(self, message):
        self.emit(VERBOSE, message, "VERBOSE")

    def verbose1(self, message):
        self.emit(VERBOSE, message, "VERBOSE1")

    def verbose2(self, message):
        self.emit(VERBOSE2, message, 'VERBOSE2')

    def verbose3(self, message):
        self.emit(VERBOSE3, message, 'VERBOSE3')

    def debug(self, message):
        self.emit(DEBUG, message, 'DEBUG')

    def is_quiet(self):
        '''is_quiet returns true if the level is under 1
        '''
        if self.level < 1:
            return False
        return True


    # Terminal ------------------------------------------

    def table(self, rows, col_width=2):
        '''table will print a table of entries. If the rows is 
        a dictionary, the keys are interpreted as column names. if
        not, a numbered list is used.
        '''

        labels = [str(x) for x in range(1,len(rows)+1)]
        if isinstance(rows, dict):
            labels = list(rows.keys())
            rows = list(rows.values())

        for row in rows: 
            label = labels.pop(0)
            label = label.ljust(col_width)
            message = "\t".join(row)
            self.custom(prefix=label,
                        message=message)
        


def get_logging_level(level=None):
    '''configure a logging to standard out based on the user's
    selected level, which should be in an environment variable called
    MESSAGELEVEL. if MESSAGELEVEL is not set, the info level
    (1) is assumed (all informational messages).
    '''
    if level is None:
        level = os.environ.get("MESSAGELEVEL", "1") # INFO
    level = level.upper()

    if level.startswith("VERBOSE"):
        return VERBOSE3

    levels = {'CRITICAL': CRITICAL,
              'ABORT': ABORT,
              'ERROR': ERROR,
              'WARNING': WARNING,
              'LOG': LOG,
              'INFO': INFO,
              'TEST': TEST,
              'QUIET': QUIET,
              'DEBUG': DEBUG}

    # Get a logging level (int) if it's in the lookup
    logging_level = levels.get(level)

    # Otherwise, return custom level for user
    if logging_level is None:
        logging_level = int(level)

    return logging_level


def get_user_color_preference():
    COLORIZE = os.environ.get('SINGULARITY_COLORIZE', None)
    if COLORIZE is not None:
        COLORIZE = convert2boolean(COLORIZE)
    return COLORIZE


def convert2boolean(arg):
    '''convert2boolean is used for environmental variables that must be
    returned as boolean'''
    if not isinstance(arg, bool):
        return arg.lower() in ("yes", "true", "t", "1", "y")
    return arg


OpenBasesMessage.spinner = Spinner()
bot = OpenBasesMessage()
