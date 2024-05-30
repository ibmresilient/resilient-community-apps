# URLScan IO Threat Searcher

This implements a custom threat service for [urlscan.io](https://urlscan.io/). This threat service is automatically triggered when adding artifacts of type 'net uri' (URL artifacts).

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

## Installation
1. Unzip rc-cts-urlscanio-x.x.x.tar.gz.zip
2. Install this tar.gz package with `pip`.
3. Use the following commands to register this custom threat service with Resilient and test it:
```
    sudo resutil threatserviceedit -name "urlscan.io" -resturl http://<resilient_circuits_url>:9000/cts/usio
    sudo resutil threatservicetest -name "urlscan.io"
```

4. Run `resilient-circuits config -u` to install the app.config settings and then edit the `[urlscanio]` section with your configuration data.
5. Run with: `resilient-circuits run`.
