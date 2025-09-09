#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_proofpoint_tap',
    display_name="Proofpoint TAP",
    version='1.1.2',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url='https://ibm.com/mysupport',
    description="Resilient Circuits Components for 'fn_proofpoint_tap'",
    long_description="""Poll Proofpoint Targeted Attack Protection (TAP) threat events and create cases in IBM SOAR.<br>

        <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
        <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        'resilient_circuits>=51.0.0',
        'resilient-lib>=51.0.6.0'
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
