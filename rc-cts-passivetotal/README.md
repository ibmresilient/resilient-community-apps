# Risk IQ PassiveTotal

This implements a custom threat service for [RISK IQ PassiveTotal](https://community.riskiq.com/home).

You must define the tags you class as "hits" in app.config to ensure you get the correct hits. An example is included. 

Install this package with 'pip', or `python setup.py install`.
Run with: `resilient-circuits run`.

To register this custom threat service with Resilient:
```
    sudo resutil threatserviceedit -name "Google SafeBrowsing"  -resturl http://10.10.10.1:9000/cts/gsb
    sudo resutil threatservicetest -name "Google SafeBrowsing"
```
