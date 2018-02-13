# McAfee TIE Threat Searcher

This Custom Threat Source uses the Python OpenDXL TIE Client to communicate with your TIE server
[GitHit: opendxl-tie-client-python](https://github.com/opendxl/opendxl-tie-client-python).

### Prerequisites
* System must have an OpenSSL version used by Python that supports TLSv1.2 (Version 1.0.1 or greater)
* ePO-managed environments must have 4.0 (or newer) version of DXL ePO extension installed

Install this package with `pip`, or `python setup.py install`.

Once installed the client must be provisioned. Refer [here](https://opendxl.github.io/opendxl-client-python/pydoc/provisioningoverview.html) for more info on provisioning

Run with: `resilient-circuits run`.

To register this custom threat service with Resilient and test it:
```
    sudo resutil threatserviceedit -name "McAfee TIE Searcher" -resturl <resilient_circuits_url>:9000/cts/mcafee_tie_searcher
    sudo resutil threatservicetest -name "McAfee TIE Searcher"
```