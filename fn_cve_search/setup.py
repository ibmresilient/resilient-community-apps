# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='fn_cve_search',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_cve_search'",
    long_description="""The CVE search API is a RESTful web service allowing to search for vulnerabilities.
                         by using this api vulnerabilities can be searched based on vendor name, product name,
                         specific CVE Id's.
                         the searched results will be updated in CVE Data Table and Incidents Notes section.
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
            "FunctionCveBrowseFunctionComponent = fn_cve_search.components.function_cve_browse:FunctionComponent",
            "FunctionCveSearchFunctionComponent = fn_cve_search.components.function_cve_search:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_cve_search.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_cve_search.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_cve_search.util.selftest:selftest_function"]
    }
)