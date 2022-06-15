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
    name='fn_netdevice',
    display_name="netMiko for SOAR",
    version='1.1.0',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url='https://ibm.biz/soarcommunity',
    description="Resilient Circuits Components for 'fn_netdevice'",
    long_description="""This implementation utilizes all the functionality of netMiko including:
        <br>
        * Multiple host execution
        <br>
        * Configuration setting execution with commits
        <br>
        * Result parsing using TextFSM templates
    """,
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib',
        'netmiko>=2.3.3'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "{}FunctionComponent = fn_netdevice.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_netdevice/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_netdevice.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_netdevice.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_netdevice.util.selftest:selftest_function"]
    }
)