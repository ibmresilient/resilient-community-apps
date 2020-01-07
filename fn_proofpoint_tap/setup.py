#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_proofpoint_tap',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    url='https://success.resilientsystems.com/',
    description="Resilient Circuits Components for 'fn_proofpoint_tap'",
    long_description="Resilient Circuits Components for 'fn_proofpoint_tap'",
    install_requires=[
        'resilient_circuits>=32.0.186',
        'resilient-lib'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnPpCampaignFunctionComponent = fn_proofpoint_tap.components.fn_pp_campaign:FunctionComponent",
            "FnPpForensicsFunctionComponent = fn_proofpoint_tap.components.fn_pp_forensics:FunctionComponent",
            "FnPpThreatPolling = fn_proofpoint_tap.components.fn_pp_threat_polling:PP_ThreatPolling",
        ],
        "resilient.circuits.configsection": ["gen_config = fn_proofpoint_tap.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_proofpoint_tap.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_proofpoint_tap.util.selftest:selftest_function"]
    }
)
