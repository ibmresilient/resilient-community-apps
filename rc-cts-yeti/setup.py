from __future__ import print_function

from setuptools import setup, find_packages

setup(
    name='rc-cts-yeti',
    setup_requires=['setuptools_scm'],
    use_scm_version={"root": "../", "relative_to": __file__},
    url='https://github.com/ibmresilient/resilient-circuits-packages',
    license='MIT',
    author='IBM Resilient',
    install_requires=[
        'rc-cts',
        'pyeti'
    ],
    author_email='support@resilientsystems.com',
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
