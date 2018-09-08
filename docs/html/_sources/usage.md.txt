# Usage

The `openbases`  python module serves several command line utils along with 
python functions for interacting with the set of openbases tools.

## Command Line

### Icons

You can use open bases python to easily get an icon! Here is how to get one randomly
selected icon:

```bash
$ ob-icons
https://openbases.github.io/openbases-icons/ic/flaticon/sea-life-collection/grampus.png
```

You can ask for more than 1, of course:

```bash
$ ob-icons --n 2
https://openbases.github.io/openbases-icons/ic/flaticon/in-the-zoo/butterfly.png
https://openbases.github.io/openbases-icons/ic/flaticon/in-the-zoo/penguin.png
```

You can also filter the search to some term you like (regular expression):

```bash
$ ob-icons --n 2 --regexp fish
https://openbases.github.io/openbases-icons/ic/flaticon/sea-life-collection/fish.png
https://openbases.github.io/openbases-icons/ic/flaticon/sea-life-collection/fish1.png
```

If you know the name of your logo, that would be how to find it!

```bash
$ ob-icons --n 2 --regexp joss
https://openbases.github.io/openbases-icons/ic/openjournals/joss-logo.png
```

### Papers

Here is a paper.md you can play with:

```bash
wget https://raw.githubusercontent.com/openbases/openbases-python/master/tests/paper/paper.md
```

Load the paper, show all fields:

```bash
$ ob-paper get paper.md
title: The Experiment Factory: Reproducible Experiment Containers
tags: ['containers', 'docker', 'psychology', 'reproducibility', 'Docker']
authors: [{'name': 'Vanessa Sochat', 'orcid': '0000-0002-4387-3819', 'affiliation': 1}]
affiliations: [{'name': 'Stanford University Research Computing', 'index': 1}]
date: 28 November 2017
bibliography: paper.bib
```

Get a specific field

```
$ ob-paper get paper.md title
The Experiment Factory: Reproducible Experiment Containers
```

Get a list, render in comma separated list

```
$ ob-paper get paper.md tags
containers,docker,psychology,reproducibility,Docker
```

Get more than one at once:

```
$ ob-paper get paper.md title tags
The Experiment Factory: Reproducible Experiment Containers
containers,docker,psychology,reproducibility,Docker
```

Look up a subfield (e.g., authors --> name)

```
$ ob-paper get paper.md authors:name
Vanessa Sochat

$ ob-paper get paper.md authors:orcid
0000-0002-4387-3819
```

All together now!

```
$ ob-paper get paper.md tags authors:name title
containers,docker,psychology,reproducibility,Docker
Vanessa Sochat
The Experiment Factory: Reproducible Experiment Containers
```


## Python Client

You can access the same functions from within Python!

### Icons

The default function returns one randomly selected icon:

```python
from openbases.main.icons import get_icons
get_icons()
['https://openbases.github.io/openbases-icons/flaticon/sea-life-collection/squid.svg']
```

You can specify a number, or filter

```python
get_icons(N=2)
['https://openbases.github.io/openbases-icons/flaticon/sea-life-collection/seahorse.svg',
 'https://openbases.github.io/openbases-icons/flaticon/sea-life-collection/stingray.svg']

get_icons(N=2, regexp="fish")
['https://openbases.github.io/openbases-icons/flaticon/sea-life-collection/fish2.svg',
 'https://openbases.github.io/openbases-icons/flaticon/sea-life-collection/fish.svg']
```

### Papers

```
from openbases.main import Paper
paper = Paper("paper.md")
```

or the same function via the client:

```
from openbases.main import Client
paper = Client.paper("paper.md")
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

```
# Get sub fields from list
paper.get('authors', field='name')
Vanessa Sochat
```

Command line will probably look like this
