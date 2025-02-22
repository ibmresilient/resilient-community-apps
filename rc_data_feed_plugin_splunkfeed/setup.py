#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='rc_data_feed_plugin_splunkfeed',
    display_name='Data Feeder for Splunk',
    version='1.3.0',
    license='MIT',
    author='IBM QRadar SOAR',
    author_email='',
    url="http://ibm.biz/soarcommunity",
    description="App Components for sending data feeds to other (BI) systems",
    long_description="""This package contains the SplunkFeed Plugin to the Data Feed extension.
    This Data Feed extension allows one to maintain 'replica' data for SOAR incidents, artifacts, tasks, notes, etc.
    The updates are performed in near real-time.
    This plugin allows this replica data to be maintained in Splunk.
    Refer to the documentation on the Data Feed extension for uses cases support and configuration options.
    Also refer to the other Data Feed plugins which can be used in combination.
<br>
    Links:
<ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
<ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        'rc_data_feed>=3.3.0',
        'resilient'
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
