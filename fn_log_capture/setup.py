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
    display_name='Log Capture',
    name='fn_log_capture',
    version='1.0.1',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    url="""<ul><a target='blank' href='https://ibm.biz/soarcommunity'>Support</a></ul>""",
    description="IBM QRadar SOAR Components for 'fn_log_capture'. Capture log data within Resilient from an Integrations server.",
    long_description="""Perform actions on Github repositories, branches, files, releases, commits and repositories.
    <br>
    Links:
    <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
    <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        'resilient_circuits>=51.0.0',
        'resilient-lib>=51.0.0'
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
            "{}FunctionComponent = fn_log_capture.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_log_capture/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_log_capture.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_log_capture.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_log_capture.util.selftest:selftest_function"]
    }
)