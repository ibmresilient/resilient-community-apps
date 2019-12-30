from __future__ import print_function

import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [('pytestargs=', 'a', "Resilient Environment Arguments")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytestargs = ""
        self.test_suite = True

    def finalize_options(self):
        import shlex
        TestCommand.finalize_options(self)
        self.test_args = ["-s",] + shlex.split(self.pytestargs)

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='rc-cts-abuseipdb',
    version='2.0.0',
    url='https://github.com/ibmresilient/resilient-community-apps',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    install_requires=[
        'rc-cts',
        'resilient_lib'
    ],
    description="Resilient Circuits Custom Threat Service for AbuseIPDB",
    long_description="Resilient Circuits Custom Threat Service Component for AbuseIPDB",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        # Register the component with resilient_circuits
        "resilient.circuits.components":
            ["AbuseIPDBThreatFeedSearcher = "
             "rc_cts_abuseipdb.components.abuseipdb_threat_feed_searcher:AbuseIPDBThreatFeedSearcher"],
        "resilient.circuits.configsection": ["gen_config = rc_cts_abuseipdb.util.config:config_section_data"],
    }
)
