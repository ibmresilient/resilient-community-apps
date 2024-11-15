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
    name="fn_extrahop",
    display_name="ExtraHop for IBM SOAR",
    version="1.2.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://ibm.com/mysupport",
    description="IBM SOAR app for ExtraHop",
    long_description="""Provide bidirectional synchronization and functions for ExtraHop <br>

        <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
        <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>
        <ul><a target='blank' href='https://ibmresilient.github.io/resilient-community-apps/fn_extrahop/README.html'>App Documentation</a></ul>""",
    install_requires=[
        "resilient-circuits>=51.0.2.2.0",
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
            "{}FunctionComponent = fn_extrahop.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_extrahop/components/funct_[a-zA-Z]*.py")
        ] +
        [ "PollerComponent = fn_extrahop.components.poller:PollerComponent" ],
        "resilient.circuits.configsection": ["gen_config = fn_extrahop.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_extrahop.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_extrahop.util.selftest:selftest_function"]
    }
)
