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
    name='fn_create_zoom_meeting',
    display_name='Zoom Functions for SOAR',
    version='1.1.0',
    url='http://ibm.biz/soarcommunity',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    description="Functions to create Zoom meetings as part of a security incident response workflow.",
    long_description="This SOAR Function package can be used to create a Zoom meeting from a workflow using the Functions feature of the SOAR Circuits integration framework.",
    install_requires=[
        'resilient_circuits>=42.0.0',
        'pyjwt',
        'pytz',
        'bs4'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "{}FunctionComponent = fn_create_zoom_meeting.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_create_zoom_meeting/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_create_zoom_meeting.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_create_zoom_meeting.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_create_zoom_meeting.util.selftest:selftest_function"]
    }
)