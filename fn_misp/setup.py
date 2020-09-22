#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import glob
import ntpath
import sys

install_requires = ['resilient_circuits>=32.0', 'resilient_lib>=32.0']
if sys.version_info[0] < 3:
    # recommended version from the pymisp docs
    install_requires.append('pymisp==2.4.119.1')
else:
    install_requires.append('pymisp>=2.4')

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
    description="Resilient Circuits Components for 'fn_misp'",
    long_description="This package provides the capability to interct with the MISP REST API. "
                     "Once installed, the user may create events in MISP from Resilient incidents, "
                     "mark artifacts as \"sighted\" if they exist in MISP, "
                     "search MISP events for a given attribute, "
                     "return sightings in MISP for a given event, "
                     "or create a tag on a MISP event or attribute.",
    install_requires=install_requires,
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