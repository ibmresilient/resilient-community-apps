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
    name="fn_parse_utilities",
    display_name="Parse Utilities Function for SOAR",
    version="1.1.1",
    license="MIT",
    author="IBM SOAR",
    url="http://ibm.biz/soarcommunity",
    description="Useful playbook functions to use for common parsing in the SOAR platform",
    long_description="""This package contains functions to parse information from emails, ssl certificates, and PDFs as well as a function to transform an XML document using a preexisting xsl stylesheet.""",
    install_requires=[
        "resilient-circuits",
        'pdfid~=1.1',
        'defusedxml~=0.7.1',
        'lxml~=4.8',
        'cryptography>=42.0.4', # Defining minimum to fix CVE-2024-6119, CVE-2024-26130, CVE-2023-50782 for SOARAPPS-9089
        'pyOpenSSL>=24.0', # Defining minimum to fix CVE-2024-6119, CVE-2024-26130, CVE-2023-50782 for SOARAPPS-9089
        'mail-parser~=4.1.2'
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
            "{}FunctionComponent = fn_parse_utilities.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_parse_utilities/components/[a-zA-Z]*.py")
        ]
        ,
        "resilient.circuits.configsection": ["gen_config = fn_parse_utilities.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_parse_utilities.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_parse_utilities.util.selftest:selftest_function"]
    }
)
