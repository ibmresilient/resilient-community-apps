#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_twilio',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_twilio'",
    long_description="Resilient Circuits Components for 'fn_twilio'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'twilio>=6.21.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "TwilioSendSmsFunctionComponent = fn_twilio.components.twilio_send_sms:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_twilio.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_twilio.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_twilio.util.selftest:selftest_function"]
    }
)