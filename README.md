# Whedon Python

[![PyPI version](https://badge.fury.io/py/whedon.svg)](https://badge.fury.io/py/whedon)
[![CircleCI](https://circleci.com/gh/openbases/whedon-python.svg?style=svg)](https://circleci.com/gh/openbases/whedon-python)

![docs/img/robot.png](https://github.com/openbases/whedon-python/raw/master/docs/img/robot.png)

-------------------------------------------------------------------------------

This is a small module with helper functions for using Whedon. Please contribute at
[openbases/python-whedon](https://www.github.com/openbases/whedon-python) on
Github.

> Just... no!

![docs/img/whedon-before.png](https://github.com/openbases/whedon-python/raw/master/docs/img/whedon-before.png)

> Better!

![docs/img/whedon-upgrade.png](https://github.com/openbases/whedon-python/raw/master/docs/img/whedon-upgrade.png)

# Quick Start

To install

```bash
git clone https://www.github.com/openbases/whedon-python
cd whedon-python
python setup.py install
```
```
pip install whedon
```

And then use:

```bash
$ py-whedon help

Whedon Python [v0.0.0]

usage: py-whedon [--debug] [--quiet] [--version] sep general usage ...

Whedon Python

positional arguments:
  sep            separator for printing lists, etc. (default ,)

optional arguments:
  --debug, -d    use verbose logging to debug.
  --quiet, -q    suppress all normal output
  --version      show whedon python version

actions:
  actions for py-whedon

  general usage  description
    paper        extract values from a paper.md
    shell        start an interactive shell with whedon
```

For complete usage, please see:

 - [usage documentation](https://openbases.github.io/whedon-python/html/usage.html) 
 - [documentation](https://openbases.github.io/whedon-python/)
 - implementation in [whedon docker](https://www.github.com/openbases/whedon/). 

Have fun!
