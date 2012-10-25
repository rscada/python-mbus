#!/usr/bin/env python
"""mbus: Python bindings to the libmbus library from rSCADA.

mbus offers binding to the libmbus C library.
"""

DOCLINES = __doc__.split('\n')

CLASSIFIERS = """\
Programming Language :: Python
Topic :: Engineering
Operating System :: POSIX
Operating System :: Unix
"""

from distutils.core import setup

MAJOR               = 0
MINOR               = 0
MICRO               = 1

setup(
    name = "mbus",
    version = "%d.%d.%d" % (MAJOR, MINOR, MICRO),
    packages = ['mbus'],
    scripts = ['examples/mbus-test-1.py'],
    author = "Robert Johansson",
    author_email = "rob@raditex.nu",
    license = "BSD",
    description = DOCLINES[0],
    long_description = "\n".join(DOCLINES[2:]),
    keywords = "M-Bus library for python",
    url = "http://www.rscada.se",
    platforms = ["Linux", "Unix"],
    )
