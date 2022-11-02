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
    name="fn_darktrace",
    display_name="Darktrace",
    version="1.0.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://ibm.com/mysupport",
    description="IBM SOAR app for bi-directional synchronization with Darktrace Threat Visualizer",
    long_description="""Bi-directional App for Darktrace. Pulls in new AI Analyst Events as they are created \
        and creates a case in SOAR for each group of events.
    <br>As new events are added to a group, the case automatically updates with the new data.
    <br><br>Also provides functionality for acknowledging an event, group, or breach,\
        sending notes to Darktrace, listing similar devices in Darktrace,\
        and getting external endpoint details from Darktrace.""",
    install_requires=[
        "resilient-circuits>=47.0.0"
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
            "{}FunctionComponent = fn_darktrace.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_darktrace/components/[a-zA-Z]*.py")
        ]
        + [
            "PollerComponent = fn_darktrace.poller.poller:PollerComponent"
        ]
        ,
        "resilient.circuits.configsection": ["gen_config = fn_darktrace.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_darktrace.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_darktrace.util.selftest:selftest_function"]
    }
)
