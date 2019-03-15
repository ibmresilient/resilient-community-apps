#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_google_cloud_dlp',
    version='1.0.0',
    license='MIT',
    author='Ryan',
    author_email='ryan@resilientlab.co.uk',
    description="Resilient Circuits Components for 'fn_google_cloud_dlp'",
    long_description="An integration with Google Cloud DLP which enables you to inspect an Attachment for Personally Indentifiable Information or to De-Identify an Attachment or Artifact.",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'google-cloud-dlp>=0.10.0'
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