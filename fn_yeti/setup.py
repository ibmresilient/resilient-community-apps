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
    name="fn_yeti",
    display_name="Yeti",
    version="1.0.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://github.com/ibmresilient/fn_yeti",
    description="IBM Security SOAR app for Yeti",
    long_description="""Queries Yeti and updates SOAR with any information gained on the artifact. All Yeti observables are supported by this integration. For more info about YETI platform, please visit https://yeti-platform.github.io.	""",
    install_requires=[
        "resilient-circuits>=44.0.0",
        "pyeti-python3~=1.1"
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
            "{}FunctionComponent = fn_yeti.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_yeti/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_yeti.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_yeti.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_yeti.util.selftest:selftest_function"]
    }
)
