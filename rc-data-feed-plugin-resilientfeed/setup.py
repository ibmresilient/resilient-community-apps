#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='rc_data_feed_plugin_resilientfeed',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='resil.labs@gmail.com',
    url='http://ibm.biz/resilientcommunity',
    description="Resilient Circuits Components for sending data feeds to other (BI) systems",
    long_description="Resilient Circuits Components for sending data feeds to other (BI) systems",
    install_requires=[
        'cachetools',
        'pyodbc',
        'rc_data_feed',
        'resilient',
        'resilient-lib'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.configsection": ["gen_config = data_feeder_plugins.resilientfeed.util.config:config_section_data"],
        "resilient.circuits.apphost.configsection": ["gen_config = data_feeder_plugins.resilientfeed.util.config:apphost_config_section_data"],
        "resilient.circuits.customize": ["customize = data_feeder_plugins.resilientfeed.util.customize:customization_data"],
    },
    tests_require=["pytest < 4.0.0",
                   "pytest_resilient_circuits"]
)
