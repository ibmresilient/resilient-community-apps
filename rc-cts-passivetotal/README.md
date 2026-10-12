# RiskIQ PassiveTotal

This implements a custom threat service for [RiskIQ PassiveTotal](https://community.riskiq.com/home). This threat service is automatically triggered when adding artifacts of type 'net.name' (domain name artifact), 'net.uri' (URL) or 'net.ip' (IP address).

To query RiskIQ PassiveTotal API user needs to provide API key.

Prerequisites
```
resilient_circuits
rc-webserver
rc-cts
```

## Installation
1. Unzip rc-cts-passivetotal-x.x.x.tar.gz.zip
2. Install this tar.gz package with `pip`.
3. Use the following commands to register this custom threat service with Resilient and test it:
```
    sudo resutil threatserviceedit -name "RiskIQ PassiveTotal" -resturl http://<resilient_circuits_url>:9000/cts/pst

    sudo resutil threatservicetest -name "RiskIQ PassiveTotal"
```

4. Run `resilient-circuits config -u` to install the app.config settings and then edit the `[passivetotal]` section with your configuration data.
5. Run with: `resilient-circuits run`.