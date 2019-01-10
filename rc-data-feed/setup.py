#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys

tests_require=[]

if sys.version_info[0] < 3:
    tests_require.add('mock')

setup(
    name='rc_data_feed',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Components for sending data feeds to other (BI) systems",
    long_description="Resilient Circuits Components for sending data feeds to other (BI) systems",
    install_requires=[
        'resilient_circuits>=31.0.0',
        'resilient>=31.0.0',
        'pyodbc'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FeedComponent = rc_data_feed.components.feed_ingest:FeedComponent"
        ]
    },
    extras_require=dict(
        tests = tests_require
    )
)
