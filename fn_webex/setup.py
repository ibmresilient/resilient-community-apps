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
    name="fn_webex",
    display_name="Cisco Webex",
    version="2.0.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="http://ibm.biz/soarcommunity",
    description="This package extends the meeting and collaboration functionality of Webex to IBM Security QRadar SOAR Platform ",
    long_description='''This package provides SOAR platform with the ability to interface with Cisco Webex and create rooms teams and meetings.
    The user now can create Meeitngs, Rooms and teams from within a SOAR incident and assign its members to it.''',
    install_requires=[
        "resilient-circuits>=45.0.0"
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_webex.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_webex/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_webex.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_webex.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_webex.util.selftest:selftest_function"]
    }
)
