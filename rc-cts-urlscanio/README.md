# URLScan Threat Searcher

This implements a custom threat service for the [urlscan.io](https://urlscan.io/).

This integration does *not* submit URLs to urlscan.io.  It only searches existing URLs that have previously been
submitted for public scan (private scans do not appear in search results).  If the site has been scanned, and is
marked as malicious by urlscan.io, the searcher returns a "Hit".


## Installation

Install this package with 'pip', or `python setup.py install`.
Run with: `resilient-circuits run`.

To register this custom threat service with Resilient:
(if your `resilient-circuits` is running at IP address 10.10.10.1)
```
    sudo resutil threatserviceedit -name "urlscan.io"  -resturl http://10.10.10.1:9000/cts/usio
    sudo resutil threatservicetest -name "urlscan.io"
```
