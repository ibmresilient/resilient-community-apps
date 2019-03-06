# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_mxtoolbox',
    version='1.0.1',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_mxtoolbox'",
    long_description="""The MxToolBox API is a RESTful Web Service allowing MxToolbox customers 
    to query the status of their monitors and run lookups (blacklist, smtp, mx, etc.). Generally, 
    programmers use this API to integrate MxToolBox into their products. For example,
    customers have created a dashboard on their site which shows
    the real-time status of their monitors.""",
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
            "FnMxtoolboxFunctionComponent = fn_mxtoolbox.components.function_mxtoolbox:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_mxtoolbox.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mxtoolbox.util.customize:customization_data"]
    }
)