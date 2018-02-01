YETI Threat Service
=============

This CTS pulls data from a YETI instance and fill Resilient with info about artifacts.
All Yeti observables are supported by this integration.
For more info about YETI platform, please visit https://yeti-platform.github.io/

## Environment

This package requires that it is installed on a RHEL platform and that the resilient-circuits application is running.
Install this package with 'pip', or `python setup.py install`.
Run with: `resilient-circuits run`.

## Setup
Install the threat service:

'''
sudo resutil threatserviceedit -name "YETI" -resturl <resilient_circuits_url>cts/yeti_threat_service
'''

To test the connection:

'''
sudo resutil threatservicetest -name "YETI"
'''

To delete:

'''
sudo resutil threatservicedel -name "YETI"
'''