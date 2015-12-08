#!/usr/bin/env python
"""PySwitchvox

Copyright (C) 2015, Digium, Inc.
Matthew Jordan <mjordan@digium.com>
"""

import os

from setuptools import setup


setup(
    name="pyswitchvox",
    version="0.0.1",
    license="BSD 3-Clause License",
    description="Library for accessing the Switchvox Extend API",
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       "README.rst")).read(),
    author="Digium, Inc.",
    author_email="mjordan@digium.com",
    url="https://github.com/digium/pyswitchvox",
    packages=["pyswitchvox"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    tests_require=[],
    install_requires=["requests>=2.8.1"],
)
