# Google Safe Browsing Threat Searcher

This implements a custom threat service for the
[Google Safe Browsing Lookup API](https://developers.google.com/safe-browsing/v4/get-started).

>   NOTE: For high volume applications it would be better (faster and more private)
>   to use the Google Safe Browsing *Update API* which provides downloadable lists
>   of threat information that can be queried by hash.

Install this package with 'pip', or `python setup.py install`.
Run with: `resilient-circuits run`.

To register this custom threat service with Resilient:
```
    sudo resutil threatserviceedit -name "Google SafeBrowsing"  -resturl http://10.10.10.1:9000/cts/gsb
    sudo resutil threatservicetest -name "Google SafeBrowsing"
```
