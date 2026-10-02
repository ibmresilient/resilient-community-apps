#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Generated with resilient-sdk v48.2.4321

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
    name="fn_artifact_utils",
    display_name="Artifact Functions for SOAR",
    version="1.0.1",
    license="Apache",
    author="Nick Mumaw",
    author_email="Nick.Mumaw@ibm.com",
    url="http://ibm.biz/soarcommunity",
    description="Functions allowing interactions with Artifacts.",
    long_description="""This package contains 4 functions allowing you to interact with SOAR Artifacts for use with other automations. The capabilities this app supports is:<br>- Searching for Artifacts<br>- Tagging Artifacts<br>- Removing Tags<br>- Deleting Artifacts""",
    install_requires=[
        "resilient-circuits>=51.0.0"
    ],
    python_requires='>=3.9',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_artifact_utils.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_artifact_utils/components/[a-zA-Z]*.py")
        ]
        ,
        "resilient.circuits.configsection": ["gen_config = fn_artifact_utils.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_artifact_utils.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_artifact_utils.util.selftest:selftest_function"]
    }
)
