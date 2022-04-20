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
    display_name='Scheduler',
    name='fn_scheduler',
    version='1.2.0',
    license='MIT',
    author='IBM SOAR',
    url='https://ibm.com/mysupport',
    description="Functions to allow Rules to be scheduled",
    long_description="""This package of functions allows an enterprise to schedule a rule to run in the future associated with a incident, task, artifact, and datatable.<br>
        Functions available include:<br>
            1) Scheduling a rule<br>
            2) Listing scheduled rules<br>
            3) Pause and resume scheduled rules<br>
            4) Removing a scheduled rule""",
    install_requires=[
        'resilient_circuits>=42.0.0',
        'pytz',
        "APScheduler < 3.9;python_version < '3.6'",
        "APScheduler >= 3.9;python_version >= '3.6'",
        'SQLAlchemy>=1.3.8',
        'python-dateutil>=2.8.1'
    ],
    extras_require={
        'apphost': ['py-postgresql']
    },
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_scheduler.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_scheduler/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_scheduler.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_scheduler.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_scheduler.util.selftest:selftest_function"]
    }
)