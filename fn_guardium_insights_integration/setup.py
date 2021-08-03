#!/usr/bin/env python
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
    name="fn_guardium_insights_integration",
    display_name="Resilient Guardium Insights Integration App",
    version="1.0.0",
    license="MIT",
    author="Neetin Kandhare",
    author_email="nkandha1@in.ibm.com",
    url="https://github.com/ibmresilient/resilient-community-apps/fn_guardium_insights_integration",
    description="Resilient Circuits Components for 'fn_guardium_insights_integration'",
    long_description="""This Resilient Circuit Component provides below features to Resilient:
    1. Automatic Resilient incidents creation based on realtime anamolies generated in Guardium Insights.
    2. Block a specifiec user from Resilient
    3. Generate classification report
    4. Automatically populate the breach data types based on classification report data.
    5. Automatically create artifacts based on anamolies data in each crated incident.
    6. Enrich who, what, when, where information for each created incidents.""",
    install_requires=[
        'resilient_circuits>=37.0.0',
        'resilient_lib>=37.0.0',
        'resilient>=37.0.0',
        'circuits>=3.2',
        'six>=1.15.0',
        'requests>=2.25.0',
        'pytz>=2020.5'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_guardium_insights_integration.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_guardium_insights_integration/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_guardium_insights_integration.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_guardium_insights_integration.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_guardium_insights_integration.util.selftest:selftest_function"]
    }
)
