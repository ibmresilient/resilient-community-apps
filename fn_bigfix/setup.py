#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_bigfix',
    version='1.1.2',
    license='Resilient License',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for BigFix",
    long_description="""BigFix is a systems-management platform for managing a large numbers of endpoints.
        The BigFix integration with the Resilient platform allows for the querying and updating of a BigFix deployment. 
        The integration includes a function to query for IOCs in the BigFix environment. Returned results can be used 
        to remediate issues or hits, such as a malicious path or filename,  a service or process name, or a registry 
        key. The integration can also be used to query properties of an endpoint.""",
    install_requires=[
        'resilient_circuits>=31.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnBigfixAssetsFunctionComponent = fn_bigfix.components.fn_bigfix_assets:FunctionComponent",
            "FnBigfixActionStatusFunctionComponent = fn_bigfix.components.fn_bigfix_action_status:FunctionComponent",
            "FnBigfixArtifactFunctionComponent = fn_bigfix.components.fn_bigfix_artifact:FunctionComponent",
            "FnBigfixRemediationFunctionComponent = fn_bigfix.components.fn_bigfix_remediation:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_bigfix.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_bigfix.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_bigfix.util.selftest:selftest_function"]
    }
)
