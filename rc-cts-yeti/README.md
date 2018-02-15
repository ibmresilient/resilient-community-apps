YETI Threat Service
=============

This CTS queries a YETI instance and updates Resilient with information about artifacts.
All Yeti observables are supported by this integration.
For more info about YETI platform, please visit https://yeti-platform.github.io/

## Environment

This package requires that it is installed on a RHEL platform and that the resilient-circuits application is running.
Install this package with 'pip', or `python setup.py install`.
Run with: `resilient-circuits run`.

## Requirements

This package requires pyeti library. To install it follow these steps:

- clone https://github.com/yeti-platform/pyeti

- run 'python setup.py sdist --formats=gztar'

- cd to the new dist/ folder

- run 'pip install -U pyeti...tar.gz'


## Setup
Install the threat service:

```
sudo resutil threatserviceedit -name "YETI" -resturl <resilient_circuits_url>/cts/yeti_threat_service
```

To test the connection:

```
sudo resutil threatservicetest -name "YETI"
```

To delete:

```
sudo resutil threatservicedel -name "YETI"
```
