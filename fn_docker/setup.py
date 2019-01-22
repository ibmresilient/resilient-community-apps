#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.


from setuptools import setup, find_packages

setup(
    name='fn_docker',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient Support',
    author_email='support@resilientsystems.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_docker'",
    long_description="Resilient Circuits Components for 'fn_docker'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'docker'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "DockerRunDockerContainerFunctionComponent = fn_docker.components.docker_run_docker_container:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_docker.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_docker.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_docker.util.selftest:selftest_function"]
    }
)