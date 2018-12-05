# RiskIQ PassiveTotal

This implements a custom threat service for [RiskIQ PassiveTotal](https://community.riskiq.com/home). This threat service is automatically triggered when adding artifacts of type 'net.name' (domain name artifact), 'net.uri' (URL) or 'net.ip' (IP address).

To query RiskIQ PassiveTotal API user needs to provide API key.

Prerequisites
```
resilient_circuits
rc-webserver
rc-cts
```

## Environment

To install in "development mode"
    `pip install -e ./rc-cts-passivetotal/`
or 
    `python setup.py install`.

To configure the PassiveTotal, run `resilient-circuits config [-u | -c]`. 

Then edit the `[passivetotal]` template with the API URLs and define the tags you classify as "hits" to ensure you get the correct hits. An example is included.

Run with: `resilient-circuits run`.

To register this custom threat service with Resilient:
```
    sudo resutil threatserviceedit -name "RiskIQ PassiveTotal" -resturl http://<resilient_circuits_url>:9000/cts/pst
    sudo resutil threatservicetest -name "RiskIQ PassiveTotal"
```