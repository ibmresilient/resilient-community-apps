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
    name="fn_playbook_utils",
    display_name="Playbook Utils",
    version="1.2.1",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://github.com/ibmresilient/resilient-community-apps",
    description="Tools to perform activities on playbooks",
    long_description="""This app includes functions
    <br>
    <ul>
    <li>to mine information about workflow and playbook usage across incidents so that an enterprise can learn the best practices on past threat intelligence and actions performed.</li>
    </ul>""",
    install_requires=[
        "resilient-circuits>=51.0.0",
        "resilient>=51.0",
        "cachetools",
        "defusedxml"
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
            "{}FunctionComponent = fn_playbook_utils.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_playbook_utils/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_playbook_utils.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_playbook_utils.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_playbook_utils.util.selftest:selftest_function"]
    }
)
