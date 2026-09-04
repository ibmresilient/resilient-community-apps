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
    name='fn_machine_learning_nlp',
    version='1.0.0',
    license='MIT License',
    author='IBM Resilient',
    author_email='',
    url='https://ibm.com/mysupport',
    description="Resilient Circuits Components for 'fn_machine_learning_nlp'",
    long_description="fn_machine_learning_nlp supports NLP search for finding most similar incidents",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'gensim>=3.8.0',
        'numpy>=1.17.2',
        'pandas>=0.25.1',
        'nltk>=3.4.5',
        'beautifulsoup4>=4.8.0',
        'scikit-learn>=0.21.3',
        'scipy>=1.3.1'
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
            "{}FunctionComponent = fn_machine_learning_nlp.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob(
                "fn_machine_learning_nlp/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_machine_learning_nlp.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_machine_learning_nlp.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_machine_learning_nlp.util.selftest:selftest_function"],
        "console_scripts": ["res-ml = fn_machine_learning_nlp.bin.res_ml:main"]
    }
)