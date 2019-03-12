# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='fn_alienvault_otx',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_alienvault_otx'",
    long_description="""The Alien vault OTX is a RESTFul web service, using OTX Direct Connect API allows you to easily 
                        Synchronize the threat Intelligence available on OTX.using the API you can detect the threats 
                        targeting your environment.
                    """,
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
            "FnAlienvaultOtxThreatLookupFunctionComponent = fn_alienvault_otx.components.fn_alienvault_otx_threat_lookup:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_alienvault_otx.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_alienvault_otx.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_alienvault_otx.util.selftest:selftest_function"]
    }
)