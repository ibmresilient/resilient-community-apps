# MISP Threat Searcher

This implements a custom threat service for the [MISP](http://www.misp-project.org/) Threat Intelligence Platform.

Install this package with 'pip', or `python setup.py install`.

Update your `app.config` file with parameters for the MISP connection.
To update the configuration file with default parameters:
```
    resilient-circuits config -u
```

To run the service:
```
resilient-circuits run
```

Register the custom threat service onto your Resilient server (assuming that the
`resilient-circuits` application is running on the same server, and that the webserver
is listening on port 9000):

```
    sudo resutil threatserviceedit -name MISP -resturl http://127.0.0.1:9000/cts/misp
    sudo resutil threatservicetest -name MISP
```
