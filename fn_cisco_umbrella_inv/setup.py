#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_cisco_umbrella_inv',
    version='1.0.0',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_cisco_umbrella_inv'",
    long_description="Resilient Circuits Components for 'fn_cisco_umbrella_inv'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'investigate>=1.3.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "UmbrellaPatternSearchFunctionComponent = fn_cisco_umbrella_inv.components.umbrella_pattern_search:FunctionComponent",
            "UmbrellaDomainStatusAndCategoryFunctionComponent = fn_cisco_umbrella_inv.components.umbrella_domain_status_and_category:FunctionComponent",
            "UmbrellaIpLatestMaliciousDomainsFunctionComponent = fn_cisco_umbrella_inv.components.umbrella_ip_latest_malicious_domains:FunctionComponent",
            "UmbrellaDnsRrHistFunctionComponent = fn_cisco_umbrella_inv.components.umbrella_dns_rr_hist:FunctionComponent",
            "UmbrellaTimelineFunctionComponent = fn_cisco_umbrella_inv.components.umbrella_timeline:FunctionComponent",
            "UmbrellaDomainSecurityInfoFunctionComponent = fn_cisco_umbrella_inv.components.umbrella_domain_security_info:FunctionComponent",
            "UmbrellaDomainCoOccurrencesFunctionComponent = fn_cisco_umbrella_inv.components.umbrella_domain_co_occurrences:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_cisco_umbrella_inv.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_cisco_umbrella_inv.util.customize:customization_data"]
    }
)