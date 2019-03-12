#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_twilio',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='http://ibm.biz/resilientcommunity',
    description="This package contains a function to send an SMS via the Twilio platform",
    long_description="The function uses the Twilio REST API to send an SMS message to a destination number(s)",
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
