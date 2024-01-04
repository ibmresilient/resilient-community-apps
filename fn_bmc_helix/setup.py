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
    name="fn_bmc_helix",
    display_name="BMC Helix",
    version="1.0.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://ibm.com/mysupport",
    description="BMC Helix for IBM SOAR",
    long_description="BMC Helix for IBM SOAR "
                    "This integration provides the capability to create "
                    "new incidents in BMC Helix from SOAR tasks and incidents via the "
                    "HPD:IncidentInterface_Create form over the REST API. "
                    "Once the task or incident is complete, this integration also provides "
                    "the capability to close existing BMC Helix Incidents.",
    install_requires=[
        "resilient-circuits>=46.0.0"
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
            "{}FunctionComponent = fn_bmc_helix.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_bmc_helix/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_bmc_helix.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_bmc_helix.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_bmc_helix.util.selftest:selftest_function"]
    }
)
