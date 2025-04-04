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
    name='fn_qradar_integration',
    display_name="QRadar SIEM",
    version='2.4.1',
    license='MIT License',
    author='IBM SOAR',
    author_email='',
    url='https://github.com/ibmresilient/resilient-community-apps/tree/master/fn_qradar_integration',
    description="Set and retrieve information from IBM QRadar SIEM",
    long_description="""This app supports: 
<ul>
<li>executing ariel searches to retrieve data from QRadar.</li> 
<li>functions to find/add/delete reference set items.</li>
<li>functions to add notes to offenses and update offenses (such as close an offense).</li>
</ul>
<br>
Links:
<ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
<ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        'resilient_circuits>=50.0.0',
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_qradar_integration.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_qradar_integration/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_qradar_integration.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_qradar_integration.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_qradar_integration.util.selftest:selftest_function"]
    }
)
