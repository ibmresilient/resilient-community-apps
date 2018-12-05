#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_html2pdf',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Components for 'fn_html2pdf'",
    long_description="Convert HTML data into a base64 encoded PDF documnent. Alternatively, provide a URL to a website.",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'pika',
        'weasyprint'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "Html2PdfFunctionComponent = fn_html2pdf.components.html2pdf:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_html2pdf.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_html2pdf.util.customize:customization_data"]
    }
)