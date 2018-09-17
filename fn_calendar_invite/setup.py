#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

from setuptools import setup, find_packages

setup(
    name='fn_calendar_invite',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_calendar_invite'",
    long_description="Resilient Circuits Components for 'fn_calendar_invite'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'email; python_version<"3.0"'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnCalendarInviteFunctionComponent = fn_calendar_invite.components.function_calendar_invite:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_calendar_invite.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_calendar_invite.util.customize:customization_data"]
    }
)