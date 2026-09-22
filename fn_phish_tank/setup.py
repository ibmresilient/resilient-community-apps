# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_phish_tank',
    display_name='Phish Tank for SOAR',
    version='1.0.4',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url="""<ul><a target='blank' href='https://ibm.biz/soarcommunity'>Support</a></ul>""",
    description="PhishTank Lookup URL Function for IBM QRadar SOAR",
    long_description="""Searches the PhishTank database (https://www.phishtank.com/) to determine if a URL is a phishing URL or not. 
        The information returned from PhishTank is used to update the Artifacts description and add a note to the incident.
    <br>
    Links:
    <ul><a target='blank' href='https://ibm.biz/soarcommunity'>Support</a></ul>
    <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        'resilient_circuits>=51.0.0',
        'python-dateutil>=2.8.0',
        'requests>=2.21.0',
        'resilient-lib>=51.0.6',
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnPhishTankSubmitUrlFunctionComponent = fn_phish_tank.components.fn_phish_tank_submit_url:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_phish_tank.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_phish_tank.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_phish_tank.util.selftest:selftest_function"]
    }
)