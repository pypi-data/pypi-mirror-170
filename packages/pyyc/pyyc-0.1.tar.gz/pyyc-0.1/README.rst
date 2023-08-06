pyyc - a sample project
=======================

A sample project.

Package initialization (`__init__.py`)
--------------------------------------

>>> import pyyc
Initialisation  A1
Initialisation  A2
Initialisation  A1B
>>> pyyc.subpkgA.modA1.version
'A1'
>>> pyyc.subpkgB.version
'A1B'

Data files (e.g. `config/`)
---------------------------

Example to access data file at runtime:

>>> from pyyc.subpkgB.mod import read_config  # always possible, no matter __all__
>>> cfg = read_config()                       # will look for config files distributed along pyyc
>>> cfg['DEFAULT']['version']
'cfg-1.0'

Source: https://setuptools.pypa.io/en/latest/userguide/datafiles.html#accessing-data-files-at-runtime

To be completed
---------------

* sphinx documentation (`docs/`),
* continuous integration (`.gitlab-ci.yml`),
* tests (`tests/`),
* coverage.
