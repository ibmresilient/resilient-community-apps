#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

from setuptools import setup, find_packages

setup(
    name="fn_calendar_invite",
    display_name="Calendar Invite",
    version='1.1.2',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url="https://ibm.com/mysupport",
    description="Calendar Invitation Function for IBM Security SOAR",
    long_description="""Calendar Invitation Function for IBM Security SOAR
        
        <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
        <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        'resilient_circuits>=49.0.0',
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