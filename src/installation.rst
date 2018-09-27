.. highlight:: shell

============
Installation
============


Stable release
--------------

To install OpenBases Python, run this command in your terminal:

.. code-block:: console

    $ pip install openbases

This is the preferred method to install openbases Python, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


To install extra modules and functionality (e.g., testing and validation functions)
then you need to issue the following:

.. code-block:: console

    $ pip install openbases[test]
    $ pip install openbases[validate]


From sources
------------

The sources for openbases Python can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/openbases/openbases-python

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/openbases/openbases-python/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install

.. _Github repo: https://github.com/openbases/openbases-python
.. _tarball: https://github.com/vsoch/openbases/tarball/master
