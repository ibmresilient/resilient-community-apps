#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_urlscanio',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_urlscanio'",
    long_description="Resilient Circuits Components for 'fn_urlscanio'",
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
            "UrlscanioFunctionComponent = fn_urlscanio.components.urlscanio:FunctionComponent",
            "Base64ToAttachmentFunctionComponent = fn_urlscanio.components.base64_to_attachment:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_urlscanio.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_urlscanio.util.customize:customization_data"]
    }
)