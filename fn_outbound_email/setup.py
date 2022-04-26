#!/usr/bin/env python
#-- coding: utf-8 --
#(c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long

from setuptools import setup, find_packages

setup(
    name='fn_outbound_email',
    display_name='Outbound Email',
    version='1.3.1',
    license='MIT',
    author='IBM QRadar SOAR',
    url='https://github.com/ibmresilient/resilient-community-apps/tree/master/fn_outbound_email',
    description="IBM Security SOAR app for 'fn_outbound_email'",
    long_description="IBM Security SOAR app for 'fn_outbound_email'",
    install_requires=[
        'resilient_circuits>=39.0.0',
        'resilient_lib>=32.0.0',
        'Jinja2>=2.9.6',
        'six'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "SendEmailFunctionComponent = fn_outbound_email.components.send_email:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_outbound_email.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_outbound_email.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_outbound_email.util.selftest:selftest_function"]
    }
)
