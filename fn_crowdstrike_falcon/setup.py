#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_crowdstrike_falcon',
    version='1.0.1',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='http://ibm.biz/resilientcommunity',
    description="Functions to Integration with your CrowdStrike Falcon Platform",
    long_description="This Integration has provides the ability to Search Devices and Contain or Lift Containment on Devices",
    install_requires=[
        'resilient_circuits>=31.0.0',
        'resilient-lib>=32.0.0',
        'six>=1.12.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnCsFalconSearchFunctionComponent = fn_crowdstrike_falcon.components.fn_cs_falcon_search:FunctionComponent",
            "FnCsFalconGetDevicesIocRanOnFunctionComponent = fn_crowdstrike_falcon.components.fn_cs_falcon_get_devices_ioc_ran_on:FunctionComponent",
            "FnCsFalconDeviceActionsFunctionComponent = fn_crowdstrike_falcon.components.fn_cs_falcon_device_actions:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_crowdstrike_falcon.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_crowdstrike_falcon.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_crowdstrike_falcon.util.selftest:selftest_function"]
    }
)