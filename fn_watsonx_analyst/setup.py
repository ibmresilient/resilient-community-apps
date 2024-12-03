#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.0.974

import glob
import ntpath

from setuptools import setup, find_packages


def get_module_name(module_path):
    """
    Return the module name of the module path
    """
    return ntpath.split(module_path)[1].split(".")[0]


def snake_to_camel(word):
    """
    Convert a word from snake_case to CamelCase
    """
    return "".join(x.capitalize() or "_" for x in word.split("_"))


setup(
    name="fn_watsonx_analyst",
    display_name="watsonx.ai for SOAR Analysts",
    version="1.0.0",
    license="© Copyright IBM Corporation 2024.",
    author="IBM™ Security",
    url="https://ibm.com/security",
    description="Leverage generative AI with watsonx.ai",
    long_description="""Leverage generative AI with watsonx.ai for artifact scanning, incident summarization and Q&A (Questions & Answers), and generic watsonx.ai text generation.""",
    install_requires=["resilient-circuits>=51.0.2.0.0", "scikit-learn==1.5.2", "tiktoken==0.8.0"],
    python_requires=">=3.11",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_watsonx_analyst.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_watsonx_analyst/components/[a-zA-Z]*.py")
        ]
        ,
        "resilient.circuits.configsection": ["gen_config = fn_watsonx_analyst.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_watsonx_analyst.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_watsonx_analyst.util.selftest:selftest_function"]
    }
)
