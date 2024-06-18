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
    name='fn_cisco_amp4ep',
    display_name = 'Cisco Secure Endpoint',
    version='1.1.0',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url="https://ibm.com/mysupport",
    description="IBM SOAR Components for Cisco Secure Endpoint",
    long_description="The Cisco Secure Endpoint (formerly, Cisco AMP for Endpoints) integration with the SOAR platform allows for the querying and "
                     "updating of an AMP for Endpoints deployment. The integration includes functions that return "
                     "results which show security events for endpoints in the deployment. The returned results can be "
                     "used to make customized updates to the SOAR platform, such as updating incidents, artifacts, "
                     "data tables and so on. The integration can also be used to make changes to a deployment including "
                     "adding or removing a hash to a blacklist and moving an endpoint to a different group.",
    install_requires=[
        'resilient_circuits>=51.0.0'
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
            "{}FunctionComponent = fn_cisco_amp4ep.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_cisco_amp4ep/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_cisco_amp4ep.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_cisco_amp4ep.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_cisco_amp4ep.util.selftest:selftest_function"]
    }
)