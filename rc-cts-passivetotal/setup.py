from __future__ import print_function

from setuptools import setup, find_packages

setup(
    name='rc-cts-passivetotal',
    setup_requires=['setuptools_scm'],
    use_scm_version={"root": "../", "relative_to": __file__},
    url='https://github.com/ibmresilient/resilient-circuits-packages',
    license='MIT',
    author='IBM Resilient',
    install_requires=[
        'rc-cts'
    ],
    author_email='support@resilientsystems.com',
    description="Custom Threat Service - Passive Total",
    long_description="Custom Threat Service - Passive Total",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        # Register the component with resilient_circuits
        "resilient.circuits.components": ["PassiveTotalSearcher = rc_cts_passivetotal.components.searcher:PassiveTotalSearcher"]
    }
)
