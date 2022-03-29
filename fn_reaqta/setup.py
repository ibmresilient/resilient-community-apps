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
    name="fn_reaqta",
    display_name="ReaQta for IBM QRadar SOAR",
    version="1.0.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://ibm.com/mysupport",
    description="IBM SOAR app bidirectional synchronization and functions for ReaQta",
    long_description="""Bidirectional synchronization of ReaQta Alerts to IBM SOAR.
    Additional functions exists to list and kill endpoint processes, isolate the endpiont and synchronize notes and close events.""",
    install_requires=[
        "resilient-circuits>=43.0.0",
        "cachetools ~= 2.1",
        "retry2 ~= 0.9"
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
            "{}FunctionComponent = fn_reaqta.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_reaqta/components/funct_[a-zA-Z]*.py")
        ] +
        [ "PollerComponent = fn_reaqta.components.poller:PollerComponent" ],
        "resilient.circuits.configsection": ["gen_config = fn_reaqta.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_reaqta.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_reaqta.util.selftest:selftest_function"]
    }
)
