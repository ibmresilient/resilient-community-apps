#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_twitter_most_popular',
    version='1.0.0',
    license='MIT',
    author='Ryan',
    author_email='ryan@resilientlab.co.uk',
    description="Resilient Circuits Twitter Search Function",
    long_description="A Resilient Circuits Function allowing you to search tweets with one or more tags",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'twython>= 3.7.0'
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
        "resilient.circuits.customize": ["customize = fn_twitter_most_popular.util.customize:customization_data"]
    }
)