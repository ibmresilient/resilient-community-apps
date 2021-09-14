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
    version='1.1.0',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url='http://ibm.biz/soarcommunity',
    description="Resilient Circuits Components for 'fn_google_cloud_dlp'",
    long_description="The Resilient Integration with Google Cloud DLP provides tools to integrate into your Incident Response Plan. The integration brings Automation and Orchestration capabilities for either identifying, redacting or de-identifying Personally identifiable information (PII) in a body of text.",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib>=32.0.140',
        'google-cloud-dlp>=0.10.0,<2.0.0',
        'PyPDF2>=1.26.0',
        'python-docx>=0.8.10'
    ],
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