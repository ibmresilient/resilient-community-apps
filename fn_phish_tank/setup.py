# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_phish_tank',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_phish_tank'",
    long_description="""This function checks URLs against PhishTank(https://www.phishtank.com/)
     database to see if the URL is flagged as Phishing or not Phishing.""",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'python-dateutil>=2.8.0',
        'requests>=2.21.0',

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