# IBM Resilient Integration for Panorama

- [Overview](#overview)
- [Key Features](#key-features)
- [Requirements](#requirements)
- [Install + Customize](#install--customize)

## Overview
Integration with Resilient and Palo Alto Panorama for adding and removing IP addresses, DNS entries, and users from groups.

---

## Key Features
* Create new IP address or DNS entry in Panorama if it does not already exist.
* Get list of existing addresses and DNS entries in Panorama.
* Add IP address or DNS entry to a group in Panorama.
* Remove IP address or DNS entry from a group in Panorama.
* Get list of users in a group in Panorama.
* Add user to a group in Panorama.
* Remove a user from a group in Panorama.

---

## Requirements
* IBM Resilient >= version `31.0.4254`
* Panorama >= version `9.0.0`
* Integration server with `resilient-circuits >= v31.0.0`, `resilient-lib > v32.0.140`, `xmltodict`

---

## Install + Customize
* Follow our [Install Guide](./docs/install_guide) to get up and running. 

---