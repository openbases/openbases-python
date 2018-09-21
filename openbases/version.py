# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

__version__ = "0.0.52"
AUTHOR = 'Vanessa Sochat'
AUTHOR_EMAIL = 'vsochat@stanford.edu'
NAME = 'openbases'
PACKAGE_URL = "http://www.github.com/openbases/openbases-python"
KEYWORDS = 'openbases, markdown, pandoc'
DESCRIPTION = "openbases python helper functions for https://openbases.github.io"
LICENSE = "LICENSE"

INSTALL_REQUIRES = (
    ('pyaml', {'min_version': '17.12.1'}),
    ('requests', {'min_version': None})
)

TEST_REQUIRES = (
    ('pytest', {'min_version': None}),
    ('requests', {'min_version': None})
)

