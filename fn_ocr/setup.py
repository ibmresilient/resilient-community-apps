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
    name="fn_ocr",
    display_name="Image OCR",
    version="1.0.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://ibm.biz/soarcommunity",
    description="IBM SOAR app for text recognition in images",
    long_description="""An App that introduces OCR functionality to SOAR, which can parse text from images. Uses Tesseract OCR, an open-source package with python bindings, to parse an image and return each line with an attached confidence metric.\nAbout OCR: OCR stands for Optical Character Recognition, and most often refers to the detection of letters, words, and sentences in images. The goal with any OCR is the same: extract the useful chunks of text from an image in an easy-to-read format.""",
    install_requires=[
        "resilient-circuits>=45.0.0",
        "pytesseract==0.3.8; python_version <= 3.6",
        "pytesseract~=0.3.9; python_version > 3.6"
        "numpy~=1.19",
        "opencv-python-headless~=4.5.5.64",
        "pandas~=1.1.5"
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_ocr.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_ocr/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_ocr.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_ocr.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_ocr.util.selftest:selftest_function"]
    }
)
