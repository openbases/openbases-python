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
https://openbases.github.io/openbases-icons/ic/iconarchive/tuxlets/testdummytux2.svg.png
```

You can ask for more than 1, of course:

```bash
$ ob-icons --n 2
https://openbases.github.io/openbases-icons/ic/iconarchive/tuxlets/surgeontux2.svg.png
https://openbases.github.io/openbases-icons/ic/iconarchive/tuxlets/clowntux.svg.png
```

You can also filter the search to some term you like (regular expression):

```bash
$ ob-icons --n 2 --regexp pencil
https://openbases.github.io/openbases-icons/ic/iconarchive/office-set/pencil-blue-icon.png
https://openbases.github.io/openbases-icons/ic/iconarchive/office-set/colorful-pencil-icon.png
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

### Validation

The validation functions are provided via the `ob-validate` client. Note that you
need to install dependencies first:

```bash
pip install openbases[validate]
```

For using it, the simplest use case it to provide the path to the paper with the
`--infile` variable. By default:

 - the `paper.bib` will be looked for in the same directory as the paper
 - the repository base (with an open source LICENSE and CONTRIBUTING.md) is assumed to be $PWD
 - the default criteria provided by the library are used.

Here we are running from the root of the 
[openbases-python](https://www.github.com/openbases/openbases-python)  repository, 
so the paper.md file is located under `tests/paper/paper.md`

```bash
$ ob-validate paper --infile tests/paper/paper.md
Found /home/vanessa/Documents/Dropbox/Code/openbases/openbases-python/tests/paper/paper.md, valid name
Found /home/vanessa/Documents/Dropbox/Code/openbases/openbases-python/tests/paper/paper.bib, valid name
[criteria:paper.yml]
WARNING Skipping parameter bibfile for environment
[criteria:paper.yml]
[group|start:length]
WARNING Length of paper is approximately 5277 chars.
WARNING Paper estimated > 1000 characters
[check:Check that the paper is between 250-1000 characters]
 test:function openbases.main.papers.tests.test_length
 test:result pass
[group|end:length]
[group|start:authors]
[check:Submission must include a list of authors with associated metadata]
 test:function openbases.main.papers.tests.test_authors
 test:result pass
[group|end:authors]
[group|start:license]
Found Open Source license flags! "AS IS"
BSD License

Copyright (c) 2018, Vanessa Sochat
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:
...
[check:An OSI license is included in the repository]
 test:function openbases.main.papers.tests.test_license
 test:result pass
[group|end:license]
[group|start:references]
Testing bibliography entry Stodden2010-cu
  type: article
  title: The Scientific Method in Practice: Reproducibility in the Computational Sciences
Testing bibliography entry Ram2013-km
  type: article
  title: Git can facilitate greater reproducibility and increased transparency in science
...
Testing bibliography entry Santana-Perez2015-wo
  type: article
  title: Towards Reproducibility in Scientific Workflows: An {Infrastructure-Based} Approach
Testing bibliography entry Wandell2015-yt
  type: article
  title: Data management to support reproducible research
[check:References are included and complete]
 test:function openbases.main.papers.tests.test_references
 test:result pass
[group|end:references]
[group|start:contributing]
Found CONTRIBUTING file(s) in repository!
[check:Software has CONTRIBUTING.md]
 test:function openbases.main.papers.tests.test_contributing
 test:result pass
[group|end:contributing]
ALL TESTS PASSING
```

Let's say we moved out of this repository base, and wanted to define custom
paths to the repo base and the paper.bib. Let's do that.

```bash
$ ob-validate --repo ../../ paper --infile paper.md --bib paper.bib
```

Note that the `--repo` argument comes before paper (because potentially we will
have other kinds of validators that also need a repo!)

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

For the easiest use case, you should have your paper.md and paper.bib in the same folder.
This is likely the Github repository that you would submit your paper to! I like to keep
these files in another directory called "paper":

```
$ paper/
    paper.md
    paper.bib
```

In an interactive Python session, import the `PaperValidator`

```python
from openbases.main import Client
```

#### 1. Loading the Paper

Define our input file to be `paper.md` in the present working directory. If you
have downloaded the [openbases-python](https://www.github.com/openbases/openbases-python) 
repository, this file is located under `tests/paper/paper.md`

```
infile = 'tests/paper/paper.md'
validator = Client.PaperValidator(infile)
Found paper.md, valid name
Found /home/vanessa/Documents/Dropbox/Code/openbases/openbases-python/tests/paper/paper.bib, valid name
```
Notice that this first step just ensures that your fileis there, and it also checks for the bibliography
file. With the defaults above, we check for the `paper.bib` in the same folder. Our
validator is ready to go!

```
$ validator
$ [paper-validator:paper.md]
```

You can consider these files now loaded into the validator. For the remainder of function
calls you *could* specify new paths, but if you don't, these that are loaded will be used.

#### 2. Loading the Criteria

If you want to take a look at your criteria, just (re) load it. Note that you
can skip this step (and section) if you just want to use defaults and run the validation.

```bash
validator.load_criteria()
```

Again, not specifying a `criteria=` variable to this function uses the default!
Now we can see the checks that are to be run:

```
{'checks': {'authors': [{'name': 'Submission must include a list of authors with associated metadata'},
   {'level': 'error'},
   {'function': 'openbases.main.papers.tests.test_authors'}],
  'contributing': [{'name': 'Software has CONTRIBUTING.md'},
   {'level': 'error'},
   {'function': 'openbases.main.papers.tests.test_contributing'}],
  'length': [{'name': 'Check that the paper is between 250-1000 characters'},
   {'level': 'warning'},
   {'function': 'openbases.main.papers.tests.test_length'},
   {'kwargs': [{'min_length': 250}, {'max_length': 1000}]}],
  'license': [{'name': 'An OSI license is included in the repository'},
   {'level': 'error'},
   {'function': 'openbases.main.papers.tests.test_license'},
   {'environment': [{'OPENBASESENV_REPO_BASE': None}]}],
  'references': [{'name': 'References are included and complete'},
   {'level': 'warning'},
   {'function': 'openbases.main.papers.tests.test_references'},
   {'environment': [{'OPENBASESENV_REPO_BASE': None}]}]},
 'version': 1}
```

I'm glad I looked, Notice that two of the validation functions require an 
environment variable, `OPENBASESENV_REPO_BASE` that normally I'd set on the
command line **or** would be discovered by running the executable from
the base of my repository (with an open source license, for example).
Since we are running from the root (and we have a LICENSE!) we will be OK. 
If you werent, you would need to make sure the variable is
in the environment like this:

```python
import os
os.environ['OPENBASESENV_REPO_BASE'] = os.path.abspath('/path/to/repo')
```

You could also load your own custom criteria, and copy the format of the criteria flie
[here](https://www.github.com/openbases/openbases-python/tree/master/openbases/main/validator/criteria/paper.yml)
(more on this later).

```bash
validator.load_criteria(criteria='mypaper.yml')
```

#### 3: Run the Validation!

To perform the validation, just ask to do that! We are validating based on criteria, so
that's the function that we call. Note that you don't necessarily need to call
the `load_criteria` above - you could just call this and it would load the default for
you. You could also provide the `criteria` directly to this function.

```python
validator.validate_criteria()
[criteria:paper.yml]
WARNING Skipping parameter bibfile for environment
[criteria:paper.yml]
[group|start:length]
WARNING Length of paper is approximately 5277 chars.
WARNING Paper estimated > 1000 characters
[check:Check that the paper is between 250-1000 characters]
 test:function openbases.main.papers.tests.test_length
 test:result pass
[group|end:length]
[group|start:authors]
[check:Submission must include a list of authors with associated metadata]
 test:function openbases.main.papers.tests.test_authors
 test:result pass
[group|end:authors]
[group|start:license]
Found Open Source license flags! "AS IS"
BSD License

Copyright (c) 2018, Vanessa Sochat
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this
  list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from this
  software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.

Found Open Source license flags! "AS IS"
Copyright Jason R. Coombs

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[check:An OSI license is included in the repository]
 test:function openbases.main.papers.tests.test_license
 test:result pass
[group|end:license]
[group|start:references]
Testing bibliography entry Stodden2010-cu
  type: article
  title: The Scientific Method in Practice: Reproducibility in the Computational Sciences
Testing bibliography entry Ram2013-km
  type: article
  title: Git can facilitate greater reproducibility and increased transparency in science
Testing bibliography entry noauthor_2015-ig
  type: misc
  title: Docker-based solutions to reproducibility in science - Seven Bridges
...
Testing bibliography entry Boettiger2014-cz
  type: article
  title: An introduction to Docker for reproducible research, with examples from the {R} environment
Testing bibliography entry Santana-Perez2015-wo
  type: article
  title: Towards Reproducibility in Scientific Workflows: An {Infrastructure-Based} Approach
Testing bibliography entry Wandell2015-yt
  type: article
  title: Data management to support reproducible research
[check:References are included and complete]
 test:function openbases.main.papers.tests.test_references
 test:result pass
[group|end:references]
[group|start:contributing]
Found CONTRIBUTING file(s) in repository!
[check:Software has CONTRIBUTING.md]
 test:function openbases.main.papers.tests.test_contributing
 test:result pass
[group|end:contributing]
ALL TESTS PASSING
```

Here is a quick demo of the above!

<script src="https://asciinema.org/a/203355.js" id="asciicast-203355" async data-speed="2"></script>


#### 4. Write your Own Criteria

If you look at the default criteria, which is provided for you
[here](https://www.github.com/openbases/openbases-python/tree/master/openbases/main/validator/criteria/paper.yml).
it's really quite trivial to write a criteria file, and use your own functions!
The first thing you should do is create some `criteria.yml` 
(or similarly named) file, and create chunks that look 
like this:

```yaml
version: 1
checks:
    mycheck:
      - name: This check will always print a message and pass
      - level: log
      - function: openschemas.main.validate.criteria.base.dummy
```

The function itself can be anywhere, as long as you provide the full path
to the python module (a `module.py` file, not an __init__.py file)
as shown above. In the example above, the function "dummy" would be
defined in the file `base.py`.

Once you write this file, you can use it with the same `paper.md` and
openbases validator, as shown above. Remember that you should first
load your criteria, or the default will be used. 

```python
from openschemas.main import Client
validator = Client.PaperValidator(infile="paper.md")
```

Either of these would work
```
validator.load_criteria(criteria="dummy.yml")
validator.validate_criteria()
```
or
```
validator.validate_criteria(criteria="dummy.yml")
```

#### 5. How to write a test
Any test that goes into the critria.yml is expected to take a `YamlManager`
as the first argument, followed by a general set of `kwargs`. This means that:

 - The first argument should refer to the YamlManager, call it "manager," but it's positional so it's up to you.
 - `manager.loaded` will have the loaded yaml frontend matter
 - `manager.content` will have the remainder of the markdown file (the paper content)
 - `manager.infile` will have the path to the file.
 - You can either handle exiting in the function, or return False if a test fails. Return True if it passes.
 - You are free to use whatever logging or printing you desire! Generally, it's a good idea to provide a user with enough information to see what is being tested, and any requirements to debug if a test is not passing.

If you need to see what a manager provides you, do this:

```python
from openbases.utils.managers import YamlManager
$ manager = YamlManager('paper.md')

manager
{'affiliations': [{'index': 1,
   'name': 'Stanford University Research Computing'}],
 'authors': [{'affiliation': 1,
   'name': 'Vanessa Sochat',
   'orcid': '0000-0002-4387-3819'}],
 'bibliography': 'paper.bib',
 'date': '28 November 2017',
 'tags': ['containers', 'docker', 'psychology', 'reproducibility', 'Docker'],
 'title': 'The Experiment Factory: Reproducible Experiment Containers'}
```

And the content we discussed above:

```python
$ manager.content
'\n\n# Summary\n\nThe Experiment Factory [@vanessa_sochat_2017_1059119] is Open Source ...
```

And the frontend matter

```
: manager.loaded
Out[31]: 
{'affiliations': [{'index': 1,
   'name': 'Stanford University Research Computing'}],
 'authors': [{'affiliation': 1,
   'name': 'Vanessa Sochat',
   'orcid': '0000-0002-4387-3819'}],
 'bibliography': 'paper.bib',
 'date': '28 November 2017',
 'tags': ['containers', 'docker', 'psychology', 'reproducibility', 'Docker'],
 'title': 'The Experiment Factory: Reproducible Experiment Containers'}
```
