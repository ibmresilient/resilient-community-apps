# ThreatMiner API Integration

## Overview

- This Integration queries the ThreatMiner API to extract additional information from artifacts associated with an incident

For more information regarding the ThreatMiner API, see https://www.threatminer.org/api.php

## Functions

+ Domain Whois:
  + Domain Whois performs a Whois against a DNS Artifact and returns the result to a Note
+ Domain Subdomains
  + Domain Subdomains returns a list of all subdomains known to the Threatminer API and returns the result to a Note
+ Email Reverse
  + Email Reverse returns a list of known domains associated with an email address and returns the result to a Note
+ IP Whois
  + IP Whois queries the ThreatMiner API and returns the results to a Note
+ Samples Metadata
  + Samples Metadata takes a Malware MD5 hash and returns known metadata for that hash in the form of a Note

## Installation 

To install in "development mode"

    pip install -e ./fn_threatminer/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall,

    pip uninstall fn_threatminer


To package for distribution,

    python ./fn_threatminer/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install fn_threatminer-<version>.tar.gz
