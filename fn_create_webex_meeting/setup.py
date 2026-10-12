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
    name="fn_create_webex_meeting",
    display_name="Create Webex Meeting",
    version="1.1.2",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="'https://github.com/ibmresilient/resilient-community-apps'",
    description="Resilient Circuits Components for 'fn_create_webex_meeting'",
    long_description="""Perform actions on Github repositories, branches, files, releases, commits and repositories.
    <br>
    Links:
    <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
    <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        "resilient_circuits>=51.0.0",
        "resilient-lib",
        "pytz"
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "{}FunctionComponent = fn_create_webex_meeting.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_create_webex_meeting/components/[a-zA-Z]*.py")        
        ],
        "resilient.circuits.configsection": ["gen_config = fn_create_webex_meeting.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_create_webex_meeting.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_create_webex_meeting.util.selftest:selftest_function"]
    }
)