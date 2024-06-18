#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='rc_data_feed_plugin_resilientfeed',
    display_name='Data Feeder for QRadar SOAR',
    version='2.0.0',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url='http://github.com/ibmresilient/resilient-community-apps',
    description="Sync incident data from one QRadar SOAR organization to another",
    long_description="""Sync incident, artifact, attachment, milestone, note, task, and datatable data from one Resilient organization to another. 
Sync data in bulk and in real-time. This can be used to migrate incident data between different organizations within the same Resilient instance or with a new instance.
<br>
Bidirectional synchronization is now supported.
<br>
<br><ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
<br><ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        'cachetools',
        'rc_data_feed >= 3.2.0',
        'resilient',
        'resilient-lib'
    ],
    extras_require={
        'postgres': ['pyodbc']
    },
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.configsection": ["gen_config = data_feeder_plugins.resilientfeed.util.config:config_section_data"],
        "resilient.circuits.apphost.configsection": ["gen_config = data_feeder_plugins.resilientfeed.util.config:apphost_config_section_data"],
        "resilient.circuits.customize": ["customize = data_feeder_plugins.resilientfeed.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = data_feeder_plugins.resilientfeed.util.selftest:selftest_function"],
    },
    tests_require=["pytest < 4.0.0",
                   "pytest_resilient_circuits"]
)
