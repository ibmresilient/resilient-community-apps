from __future__ import print_function

from setuptools import setup, find_packages

setup(
    name='rc-cts-googlesafebrowsing',
    setup_requires=['setuptools_scm'],
    use_scm_version={"root": "../../", "relative_to": __file__},
    url='https://www.resilientsystems.com/',
    license='Resilient License',
    author='IBM Resilient',
    install_requires=[
        'rc-cts'
    ],
    author_email='support@resilientsystems.com',
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
