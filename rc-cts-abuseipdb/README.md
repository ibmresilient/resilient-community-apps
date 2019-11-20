AbuseIPDB Threat Service
=============

This Custom Threat Service (CTS) pulls data from AbuseIPDB (www.abuseipdb.com) and checks if an IP artifact is blacklisted.
This CTS needs an AbuseIPDB account and an v2 api key to work.

## Revision History

* v2.0.0 - support for abuseipdb v2 api
* v1.0.0 - initial implementation

## Environment

This package requires that it is installed on your integration server and that the resilient-circuits application is running.

Unzip the package from the App Exchange and install the .tar.gz file:
```$xslt
$ unzip rc-cts-abuseipdb-<version>.zip
$ pip install rc-cts-abuseipdb-<version>.tar.gz
```
To set the config values in the app.config file run `resilient-circuits config -u`.

Config values example:
```
[abuseipdb_cts]
abuseipdb_url=https://api.abuseipdb.com/api/v2/check
abuseipdb_key=[your api key from your AbuseIPDB account]
ignore_white_listed=True
```

Run with: `resilient-circuits run`.

## Upgrade Instructions
Uninstall the previous pip package and install the new new package. 
When upgrading from v1.0.0, change your app.config `abuseipdb_url` key to reference the v2 api URL:
```
abuseipdb_url=https://api.abuseipdb.com/api/v2/check
```

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

