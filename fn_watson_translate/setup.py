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
    name='fn_watson_translate',
    version='1.1.0',
    license='MIT',
    author='Resilient Labs',
    author_email='',
    url='http://ibm.biz/soarcommunity',
    description="Resilient Circuits Components for 'fn_watson_translate'",
    long_description="""This function integrates with IBM Watson Translator to provide translation services for text based content.
Machine learning is incorporated to understand the source language for translation.""",
    install_requires=[
        'resilient_circuits>=39.0.0',
        'resilient_lib>=39.0.0',
        'ibm-watson',
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
            "{}FunctionComponent = fn_watson_translate.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_watson_translate/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_watson_translate.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_watson_translate.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_watson_translate.util.selftest:selftest_function"]
    }
)