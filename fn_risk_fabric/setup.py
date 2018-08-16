#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_risk_fabric',
    version='1.0.0',
    license='Resilient License',
    author='Bay Dynamics',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_risk_fabric'",
    long_description="Resilient Circuits Components for 'fn_risk_fabric'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'requests'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "GetHostRiskFunctionComponent = fn_risk_fabric.components.get_host_risk:FunctionComponent",
            "GetRiskModelInstancesFunctionComponent = fn_risk_fabric.components.get_risk_model_instances:FunctionComponent",
            "GetUserRiskFunctionComponent = fn_risk_fabric.components.get_user_risk:FunctionComponent",
            "SetEventClassificationsFunctionComponent = fn_risk_fabric.components.set_event_classifications:FunctionComponent",
            "GetRiskModelInstanceDetailsFunctionComponent = fn_risk_fabric.components.get_risk_model_instance_details:FunctionComponent",
            "SetEventMitigationsFunctionComponent = fn_risk_fabric.components.set_event_mitigations:FunctionComponent",
            "GetActionPlansFunctionComponent = fn_risk_fabric.components.get_action_plans:FunctionComponent",
            "GetIpRiskFunctionComponent = fn_risk_fabric.components.get_ip_risk:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_risk_fabric.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_risk_fabric.util.customize:customization_data"]
    }
)