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
    name='fn_task_utils',
    display_name="Task Utilities Function for SOAR",
    version='1.1.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='http://ibm.biz/resilientcommunity',
    description="Resilient Circuits Components for 'fn_task_utils'",
    long_description="""Resilient Circuits Components which can be used to manipulate existing tasks or create new ones. Provides functions which can be invoked through standalone example rules or can be integrated as part of a custom workflow<br>
    Link:
        <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
        <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>
        <ul><a target='blank' href='https://ibmresilient.github.io/resilient-community-apps/fn_soar_utils/README.html'>App Documentation</a></ul>""",
    install_requires=[
        'resilient_circuits>=51.0.0',
        'resilient_lib>=51.0.0'
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
            "{}FunctionComponent = fn_task_utils.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_task_utils/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_task_utils.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_task_utils.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_task_utils.util.selftest:selftest_function"]
    }
)