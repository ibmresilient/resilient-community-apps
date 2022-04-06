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
    name="fn_remedy",
    display_name="Remedy for IBM SOAR",
    version="1.0.1",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://ibm.com/mysupport",
    description="Remedy for IBM SOAR",
    long_description="Remedy for IBM SOAR "
                    "This integration provides the capability to create "
                    "new incidents in Remedy from SOAR tasks via the "
                    "HPD:IncidentInterface_Create form over the REST API. "
                    "Once the task is complete, this integration also provides "
                    "the capability to close existing Remedy Incidents.",
    install_requires=[
        "resilient-circuits>=30.0.0",
        "resilient-lib>=39.0.0"
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
            "{}FunctionComponent = fn_remedy.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_remedy/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_remedy.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_remedy.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_remedy.util.selftest:selftest_function"]
    }
)
