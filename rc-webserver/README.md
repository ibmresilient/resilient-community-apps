# Resilient Circuits Web Server

Provides a Web server that can be extended by additional components.
This is useful for implementing a Threat Service, or for webhooks.

To have your Python method called with requests at `/path/endpoint`, 
* Make a class that inherits from `circuits.web.BaseController`,
* Set `self.channel="path"`,
* Use the `rc_webserver.web.@exposeWeb` decorator on a method, e.g. `@exposeWeb("endpoint")`.


