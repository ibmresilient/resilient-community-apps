#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_exchange',
    display_name='Microsoft Exchange',
    version='1.0.3',
    license='MIT',
    author='IBM SOAR',
    url='https://ibm.com/mysupport',
    description="Integrate with Microsoft Exchange email and meeting functionality",
    long_description="""This package provides functions that can be used to access Microsoft \
Exchange email and meeting capabilities. The package provided has the following capabilities:<br>
- Create a meeting in Microsoft Exchange and send out invites<br>
- Delete queried emails from a user's mailbox<br>
- Query emails from a user's mailbox<br>
- Get mailbox info for a sender<br>
- Move the contents of one folder to another folder and deletes the original<br>
- Move queried emails from one folder to another folder<br>
- Send email to a list of recipients""",
    install_requires=[
        'resilient_circuits>=45.0.0',
        'exchangelib==2.2.0; python_version<"3"',
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
        "resilient.circuits.selftest": ["selftest = fn_exchange.util.selftest:selftest_function"]
    }
)