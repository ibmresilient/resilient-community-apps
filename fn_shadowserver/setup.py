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
    name="fn_shadowserver",
    display_name="Shadow Server Function for IBM SOAR",
    version="1.0.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://github.com/ibmresilient/fn_shadowserver",
    description="IBM Security SOAR app for ShadowServer",
    long_description="""Queries ShadowServer to check if the hash provided matches an entry in our database. Returns details on the data source if there is a match.""",
    install_requires=[
        "resilient-circuits>=44.0.0"
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
            "{}FunctionComponent = fn_shadowserver.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_shadowserver/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_shadowserver.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_shadowserver.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_shadowserver.util.selftest:selftest_function"]
    }
)
