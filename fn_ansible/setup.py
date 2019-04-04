# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_ansible',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Simple agentless IT automation tool.",
    long_description="Automation scripts are written in YAML files called playbook, which are besically tasks and instructions. Those tasks can be performed on a remote system from resilient using this function.",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'ansible==2.7.9'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnAnsibleFunctionComponent = fn_ansible.components.function_ansible:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_ansible.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_ansible.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_ansible.util.selftest:selftest_function"]
    }
)