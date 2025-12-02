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
    name="fn_timer",
    display_name="Timer Function for SOAR",
    version="1.0.1",
    license="MIT",
    author="IBM SOAR",
    url="""<ul><a target='blank' href='https://ibm.biz/soarcommunity'>Support</a></ul>""",
    description="Simple timer function to be used in the SOAR platform",
    long_description="""App used in the SOAR platform. A workflow using this function will sleep for the
        specified amount of time. The function takes as input timer_time or timer_epoch as input.
        The function periodically checks the status of the calling workflow and will end
        function execution if the workflow has been terminated.
        Links:
    <ul><a target='blank' href='https://ibm.biz/soarcommunity'>Support</a></ul>
    <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        "resilient-circuits>=51.0.0"
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
            "{}FunctionComponent = fn_timer.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_timer/components/[a-zA-Z]*.py")
        ]
        ,
        "resilient.circuits.configsection": ["gen_config = fn_timer.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_timer.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_timer.util.selftest:selftest_function"]
    }
)
