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
    name='fn_sep',
    display_name='Symantec Endpoint Protection',
    version='1.2.0',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Symantec Endpoint Protection Integration for IBM SOAR",
    long_description="""Integration with Symantec Endpoint Protection to facilitate manual enrichment and targeted 
                    remediation actions. Teams can investigate an attack by hunting for IOCs or suspect Endpoints 
                    across an enterprise, and quickly respond to attacks by executing endpoint remediation actions, 
                    such as deleting or blacklisting suspicious files from within the IBM SOAR platform.""",
    install_requires=[
        'resilient_circuits>=51.0.0',
        'resilient_lib>=51.0.0',
        'defusedxml==0.7.1'
    ],
    packages=find_packages(),
    python_requires='>=3.9',
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_sep.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_sep/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_sep.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_sep.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_sep.util.selftest:selftest_function"]
    }
)
