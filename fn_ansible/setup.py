# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
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
    name='fn_ansible',
    version='1.2.0',
    license='MIT',
    author='IBM QRadar SOAR',
    display_name="Ansible for SOAR",
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Run Ansible Playbooks and Modules",
    long_description="""This app runs the Ansible environment to allow the running of playbooks and modules against your enterprise.
        Specify the playbooks, hosts and environment variables necessary for execution.""",
    install_requires=[
        'ansible>=9.3.0; python_version>="3.11"',
        'ansible~=8.7.0; python_version=="3.9"',
        'ansible-runner~=2.3.6; python_version>="3.9"',
        'python-daemon~=3.0.1; python_version>="3.9"',
        'ansible==2.8.3; python_version=="3.6"',
        'ansible-runner==1.3.4; python_version=="3.6"',
        'python-daemon==2.3.2; python_version=="3.6"', # a sub dependency of ansible-runner whose version needs to be pinned for PY36
        'resilient_circuits>=50.0.0',
        'resilient_lib>=50.0.0',
        'pywinrm'
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_ansible.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename))for filename in glob.glob("./fn_ansible/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_ansible.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_ansible.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_ansible.util.selftest:selftest_function"]
    }
)
