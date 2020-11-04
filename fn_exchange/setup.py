#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_exchange',
    display_name='Microsoft Exchange for IBM Resilient',
    version='1.0.1',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_exchange'",
    long_description="""This IBM Resilient Function package provides functions that can be used to access Microsoft 
        Exchange email and meeting capabilities. The package provided has the following capabilities: Create a meeting 
        in Microsoft Exchange and send out invites, Delete queried emails from a user’s mailbox, Query emails from a 
        user’s mailbox, Get mailbox info for a sender, Move the contents of one folder to another folder and deletes 
        the original, Move queried emails from one folder to another folder, Send email to a list of recipients.""",
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
            "ExchangeCreateMeetingFunctionComponent = fn_exchange.components.exchange_create_meeting:FunctionComponent",
            "ExchangeDeleteEmailsFunctionComponent = fn_exchange.components.exchange_delete_emails:FunctionComponent",
            "ExchangeFindEmailsFunctionComponent = fn_exchange.components.exchange_find_emails:FunctionComponent",
            "ExchangeGetMailboxInfoFunctionComponent = fn_exchange.components.exchange_get_mailbox_info:FunctionComponent",
            "ExchangeMoveEmailsFunctionComponent = fn_exchange.components.exchange_move_emails:FunctionComponent",
            "ExchangeMoveFolderContentsAndDeleteFolderFunctionComponent = fn_exchange.components.exchange_move_folder_contents_and_delete_folder:FunctionComponent",
            "ExchangeSendEmailFunctionComponent = fn_exchange.components.exchange_send_email:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_exchange.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_exchange.util.customize:customization_data"],
    }
)