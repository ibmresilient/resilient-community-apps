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
    name='fn_misp',
    version='3.0.1',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='http://ibm.biz/resilientcommunity',
    description="Creates Events, Attributes and Sightings in MISP from incidents and artifacts in Resilient.",
    long_description="The purpose of this package is to allow the creation of an event in MISP from an incident in Resilient. "
                     "This could represent a multiple-to-one or a one-to-one relationship. Once the event is created, "
                     "attributes can be populated to it. "
                     "For artifacts which have a hit in MISP, one can create a sighting back to MISP to show threat "
                     "intelligence teams the indicator has been seen in the wild. "
                     "Additional search functions allow one to search all attributes and return sightings from an event. "
                     "This package does not replace or supersede the MISP Custom Threat Service, "
                     "the aim is to supplement it and create a bi-directional connection and integration. "
                     "The package is built in a flexible way so it can be used with any real rule or workflow configuration. "
                     "Sample rules and workflows are provided. "
                     "Custom attribute types can be mapped from the workflow pre-processing script of the function. "
                     "See the sample workflows for sample payloads returned.",
    install_requires=['resilient_circuits>=32.0',
                      'resilient_lib>=32.0',
                      'pymisp>=2.4; python_version>="3"',
                      'pymisp==2.4.119.1; python_version<"3"'
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
            "{}FunctionComponent = fn_misp.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_misp/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_misp.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_misp.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_misp.util.selftest:selftest_function"]
    }
)