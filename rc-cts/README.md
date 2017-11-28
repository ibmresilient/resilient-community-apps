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
(https://github.com/Co3Systems/co3-api/tree/master/python/examples/custom-threat-service).


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

