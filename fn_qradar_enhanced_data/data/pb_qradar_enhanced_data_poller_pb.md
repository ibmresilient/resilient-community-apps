<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.2.1096
-->

# Playbook - QRadar Enhanced Data Poller (PB)

### API Name
`qradar_enhanced_data_poller_pb`

### Status
`disabled`

### Activation Type
`Automatic`

### Activation Conditions
`incident.properties.qr_last_updated_time changed AND incident.properties.qradar_destination has_a_value AND incident.properties.qradar_id has_a_value`

### Object Type
`incident`

### Description
None


---


## Sub-Playbook - Example of searching and returning Categories

### Output Name
`category_result`

 ### Input Script
```python
None
```

---
## Sub-Playbook - Example of fetching contributing rules for Offense

### Output Name
`rule_result`

 ### Input Script
```python
None
```

---
## Sub-Playbook - Example of searching and returning Assets information

### Output Name
`asset_result`

 ### Input Script
```python
None
```

---
## Sub-Playbook - Example of searching and returning Destination IPs information

### Output Name
`dest_ip_info`

 ### Input Script
```python
None
```

---
## Sub-Playbook - Example of searching and returning Source IPs information

### Output Name
`source_ip_info`

 ### Input Script
```python
None
```

---
## Sub-Playbook - Example of searching QRadar Flows using offense id

### Output Name
`flow_result`

 ### Input Script
```python
None
```

---
## Sub-Playbook - Example of searching QRadar Top Events using offense id

### Output Name
`events_result`

### Static Inputs
| Input Name | Input API Name | Input Value | Input Type |
| ---------- | -------------- | ----------- | ---------- |
| Create extra artifacts | create_extra_artifacts | False | `boolean` |

---
## Sub-Playbook - QRadar Offense Summary

### Output Name
`offense_sum`

 ### Input Script
```python
None
```

---
