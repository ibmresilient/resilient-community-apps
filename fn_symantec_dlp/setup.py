# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
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
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components used to establish DLP as a source of Incidents for Resilient",
    long_description="Included in this package are two main components; a Incident Poller used to gather Incidents from DLP and a Resilient Circuits Function for updating a Symantec DLP Incident from Resilient.",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib>=32.0.140',
        'zeep>=3.4.0'
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
            "{}FunctionComponent = fn_symantec_dlp.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_symantec_dlp/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_symantec_dlp.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_symantec_dlp.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_symantec_dlp.util.selftest:selftest_function"]
    }
)