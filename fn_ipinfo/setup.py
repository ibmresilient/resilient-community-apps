#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_ipinfo',
    version='1.0.0',
    license='MIT',
    author='Ryan',
    author_email='ryan@resilientlab.co.uk',
    url='https://ibm.biz/resilientcommunity',
    description="Resilient Circuits Components for IPInfo IP Enrichment API",
    long_description="Contains a function which accepts an IP Address as an input and attempts to query IPInfo against this IP",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'ipinfo',
        'ipaddress'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnIpinfoQueryIpAddressFunctionComponent = fn_ipinfo.components.fn_ipinfo_query_ip_address:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_ipinfo.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_ipinfo.util.customize:customization_data"]
    }
)