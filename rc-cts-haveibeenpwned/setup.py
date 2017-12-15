from __future__ import print_function
from setuptools import setup, find_packages

setup(
    name='rc-cts-haveibeenpwned',
    version="1.0.0",
    url='https://www.resilientsystems.com/',
    license='Resilient License',
    author='IBM Resilient',
    install_requires=[
        'rc-cts'
    ],
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Custom Threat Service for Have I Been Pwned",
    long_description="Resilient Circuits Custom Threat Service Component for Have I Been Pwned",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        # Register the component with resilient_circuits
        "resilient.circuits.components":
            ["HaveIBeenPwnedThreatFeedSearcher = rc_cts_haveibeenpwned.components.searcher:HaveIBeenPwnedSearcher"]
    }
)