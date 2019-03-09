#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_threatminer',
    version='1.0.0',
    license='MIT License',
    author='Michael Piekarski',
    author_email='mpiekarski@essextec.com',
    url='https://essextec.com',
    description="Resilient Circuits integration for ThreatMiner domain",
    long_description="Resilient Circuits integration for ThreatMiner API to gather additional information for artifacts",
    install_requires=[
        'resilient_circuits>=30.0.0',
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
            "ThreatminerDomainWhoisFunctionComponent = fn_threatminer.components.threatminer_domain_whois:FunctionComponent",
            "ThreatminerEmailReverseFunctionComponent = fn_threatminer.components.threatminer_email_reverse:FunctionComponent",
            "ThreatminerSamplesMetadataFunctionComponent = fn_threatminer.components.threatminer_samples_metadata:FunctionComponent",
            "ThreatminerIpWhoisFunctionComponent = fn_threatminer.components.threatminer_ip_whois:FunctionComponent",
            "ThreatminerDomainSubdomainsFunctionComponent = fn_threatminer.components.threatminer_domain_subdomains:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_threatminer.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_threatminer.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_threatminer.util.selftest:selftest_function"]
    }
)
