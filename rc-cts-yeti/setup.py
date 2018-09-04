from __future__ import print_function

from setuptools import setup, find_packages

setup(
    name='rc-cts-yeti',
    version='1.0.0',
    url='https://github.com/ibmresilient/resilient-community-apps',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    install_requires=[
        'rc-cts',
    ],
    description="Resilient Circuits Custom Threat Service for YETI",
    long_description="Resilient Circuits Custom Threat Service Component for YETI",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.configsection":
            ["gen_config = rc_cts_yeti.components.yeti_threat_feed_searcher:config_section_data"],
        # Register the component with resilient_circuits
        "resilient.circuits.components":
            ["YetiThreatFeedSearcher = rc_cts_yeti.components.yeti_threat_feed_searcher:YetiThreatFeedSearcher"]
    }
)
