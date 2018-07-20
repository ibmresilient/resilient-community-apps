#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='create_webex_meeting',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='info@resilientsystems.com',
    description="Resilient Circuits Components for 'create_webex_meeting'",
    long_description="Resilient Circuits Components for 'create_webex_meeting'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'requests',
        'pytz'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "CreateWebexMeetingFunctionComponent = create_webex_meeting.components.create_webex_meeting:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = create_webex_meeting.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = create_webex_meeting.util.customize:customization_data"]
    }
)