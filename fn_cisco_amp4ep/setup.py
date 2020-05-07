#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_cisco_amp4ep',
    version='1.0.1',
    license='Resilient License',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for Cisco AMP for Endpoints",
    long_description="The Cisco AMP for Endpoints integration with the Resilient platform allows for the querying and "
                     "updating of an AMP for Endpoints deployment. The integration includes 12 functions that return "
                     "results which show security events for endpoints in the deployment. The returned results can be "
                     "used to make customized updates to the Resilient platform, such as updating incidents, artifacts, "
                     "data tables and so on. The integration can also be used to make changes to a deployment including "
                     "adding or removing a hash to a blacklist and moving an endpoint to a different group.",
    install_requires=[
        'resilient_circuits>=30.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnAmpGetEventTypesFunctionComponent = fn_cisco_amp4ep.components.fn_amp_get_event_types:FunctionComponent",
            "FnAmpGetComputersFunctionComponent = fn_cisco_amp4ep.components.fn_amp_get_computers:FunctionComponent",
            "FnAmpGetEventsFunctionComponent = fn_cisco_amp4ep.components.fn_amp_get_events:FunctionComponent",
            "FnAmpGetFileListsFunctionComponent = fn_cisco_amp4ep.components.fn_amp_get_file_lists:FunctionComponent",
            "FnAmpSetFileListFilesFunctionComponent = fn_cisco_amp4ep.components.fn_amp_set_file_list_files:FunctionComponent",
            "FnAmpMoveComputerFunctionComponent = fn_cisco_amp4ep.components.fn_amp_move_computer:FunctionComponent",
            "FnAmpGetGroupsFunctionComponent = fn_cisco_amp4ep.components.fn_amp_get_groups:FunctionComponent",
            "FnAmpGetComputerFunctionComponent = fn_cisco_amp4ep.components.fn_amp_get_computer:FunctionComponent",
            "FnAmpGetComputerTrajectoryFunctionComponent = fn_cisco_amp4ep.components.fn_amp_get_computer_trajectory:FunctionComponent",
            "FnAmpGetActivityFunctionComponent = fn_cisco_amp4ep.components.fn_amp_get_activity:FunctionComponent",
            "FnAmpGetFileListFilesFunctionComponent = fn_cisco_amp4ep.components.fn_amp_get_file_list_files:FunctionComponent",
            "FnAmpDeleteFileListFilesFunctionComponent = fn_cisco_amp4ep.components.fn_amp_delete_file_list_files:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_cisco_amp4ep.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_cisco_amp4ep.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_cisco_amp4ep.util.selftest:selftest_function"]
    }
)