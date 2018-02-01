
AbuseIPDB Threat Service
=============

This CTS pulls data from AbuseIPDB(www.abuseipdb.com) and check if an IP artifact is blacklisted.
This CTS needs an account and an api key from AbuseIPDB to work.

## Environment

This package requires that it is installed on a RHEL platform and that the resilient-circuits application is running.
Install this package with 'pip', or `python setup.py install`.
Run with: `resilient-circuits run`.

## Setup
Install the threat service:

'''
sudo resutil threatserviceedit -name "AbuseIPDB" -resturl <resilient_circuits_url>cts/abuseipdb_threat_feed
'''

To test the connection:

'''
sudo resutil threatservicetest -name "AbuseIPDB"
'''

To delete:

'''
sudo resutil threatservicedel -name "AbuseIPDB"
'''