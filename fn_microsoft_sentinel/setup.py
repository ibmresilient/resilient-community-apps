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

def get_function_list():
    return ["{}FunctionComponent = fn_microsoft_sentinel.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_microsoft_sentinel/components/funct_[a-zA-Z]*.py")]

setup(
    name="fn_microsoft_sentinel",
    display_name="Microsoft Sentinel",
    version="1.0.3",
    license="MIT",
    author="IBM Resilient",
    author_email="",
    url="https://github.com/ibmresilient/fn_microsoft_sentinel",
    description="Resilient Circuits Components for 'fn_microsoft_sentinel'",
    long_description="""This app allows bi-directional synchronization between IBM SOAR and Microsoft Sentinel.
    Key features:
    * Escalate Microsoft Sentinel Incidents to IBM Resilient SOAR Cases
    * Automatically keep Incidents and Cases synchronized
    * Retrieve Sentinel Incident alert entities as artifacts
    * Sync comments to and from Sentinel Incidents
    * Support editable templates for field mapping between the two systems""",
    install_requires=[
        "resilient_circuits>=37.0.0",
        "resilient-lib>=37.0.0",
        "jinja2",
        "simplejson"
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
                "{}FunctionComponent = fn_microsoft_sentinel.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_microsoft_sentinel/components/f[a-zA-Z]*.py")
            ]+
            [ "PollerComponent = fn_microsoft_sentinel.components.sentinel_poller:SentinelPollerComponent" ],
        "resilient.circuits.configsection": ["gen_config = fn_microsoft_sentinel.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_microsoft_sentinel.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_microsoft_sentinel.util.selftest:selftest_function"]
    }
)
