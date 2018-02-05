ShadowServer Threat Service
=============

This CTS queries ShadowServer (http://bin-test.shadowserver.org/) and updates Resilient with information about a hash artifact.

## Environment

This package requires that it is installed on a RHEL platform and that the resilient-circuits application is running.
Install this package with 'pip', or `python setup.py install`.
Run with: `resilient-circuits run`.

## Setup
Install the threat service:

```
sudo resutil threatserviceedit -name "Shadow Server" -resturl <resilient_circuits_url>/cts/shadow_server_threat_feed
```

To test the connection:

```
sudo resutil threatservicetest -name "Shadow Server"
```

To delete:

```
sudo resutil threatservicedel -name "Shadow Server"
```
