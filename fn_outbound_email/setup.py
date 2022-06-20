#!/usr/bin/env python
#-- coding: utf-8 --
#(c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long

from setuptools import setup, find_packages

setup(
    name='fn_outbound_email',
    version='2.0.0',
    license='MIT',
    author='IBM Resilient',
    url='https://github.com/ibmresilient/resilient-community-apps/tree/master/fn_outbound_email',
    description="Resilient Circuits Components for 'fn_outbound_email'",
    long_description="Resilient Circuits Components for 'fn_outbound_email'",
    install_requires=[
        'resilient_circuits>=39.0.0',
        'resilient_lib>=32.0.0',
        'Jinja2>=2.9.6',
        'six',
        'flask==1.1.1',
        'pyOpenssl==21.0.0'
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
        "console_scripts": [
            "generate_oauth2_refresh_token=fn_outbound_email.bin.generate_oauth2_refresh_token:main"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_outbound_email.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_outbound_email.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_outbound_email.util.selftest:selftest_function"]
    }
)
