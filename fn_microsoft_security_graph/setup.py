#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_microsoft_security_graph',
    version='1.1.1',
    license='MIT',
    author='IBM Resilient',
    author_email='',
    url = 'https://ibm.com/mysupport',
    description="Resilient Circuits Components for 'fn_microsoft_security_graph'",
    long_description="Resilient Circuits Components for 'fn_microsoft_security_graph'",
    install_requires=[
        'resilient_circuits>=35.0.0',
        'resilient-lib>=35.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "MicrosoftSecurityGraphUpdateAlertsIntegrationComponents = fn_microsoft_security_graph.components.microsoft_security_graph_alerts_integrations:IntegrationComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_microsoft_security_graph.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_microsoft_security_graph.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_microsoft_security_graph.util.selftest:selftest_function"]
    }
)
