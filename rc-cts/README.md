# Resilient Lightweight Custom Threat Service

This package implements the Custom Threat Service API, providing a
simple framework to develop threat source lookups in Python using the
Resilient Circuits integration framework.
  
It's suitable for simple "lightweight" threat source lookups.
* All lookups are asynchronous.
* There is currently no support for file-attachment handling.
* Queries are not stored persistently, so if you need to track external resources
  (for example, if your threat service starts a long-running task such as
  sandbox processing) those will not be tracked across restarts.

For more robust and advanced features, you should consider deploying
a standalone threat service, for example based on the Django example
(https://github.com/ibmresilient/resilient-python-examples/tree/master/django-custom-threat-service).


## Environment

This package requires that it is installed on a RHEL platform and that the resilient-circuits application is running.
Install this package with 'pip', or `python setup.py install`.
To set the config values in the app.config file run `resilient-circuits config -u`.

Config values example:
```
[custom_threat_service]

# Base URL for threat services API
urlbase=/cts

# Whether we support file upload (for "file"-type artifacts)
# upload_file=False

# Retry time indicators
#first_retry_secs=5
#later_retry_secs=60
#max_retries=60

# Cache management
#cache_size=10000
#cache_ttl=600000
```

Run with: `resilient-circuits run`.

## Custom Threat Service Example

This package includes an **example** threat service that responds to 'URL' artifacts with
static data.  To register the example onto your Resilient server (assuming that the
`resilient-circuits` application is running on the same server):

```
sudo resutil threatserviceedit -name example -resturl http://127.0.0.1:9000/cts/example
sudo resutil threatservicetest -name example
```
To delete,
```
sudo resutil threatservicedel -name example
```

