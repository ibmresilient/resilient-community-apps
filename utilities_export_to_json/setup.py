from __future__ import print_function
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires_resilient_version = "29.0"
major, minor = requires_resilient_version.split('.', 2)[:2]

setup(
    name='resilient_export_to_json',
    version='1.0.1',
    use_scm_version={"root": "../", "relative_to": __file__},
    setup_requires=['setuptools_scm==1.5.0'],
    url='https://developer.ibm.com/resilient',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    author='IBM Resilient',
    install_requires=[
        'resilient>={}.{}'.format(major, minor)
    ],
    author_email='support@resilientsystems.com',
    description='Extracts incident data from Resilient into a JSON file',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': ['resilient-export-to-json=export_to_json.bin.export_to_json:main',
                            'resilient-merge-incident-json=export_to_json.bin.merge_incidents_json:main']
    }
)
