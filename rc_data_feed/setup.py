#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='rc_data_feed',
    version='2.2.1',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='http://ibm.biz/resilientcommunity',
    description="Resilient Circuits Components for sending data feeds to other (BI) systems",
    long_description="Resilient Circuits Components for sending data feeds to other (BI) systems",
    install_requires=[
        'resilient_circuits>=39',
        'resilient>=39',
        'resilient_lib'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FeedComponent = rc_data_feed.components.feed_ingest:FeedComponent",
            "SyncIncidentsFunctionComponent = rc_data_feed.components.data_feeder_sync_incidents:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = rc_data_feed.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = rc_data_feed.util.customize:customization_data"],
    },
    tests_require=["pytest < 4.0.0",
                   "pytest_resilient_circuits"]
)
