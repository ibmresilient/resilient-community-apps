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
    display_name='Email Header Validation', 
    name='fn_email_header_validation',
    version='1.0.2',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url="""<ul><a target='blank' href='https://ibm.biz/soarcommunity'>Support</a></ul>""",
    description="IBM QRadar SOAR Components for 'fn_email_header_validation'",
    long_description="""Perform actions on Github repositories, branches, files, releases, commits and repositories.
    <br>
    Links:
    <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
    <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        'resilient_circuits>=51.0.0',
        'dkimpy~=1.0.5'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "{}FunctionComponent = fn_email_header_validation.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_email_header_validation/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_email_header_validation.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_email_header_validation.util.customize:customization_data"]
    }
)