<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# VirusTotal Scan Hits

## Function - VirusTotal

### API Name
`virustotal`

### Output Name
`None`

### Message Destination
`fn_virustotal`

### Pre-Processing Script
```python
typeLookup = { 'Email Attachment': 'file', 'Malware Sample': 'file', 'Malware MD5 Hash': 'hash', 'Malware SHA-1 Hash': 'hash', 'Malware SHA-256 Hash': 'hash', 'Other File': 'file', 'RCF 822 Email Message Fife': 'file', 'File Name': 'filename',
 'URL': 'url', 'IP Address': 'ip', 'DNS Name':'domain'}
if artifact.type in typeLookup:
  inputs.vt_type = typeLookup.get(artifact.type, artifact.type)
else:
  inputs.vt_type = artifact.type

inputs.incident_id = incident.id
inputs.artifact_id = artifact.id
inputs.vt_data = artifact.value
```

### Post-Processing Script
```python
if results:
  scan = results.get('scan')
  
  if scan.get('positives') is not None:
    if scan.get('positives') > 0:
      hit = [
      {
        'name': 'Detection Ratio',
        'type': 'number',
        'value': '{} / {}'.format(scan.get('positives'), scan.get('total'))
      },
      {
        'name': 'VirusTotal Report',
        'type': 'uri',
        'value': '{}'.format(scan.get('permalink'))
      },
      {
        "name": "Scan Date",
        "type": "string",
        "value": "{}".format(scan.get('scan_date'))
      }
  ]
  elif artifact.type == 'DNS Name' or 'IP Address':
    test_for_positive = scan.get('detected_urls')
    if test_for_positive is not None:
      sample = test_for_positive[0]
      if sample.get('positives', -1) > 0:
        if artifact.type == 'DNS Name':
          url_fragment = "domain"
        else:
          url_fragment = "ip-address"
        hit = [
                  {
                    'name': 'Detected URL\'s Detection Ratio',
                    'type': 'number',
                    'value': '{} / {}'.format(sample.get('positives'), sample.get('total'))
                  },
                  {
                    'name': 'VirusTotal Report',
                    'type': 'uri',
                    'value': 'https://www.virustotal.com/{}/{}/information/'.format(url_fragment, artifact.value)
                  },
                  {
                    "name": "Detected URL\'s Scan Date",
                    "type": "string",
                    "value": "{}".format(sample.get('scan_date'))
                  }
                ]
  else:
    hit = [
            {
              "name": "Artifact Value",
              "type": "string",
              "value": "{}".format(artifact.value)
            },
            {
              "name": "Verbose Message",
              "type": "string",
              "value": "{}".format(scan['verbose_msg'])
            },
            {
              'name': 'VirusTotal Report',
              'type': 'uri',
              'value': '{}'.format(scan.get('permalink'))
            }
          ]
  artifact.addHit("VirusTotal hits added.", hit)
  
  if results.scan.get('md5') is not None:
    incident.addArtifact('Malware MD5 Hash', scan.get('md5'), None)
  
  if results.scan.get('sha1') is not None:
    incident.addArtifact('Malware SHA-1 Hash', scan.get('sha1'), None)
    
  if results.scan.get('sha256') is not None:
    incident.addArtifact('Malware SHA-256 Hash', scan.get('sha256'), None)
else:
  incident.addNote('VirusTotal has failed')
```

---

