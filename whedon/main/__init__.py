# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/whedon-python

def get_client(quiet=False, debug=False):
    '''
       return the helper function client for Whedon, the fabulous paper bot!

       Parameters
       ==========
       quiet: if True, suppress most output about the client
       debug: turn on debugging mode

    '''
    from .base import Client

    Client.quiet = quiet
    Client.debug = debug

    from .paper import Paper

    # Actions
    Client.paper = Paper

    # Initialize
    cli = Client()
    return cli

Client = get_client()
