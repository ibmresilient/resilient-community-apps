## About Apility.IO

This integration package allows the Resilient user to get the reputation score for your **Emails, Domain Names and IP Addresses**. In addition, receive additional information regarding your assets such as **_geoip, as-network, freemail score, disposable score_**. 

One function is included in support of three capabilities:

* Check an IP addresses reputation
* Check a domain name's reputation
* Check an email sender's reputation

## Using the Ability.IO Function

We have included 3 rules and 3 workflows for Full IP reputation, Email reputation and Domain reputation checks as examples.

## Environment
To install in "development mode", run 
    `pip install -e ./fn_apility/`
    
The distribution file can be installed using
    `pip install fn_apility-<version>.tar.gz`
    
Import the package into Resilient by running `resilient-circuits customize`

To configure the Apility.io parameters, run `resilient-circuits config [-u | -c]`. 
Then edit the `[fn_apility]` template with the URL and basic authentication settings.

Run with: `resilient-circuits run`.

To uninstall, run: `pip uninstall fn_apility`
    
## Resilient Configuration
Follow the steps to add a fn_apility section to your `app.config` file by running `resilient-circuits config [-u | -c]` and updating the fields:

```
[fn_apility]
url=https://api.apility.net
api_token=<your-api-token>
