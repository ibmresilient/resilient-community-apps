#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import glob
import ntpath

def get_module_name(module_path):
    """
    Return the module name of the module path
    """
    return ntpath.split(module_path)[1].split(".")[0]

def snake_to_camel(word):
    """
    Convert a word from snake_case to CamelCase
    """
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

setup(
    name='fn_whois_rdap',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Retrieving registry information for IP, URL or DNS Artifacts",
    long_description="""This integration retrieves registry information (via the RDAP protocol) for IP, URL or DNS Artifacts that provides
    enrichment and threat intelligence on suspicious address. The information is added directly to artifact description and can include
    dns-zone, asn and asn description & other useful metadata. """,
    install_requires=[
        'resilient_circuits>=31.0.0',
        'resilient_lib>=33.0.189',
        'ipwhois>=1.1.0',
        'tldextract>=2.2.1'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_whois_rdap.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_whois_rdap/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_whois_rdap.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_whois_rdap.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_whois_rdap.util.selftest:selftest_function"]
    }
)