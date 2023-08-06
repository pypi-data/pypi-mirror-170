#!/usr/bin/env python3
""" Setup file for mailpy package """
from setuptools import setup


# Package meta-data.
NAME = 'mailpy'
PACKAGES = ['mailpy']
DESCRIPTION = 'Python IMAP and SMTP Wrapper'
URL = 'http://github.com/Y4hL/mailpy'
AUTHOR = 'https://github.com/Y4hL'
REQUIRES_PYTHON = '>=3.5.0'
VERSION = '1.0.1'

# Required Packages
REQUIRED = []

# Optional Packages
EXTRAS = {

    # 'Feature Name': ['Extra Package']

    }



# Setup
setup(
    name=NAME,
    packages=PACKAGES,
    description=DESCRIPTION,
    install_requires=REQUIRED,
    licence="GNU GPLv3",
    version=VERSION,
    url=URL,
    author=AUTHOR,
    tests_require=[],
    include_package_data=True,
    python_requires=REQUIRES_PYTHON,
    # setup_requires=[],
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Communications :: Email',
        'Topic :: Communications :: Email :: Email Clients (MUA)',
    ],
)
