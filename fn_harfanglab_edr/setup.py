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
    name="fn_harfanglab_edr",
    display_name="HarfangLab EDR",
    version="1.0.0",
    license="MIT",
    author="HarfangLab",
    author_email="support@harfanglab.fr",
    url="https://support.harfanglab.fr",
    description="Fetch security events from a HarfangLab EDR Manager and manage the incident response.",
    long_description="""This connector allows to fetch security events from a HarfangLab EDR Manager and respond to any incident. \
It provides the following functions:
<br>- Fetch security events with specific criterias (status, minimum severity...) and create IBM SOAR Incidents;
<br>- Isolate and unisolate endpoints to prevent an attacker from moving in an information system;
<br>- Run investigation and remediation jobs on the endpoints
<br>- Run hunting queries in the EDR's datalake
<br>- Manage IOC source list.
""",
    install_requires=[
        "resilient-circuits>=47.1.0",
        "resilient-lib",
        "jinja2",
        "requests==2.28.1",
        "python-dateutil==2.8.2",
        "DateTime==4.7",
        "Markdown==3.4.1",
        "pyminizip==0.2.6"
    ],
    python_requires='>=3.8',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_harfanglab_edr.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_harfanglab_edr/components/f[a-zA-Z]*.py")
        ] +
        ["PollerComponent = fn_harfanglab_edr.components.harfanglab_poller:HarfangLabPollerComponent"],
        "resilient.circuits.configsection": ["gen_config = fn_harfanglab_edr.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_harfanglab_edr.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_harfanglab_edr.util.selftest:selftest_function"]
    }
)
