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
    name="fn_trusteer_ppd",
    display_name="Trusteer Pinpoint Detect",
    version="1.0.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://ibm.com/mysupport",
    description="IBM SOAR app for Trusteer Pinpoint Detect",
    long_description="""Bi-directional App for Trusteer Pinpoint Detect. Parse emails from Trusteer Pinpoint Detect \
        and create cases in SOAR and send classification information back to Trusteer.<br>

        <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
        <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        "resilient-circuits>=47.1.0"
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
            "{}FunctionComponent = fn_trusteer_ppd.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_trusteer_ppd/components/[a-zA-Z]*.py")
        ]
        ,
        "resilient.circuits.configsection": ["gen_config = fn_trusteer_ppd.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_trusteer_ppd.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_trusteer_ppd.util.selftest:selftest_function"]
    }
)
