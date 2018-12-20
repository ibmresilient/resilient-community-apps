# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_query_tor_network',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_query_tar_network'",
    long_description="""The Query TOR Network API is RESTful web service allowing query tar network customer
                    search for IP Addresses or host names in tor relay exit node database.and results
                    will be updated on the Incidents Notes Dashboard.
                 """,
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
            "FnTorFunctionComponent = fn_query_tor_network.components.fn_tor:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_query_tor_network.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_query_tor_network.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_query_tor_network.util.selftest:selftest_function"]
    }
)