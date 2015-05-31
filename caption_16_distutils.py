#!/usr/bin/env python  
from distutils.core import setup

setup(  # Distribution meta-data
        name="testpackage",
        version="1.0",
        description="Distutils sample distribution testpackage",
        # py_modules = [''],
        packages=['TestPackage'])


# pachage cli:
# python setup.py sdist
# python setup.py bdist_wininst
# python setup.py bdist_rpm