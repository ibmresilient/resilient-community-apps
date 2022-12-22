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
    name='fn_html2pdf',
    version='1.1.0',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url="http://ibm.biz/soarcommunity",
    description="Convert HTML to a PDF",
    long_description="Convert HTML data into a base64 encoded PDF documnent. Alternatively, provide a URL to a website.",
    install_requires=[
        'resilient_circuits>=42.0.0',
        'pika',
        'weasyprint<53.0'
    ],
    python_requires='>=3', # weasyprint no longer supports python27 so we're moving to py3 only
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "{}FunctionComponent = fn_html2pdf.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_html2pdf/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_html2pdf.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_html2pdf.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_html2pdf.util.selftest:selftest_function"]
    }
)