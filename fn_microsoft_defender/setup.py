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
    name="fn_microsoft_defender",
    display_name="Microsoft Defender ATP Functions",
    version="1.0.0",
    license="MIT",
    author="IBM Resilient",
    author_email="mscherfling@ibm.com",
    url="https://github.com/ibmresilient/resilient-community-apps",
    description="Resilient Circuits Components for 'fn_microsoft_defender'",
    long_description="""Perform operations against Defender ATP such as set indicators, isolate and quarantine machines, and block file execution""",
    install_requires=[
        "resilient_circuits>=30.0.0",
        "resilient_lib",
        "msal",
        "simplejson",
        "python-rapidjson"
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_microsoft_defender.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_microsoft_defender/components/f[a-zA-Z]*.py")
        ]+
        [ "PollerComponent = fn_microsoft_defender.components.defender_poller:DefenderPollerComponent" ],
        "resilient.circuits.configsection": ["gen_config = fn_microsoft_defender.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_microsoft_defender.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_microsoft_defender.util.selftest:selftest_function"]
    }
)
