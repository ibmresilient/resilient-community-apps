#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_create_zoom_meeting',
    version='1.0.0',
    url='https://github.com/ibmresilient/resilient-community-apps',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Components for 'fn_create_zoom_meeting'",
    long_description="Resilient Circuits Components for 'fn_create_zoom_meeting'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'pyjwt',
        'requests',
        'pytz',
        'bs4'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnCreateZoomMeetingFunctionComponent = fn_create_zoom_meeting.components.create_zoom_meeting:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_create_zoom_meeting.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_create_zoom_meeting.util.customize:customization_data"]
    }
)