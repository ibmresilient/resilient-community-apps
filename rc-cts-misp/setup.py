from __future__ import print_function

from setuptools import setup, find_packages

setup(
    name='rc-cts-misp',
    version='1.0.0',
    url='https://github.com/ibmresilient/resilient-community-apps',
    license='MIT',
    author='IBM Resilient',
    install_requires=[
        'pymisp',
        'rc-cts'
    ],
    author_email='support@resilientsystems.com',
    description="Custom Threat Service - MISP",
    long_description="Custom Threat Service - MISP",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        # Register the component with resilient_circuits
        "resilient.circuits.components": ["MISPThreatSearcher = rc_cts_misp.components.searcher:MISPThreatSearcher"],
        "resilient.circuits.configsection": ["gen_config = rc_cts_misp.components.searcher:config_section_data"]
    }
)
