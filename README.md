# Resilient Community Applications

These packages are installable components for the [resilient-circuits](https://github.com/ibmresilient/resilient-python-api/tree/master/resilient-circuits) framework.

Applications include,
* `rc-query-runner`, a base for components that execute queries against another system and update the Resilient incident
  with search results.  This includes a simple and powerful query definition file format.  
* Query-runner packages for searching QRadar, Splunk, LDAP, generic REST APIs, and more.
* `rc-webserver`, a base for components that listen to incoming Web Service requests.
* `rc-cts`, a simple Resilient Custom Threat Service
* Custom Threat Service packages that implement several types of integration with third-party
  threat intelligence sources.
* `rc-shell-runner`, a package for running shell scripts from Resilient rules.


### Setup

Download the latest release packages here:
  
[Latest Release](https://github.com/ibmresilient/resilient-circuits-packages/releases/latest)

To install a package,
```shell
pip install <filename>.tar.gz
```
Refer to each package directory for pre-requisites and specific install instructions.

To list your installed packages,
```shell
resilient-circuits list
```


### Contributing

These packages are provided "as-is", without any support.  Please report issues using the [Issues](https://github.com/ibmresilient/resilient-circuits-packages/issues) tab on GitHub.

Contributions are welcome.

