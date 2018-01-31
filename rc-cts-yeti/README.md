# YETI

This implements a custom threat service for YETI.

YETI URL https://yeti-platform.github.io/

Install this package with 'pip', or `python setup.py install`.
Run with: `resilient-circuits run`.

This integration requires to install PYeti https://github.com/yeti-platform/pyeti

To register this custom threat service with Resilient:
```
    sudo resutil threatserviceedit -name "YETI"  -resturl <resilient_circuits_url>:9000/cts/yeti_threat_service
    sudo resutil threatservicetest -name "YETI"
```
