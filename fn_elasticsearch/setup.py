#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    display_name='ElasticSearch Functions for IBM SOAR',
    name='fn_elasticsearch',
    version='1.0.8',
    url='https://ibm.biz/soarcommunity',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    description="Functions to query Elasticsearch with incident or artifact data",
    long_description="Allows users of the SOAR Platform to connect to and query an ElasticSearch Database. Users can specify the location of a remote ElasticSearch instance and query this instance for data through the Resilient Platform ",
    install_requires=[
        'resilient_circuits>=31.0.0',
        'elasticsearch~=7.17',
        'resilient_lib>=35.0.0'
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
        "resilient.circuits.customize": ["customize = fn_elasticsearch.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_elasticsearch.util.selftest:selftest_function"]
    }
)
