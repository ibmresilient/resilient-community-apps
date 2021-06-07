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
    name='fn_joe_sandbox_analysis',
    version='1.0.4',
    license='MIT',
    author='IBM Resilient',
    author_email='resil.labs@gmail.com',
    url='http://ibm.biz/resilientcommunity',
    description="Resilient Circuits Joe Sandbox Function",
    long_description="Resilient Circuits Joe Sandbox Function",
    install_requires=[
        'resilient_circuits>=32.0.0',
        'jbxapi==2.10.1',
        'resilient_lib'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
        "{}FunctionComponent = fn_joe_sandbox_analysis.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_joe_sandbox_analysis/components/[a-zA-Z]*.py")
	],
        "resilient.circuits.configsection": ["gen_config = fn_joe_sandbox_analysis.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_joe_sandbox_analysis.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_joe_sandbox_analysis.util.selftest:selftest_function"]
    }
)
