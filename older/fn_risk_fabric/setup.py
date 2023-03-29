#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_risk_fabric',
    version='1.0.0',
    license='Resilient License',
    author='Bay Dynamics',
    author_email='support@baydynamics.com',
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
            "RfSetEventMitigationsFunctionComponent = fn_risk_fabric.components.rf_set_event_mitigations:FunctionComponent",
            "RfGetHostRiskFunctionComponent = fn_risk_fabric.components.rf_get_host_risk:FunctionComponent",
            "RfSetEventClassificationsFunctionComponent = fn_risk_fabric.components.rf_set_event_classifications:FunctionComponent",
            "RfGetRiskModelInstanceDetailsFunctionComponent = fn_risk_fabric.components.rf_get_risk_model_instance_details:FunctionComponent",
            "RfGetRiskModelInstancesFunctionComponent = fn_risk_fabric.components.rf_get_risk_model_instances:FunctionComponent",
            "RfGetIpRiskFunctionComponent = fn_risk_fabric.components.rf_get_ip_risk:FunctionComponent",
            "RfGetActionPlansFunctionComponent = fn_risk_fabric.components.rf_get_action_plans:FunctionComponent",
            "RfGetUserRiskFunctionComponent = fn_risk_fabric.components.rf_get_user_risk:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_risk_fabric.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_risk_fabric.util.customize:customization_data"]
    }
)