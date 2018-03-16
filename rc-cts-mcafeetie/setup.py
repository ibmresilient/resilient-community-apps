from __future__ import print_function

import datetime
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


PUBLISH_VERSION = "1.0.0"


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
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='rc-cts-mcafeetie',
    version=PUBLISH_VERSION,
    url='https://github.com/ibmresilient/resilient-community-apps/releases',
    license='MIT',
    author='IBM Resilient',
    install_requires=[
        'rc-cts',
        'dxltieclient'
    ],
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Custom Threat Service for McAfee TIE client",
    long_description="Resilient Circuits Custom Threat Service Component for McAfee TIE client",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        # Register the component with resilient_circuits
        "resilient.circuits.components":
            ["McAfeeTieThreatFeedSearcher = rc_cts_mcafeetie.components.mcafee_tie_searcher:McAfeeTieSearcher"],
        "resilient.circuits.configsection":
            ["gen_config = rc_cts_mcafeetie.components.mcafee_tie_searcher:config_section_data"]
    }
)