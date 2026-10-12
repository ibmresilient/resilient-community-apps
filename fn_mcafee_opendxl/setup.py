#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_mcafee_opendxl',
    version='1.2.0',
    license='MIT',
    author='IBM Resilient',
    url='https://ibm.com/mysupport',
    author_email='',
    description="Resilient Circuits Components for McAfee publishing to DXL Functions",
    long_description="Publish a message to on OpenDXL topic. Listen on the default DXL topic and create incidents and artifacts in Resilient based on received messages.",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient_lib',
        'PySocks<1.7', # required for dxclient even though resilient circuits allows ~= 1.6
        'dxlclient'
    ],
    python_requires='<3.11', # because dxlclient requires PySocks<1.7, PY311 requires PySocks >= 1.7
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "McafeePublishToDxlFunctionComponent = fn_mcafee_opendxl.components.mcafee_publish_to_dxl:FunctionComponent",
            "McafeeSubscribeToDxlComponent = fn_mcafee_opendxl.components.mcafee_subscribe_to_dxl:DxlComponentSubscriber"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_mcafee_opendxl.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mcafee_opendxl.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_mcafee_opendxl.util.selftest:selftest_function"]
    }
)
