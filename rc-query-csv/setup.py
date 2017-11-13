from __future__ import print_function
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
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
        # import here, because outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='rc-query-csv',
    use_scm_version={"root": "../", "relative_to": __file__},
    setup_requires=['setuptools_scm'],
    url='https://github.com/ibmresilient/resilient-circuits-packages',
    license='MIT',
    author='IBM Resilient',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires=[
        'resilient_circuits>=28.0.0',
        'rc-query-runner>=28.1.0'
    ],
    tests_require=["pytest",
                   "pytest_resilient_circuits"],
    cmdclass={"test": PyTest},
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Component for Searching CSV Files",
    packages=find_packages(),
    include_package_data=True,
    data_files=[("rc_query_csv", ["rc_query_csv/LICENSE"])],
    platforms='any',
    entry_points={
        # Register the components with resilient_circuits
        "resilient.circuits.components": ["QueryCSV = rc_query_csv.components.query_csv:QueryCSV"],
        "resilient.circuits.configsection": ["gen_config = rc_query_csv.components.query_csv:config_section_data"]
    }
)
