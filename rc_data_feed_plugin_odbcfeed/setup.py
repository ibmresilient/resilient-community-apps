#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='rc_data_feed_plugin_odbcfeed',
    display_name='Data Feeder ODBC Plugin for SOAR',
    version='1.0.6',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url='http://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for sending data feeds to other (BI) systems",
    long_description="""This app contains the Data Feed plugin for ODBC-based databases. Updates are performed in near real-time.
Supported ODBC databases:
    PostgreSQL,
    MySQL (MariaDB),
    Microsoft SQLServer,
    Oracle,
    SQLite file/database
    """,
    install_requires=[
        'resilient>=44.0',
        'rc_data_feed>=2.2.1',
        'cachetools~=2.1',
        'cx_Oracle~=8.3; python_version>="3.0"',
        'cx_Oracle~=7.3; python_version<"3.0"',
        'pyodbc~=4.0',
        'six~=1.16',
        'sqlparams~=3.0; python_version>="3.6"',
        'sqlparams~=1.2; python_version<"3.6"'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.configsection": ["gen_config = data_feeder_plugins.sqllib.util.config:config_section_data"],
        "resilient.circuits.apphost.configsection": ["gen_config = data_feeder_plugins.sqllib.util.config:apphost_config_section_data"],
        "resilient.circuits.customize": ["customize = data_feeder_plugins.sqllib.util.customize:customization_data"]
    },
    tests_require=["pytest < 4.0.0",
                   "pytest_resilient_circuits"]
)
