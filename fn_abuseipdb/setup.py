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
    name="fn_abuseipdb",
    display_name="AbuseIPDB Function for IBM SOAR",
    version="1.0.1",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://github.com/ibmresilient/fn_abuseipdb",
    description="IBM Security SOAR app for AbuseIPDB'",
    long_description="""This app pulls data from AbuseIPDB (www.abuseipdb.com) and checks if an IP artifact is blacklisted. If so, it will add a hit to the artifact. This app requires an AbuseIPDB account and an v2 api key to work.""",
    install_requires=[
        "resilient-circuits>=43.0.0",
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
            "{}FunctionComponent = fn_abuseipdb.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_abuseipdb/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_abuseipdb.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_abuseipdb.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_abuseipdb.util.selftest:selftest_function"]
    }
)
