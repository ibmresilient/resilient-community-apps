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
    name='fn_ioc_parser_v2',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='http://ibm.biz/resilientcommunity',
    description="These functions extract Indicators of Compromise (IOCs) from Resilient attachments and files.",
    long_description="""Uses the IOCParser Python Library to extract IOCs from Resilient Attachments and Artifacts. 
                        All unique IOCs that are found are added to the Resilient Incident as an Artifact.""",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'iocparser>=1.0.14',
        'pdfminer.six>=20181108',
        'python-docx>=0.8.10',
        'xlrd>=1.2.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_ioc_parser_v2.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_ioc_parser_v2/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_ioc_parser_v2.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_ioc_parser_v2.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_ioc_parser_v2.util.selftest:selftest_function"]
    }
)
