# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

from openbases.logger import bot
import requests
import random
import os
import re
import sys


def get_icons(url="https://openbases.github.io/openbases-icons/icons.json",
              regexp=None, 
              N=1):
    '''get a number of icons from the openbases-icons repository, 
       and return a list.
       Parameters
       ==========
       url: the openbases-icons json list (or other) of icons to choose from       
       regexp: a regular expression to filter by (default None, no filter)
       N: the number of icons to return (default is 1)
       Returns
       =======
       icons: a list of filtered (or not) icons      
    '''
    try:
        icons = requests.get(url).json()
    except:
        bot.error("Error parsing json at %s" % url)

    # Does the user want to filter?
    if regexp is not None:
        icons = [i for i in icons if re.search(regexp, i)]

    # The number of results to return
    random.shuffle(icons)
    
    # A search might not have results
    if len(icons) >= N:
        icons = icons[0:0+N]
    return icons
