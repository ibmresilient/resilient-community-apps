#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

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
    name="fn_search_for_py2",
    display_name="Search for Python 2",
    version="1.0.0",
    license="MIT",
    author="IBM QRadar SOAR",
    author_email="",
    url="https://github.com/ibmresilient/resilient_community_apps",
    description="Search for Python 2 in scripts, workflows and playbooks in the SOAR environment",
    long_description="""This app identifies the use of Python 2 in scripts, workflows and playbooks. Python 2 will soon be deprecated from SOAR.
A datatable is used to present the results of any scripts, workflows and playbooks using Python 2.
Scripts, workflows and playbooks identified in the datatable as 'Fixable' can be automatically converted by this app.
    <br>
Links:
<ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
<ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        "resilient-circuits>=51.0.0.0",
        "lxml"
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "console_scripts": [
            "search_for_py2 = fn_search_for_py2.main:main",
        ],
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_search_for_py2.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_search_for_py2/components/[a-zA-Z]*.py")
        ]
        ,
        "resilient.circuits.configsection": ["gen_config = fn_search_for_py2.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_search_for_py2.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_search_for_py2.util.selftest:selftest_function"]
    }
)
