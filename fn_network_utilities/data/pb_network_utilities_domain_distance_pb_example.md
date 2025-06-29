<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.5.0.1475
-->

# Playbook - Network Utilities Domain Distance (PB) Example

### API Name
`network_utilities_domain_distance_pb_example`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`artifact.type in ['DNS Name', 'URL', 'Email Sender', 'Email Recipient', 'String', 'URL Referer', 'URI Path']`

### Object Type
`artifact`

### Description
An example testing for confusable domain names


---
## Function - Network Utilities: Domain Distance

### API Name
`network_utilities_domain_distance`

### Output Name
`domain_distance_result`

### Message Destination
`fn_network_utilities`

### Function-Input Script
```python
# if email address, return only domain portion
if "email" in artifact.type.lower():
  split_email = artifact.value.split("@")
  if len(split_email) > 1:
    inputs.network_utilities_domain_name = split_email[1]
  else:
    inputs.network_utilities_domain_name = artifact.value
else:
  # The domain name being tested
  inputs.network_utilities_domain_name = artifact.value

# The list of domains to test against - change as necesary
inputs.network_utilities_domain_list = "ibm.com, resilientsystems.com, ibmcloud.com, bluemix.com"
```

---

## Local script - domain_distance_results

### Description


### Script Type
`Local script`

### Object Type
`artifact`

### Script Content
```python
results = playbook.functions.results.domain_distance_result

# The result includes:
#   "domain_name" - the name being tested
#   "distances" - a dicctionary of all the distances
#   "closest" - the closest match from the list.
# If the match distance is only 1 or 0, the domain name is very easily confused with one on the list!

if results.closest.get("distance") <= 1:
  html = u"<div>Warning!  Domain {} is easily confused with {}!</div>".format(results.get("domain_name"), results.closest.get("name"))
  incident.addNote(helper.createRichText(html))

```

---

