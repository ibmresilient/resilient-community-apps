#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v50.0.108

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
    name="fn_mandiant",
    display_name="<<display name of your app here>>",
    version="1.0.0",
    license="<<insert here>>",
    author="<<your name here>>",
    author_email="you@example.com",
    url="<<your company url>>",
    description="<<::CHANGE_ME::>>Enter a short description of the App",
    long_description="""<<::CHANGE_ME::>> Enter a long description, including the key features of the App. \\\nMultiple continuation lines are supported with a backslash. Line breaks are supported too:\n<br>- This will be rendered like a list\n<br>- once the App is installed in SOAR""",
    install_requires=[
        "resilient-circuits>=49.1.0"
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
            "{}FunctionComponent = fn_mandiant.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_mandiant/components/[a-zA-Z]*.py")
        ]
        ,
        "resilient.circuits.configsection": ["gen_config = fn_mandiant.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mandiant.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_mandiant.util.selftest:selftest_function"]
    }
)
