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
    name="fn_zia",
    display_name="Zscaler Internet Access Functions for IBM SOAR",
    version="1.0.1",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="http://ibm.biz/soarcommunity",
    description="Resilient Circuits Components for 'fn_zia'",
    long_description="""The Zscaler Internet Access Integration (ZIA) for SOAR to facilitate manual enrichment and 
        actions against a ZIA environment in the IBM SOAR Platform.
        <br>
        The ZIA Integration provides the following functionality:
        <br>
        * Functions to add URLs, URIs, DNS hostnames and IP addresses to the main blocklist and allowlist.
        <br>
        * Functions to remove URLs, URIs, DNS hostnames and IP addresses from the main blocklist and allowlist.
        <br>
        * Functions to get URL categories and create custom URL categories.
        <br>
        * Functions to add URLs, URIs, DNS hostnames and IP addresses to custom URL categories.
        <br>
        * A function to query the ZIA sandbox for a hash value.
         <br>
        * A function to lookup the category of a URL.
    """,
    install_requires=[
        "resilient-circuits>=30.0.0",
        "resilient-lib>=39.0.0",
        "validators>=0.18.2"
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
            "{}FunctionComponent = fn_zia.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_zia/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_zia.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_zia.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_zia.util.selftest:selftest_function"]
    }
)
