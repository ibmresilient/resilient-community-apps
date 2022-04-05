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
    name='fn_microsoft_security_graph',
    display_name='Microsoft Security Graph Integration for SOAR',
    version='1.2.0',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url = 'https://ibm.com/mysupport',
    description="SOAR Components for 'fn_microsoft_security_graph'",
    long_description="SOAR Components for 'fn_microsoft_security_graph'",
    install_requires=[
        'resilient_circuits>=35.0.0',
        'resilient-lib>=35.0.0'
    ],
    packages=find_packages(),
    python_requires='>=3',
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "{}FunctionComponent = fn_microsoft_security_graph.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_microsoft_security_graph/components/funct_[a-zA-Z]*.py")
            # "MicrosoftSecurityGraphUpdateAlertsIntegrationComponents = fn_microsoft_security_graph.components.microsoft_security_graph_alerts_integrations:IntegrationComponent"
        ] +
        [ "PollerComponent = fn_microsoft_security_graph.components.poller:PollerComponent" ],
        "resilient.circuits.configsection": ["gen_config = fn_microsoft_security_graph.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_microsoft_security_graph.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_microsoft_security_graph.util.selftest:selftest_function"]
    }
)
