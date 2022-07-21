#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='rc_data_feed_plugin_elasticfeed',
    version='1.1.0',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url='http://ibm.biz/resilientcommunity',
    description="IBM SOAR Components for sending data feeds to other (BI) systems",
    long_description="IBM SOAR Components for sending data feeds to other (BI) systems",
    install_requires=[
        'rc_data_feed>=2.2.1',
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
