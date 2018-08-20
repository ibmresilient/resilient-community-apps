#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_exchange',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    auhor_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_exchange'",
    long_description="fn_exchange is a package that contains functions for querying, deleting, and moving emails, moving entire folder contents, sending emails, creating meetings, and getting mailbox info. It also includes workflows that create appropriate artifacts and notes from the results of these functions",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'exchangelib'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "ExchangeFindEmailsFunctionComponent = fn_exchange.components.exchange_find_emails:FunctionComponent",
            "ExchangeDeleteEmailsFunctionComponent = fn_exchange.components.exchange_delete_emails:FunctionComponent",
            "ExchangeMoveAndDeleteFolderFunctionComponent = fn_exchange.components.exchange_move_and_delete_folder:FunctionComponent",
            "ExchangeCreateMeetingFunctionComponent = fn_exchange.components.exchange_create_meeting:FunctionComponent",
            "ExchangeMoveEmailsFunctionComponent = fn_exchange.components.exchange_move_emails:FunctionComponent",
            "ExchangeGetMailboxInfoFunctionComponent = fn_exchange.components.exchange_get_mailbox_info:FunctionComponent",
            "ExchangeSendEmailFunctionComponent = fn_exchange.components.exchange_send_email:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_exchange.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_exchange.util.customize:customization_data"]
    }
)