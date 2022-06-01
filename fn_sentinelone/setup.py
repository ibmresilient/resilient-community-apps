#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import glob
import ntpath


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
    name="fn_sentinelone",
    display_name="SentinelOne",
    version="1.0.1",
    license="MIT",
    author="IBM Resilient",
    author_email="",
    url="https://github.com/ibmresilient/fn_sentinelone",
    description="IBM Security SOAR app for SentinelOne",
    long_description="""This app allows bi-directional synchronization between IBM SOAR and SentinelOne.
    SentinelOne threats are escalated to IBM SOAR as cases with the creation of artifacts and notes in SOAR from the threat.""",
    install_requires=[
        "resilient-circuits>=40.0.0",
                "resilient-lib",
                "jinja2"
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_sentinelone.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_sentinelone/components/f[a-zA-Z]*.py")
            ]+
            [ "PollerComponent = fn_sentinelone.components.sentinelone_poller:SentinelOnePollerComponent" ],
        "resilient.circuits.configsection": ["gen_config = fn_sentinelone.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_sentinelone.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_sentinelone.util.selftest:selftest_function"]
    }
)
