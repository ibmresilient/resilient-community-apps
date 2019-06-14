#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_proofpoint',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_proofpoint'",
    long_description="Resilient Circuits Components for 'fn_proofpoint'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient',
        'requests',
        'jinja2',
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnPpCampaignFunctionComponent = fn_proofpoint.components.fn_pp_campaign:FunctionComponent",
            "FnPpForensicsFunctionComponent = fn_proofpoint.components.fn_pp_forensics:FunctionComponent",
            "FnPpThreatPolling = fn_proofpoint.components.fn_pp_threat_polling:PP_ThreatPolling",
        ],
        "resilient.circuits.configsection": ["gen_config = fn_proofpoint.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_proofpoint.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_proofpoint.util.selftest:selftest_function"]
    }
)
