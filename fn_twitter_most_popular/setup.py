#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    display_name='Twitter Search',
    name='fn_twitter_most_popular',
    version='1.0.2',
    license='MIT',
    author='Ryan',
    author_email='ryan@resilientlab.co.uk',
    url='http://ibm.biz/resilientcommunity',
    description="Resilient Circuits Twitter Search Function",
    long_description="A Resilient Circuits Function allowing you to search tweets with one or more tags",
    install_requires=[
        "resilient_circuits>=51.0.0",
        "twython < 3.8.0;python_version<'3.0'",
        "twython >= 3.8.0;python_version>='3.0'"
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "TwitterMostPopularTweetsFunctionComponent = fn_twitter_most_popular.components.twitter_most_popular_tweets:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_twitter_most_popular.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_twitter_most_popular.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_twitter_most_popular.util.selftest:selftest_function"]
    }
)