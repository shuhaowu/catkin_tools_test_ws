#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['py_dummy_pkg'],
    package_dir={'': 'src'},
    package_data={'py_dummy_pkg': ['data/*.txt']}
)

setup(**d)
