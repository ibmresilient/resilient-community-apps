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
    name="fn_maas360",
    version="1.0.1",
    license="MIT",
    author="IBM Resilient",
    url='https://ibm.com/mysupport',
    description="This package enables Mobile Device Management (MDM) actions from IBM Resilient.",
    long_description="""
The MaaS360 function package enables users to perform the following Mobile Device Management (MDM) actions:<br>
- Basic device search.<br>
- Get a list of software and versions installed ona device.<br>
- Locate a device.<br>
- Lock a device.<br>
- Wipe a device.<br>
- Cancel a pending wipe.<br>
- Stop app distribution across specific target devices.<br>
- Delete an app from the MaaS360 catalog.""",
    install_requires=[
        "resilient_circuits>=35.0.0",
        "resilient-lib>35.0.0"
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
            "{}FunctionComponent = fn_maas360.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_maas360/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_maas360.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_maas360.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_maas360.util.selftest:selftest_function"]
    }
)
