from __future__ import print_function

from setuptools import setup, find_packages

setup(
    name='rc-cts-googlesafebrowsing',
    version='1.0.0',
    url='https://github.com/ibmresilient/resilient-community-apps',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    install_requires=[
        'rc-cts'
    ],
    description="Custom Threat Service - Google SafeBrowsing",
    long_description="Custom Threat Service - Google SafeBrowsing",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        # Register the component with resilient_circuits
        "resilient.circuits.components": ["GoogleSafeBrowsingThreatSearcher = rc_cts_googlesafebrowsing.components.searcher:GoogleSafeBrowsingThreatSearcher"]
    }
)
