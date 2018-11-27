#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_elasticsearch',
    version='1.0.0',
    url='https://github.com/ibmresilient/resilient-community-apps',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Components for 'fn_elasticsearch'",
    long_description="Allows users of the Resilient Platform to connect to and query an ElasticSearch Database. Users can specify the location of a remote ElasticSearch instance and query this instance for data through the Resilient Platform ",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'elasticsearch>=6.3.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnElasticsearchQueryFunctionComponent = fn_elasticsearch.components.fn_elasticsearch_query:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_elasticsearch.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_elasticsearch.util.customize:customization_data"]
    }
)