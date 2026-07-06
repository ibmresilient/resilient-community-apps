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
    display_name='Proofpoint TRAP',
    name='fn_proofpoint_trap',
    version='1.0.4',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url="""<ul><a target='blank' href='https://ibm.biz/soarcommunity'>Support</a></ul>""",
    description="IBM QRadar SOAR integration for Proofpoint TRAP",
    long_description="""Perform actions on Github repositories, branches, files, releases, commits and repositories.
    <br>
    Links:
    <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
    <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        'resilient_circuits>=51.0.0',
        'resilient>=51.0.0',
        'resilient_lib>=51.0.6.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnProofpointTrapGetIncidentDetailsFunctionComponent = fn_proofpoint_trap.components.fn_proofpoint_trap_get_incident_details:FunctionComponent",
            "FnProofpointTrapGetListMembersFunctionComponent = fn_proofpoint_trap.components.fn_proofpoint_trap_get_list_members:FunctionComponent",
            "FnProofpointTrapAddMembersToListFunctionComponent = fn_proofpoint_trap.components.fn_proofpoint_trap_add_members_to_list:FunctionComponent",
            "FnProofpointTrapUpdateListMemberFunctionComponent = fn_proofpoint_trap.components.fn_proofpoint_trap_update_list_member:FunctionComponent",
            "FnProofpointTrapDeleteListMemberFunctionComponent = fn_proofpoint_trap.components.fn_proofpoint_trap_delete_list_member:FunctionComponent",
            "FnPptrIncidentPolling = fn_proofpoint_trap.components.fn_proofpoint_trap_polling:PPTRIncidentPolling"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_proofpoint_trap.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_proofpoint_trap.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_proofpoint_trap.util.selftest:selftest_function"]
    }
)