## About IPVOID
It is a online tool to discover details about IP addresses.

## Using the IPVOID Function

One function is included in support of six capabilities:
* IP Reputation
* Domain Blacklist
* DNS Lookup
* Email Verify
* Threat Log
* SSL Info

## Environment
To install in "development mode", run 
    `pip install -e ./fn_ipvoid/`
    
The distribution file can be installed using
    `pip install fn_ipvoid-<version>.tar.gz`
    
Import the package into Resilient by running `resilient-circuits customize`

To configure the IPVOID parameters, run `resilient-circuits config [-u | -c]`. 
Then edit the `[fn_ipvoid]` template with basic authentication settings.

Run with: `resilient-circuits run`.

To uninstall, run: `pip uninstall fn_ipvoid`
    
## Resilient Configuration
Follow the steps to add a fn_ipvoid section to your `app.config` file by running `resilient-circuits config [-u | -c]` and updating the fields:

```
[fn_ipvoid]
api_token=<your-api-token>
