#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""setup"""

from __future__ import print_function
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    """test"""
    user_options = [('pytestargs=', 'a', "Resilient Environment Arguments")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytestargs = []
        self.test_suite = True

    def finalize_options(self):
        import shlex
        TestCommand.finalize_options(self)
        self.test_args = ["-s", ] + shlex.split(self.pytestargs)

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='rc-query-runner',
    namespace_packages=['query_runner', 'query_runner.components', "query_runner.lib"],
    use_scm_version={"root": "../", "relative_to": __file__},
    setup_requires=['setuptools_scm'],
    url='https://github.com/ibmresilient/resilient-circuits-packages',
    license='MIT',
    author='IBM Resilient',
    install_requires=[
        'resilient_circuits>=28.0.0'
    ],
    tests_require=["pytest",
                   "pytest_resilient_circuits"],
    extras_require={"qradar": ["rc-qradar-search"],
                    "splunk": ["rc-splunk-search"],
                    "ldap": ["rc-ldap-search"],
                    "rest": ["rc-query-rest"]},
    cmdclass={"test": PyTest},
    author_email='support@resilientsystems.com',
    description="Resilient Circuits base pkg for running queries and updating incidents from the results",
    long_description="Resilient Circuits base pkg for running queries and updating incidents from the results",
    packages=find_packages(),
    include_package_data=True,
    data_files=[("query_runner", ["query_runner/LICENSE"])],
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ]
)
