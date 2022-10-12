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
    name='fn_google_cloud_dlp',
    version='1.2.0',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url='http://ibm.biz/soarcommunity',
    description="Resilient Circuits Components for 'fn_google_cloud_dlp'",
    long_description="The Resilient Integration with Google Cloud DLP provides tools to integrate into your Incident Response Plan. The integration brings Automation and Orchestration capabilities for either identifying, redacting or de-identifying Personally identifiable information (PII) in a body of text.",
    install_requires=[
        'resilient_circuits>=45.0.0',
        'google-cloud-dlp>=3.7.1',
        'PyPDF2~=2.1.0',
        'python-docx~=0.8.11',
        'defusedxml~=0.7.1',
        'grpcio==1.48.2;python_version<="3.6"', # subdependency of `google-cloud-dlp` that needs to be fixed for PY36
        'grpcio-status==1.48.2;python_version<="3.6"' # subdependency of `google-cloud-dlp` that needs to be fixed for PY36
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "{}FunctionComponent = fn_google_cloud_dlp.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_google_cloud_dlp/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_google_cloud_dlp.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_google_cloud_dlp.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_google_cloud_dlp.util.selftest:selftest_function"]
    }
)