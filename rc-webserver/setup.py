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
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='rc-webserver',
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
    cmdclass = {"test" : PyTest},
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Web Server Component",
    long_description="Resilient Circuits Web Server Component",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        # Register the component with resilient_circuits
        "resilient.circuits.components": ["WebRoot = rc_webserver.components.webroot:WebRoot",
                                          "WebService = rc_webserver.components.webservice:WebService"],
        "resilient.circuits.configsection": ["gen_config = rc_webserver.components.webservice:config_section_data"]
    }
)
