#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_machine_learning',
    version='1.0.0',
    license='MIT License',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_machine_learning'",
    long_description="Resilient Circuits Components for 'fn_machine_learning'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'numpy>=1.12.1',
        'scikit-learn>=0.19.2',
        'pandas>=0.23.3',
        'scipy>=1.1.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "MlPredictUrgencyFunctionComponent = fn_machine_learning.components.ml_predict_urgency:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_machine_learning.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_machine_learning.util.customize:customization_data"],
        "console_scripts": ["res-ml = fn_machine_learning.bin.res_ml:main"],

    }
)
