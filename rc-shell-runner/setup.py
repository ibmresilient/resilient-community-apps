from __future__ import print_function
import os
from setuptools import setup, find_packages

setup(
    name='rc-shell-runner',
    use_scm_version={"root": "../", "relative_to": __file__},
    setup_requires=['setuptools_scm'],
    url='https://github.com/ibmresilient/resilient-circuits-packages',
    license='MIT',
    author='IBM Resilient',
    install_requires=[
        'resilient_circuits>=28.0.0'
    ],
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Component for Shell Script Runner",
    long_description = "Resilient Circuits Component for Shell Script Runner",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        # Register the component with resilient_circuits
        "resilient.circuits.components": ["Shell = shell_runner.components.shell_runner:Shell"],
        "resilient.circuits.configsection": ["gen_config = shell_runner.components.shell_runner:config_section_data"]
    }
)
