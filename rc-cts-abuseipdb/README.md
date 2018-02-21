AbuseIPDB Threat Service
=============

This CTS pulls data from AbuseIPDB (www.abuseipdb.com) and checks if an IP artifact is blacklisted.
This CTS needs an AbuseIPDB account and an api key to work.

## Environment

This package requires that it is installed on a RHEL platform and that the resilient-circuits application is running.
Install this package with 'pip', or `python setup.py install`.
To set the config values in the app.config file run `resilient-circuits config -u`.

Config values example:
```
[abuseipdb_cts]
abuseipdb_url=https://www.abuseipdb.com/check
abuseipdb_key=[your api key from your AbuseIPDB account]
```

Run with: `resilient-circuits run`.

## Setup
Install the threat service:

```
sudo resutil threatserviceedit -name "AbuseIPDB" -resturl <resilient_circuits_url>/cts/abuseipdb_threat_feed
```

To test the connection:

```
sudo resutil threatservicetest -name "AbuseIPDB"
```

To delete:

```
sudo resutil threatservicedel -name "AbuseIPDB"
```

