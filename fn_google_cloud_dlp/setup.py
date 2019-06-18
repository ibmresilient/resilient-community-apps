#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_google_cloud_dlp',
    version='1.0.0',
    license='MIT',
    author='Ryan',
    author_email='ryan@resilientlab.co.uk',
    url='http://ibm.biz/resilientcommunity',
    description="Resilient Circuits Components for 'fn_google_cloud_dlp'",
    long_description="The Resilient Integration with Google Cloud DLP provides tools to integrate into your Incident Response Plan. The integration brings Automation and Orchestration capabilities for either identifying, redacting or de-identifying Personally identifiable information (PII) in a body of text.",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib>=32.0.140',
        'google-cloud-dlp>=0.10.0',
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
            "GoogleCloudDlpDeidentifyContentFunctionComponent = fn_google_cloud_dlp.components.google_cloud_dlp_deidentify_content:FunctionComponent",
            "GoogleCloudDlpInspectContentFunctionComponent = fn_google_cloud_dlp.components.google_cloud_dlp_inspect_content:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_google_cloud_dlp.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_google_cloud_dlp.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_google_cloud_dlp.util.selftest:selftest_function"]
    }
)