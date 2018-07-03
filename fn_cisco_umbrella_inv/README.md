# Resilient Function - fn_cisco_umbrella_inv

This Resilient Function package can be used to execute a Cisco Umbrella Investigate query from a workflow using the Functions feature of the Resilient
Circuits integration framework.

Prerequisites:
```
resilient version 30 or later
resilient_circuits version 30 or later
investigate
```
* Can be used in a Resilient workflow to populate/update a datatable or other resource.
* For more info about Cisco Umbrella Investigate, please visit https://docs.umbrella.com/developer/investigate-api/introduction-to-cisco-investigate/
* For more info about the python investigate module, please visit https://github.com/opendns/pyinvestigate/


## Environment

This package requires that it is installed on a RHEL platform and that the resilient-circuits application is running.
Install this package with 'pip', or `python setup.py install`.
To set the config values in the app.config file with a new resilient instance run `resilient-circuits config -c`.
To set the config values in the app.config file with an existing resilient instance run `resilient-circuits config -u`.

Config values example:
(Note: The api token will be supplied by Cisco and will be in uuid format)
```
[fn_cisco_umbrella_inv]
base_url=https://investigate.api.umbrella.com/
api_token=abcd1234-a123-123a-123a-123456abcdef
results_limit=200
```

Run with: `resilient-circuits run`.

## Supported Resilient Functions for Cisco Umbrella Investigate
```
umbrella_domain_volume
umbrella_classifiers
umbrella_domain_whois_info
umbrella_ip_as_info
umbrella_dns_rr_hist
umbrella_ip_latest_malicious_domains
umbrella_domain_co_occurrences
umbrella_pattern_search
umbrella_domain_related_domains
umbrella_threat_grid_sample
umbrella_domain_security_info
umbrella_threat_grid_samples
umbrella_timeline
umbrella_domain_status_and_category
```
## Sample workflows have been provided:
```
Example: AS Information for an ip address or ASN
Example: Categories for a domain
Example: Classifiers for a domain
Example: Co-occurences for a domain
Example: DNS RR history for a domain
Example: DNS RR history for an ip address
Example: Domain volume
Example: Domain WHOIS information for a domain
Example: Get list of category identifiers
Example: Latest Malicious Domains for an ip address
Example: Pattern search start epoch
Example: Pattern search start relative
Example: Related Domains for a Domain
Example: Security information for a domain
Example: ThreadGrid sample information for a hash
Example: ThreadGrid samples for a resource
Example: Timeline for a resource
```
## fn_cisco_umbrella_inv Example

The umbrella_dns_rr_hist Function requires 2 input parameters. The parameters are setup from a Resilient systems workflow on the Resilient console.
The following are examples of setup of each parameter using a simple workflow pre-processing script. The %param% token
will be replaced by the actual inputs.param value at time of execution.

```
inputs.umbinv_resource = artifact.value
inputs.umbinv_dns_type = "A"
```
For example if artifact.value gets set to an ip address (domain name also supported for this function), the results
returned to Resilient will be in JSON format and will be similar to the following format.
Note: Each Resilient Function will return a different result.
```
{"resource_name": "example.com",
 "query_execution_time": "2018-05-02 16:03:15",
 "dns_rr_history": {  "rrs": [  {
                                  "rr": "www.example.com.",
                                  "ttl": 86400,
                                  "class": "IN",
                                  "type": "A",
                                  "name": "93.184.216.119"
                                },
                                ...
                                {
                                  "rr": "examplewww.vip.icann.org.",
                                  "ttl": 30,
                                  "class": "IN",
                                  "type": "A",
                                  "name": "93.184.216.119"
                                }
                              ],
                              "features": {
                                "rr_count": 19,
                                "ld2_count": 10,
                                "ld3_count": 14,
                                "ld2_1_count": 7,
                                "ld2_2_count": 11,
                                "div_ld2": 0.5263157894736842,
                                "div_ld3": 0.7368421052631579,
                                "div_ld2_1": 0.3684210526315789,
                                "div_ld2_2": 0.5789473684210527
                              }
                    }
}
```
