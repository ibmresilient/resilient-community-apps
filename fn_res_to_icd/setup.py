# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

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
    name='fn_res_to_icd',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Manual escalation of Resilient incidents to the ICD Platform",
    long_description="""This integration allows a SOC Analyst to escalate a Resilient incident to the ICD dashboard. 
    If the icd_field_severity or icd_priority is not defined in app.config file, the INTERNAL PRIORITY on ICD platform (4) will be set on the escalated ticket corresponding to that Resilient incident. 
    IP Sources or Destination Artifacts will be automatically added to the icd ticket if the icd_field_severity is not None (or a negative number) in the app.config file.""",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib>=32.0.140',
        'beautifulsoup4>=4.7.1'
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
            "{}FunctionComponent = fn_res_to_icd.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_res_to_icd/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_res_to_icd.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_res_to_icd.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_res_to_icd.util.selftest:selftest_function"]
    }
)