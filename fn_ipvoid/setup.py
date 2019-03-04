# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_ipvoid',
     version='1.0.0',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_ipvoid'",
    long_description="Resilient Circuits Components for 'fn_ipvoid'",
    install_requires=[
        'resilient_circuits>=30.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnIpvoidFunctionComponent = fn_ipvoid.components.function_ipvoid:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_ipvoid.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_ipvoid.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_ipvoid.util.selftest:selftest_function"]
    }
)