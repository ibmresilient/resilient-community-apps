# ThreatMiner Integration

## Overview

This Integration queries the ThreatMiner API to extract additional information from artifacts associated with an incident.

For more information regarding the capability of ThreatMiner, see https://www.threatminer.org.

## Release Notes
<!--
  Specify all changes in this release. Do not remove the release 
  notes of a previous release
-->
### v1.0.0
* Initial Release
### v1.0.1
* Added selftest
* Results returned in json parsable format

## Prerequisites:
```
resilient version 34 or later
resilient_circuits version 30 or later
```
---
## Functions

+ Domain Whois:
  + Domain Whois performs a Whois against a DNS Artifact
+ Domain Subdomains
  + Domain Subdomains returns a list of all subdomains known to the Threatminer database.
+ Email Reverse
  + Email Reverse returns a list of known domains associated with an email address.
+ IP Whois
  + IP Whois returns additional information about an IP address.
+ Samples Metadata
  + Samples Metadata takes a Malware MD5 hash and returns known metadata for that hash.

## Rules and Workflows
Sample rules and workflows are provided to demonstrate the functions. In all cases, incident notes are created 
with the results. In production, create your own rules and workflows, parsing the 
results as necessary.

### Rules
* Example: ThreatMiner Domain Subdomains - Artifact 	
* Example: ThreatMiner Domain Whois 	- Artifact 	
* Example: ThreatMiner Email Reverse  	- Artifact 	
* Example: ThreatMiner IP Whois  	- Artifact 	
* Example: ThreatMiner Samples Metadata  	- Artifact 	
  	
### Workflows
* Example: ThreatMiner Domain Subdomains 	
  + Return subdomains for a top level domain
* Example: ThreatMiner Domain Whois 	
  + Returns WHOIS data for a domain
* Example: ThreatMiner Email Reverse 	
  + Reverse search an email address
* Example: ThreatMiner IP Whois 	
  + Return IP Whois information 	
* Example: ThreatMiner Samples Metadata 	
  + Query ThreatMiner API for file metadata via MD5 Hash


## Installation
Unzip the `fn_threatminer-<version>.zip` file to access the uncompressed tar.gz python package
distribution file.

Add to the python package library:
    
    pip install fn_threatminder-<version>.tar.gz

After installation, install the function definition and rules and workflows by running:
```aidl
resilient-circuits customize -l fn-threatminder
```

Add the configuration settings to your app.config file by running:

```resilient-circuits config -u -l fn-threatminer```
 
No other changes are necessary after this step.

```aidl
[fn_threatminer]
url=https://api.threatminer.org/v2
```

Test connectivity by running:
```aidl
resilient-circuits selftest -l fn-threatminer
```

To uninstall, run:

    pip uninstall fn-threatminer
