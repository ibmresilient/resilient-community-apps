from __future__ import print_function

from setuptools import setup, find_packages

setup(
    name='rc-cts-urlscanio',
    setup_requires=['setuptools_scm'],
    use_scm_version={"root": "../", "relative_to": __file__},
    url='https://github.com/IBMResilient/resilient-community-apps/',
    license='MIT',
    author='IBM Resilient',
    install_requires=[
        'rc-cts'
    ],
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Custom Threat Service for urlscan.io",
    long_description="Resilient Circuits Custom Threat Service for urlscan.io",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        # Register the component with resilient_circuits
        "resilient.circuits.components": [
            "UrlScanIoSearcher = rc_cts_urlscanio.components.searcher:UrlScanIoSearcher"
        ],
        "resilient.circuits.configsection": ["gen_config = rc_cts_urlscanio.util.config:config_section_data"],
    }
)