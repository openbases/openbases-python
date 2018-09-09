# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

from openbases.logger import bot
import os
import re
import requests
import sys

from openbases.main.defaults import (
    BADGE_BASE,
    BADGE_COLORS,
    BADGE_LABELS,
    BADGE_STYLES
)

try:
    from urllib import urlencode
except:
    from urllib.parse import urlencode

class Badge:

    def __init__(self, 
                 label,
                 name, 
                 link=None, 
                 longCache=True,
                 style=None):

        '''create a new badge for an open base. The only required fields are the
           subject and status (e.g., experiment labjs) and the rest have 
           reasonably set defaults

           Parameters
           ==========
           label: the type of badge, if not one in openbases, "other" is used.
           This label corresponds with "subject" used by shields.io
           name: the name for the badge, corresponds with "status" in shields.io
        '''

        self.params = {"style": "flat",
                       "link": "https://openbases.github.io"}

        self._init_design(label, name)
        self._init_cache(longCache)
        self.set_style(style)
        self.set_link(link)

    def get_style(self):
        return self.params["style"]

    def get_link(self):
        return self.params["link"]

    def set_style(self, style):
        if style in BADGE_STYLES:
            self.params["style"] = style

    def set_link(self, link):
        if link is not None:
            self.params["link"] = link

    def _init_design(self, subject, status):
        '''the base of the design is the subject, and status.
        
           Parameters
           ==========
           subject: the type of open base, e.g., "experiment"
           status: the name of the open bsae, e.g., "labjs"
        '''
            
        # Look up the color based on the subject
        subject = subject.lower()
        status = status.replace("-","_")

        # Save parameters for later
        self.name = subject
        self.label = status

        color = BADGE_COLORS.get(subject, BADGE_COLORS["other"])
            
        # https://img.shields.io/badge/<SUBJECT>-<STATUS>-<COLOR>.sv
        self.baseurl = BADGE_BASE % (subject, status, color)
        bot.debug(self.baseurl)
        return self.baseurl

    def _init_cache(self, enable=False):
        '''add a variable to turn on longCache'''
        if enable is True:
            self.params['longCache'] = "true"

    def get_url(self):
        # Add the parameters
        params = urlencode(self.params)
        return "%s?%s" % (self.baseurl, params)

    def get_markdown(self):
        '''return markdown of the badge based on the generated base string
        '''
        url = self.get_url()
        return "![%s](%s)" %(url, url)

    def get_svg(self):
        '''return an svg of the badge by retrieving the url'''
        url = self.get_url()
        return requests.get(url).text

    def __str__(self):
        return "<badge: %s>" % self.baseurl

    def __repr__(self):
        return self.__str__()
