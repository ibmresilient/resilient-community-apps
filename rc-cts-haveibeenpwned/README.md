# Have I Been Pwned Threat Searcher

This implements a custom threat service for the
[Have I Been Pwned API](https://haveibeenpwned.com/API/v2).

Required:
resilient
resilient_circuits
rc-webserver
rc-cts

Install this package with 'pip', or `python setup.py install`.
Run with: `resilient-circuits run`.

To register this custom threat service with Resilient:
```
    sudo resutil threatserviceedit -name "Have I Been Pwned" -resturl <resilient_circuits_url>:9000/cts/have_i_been_pwned_threat_service
    sudo resutil threatservicetest -name "Have I Been Pwned"
```