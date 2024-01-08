#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long

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
    name="fn_relations",
    display_name="Parent/Child Relationships",
    version="3.0.0",
    license="MIT",
    author="Nick Mumaw",
    author_email="Nick.Mumaw@ibm.com",
    url="http://ibm.biz/soarcommunity",
    description="Builds Relationships of Incidents within IBM Security SOAR",
    long_description="""App used within the SOAR platform allowing the relationship building of incidents as Children and Parents.
    The app will also allow syncing of notes between the incidents with a relationship, auto closing child incidents of a closed parent,
    and syncing changes in child status with the parent datatable that shows all children.""",
    install_requires=[
        "resilient-circuits>=48.0.0"
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_relations.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_relations/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_relations.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_relations.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_relations.util.selftest:selftest_function"]
    }
)
