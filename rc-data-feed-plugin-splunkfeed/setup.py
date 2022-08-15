#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='rc_data_feed_plugin_splunkfeed',
    version='1.0.3',
    license='MIT',
    author='IBM Resilient',
    author_email='',
    url="http://ibm.biz/resilientcommunity",
    description="Resilient Circuits Components for sending data feeds to other (BI) systems",
    long_description="""This package contains the SplunkFeed Plugin to the Data Feed extension.
    This Data Feed extension allows one to maintain 'replica' data for Resilient incidents, artifacts, tasks, notes, etc.
    The updates are performed in near real-time.
    This plugin allows this replica data to be maintained in Splunk.
    Refer to the documentation on the Data Feed extension for uses cases support and configuration options.
    Also refer to the other Data Feed plugins which can be used in combination.""",
    install_requires=[
        'rc_data_feed',
        'resilient',
        'resilient-lib>=34.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.configsection": ["gen_config = data_feeder_plugins.splunkhecfeed.util.config:config_section_data"],
        "resilient.circuits.apphost.configsection": ["gen_config = data_feeder_plugins.splunkhecfeed.util.config:apphost_config_section_data"],
        "resilient.circuits.customize": ["customize = data_feeder_plugins.splunkhecfeed.util.customize:customization_data"]
    },
    tests_require=["pytest < 4.0.0",
                   "pytest_resilient_circuits"]
)
