#!/usr/bin/env python
#-- coding: utf-8 --
#(c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long

from setuptools import setup, find_packages
import glob
import ntpath

def get_module_name(module_path):
    """
    Return the module name of the module path
    """
    return ntpath.split(module_path)[1].split(".")[0]

def snake_to_camel(word):
    """
    Convert a word from snake_case to CamelCase
    """
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


setup(
    name='fn_outbound_email',
    display_name='Outbound Email',
    version='2.0.2',
    license='MIT',
    author='IBM QRadar SOAR',
    url='https://github.com/ibmresilient/resilient-community-apps/tree/master/fn_outbound_email',
    description="Outbound Email",
    long_description="""The Outbound Email App for IBM SOAR provides a way of sending email from the SOAR platform. The email message contains information about the incident that the email action was performed on.
<br>
<br>Key Features
<br>* Send email to lists of recipients (to, cc, bcc).
<br>* Format email using a predefined html template or specify your own template.
<br>* Send attachments with the email at the incident level or task level.
<br>* Example rules included at the incident and task levels.
<br>
<br>New in version 2.0
<br>* Ability to reference additional email headers: message-id, importance, in-reply-to.
<br>* Define multiple templates from the app.config file.
<br>* Capture outbound email conversations including both inbound and outbound messages.
<br>* Expanded template support to include artifact, notes and SOAR links (case and task).
<br>* Support for OAuth authentication.""",
    install_requires=[
        'b4',
        'resilient_circuits>=39.0.0',
        'resilient_lib>=46.0.0',
        'Jinja2>=2.9.6',
        'six'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
         "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_outbound_email.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_outbound_email/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_outbound_email.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_outbound_email.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_outbound_email.util.selftest:selftest_function"]
    }
)
