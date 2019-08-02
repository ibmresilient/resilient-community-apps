#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_proofpoint_trap',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient integration for Proofpoint TRAP",
    long_description="Resilient integration for Proofpoint TRAP. Pulls information data from Proofpoint TRAP",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient',
        'requests',
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
            "FnPptIncidentPolling = fn_proofpoint_trap.components.fn_proofpoint_trap_polling:PPT_IncidentPolling",
        ],
        "resilient.circuits.configsection": ["gen_config = fn_proofpoint_trap.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_proofpoint_trap.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_proofpoint_trap.util.selftest:selftest_function"]
    }
)