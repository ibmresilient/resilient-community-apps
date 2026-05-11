# -*- coding: utf-8 -*-

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
    name='fn_exchange',
    display_name='Microsoft Exchange',
    version='2.0.1',
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
- Send email to a list of recipients<br>
- Links:
        <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
        <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>
        <ul><a target='blank' href='https://ibmresilient.github.io/resilient-community-apps/fn_exchange/README.html'>App Documentation</a></ul>""",
    install_requires=[
        "resilient_circuits>=51.0.0",
        "backports-datetime-fromisoformat == 2.0.0;python_version=='3.6'",
        "exchangelib ~= 4.6.2;python_version=='3.6'",
        "exchangelib ~= 4.9.0;python_version>='3.9'"
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_exchange.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_exchange/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_exchange.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_exchange.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_exchange.util.selftest:selftest_function"]
    }
)