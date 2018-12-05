# URLScan IO Threat Searcher

This implements a custom threat service for the 
[urlscan.io](https://urlscan.io/). This threat service is automatically triggered when adding artifacts of type 'net uri' (URL artifacts).

This integration does *not* submit URLs to urlscan.io.  It only searches existing URLs that have previously been
submitted for public scan (private scans do not appear in search results).  If the site has been scanned, and is
marked as malicious by urlscan.io, the searcher returns a one or more "Hit/s".

To query urlscan.io Search API user does not need to provide API key.

Prerequisites
```
resilient_circuits
rc-webserver
rc-cts
```

## Environment

To install in "development mode"
    `pip install -e ./rc-cts-urlscanio/`
or 
    `python setup.py install`.

To configure the urlscanio, run `resilient-circuits config [-u | -c]`. 

Then edit the `[urlscanio]` template with the Search API and Result API URLs and an optional setting search_size.

Run with: `resilient-circuits run`.

To register this custom threat service with Resilient:
```
    sudo resutil threatserviceedit -name "urlscan.io" -resturl http://<resilient_circuits_url>:9000/cts/usio
    sudo resutil threatservicetest -name "urlscan.io"
```
