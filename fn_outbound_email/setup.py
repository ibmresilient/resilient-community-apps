#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_outbound_email',
    version='1.0.6',
    license='See license file',
    author='IBM Security Expert Labs',
    url='https://www.ibm.com/security/intelligent-orchestration/resilient',
    description="Resilient Circuits Components for 'fn_outbound_email'",
    long_description="Resilient Circuits Components for 'fn_outbound_email'",
    install_requires=[
        'resilient_circuits>=35.0.203',
        'resilient_lib>=35.0.203',
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