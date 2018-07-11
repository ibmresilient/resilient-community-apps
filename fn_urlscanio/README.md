# URLScan.io Function 

[https://urlscan.io](urlscan.io) is a service to scan and analyse websites. When a URL is submitted to urlscan.io,
an automated process will browse to the URL like a regular user and record the activity that this page navigation
creates. This includes the domains and IPs contacted, the resources (JavaScript, CSS, etc) requested from those
domains, as well as additional information about the page itself. urlscan.io will take a screenshot of the page,
record the DOM content, JavaScript global variables, cookies created by the page, and a myriad of other observations.

This integration is a Resilient function that can be called from workflows, to submit a URL for analysis by urlscan.io.
It returns the report metadata, report URL, and base64-encoded screenshot that you can attach to the incident.


## Installation

To install in "development mode"

    pip install -e ./fn_urlscanio/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall,

    pip uninstall fn_urlscanio


To package for distribution,

    python ./fn_urlscanio/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz

