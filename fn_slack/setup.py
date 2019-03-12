#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_slack',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_slack'",
    long_description="Function creates a Slack message based on a Resilient Incident, it's Tasks, Notes, Artifacts "
                     "and Attachments, exports conversation history from Slack channel to a text file, saves the "
                     "text file as an Attachment and archives the Slack channel.",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'slackclient',
        'bs4'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "SlackPostMessageFunctionComponent = fn_slack.components.slack_post_message:FunctionComponent",
            "SlackArchiveChannelFunctionComponent = fn_slack.components.slack_archive_channel:FunctionComponent",
            "SlackPostAttachmentFunctionComponent = fn_slack.components.slack_post_attachment:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_slack.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_slack.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_slack.util.selftest:selftest_function"]
    }
)