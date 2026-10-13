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
    name='fn_virustotal',
    display_name="VirusTotal",
    version='1.1.1',
    license='MIT',
    author='IBM SOAR',
    url='https://ibm.biz/soarcommunity',
    description='IBM SOAR app for VirusTotal',
    long_description="""App performs VirusTotal on IP Addresses, URLs, hashes, domain and file artifacts.
Files and URLs may require additional time to complete their scans, so a link is returned to review the results at a later time..<br>

        <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
        <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>
                     """,
    install_requires=[
        "resilient-circuits>=50.0.0",
        'bs4==0.0.1'
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
            "{}FunctionComponent = fn_virustotal.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_virustotal/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_virustotal.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_virustotal.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_virustotal.util.selftest:selftest_function"]
    }
)