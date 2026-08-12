#!/usr/bin/env python
#-- coding: utf-8 --
#(c) Copyright IBM Corp. 2025. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long

from setuptools import setup, find_packages

setup(
    display_name='Oauth Utilities for SOAR',
    name="oauth-utils",
    version='1.0.1',
    license='MIT',
    author='IBM SOAR',
    url='https://ibm.com/mysupport',
    description="OAuth utilities for IBM SOAR apps",
    long_description="Utilities to support OAuth for SOAR apps",
    install_requires=[
        'Jinja2>=2.9.6',
        'six',
        'urllib3',
        'requests',
        'click'
    ],
    extras_require={
        'browser': [
            'flask==2.0.3',
            'pyOpenssl==21.0.0'
        ]
    },
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "console_scripts": [
            "oauth-utils=oauth_utils.app:main"
        ]
    }
)
