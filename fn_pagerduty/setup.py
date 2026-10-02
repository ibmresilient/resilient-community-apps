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
    name='fn_pagerduty',
    display_name="PagerDuty App",
    version='1.2.0',
    url='https://ibm.biz/soarcommunity',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    description="IBM SOAR app for PagerDuty integration",
    long_description="An app that integrates SOAR incidents with PagerDuty incidents. Used to create PagerDuty incidents from SOAR incidents, as well as automatically creating notes and transitioning incidents (acknowledged and resolved)",
    install_requires=[
        'resilient_circuits>=50.0.0',
        'beautifulsoup4~=4.11.1',
        'pdpyras~=4.5.0',
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "{}FunctionComponent = fn_pagerduty.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_pagerduty/components/[a-zA-Z]*.py")
        ]+
            [ "PollerComponent = fn_pagerduty.poller.poller:PollerComponent" ],
        "resilient.circuits.configsection": ["gen_config = fn_pagerduty.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_pagerduty.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_pagerduty.util.selftest:selftest_function"]
    }
)