#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='rc_data_feed',
    display_name='Data Feeder for SOAR',
    version='3.3.2',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url='http://ibm.biz/resilientcommunity',
    description="QRadar SOAR integration for sending data feeds to other (BI) systems",
    long_description="QRadar SOAR integration for sending data feeds to other (BI) systems",
    install_requires=[
        'resilient_circuits>=51.0.0',
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
