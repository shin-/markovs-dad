#!/usr/bin/env python
from __future__ import print_function

import codecs
import os

from setuptools import find_packages, setup

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

requirements = [
    'requests==2.20.1',
    'Flask==1.0.2',
    'gevent==1.3.7',
]

test_requirements = [
    'pytest==4.0.0',
]


long_description = ''
try:
    with codecs.open('./README.md', encoding='utf-8') as readme_rst:
        long_description = readme_rst.read()
except IOError:
    pass

setup(
    name="markovs_dad",
    version="1.0.0b",
    description="A Markov dad joke generator.",
    long_description=long_description,
    url='https://github.com/shin-/markovs-dad',
    packages=find_packages(exclude=["tests.*", "tests"]),
    install_requires=requirements,
    tests_require=test_requirements,
    extras_require={},
    zip_safe=False,
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Dads',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
    maintainer='Joffrey F',
    maintainer_email='f.joffrey@gmail.com',
)
