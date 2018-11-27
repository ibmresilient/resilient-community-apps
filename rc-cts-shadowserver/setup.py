from __future__ import print_function

import sys
from setuptools import setup, find_packages

setup(
    name='rc-cts-shadow-server',
    version='1.0.0',
    url='https://github.com/ibmresilient/resilient-community-apps',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    install_requires=[
        'rc-cts'
    ],
    description="Resilient Circuits Custom Threat Service for Shadow Server",
    long_description="Resilient Circuits Custom Threat Service Component for Shadow Serverd",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        # Register the component with resilient_circuits
        "resilient.circuits.components":
            ["ShadowServerThreatFeedSearcher = "
             "rc_cts_shadow_server.components.shadow_server_threat_feed_searcher:ShadowServerThreatFeedSearcher"],
        "resilient.circuits.configsection":
            ["gen_config = rc_cts_shadow_server.components.shadow_server_threat_feed_searcher:config_section_data"]
    }
)
