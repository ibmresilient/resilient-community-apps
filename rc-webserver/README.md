# Resilient Circuits Web Server

Provides a Web server that can be extended by additional components.
This is useful for implementing a Threat Service, or for webhooks.

To have your Python method called with requests at `/path/endpoint`, 
* Make a class that inherits from `circuits.web.BaseController`,
* Set `self.channel="path"`,
* Use the `rc_webserver.web.@exposeWeb` decorator on a method, e.g. `@exposeWeb("endpoint")`.

## Environment

This package requires that it is installed on a RHEL platform and that the resilient-circuits application is running.
Install this package with 'pip', or `python setup.py install`.
To set the config values in the app.config file run `resilient-circuits config -u`.

Config values example:
```
[webserver]

# IP or DNS for the web server. Default is localhost.
# server=0.0.0.0

# Port for the web server. Default is 9000.
# port=9000

# Set the web server to use secure protocol. secure=1 means HTTPS, and secure=0 means HTTP. Default is 0
# secure=1

# The cert file is the private key certificate for the TLS server. This is required if secure=1. Default is None.
# certfile=~/.resilient/ssl.cer
```

Run with: `resilient-circuits run`.


