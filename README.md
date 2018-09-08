# OpenBases Python

[![PyPI version](https://badge.fury.io/py/openbases.svg)](https://badge.fury.io/py/openbases)
[![CircleCI](https://circleci.com/gh/openbases/openbases-python.svg?style=svg)](https://circleci.com/gh/openbases/openbases-python)

![docs/img/robot.png](https://github.com/openbases/openbases-python/raw/master/docs/img/robot.png)

-------------------------------------------------------------------------------

This is a small module with helper functions and scripts for using Open Bases tools. 
Please contribute at [openbases/openbases-python](https://www.github.com/openbases/openbases-python) on
Github.

> Just... no!

![docs/img/before.png](https://github.com/openbases/openbases-python/raw/master/docs/img/before.png)

> Better!

![docs/img/upgrade.png](https://github.com/openbases/openbases-python/raw/master/docs/img/upgrade.png)

# Quick Start

To install

```bash
git clone https://www.github.com/openbases/openbases-python
cd openbases-python
python setup.py install
```
```
pip install openbases
```

There are different console entry points depending on the kind of functions that you need.

## Open Bases Paper

`ob-paper` is the console entry point for interacting with a paper, typically a paper.md.

```bash
$ ob-paper help

Open Bases Paper Python [v0.0.0]

usage: ob-paper [--debug] [--quiet] [--version] general usage ...

OpenBases Python Paper

optional arguments:
  --debug, -d    use verbose logging to debug.
  --quiet, -q    suppress all normal output
  --version      show openbases python version

actions:
  actions for openbases

  general usage  description
    get          extract values from a paper.md
    shell        start an interactive shell with openbases paper
```

For complete usage, please see:

 - [usage documentation](https://openbases.github.io/openbases-python/html/usage.html) 
 - [documentation](https://openbases.github.io/openbases-python/)
 - implementation in [openbases-pdf](https://www.github.com/openbases/openbases-pdf/) and [builder-pdf](https://www.github.com/openbases/builder-pdf/)

Have fun!
