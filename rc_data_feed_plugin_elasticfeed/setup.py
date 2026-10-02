#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='rc_data_feed_plugin_elasticfeed',
    display_name='Data Feeder for Elasticsearch',
    version='1.2.0',
    license='MIT',
    author='IBM QRadar SOAR',
    author_email='',
    url='http://ibm.biz/soarcommunity',
    description="IBM SOAR Components for sending data feeds to other (BI) systems",
    long_description="""This package contains the Elasticsearch Plugin to the Data Feed extension.
    This Data Feed extension allows one to maintain 'replica' data for SOAR incidents, artifacts, tasks, notes, etc.
    The updates are performed in near real-time.
    This plugin allows this replica data to be maintained in Elasticsearch.
    Refer to the documentation on the Data Feed extension for uses cases support and configuration options.
    Also refer to the other Data Feed plugins which can be used in combination.

    <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
    <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>
    <ul><a target='blank' href='https://github.com/ibmresilient/resilient-community-apps/blob/main/rc_data_feed_plugin_elasticfeed/README.md'>App Documentation</a></ul>""",
    install_requires=[
        'rc_data_feed>=3.3.0',
        'elasticsearch>=8.3',
        'resilient'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.configsection": ["gen_config = data_feeder_plugins.elasticfeed.util.config:config_section_data"],
        "resilient.circuits.apphost.configsection": ["gen_config = data_feeder_plugins.elasticfeed.util.config:apphost_config_section_data"],
        "resilient.circuits.customize": ["customize = data_feeder_plugins.elasticfeed.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = data_feeder_plugins.elasticfeed.util.selftest:selftest_function"],
    },
    tests_require=["pytest < 4.0.0",
                   "pytest_resilient_circuits"]
)
