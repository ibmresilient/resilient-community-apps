#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_joe_sandbox_analysis',
    version='1.0.1',
    license='Copyright © IBM Corporation 2010, 2018Permission is hereby granted, free of charge, to any person obtaining a copyof this software and associated documentation files (the "Software"), todeal in the Software without restriction, including without limitation therights to use, copy, modify, merge, publish, distribute, sublicense, and/orsell copies of the Software, and to permit persons to whom the Software isfurnished to do so, subject tothe following conditions:The above copyright notice and this permission notice shall be included inall copies or substantial portions of the Software.THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS ORIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THEAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHERLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISINGFROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGSIN THE SOFTWARE.',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Joe Sandbox Function",
    long_description="Resilient Circuits Joe Sandbox Function",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'jbxapi'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnJoeSandboxAnalysisFunctionComponent = fn_joe_sandbox_analysis.components.fn_joe_sandbox_analysis:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_joe_sandbox_analysis.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_joe_sandbox_analysis.util.customize:customization_data"]
    }
)