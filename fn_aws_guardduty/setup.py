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
    name="fn_aws_guardduty",
    display_name="AWS GuardDuty",
    version="2.0.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url='https://ibm.com/mysupport',
    description="Amazon AWS GuardDuty Integration for SOAR",
    long_description="""The Amazon AWS GuardDuty Integration for SOAR allows you to process and respond to Amazon 
        AWS GuardDuty findings within the IBM SOAR Platform.
        <br>
        The AWS GuardDuty Integration provides the following functionality:
        <ul>
        * A poller which gathers current findings from GuardDuty and escalates to the SOAR platform as incidents.
        </ul><ul>
        * A function to archive a GuardDuty finding when the corresponding SOAR incident is closed.
        </ul><ul>
        * A function to refresh a SOAR incident with the latest information from the corresponding GuardDuty finding.
        </ul><br>
        Links:
<ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
<ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>
        """,
    install_requires=[
        'resilient_circuits>=51.0.0',
        'resilient_lib>=51.0.6',
        'boto3>=1.16.19'
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
            "{}FunctionComponent = fn_aws_guardduty.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_aws_guardduty/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_aws_guardduty.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_aws_guardduty.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_aws_guardduty.util.selftest:selftest_function"]
    }
)


