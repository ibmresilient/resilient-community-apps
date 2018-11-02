#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_microsoft_security_graph',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_microsoft_security_graph'",
    long_description="Resilient Circuits Components for 'fn_microsoft_security_graph'",
    install_requires=[
        'resilient_circuits>=30.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "MicrosoftSecurityGraphUpdateAlertFunctionComponent = fn_microsoft_security_graph.components.microsoft_security_graph_update_alert:FunctionComponent",
            "MicrosoftSecurityGraphGetAlertDetailsFunctionComponent = fn_microsoft_security_graph.components.microsoft_security_graph_get_alert_details:FunctionComponent",
            "MicrosoftSecurityGraphAlertsPolling = fn_microsoft_security_graph.components.microsoft_security_graph_alerts_polling:MicrosoftSecurityGraphAlertsPolling"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_microsoft_security_graph.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_microsoft_security_graph.util.customize:customization_data"]
    }
)