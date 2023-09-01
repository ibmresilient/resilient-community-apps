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
    name="fn_rest_api",
    display_name="REST API Functions for SOAR",
    version="1.2.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://ibm.com/mysupport",
    description="Function to call REST web services in the SOAR Platform",
    long_description="""This function calls a REST web service. It supports the standard REST methods: GET, HEAD, POST, PUT, DELETE, OPTIONS and PATCH.
 The function parameters determine the type of call, the URL, and optionally the headers, cookies and body.
 The results include the text or structured (JSON) result from the web service, and additional information including the elapsed time.""",
    install_requires=[
        "resilient-circuits>=46.0.0",
        "PyJWT"
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
            "{}FunctionComponent = fn_rest_api.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_rest_api/components/[a-zA-Z]*.py")
        ]
        ,
        "resilient.circuits.configsection": ["gen_config = fn_rest_api.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_rest_api.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_rest_api.util.selftest:selftest_function"]
    }
)
