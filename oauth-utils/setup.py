#!/usr/bin/env python
#-- coding: utf-8 --
#(c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long

from setuptools import setup, find_packages

setup(
    name="oauth-utils",
    version='1.0.0',
    license='MIT',
    author='IBM SOAR',
    url='https://ibm.com/mysupport',
    description="OAuth utilities for IBM SOAR apps",
    long_description="Utilities to support OAuth2 for SOAR functions",
    install_requires=[
        'Jinja2>=2.9.6',
        'six',
        'urllib3',
        'requests'
    ],
    extras_require={
        'browser': [
            'flask==1.1.1',
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
            "generate_oauth2_refresh_token=oauth_utils.bin.generate_oauth2_refresh_token:main"
        ]
    }
)
