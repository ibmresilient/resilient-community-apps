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
    name="fn_google_cloud_scc",
    display_name="Google Cloud Security Command Center",
    version="1.0.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://ibm.com/mysupport",
    description="IBM SOAR app with bidirectional synchronization and functions for Google Cloud SCC",
    long_description="""Bidirectional synchronization of Google Cloud Security Command Center Findings. Additional functions are provided for manual synchronization, manually updating findings, and listing cloud assets monitored in Google SCC.""",
    install_requires=[
        "resilient-circuits          >= 45.0",
        "google-cloud-securitycenter ~= 1.11",
        'grpcio==1.48.2;python_version<="3.6"', # subdependency of `google-cloud-securitycenter` that needs to be fixed for PY36
        'grpcio-status==1.48.2;python_version<="3.6"' # subdependency of `google-cloud-securitycenter` that needs to be fixed for PY36
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_google_cloud_scc.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_google_cloud_scc/components/[a-zA-Z]*.py")
        ] + 
        [ "PollerComponent = fn_google_cloud_scc.poller.google_cloud_scc_poller:PollerComponent"],
        "resilient.circuits.configsection": ["gen_config = fn_google_cloud_scc.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_google_cloud_scc.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_google_cloud_scc.util.selftest:selftest_function"]
    }
)
