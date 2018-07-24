#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_elasticsearch_query',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_elasticsearch_query'",
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
            "QueryElasticsearchDatastoreFunctionComponent = fn_elasticsearch_query.components.query_elasticsearch_datastore:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_elasticsearch_query.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_elasticsearch_query.util.customize:customization_data"]
    }
)