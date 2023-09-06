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
    name="fn_siemplify",
    display_name="Siemplify",
    version="1.0.0",
    license="MIT",
    author="IBM QRadar SOAR",
    author_email="",
    url="https://github.com/ibm/resilient/resilient-community-apps",
    description="Siemplify App for IBM QRadar SOAR",
    long_description="""Bi-directional synchronization with Siemplify Cases, Entities, Attachments and Insights. Additional capabilities exist to list and add entries to the Siemplify Blocklist and Custom List.""",
    install_requires=[
        "resilient-circuits>=43.0.0",
        "jinja2",
        "pytz",
        "retry2 ~= 0.9",
        "simplejson"
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
            "{}FunctionComponent = fn_siemplify.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_siemplify/components/funct_[a-zA-Z]*.py")
        ]+
        [ "PollerComponent = fn_siemplify.components.siemplify_poller:SiemplifyPollerComponent" ],
        "resilient.circuits.configsection": ["gen_config = fn_siemplify.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_siemplify.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_siemplify.util.selftest:selftest_function"]
    }
)
