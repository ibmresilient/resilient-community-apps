# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# #!/usr/bin/env python
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
    name='fn_secureworks_ctp',
    version='0.9.1',
    license='MIT',
    author_email='',
    url='https://ibm.com/mysupport',
    description="Resilient Circuits Components for 'fn_secureworks_ctp'",
    long_description="Resilient Circuits Components for 'fn_secureworks_ctp'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib>=35.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "fn_secureworks_ctpFunctionComponent = fn_secureworks_ctp.components.scwx_ctp_poll:SecureworksCTPPollComponent",
            "funct_secureworks_ctp_close_ticketFunctionComponent = fn_secureworks_ctp.components.funct_secureworks_ctp_close_ticket:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_secureworks_ctp.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_secureworks_ctp.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_secureworks_ctp.util.selftest:selftest_function"]
    }
)