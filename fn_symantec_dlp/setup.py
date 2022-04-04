# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
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
    name='fn_symantec_dlp',
    display_name="Symantec DLP",
    version='2.0.0',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url='https://ibm.com/mysupport',
    description="IBM QRadar SOAR app for Symantec DLP",
    long_description="""This app allows bi-directional synchronization between IBM SOAR and Symantec DLP.
    Symantec DLP incidents are escalated to IBM SOAR as cases with the creation of artifacts and notes in SOAR from the incident.""",
    install_requires=[
        'resilient_circuits>=43.0.0',
        'jinja2'
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
            "{}FunctionComponent = fn_symantec_dlp.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_symantec_dlp/components/funct_[a-zA-Z]*.py")
        ]+
            [ "PollerComponent = fn_symantec_dlp.components.dlp_poller:SymantecDLPPollerComponent" ],
        "resilient.circuits.configsection": ["gen_config = fn_symantec_dlp.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_symantec_dlp.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_symantec_dlp.util.selftest:selftest_function"]
    }
)