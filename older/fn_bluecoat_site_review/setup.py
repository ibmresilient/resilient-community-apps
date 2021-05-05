#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_bluecoat_site_review',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Components for 'fn_bluecoat_site_review'",
    long_description="Resilient Circuits Components for 'fn_bluecoat_site_review'",
    install_requires=[
        'resilient_circuits>=31.0.0',
        'xmltodict'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "BluecoatSiteReviewLookupFunctionComponent = fn_bluecoat_site_review.components.bluecoat_site_review_lookup:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_bluecoat_site_review.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_bluecoat_site_review.util.customize:customization_data"]
    }
)
