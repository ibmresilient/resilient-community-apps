#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import ntpath
from setuptools import setup, find_packages

def get_module_name(module_path):
    """
    Return the module name of the module path
    """
    return ntpath.split(module_path)[1].split(".")[0]

def snake_to_camel(word):
    """
    Convert a word from snake_case to CamelCase
    """
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


setup(
    name='fn_wiki',
    version='1.0.1',
    license='MIT',
    author='Resilient Labs',
    author_email='',
    url="http://ibm.biz/resilientcommunity",
    description="function which looks for search term in a wiki and returns the line it contains ",
    long_description="Perform operations against the Resilient wiki: create or update pages, read wiki contents and perform lookups of content.",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient_lib'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    python_requires='>=3',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ],
    entry_points={
        "resilient.circuits.components": [
            "{}FunctionComponent = fn_wiki.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_wiki/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_wiki.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_wiki.util.customize:customization_data"],
        "resilient.circuits.selftest": ["customize = fn_wiki.util.selftest:selftest_function"]
    }
)
