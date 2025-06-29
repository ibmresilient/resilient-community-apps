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
    name="fn_microsoft_sentinel",
    display_name="Microsoft Sentinel",
    version="2.2.0",
    license="MIT",
    author="IBM QRadar SOAR",
    url="https://github.com/ibmresilient/resilient-community-apps/tree/main/fn_microsoft_sentinel",
    description="SOAR integration for Microsoft Sentinel",
    long_description="""This app allows bi-directional synchronization between IBM SOAR and Microsoft Sentinel.
    <br>Key features:
    <br>* Escalate Microsoft Sentinel Incidents to IBM SOAR Cases
    <br>* Automatically keep Incidents and Cases synchronized
    <br>* Retrieve Sentinel Incident alert entities as artifacts
    <br>* Sync comments to and from Sentinel Incidents
    <br>* Support editable templates for field mapping between the two systems
    <br>
Links:
<ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
<ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        "resilient_circuits>=51.0.0",
        "jinja2~=3.1.0",
        "simplejson~=3.19.0",
        "retry2"
    ],
    packages=find_packages(),
    python_requires='>=3.9',
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
                # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
                "{}FunctionComponent = fn_microsoft_sentinel.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_microsoft_sentinel/components/funct_[a-zA-Z]*.py")
            ]+
            [ "PollerComponent = fn_microsoft_sentinel.poller.poller:PollerComponent" ],
        "resilient.circuits.configsection": ["gen_config = fn_microsoft_sentinel.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_microsoft_sentinel.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_microsoft_sentinel.util.selftest:selftest_function"]
    }
)
