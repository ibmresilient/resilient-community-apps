#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

from setuptools import setup, find_packages

setup(
    name='fn_calendar_invite',
    version='1.1.1',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Components for 'fn_calendar_invite'",
    long_description="Resilient Circuits Components for 'fn_calendar_invite'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient_lib',
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
        "resilient.circuits.customize": ["customize = fn_calendar_invite.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_calendar_invite.util.selftest:selftest_function"]
    }
)