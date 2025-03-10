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
    name='fn_mitre_integration',
    version='2.2.1',
    license='MIT License',
    author='IBM QRadar SOAR',
    author_email='support@resilientsystems.com',
    description="IBM SOAR Components for 'fn_mitre_integration'",
    long_description="""Retrieve information related to MITRE ATT&CK tactics and techniques from MITRE's STIX TAXII server.
<br>
<ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
<ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        'resilient_lib',
        'resilient_circuits>=51.0.0',
        'stix2',
        'taxii2-client>=2.3.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
             # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_mitre_integration.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_mitre_integration/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_mitre_integration.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mitre_integration.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_mitre_integration.util.selftest:selftest_function"]
    }
)
