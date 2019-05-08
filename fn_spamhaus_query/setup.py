# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_spamhaus_query',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_spamhaus_query'",
    long_description="Resilient Circuits Components for 'fn_spamhaus_query'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib>=32.0.140',
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
            "FnSpamhausQuerySubmitArtifactFunctionComponent = fn_spamhaus_query.components.fn_spamhaus_query_submit_artifact:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_spamhaus_query.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_spamhaus_query.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_spamhaus_query.util.selftest:selftest_function"]
    }
)