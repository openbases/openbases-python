# OpenBases Python

[![PyPI version](https://badge.fury.io/py/openbases.svg)](https://badge.fury.io/py/openbases)
[![CircleCI](https://circleci.com/gh/openbases/openbases-python.svg?style=svg)](https://circleci.com/gh/openbases/openbases-python)

![docs/img/logo-small.png](https://github.com/openbases/openbases-python/raw/master/docs/img/logo-small.png)

-------------------------------------------------------------------------------

This is a small module with helper functions and scripts for using Open Bases tools. 
Please contribute at [openbases/openbases-python](https://www.github.com/openbases/openbases-python) on
Github. Documentation is [here](https://openbases.github.io/openbases-python/html/usage.html) 


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

## Open Bases Icons

Get an icon from [openbases-icons](https://www.github.com/openbases/openbases-icons)

```bash
$ ob-icons
https://openbases.github.io/openbases-icons/flaticon/sea-life-collection/squid.svg
```
```bash
$ ob-icons --help

Open Bases Icons [v0.0.1]

usage: ob-icons [--version] [--regexp REGEXP] [--help] [--url URL] [--n N]
                [--sep SEP]

OpenBases Python Icons

optional arguments:
  --version        show openbases python version
  --regexp REGEXP  regular expression filter for icon name
  --help           show openbases icons help
  --url URL        complete url for json list of icons
  --n N, --N N     number of icons to return
  --sep SEP        separator to print icons to screen (default newline)
```

[icons usage](https://openbases.github.io/openbases-python/html/usage.html#icons) 

## Open Base Badges

Generate badges and strings of badges with the `ob-badge` entrypoint

```bash
$ ob-badge 

Open Bases Badges Python [v0.0.3]

usage: ob-badge [-h] [--version] general usage ...

OpenBases Python Badges

optional arguments:
  -h, --help     show this help message and exit
  --version      show openbases python version

actions:
  actions for openbases

  general usage  description
    view         view options for style, labels, etc.
    create       extract values from a paper.md
```
```
$ ob-badge create experiment labjs
![https://img.shields.io/badge/experiment-labjs-%23eaab1b.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io](https://img.shields.io/badge/experiment-labjs-%23eaab1b.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io)
```
![https://img.shields.io/badge/experiment-labjs-%23eaab1b.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io](https://img.shields.io/badge/experiment-labjs-%23eaab1b.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io)

[badges usage](https://openbases.github.io/openbases-python/html/usage.html#badges) 

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
