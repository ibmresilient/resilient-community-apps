# IPVOID Search Function for IBM Resilient

## Table of Contents
  - [app.config settings](#appconfig-settings)
  - [Function Inputs](#function-inputs)
  - [Function Output](#function-output)
  - [Pre-Process Script](#pre-process-script)
  - [Post-Process Script](#post-process-script)
  - [Rules](#rules)
---

**This package contains a function that searches using your IPVOID account/subscription with the given query**

 ![screenshot](./screenshots/screen1.png)
, , , , , 
The function makes use of the IPVOID's Rest API calls to get information on a given query, followings are the available services :-
-	IP Reputation `/iprep/v1/pay-as-you-go/`
-	SSL Info `/sslinfo/v1/pay-as-you-go/`
-	Threat Log `/threatlog/v1/pay-as-you-go/`
-	Email Verify `/emailverify/v1/pay-as-you-go/`
-	DNS Lookup `/dnslookup/v1/pay-as-you-go/`
-	Domain Blacklist `/domainbl/v1/pay-as-you-go/`
## app.config settings:
```
[fn_ip_void]
ipvoid_base_url=https://endpoint.apivoid.com
ipvoid_api_key=<your-api-key>
```

## Function Inputs:
| Input Name | Type | Required | Example | Info |
| ------------- | :--: | :-------:| ------- | ---- |
| `ip_void_artifact_type` | `String` | Yes | `"IP Address"` | Helps to identify request type |
| `ip_void_artifact_value` | `String` | Yes | `"185.157.185.248"` | Make search on given value, IP Address or DNS Name |
| `ip_void_request_type` | Select `String` | Yes | `"IP Reputation"` | Makes sure which IPVOID service to call |

## Function Output:
```python
results = { 
			"data":{
			      "report":{
			         "blacklists":{
			            "engines":{
			               "9":{
			                  "engine":"Anti-Attacks BL",
			                  "detected":false,
			                  "reference":"https:\/\/www.anti-attacks.com\/",
			                  "elapsed":"0.00"
			               },
			               "10":{
			                  "engine":"BadIPs",
			                  "detected":false,
			                  "reference":"https:\/\/www.badips.com\/",
			                  "elapsed":"0.00"
			               },
			               "11":{
			                  "engine":"Bambenek Consulting",
			                  "detected":false,
			                  "reference":"http:\/\/www.bambenekconsulting.com\/",
			                  "elapsed":"0.00"
			               },
			               "12":{
			                  "engine":"Blacklists_co",
			                  "detected":false,
			                  "reference":"http:\/\/blacklists.co\/",
			                  "elapsed":"0.00"
			               },
			               "13":{
			                  "engine":"BlockList_de",
			                  "detected":false,
			                  "reference":"http:\/\/www.blocklist.de\/",
			                  "elapsed":"0.00"
			               },
			               "14":{
			                  "engine":"Blocklist.net.ua",
			                  "detected":false,
			                  "reference":"https:\/\/blocklist.net.ua\/",
			                  "elapsed":"0.00"
			               },
			               "15":{
			                  "engine":"BloggingFusion BL",
			                  "detected":false,
			                  "reference":"https:\/\/www.bloggingfusion.com\/",
			                  "elapsed":"0.00"
			               },
			               "16":{
			                  "engine":"Booru BL",
			                  "detected":false,
			                  "reference":"",
			                  "elapsed":"0.00"
			               },
			               "17":{
			                  "engine":"Botvrij.eu",
			                  "detected":false,
			                  "reference":"http:\/\/botvrij.eu\/",
			                  "elapsed":"0.00"
			               }
			            },
			            "detections":1,
			            "engines_count":70,
			            "detection_rate":"1%",
			            "scantime":"0.07"
			         }
			      }
			   },
			   "credits_remained":93934.23,
			   "credits_expiration":"Fri, 15 Mar 2019 22:06:23 GMT",
			   "estimated_queries":"1,174,177",
			   "elapsed_time":"0.17",
			   "success":true
			}
```
## Pre-Process Script:
This example sets the `ip_void_artifact_value`, `ip_void_artifact_type`, `ip_void_request_type` input to the value and type of the Artifact the user took action on
```python
# The search value to send to IPVOID (may be any String that contains an IP Address, URL etc.)
inputs.ip_void_artifact_value = artifact.value
inputs.ip_void_artifact_type = artifact.type
```

## Post-Process Script:
This example then adds `results` to Notes section.
```python
incident.addNote(str(results))
```
