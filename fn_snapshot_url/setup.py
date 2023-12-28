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
    name="fn_snapshot_url",
    display_name="Snapshot URL",
    version="1.0.0",
    license="MIT",
    author="IBM QRadar SOAR",
    author_email="",
    url="https://github.com/ibmresilient/resilient-community-apps/fn_snapshot_url",
    description="Save snapshots of web pages as incident attachments",
    long_description="""Save snapshots of web pages as incident PNG image attachments""",
    install_requires=[
        "resilient-circuits>=48.0.0",
        "selenium~=4.15.2"
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
            "{}FunctionComponent = fn_snapshot_url.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_snapshot_url/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_snapshot_url.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_snapshot_url.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_snapshot_url.util.selftest:selftest_function"]
    }
)
