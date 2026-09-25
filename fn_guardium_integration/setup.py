# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
import glob
import ntpath
from setuptools import setup, find_packages


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
    name='fn_guardium_integration',
    version='1.0.0',
    license='MIT',
    author='Neetin Kandhare',
    author_email='nkandha1@in.ibm.com',
    url='https://ibm.com',
    description="Resilient Circuits Components for 'fn_guardium_integration'",
    long_description="""
    This Resilient Circuit Component provides below features to Resilient:
    1. Automatic Resilient incidents creation based on realtime generated Guardium policy violations & outliers - Disabled.
    2. Generate Guardium Client Secret from Resilient.
    3. Search Active Risk Spotter - Risky Users Scores Report.
    4. Search for sensitive objects.
    5. List Parameter Names By Report Name.
    6. Search for all default Guardium reports.
    7. Search for outlier details.
    """,
    install_requires=[
        'resilient_circuits>=35.0.203',
        'circuits>=3.2',
        'requests>=2.23.0',
        'resilient-lib>=35.0.203',
        'paramiko>=2.7.1',
        'six>=1.14.0',
        'paramiko_expect>=0.2.8'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and
            # create the entry points.
            "{}FunctionComponent = fn_guardium_integration.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_guardium_integration/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_guardium_integration.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_guardium_integration.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_guardium_integration.util.selftest:selftest_function"]
    }
)
