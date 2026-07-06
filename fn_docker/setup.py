#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.


from setuptools import setup, find_packages

setup(
    name='fn_docker',
    version='1.0.0',
    license='MIT',
    author='Ryan',
    author_email='ryan@resilientlab.co.uk',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="The Resilient Integration with Docker provides tools to integrate Docker into your Incident Response Plan.",
    long_description="This Integration provides the ability to use either existing well-known Docker Images or to create your own, from which a Docker Container will be created and started.",
    install_requires=[
        'resilient_circuits>=31.0.0',
        'docker[ssh]>=3.7.0',
        'resilient-lib>=32.0.0'
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