# Usage

This is a temporary location to document usage (while I'm developing it). 
This will be served via a command line client `openbases` and also within
python.

## Papers

### Command Line

Load a paper, show all fields:

```bash
$ openbases paper get paper.md
title: The Experiment Factory: Reproducible Experiment Containers
tags: ['containers', 'docker', 'psychology', 'reproducibility', 'Docker']
authors: [{'name': 'Vanessa Sochat', 'orcid': '0000-0002-4387-3819', 'affiliation': 1}]
affiliations: [{'name': 'Stanford University Research Computing', 'index': 1}]
date: 28 November 2017
bibliography: paper.bib
```

Get a specific field

```
$ openbases paper get paper.md title
The Experiment Factory: Reproducible Experiment Containers
```

Get a list, render in comma separated list

```
$ openbases paper get paper.md tags
containers,docker,psychology,reproducibility,Docker
```

Change the separator to space!

```
$ openbases --sep " " paper get paper.md  tags
containers docker psychology reproducibility Docker
```

Get more than one at once:

```
$ openbases paper get paper.md title tags
The Experiment Factory: Reproducible Experiment Containers
containers,docker,psychology,reproducibility,Docker
```

Look up a subfield (e.g., authors --> name)

```
$ openbases paper get paper.md authors:name
Vanessa Sochat

$ openbases paper get paper.md authors:orcid
0000-0002-4387-3819
```

All together now!

```
$ openbases paper get paper.md  tags authors:name title
containers,docker,psychology,reproducibility,Docker
Vanessa Sochat
The Experiment Factory: Reproducible Experiment Containers
```


## Interactive

A paper will be available both of these ways:

```
from openbases.main import Paper
paper = Paper("paper.md")
```

or via a client:

```
from openbases.main import get_client
client = get_client("paper.md")
```

The output shows the parsed markdown with paper values

```
title: The Experiment Factory: Reproducible Experiment Containers
tags: ['containers', 'docker', 'psychology', 'reproducibility', 'Docker']
authors: [{'name': 'Vanessa Sochat', 'orcid': '0000-0002-4387-3819', 'affiliation': 1}]
affiliations: [{'name': 'Stanford University Research Computing', 'index': 1}]
date: 28 November 2017
bibliography: paper.bib
```

Since we want to feed these into pandoc, there will be nice functions to return
fields, and subfields, separated by a delimiter of choice.

```
# Get sub fields from list
paper.get('authors', field='name')
Vanessa Sochat
```

Command line will probably look like this
```
openbases paper get authors name
authors=$(openbases paper get authors name)
```

**under development**

!! This is fun :)
