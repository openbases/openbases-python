# Docker

The `openbases` python module is also available as a 
[Docker Image](https://hub.docker.com/r/openbases/openbases/), meaning you don't 
need to install anything locally (other than having Docker). Hooray!

Running the container shows it's entrypoints. It basically will direct you to
the various modules provided by openbases:

```bash
$ docker run openbases/openbases
Usage:

    This entrypoint connects you to the executables provided by openbases
    Python within the container. You could just as easily exec one of these
    commands to the container, but this entrypoint makes this easy to do
    with just 'run':

         ob-validate: validate a paper.md for an Open Journals submission
           docker run <container> validate --help
           docker run <container> validate

         ob-icons: produce
           docker run <container> icons --help
           docker run <container> icons

         ob-paper: generate a paper.pdf for an Open Journals submission
           docker run <container> paper --help
           docker run <container> paper

         ob-badges: generate markdown badges!
           docker run <container> badges --help
           docker run <container> badges

         or just ask to see this global help!
         docker run <container> help
```

For each of the above, note that you can run the module and ask for additional `--help`
to get usage, and see more detailed usage on the [usage page](https://openbases.github.io/html/usage.html).


## Validate

What options do we have?

```bash
$ docker run openbases/openbases validate --help
Open Bases Validator Python [v0.0.53]

usage: ob-validate [--version] [--repo [REPO]] [--basic] general usage ...

OpenBases Python Validator

optional arguments:
  --version      show openbases python version
  --repo [REPO]  repository base, if needed to check for files
  --basic        a basic validator, for custom usage

actions:
  actions for openbases

  general usage  description
    paper        validate a paper.md
```

To validate a paper, we need to bind the entire repository directory to data,
and then specify paths relative to it.

```bash
$ docker run -it -v $PWD/:/data openbases/openbases validate paper --infile /data/paper.md
```

For more detailed usage, see the [usage page](https://openbases.github.io/html/usage.html).

## Paper

What options do we have?

```bash
$ docker run openbases/openbases validate --help

Open Bases Paper Python [v0.0.53]

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

Here are a bunch of examples to try:

```bash
$ docker run -it -v $PWD:/data openbases/openbases paper get /data/paper.md
title: The Experiment Factory: Reproducible Experiment Containers
tags: ['containers', 'docker', 'psychology', 'reproducibility', 'Docker']
authors: [{'name': 'Vanessa Sochat', 'orcid': '0000-0002-4387-3819', 'affiliation': 1}]
affiliations: [{'name': 'Stanford University Research Computing', 'index': 1}]
date: 28 November 2017
bibliography: paper.bib
```

Get a specific field

```bash
$ docker run -it -v $PWD:/data openbases/openbases paper get /data/paper.md title
The Experiment Factory: Reproducible Experiment Containers
```

Get a list, render in comma separated list

```
$ docker run -it -v $PWD:/data openbases/openbases paper get /data/paper.md tags
containers,docker,psychology,reproducibility,Docker
```

Get more than one at once:

```bash
$ docker run -it -v $PWD:/data openbases/openbases paper get /data/paper.md title tags
The Experiment Factory: Reproducible Experiment Containers
containers,docker,psychology,reproducibility,Docker
```

Look up a subfield (e.g., authors --> name)

```bash
$ docker run -it -v $PWD:/data openbases/openbases paper get /data/paper.md authors:name
Vanessa Sochat

$ docker run -it -v $PWD:/data openbases/openbases paper get /data/paper.md authors:orcid
0000-0002-4387-3819
```

All together now!

```bash
$ docker run -it -v $PWD:/data openbases/openbases paper get /data/paper.md tags authors:name title
```

## Icons

What options do we have?

```bash
$ docker run openbases/openbases icons --help

Open Bases Icons [v0.0.53]

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

Examples!

```bash
$ docker run openbases/openbases icons
https://openbases.github.io/openbases-icons/ic/flaticon/sea-life-collection/grampus.png
```

You can ask for more than 1, of course:

```bash
$ docker run openbases/openbases icons --n 2
https://openbases.github.io/openbases-icons/ic/flaticon/in-the-zoo/butterfly.png
https://openbases.github.io/openbases-icons/ic/flaticon/in-the-zoo/penguin.png
```

You can also filter the search to some term you like (regular expression):

```bash
$ docker run openbases/openbases icons --n 2 --regexp fish
https://openbases.github.io/openbases-icons/ic/flaticon/sea-life-collection/fish.png
https://openbases.github.io/openbases-icons/ic/flaticon/sea-life-collection/fish1.png
```

If you know the name of your logo, that would be how to find it!

```bash
docker run openbases/openbases icons --regexp joss
https://openbases.github.io/openbases-icons/ic/openjournals/joss-logo.png
```

## Badges

What options do we have?

```bash
$ docker run openbases/openbases badges --help

Open Bases Badges Python [v0.0.53]

usage: ob-badge [--version] general usage ...

OpenBases Python Badges

optional arguments:
  --version      show openbases python version

actions:
  actions for openbases

  general usage  description
    view         view options for style, labels, etc.
    create       extract values from a paper.md
```

Here are examples to get you started.

```bash
$ docker run openbases/openbases badges create experiment labjs
![https://img.shields.io/badge/experiment-labjs-%23eaab1b.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io](https://img.shields.io/badge/experiment-labjs-%23eaab1b.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io)
```
![https://img.shields.io/badge/experiment-labjs-%23eaab1b.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io](https://img.shields.io/badge/experiment-labjs-%23eaab1b.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io)

Notice if we change the base type, we get a different color:

```bash
$ docker run openbases/openbases badges create submission labjs
```

See the [usage page](https://openbases.github.io/html/usage.html) 
for more details on how to see colors, badge types, and other settings.

## Development
If you want to develop, you can build the container locally too.

```bash
docker build -t openbases/openbases .
```
