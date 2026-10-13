# Have I Been Pwned Threat Searcher

This implements a custom threat service for the
[Have I Been Pwned API](https://haveibeenpwned.com/API/v2).

Required:
resilient
resilient_circuits
rc-webserver
rc-cts

## Installation
1. Unzip rc-cts-haveibeenpwned-x.x.x.tar.gz.zip
2. Install this tar.gz package with `pip`.
3. Use the following commands to register this custom threat service with Resilient and test it:
```
    sudo resutil threatserviceedit -name "Have I Been Pwned" -resturl <resilient_circuits_url>:9000/cts/have_i_been_pwned_threat_service

    sudo resutil threatservicetest -name "Have I Been Pwned"
```

4. Run with: `resilient-circuits run`.