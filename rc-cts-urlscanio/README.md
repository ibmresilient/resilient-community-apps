# URLScan Threat Searcher

This implements a custom threat service for the
[URLScan](https://urlscan.io/). It will *only* return hits when the site is marked as malcious by URLScan - it will not submite scans only lookup existing (due to privacy concerns). 


Install this package with 'pip', or `python setup.py install`.
Run with: `resilient-circuits run`.

To register this custom threat service with Resilient:
```
    sudo resutil threatserviceedit -name "URLScan"  -resturl http://10.10.10.1:9000/cts/usio
    sudo resutil threatservicetest -name "URLScan"
```
