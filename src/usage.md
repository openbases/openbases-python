# Usage

The `openbases`  python module serves several command line utils along with 
python functions for interacting with the set of openbases tools.

## Command Line

### Icons

You can use open bases python to easily get an icon! For a preview of the set you are 
choosing from, see [here](https://openbases.github.io/openbases-icons/preview). 
Here is how to get one randomly selected icon:

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

### Badges

The badges client is available as `ob-badges`. You minimally need to specify a base
type (e.g., "experiment") and a name for it (e.g., "labjs"). The name is typically
for you to decide for the base, but the base type, in that there are assigned colors
for each, will be looked up. 

The primary command you want to use is "create":

```bash
$ ob-badge create experiment labjs
![https://img.shields.io/badge/experiment-labjs-%23eaab1b.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io](https://img.shields.io/badge/experiment-labjs-%23eaab1b.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io)
```
![https://img.shields.io/badge/experiment-labjs-%23eaab1b.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io](https://img.shields.io/badge/experiment-labjs-%23eaab1b.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io)

Notice if we change the base type, we get a different color:

```bash
$ ob-badge create submission labjs
```

![https://img.shields.io/badge/submission-labjs-green.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io](https://img.shields.io/badge/submission-labjs-green.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io)

If you specify a base type that does not exist, a grey badge will be returned.
```bash
$ ob-badge create pancakes labjs
```
![https://img.shields.io/badge/pancakes-labjs-lightgrey.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io](https://img.shields.io/badge/pancakes-labjs-lightgrey.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io)

You likely want the link for the badge to be the URL that corresponds with your resource!

```bash
$ ob-badge create library labjs --link https://labjs.readthedocs.io
```
![https://img.shields.io/badge/library-labjs-%23ff69b4.svg?style=flat&link=https%3A%2F%2Flabjs.readthedocs.io](https://img.shields.io/badge/library-labjs-%23ff69b4.svg?style=flat&link=https%3A%2F%2Flabjs.readthedocs.io)

or instead of a markdown, you can also output svg (for embedding in other places)

```bash
$ ob-badge create data dinosaur-dataset --fmt svg
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="132" height="20"><linearGradient id="b" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="a"><rect width="132" height="20" rx="3" fill="#fff"/></clipPath><g clip-path="url(#a)"><path fill="#555" d="M0 0h31v20H0z"/><path fill="#e05d44" d="M31 0h101v20H31z"/><path fill="url(#b)" d="M0 0h132v20H0z"/></g><g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="110"> <text x="165" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="210">404</text><text x="165" y="140" transform="scale(.1)" textLength="210">404</text><text x="805" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="910">badge not found</text><text x="805" y="140" transform="scale(.1)" textLength="910">badge not found</text></g><a target="_blank" xlink:href="https://openbases.github.io"><path fill="rgba(0,0,0,0)" d="M0 0h31v20H0z"/></a> <a target="_blank" xlink:href="https://openbases.github.io"><path fill="rgba(0,0,0,0)" d="M31 0h101v20H31z"/></a></svg>
```

Or change the style

```bash
$ ob-badge create resource myresource --style for-the-badge
```

![https://img.shields.io/badge/resources-myresource-blue.svg?style=for-the-badge&link=https%3A%2F%2Fopenbases.github.io](https://img.shields.io/badge/resources-myresource-blue.svg?style=for-the-badge&link=https%3A%2F%2Fopenbases.github.io)

Or set your own color (and override the label assignments)

```
$ ob-badge create experiment labjs --color pink
![https://img.shields.io/badge/experiment-labjs-pink.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io](https://img.shields.io/badge/experiment-labjs-pink.svg?style=flat&link=https%3A%2F%2Fopenbases.github.io)
```

You can also view labels, styles, and colors, if you aren't sure about those to choose from:

```bash
$ ob-badge view styles
plastic flat flat-square for-the-badge popout popout-square social

$ ob-badge view labels
submission experiment builder openbases testing data library resource paper other

$ ob-badge view colors
black
dimgray
dimgrey
gray
...
lavenderblush
palevioletred
crimson
pink
lightpink
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

### Validation

Firstly, if you want to install the extra validation functions (namely the library
to read in bibtex) you need to do that first:

```bash
pip install openbases[validate]
```

You should have your paper.md and paper.bib in the same folder.

```
$
  paper.md
  paper.bib
```

In an interactive Python session, import the `PaperValidator`

```python
from openbases.main.validate import PaperValidator

infile = 'tests/paper/paper.md'
validator = PaperValidator(infile)
```

If there isn't a paper.bib in the same folder, you will get an error. You
should not have many cases when even a small software paper doesn't have
references.
