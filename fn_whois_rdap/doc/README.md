# **User Guide:** fn_whois_rdap_v1.0.0

## Table of Contents
- [**User Guide:** fn_whois_rdap_v1.0.0](#user-guide-fnwhoisrdapv100)
  - [Table of Contents](#table-of-contents)
  - [Key Features](#key-features)
  - [Function - RDAP: Query](#function---rdap-query)
  - [Function - WHOIS: query](#function---whois-query)
  - [Inform Resilient Users](#inform-resilient-users)

---

## Key Features
<!--
  List the Key Features of the Integration
-->
* Retrieves Registry information for IP's, DNS or URL's
* Either the RDAP or WHOIS format of data can be returned
* Information is sent directly to the Artifact Description

---

 ![screenshot: fn-rdap-query ](./screenshots/workflows.png)

## Function - RDAP: Query
Using ipwhois library to make general queries in RDAP format

 ![screenshot: fn-rdap-query ](./screenshots/fn-rdap-query.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `rdap_depth` | `number` | Yes | `0` | 0, 1 or 2 |
| `rdap_query` | `text` | Yes | `ibm.com` | IP, URL or DNS |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

```python
results = {'content': {'asn': '16807',
             'asn_cidr': '129.42.38.0/24',
             'asn_country_code': 'US',
             'asn_date': '1987-07-29',
             'asn_description': 'IBM-EI - IBM - Events Infrastructure, US',
             'asn_registry': 'arin',
             'display_content': '{ '
                                '"nir":false,"asn_registry":"arin","asn":"16807","asn_cidr":"129.42.38.0/24","asn_country_code":"US","asn_date":"1987-07-29","asn_description":"IBM-EI '
                                '- IBM - Events Infrastructure, '
                                'US","query":"129.42.38.10","network":{ '
                                '"handle":"NET-129-42-0-0-1","remarks":false,"raw":false,"start_address":"129.42.0.0","end_address":"129.42.255.255","cidr":"129.42.0.0/16","ip_version":"v4","type":"DIRECT '
                                'ASSIGNMENT","name":"IBM-RSCH-NET2","country":false,"parent_handle":"NET-129-0-0-0-0" '
                                '},"objects":{ "IBM-1":{ '
                                '"handle":"IBM-1","status":false,"remarks":false,"notices":false,"raw":false,"contact":{ '
                                '"name":"IBM","kind":"org","phone":false,"email":false,"role":false,"title":false '
                                '},"events_actor":false } '
                                '},"raw":false,"dns_zone":"10.38.42.129.origin.asn.cymru.com" '
                                '}',
             'dns_zone': '10.38.42.129.origin.asn.cymru.com',
             'entities': ['IBM-1'],
             'network': {'cidr': '129.42.0.0/16',
                         'country': None,
                         'end_address': '129.42.255.255',
                         'events': [{'action': 'last changed',
                                     'actor': None,
                                     'timestamp': '2015-10-20T16:09:08-04:00'},
                                    {'action': 'registration',
                                     'actor': None,
                                     'timestamp': '1987-07-28T23:00:00-04:00'}],
                         'handle': 'NET-129-42-0-0-1',
                         'ip_version': 'v4',
                         'links': ['https://rdap.arin.net/registry/ip/129.42.0.0',
                                   'https://whois.arin.net/rest/net/NET-129-42-0-0-1'],
                         'name': 'IBM-RSCH-NET2',
                         'notices': [{'description': 'By using the ARIN '
                                                     'RDAP/Whois service, you '
                                                     'are agreeing to the '
                                                     'RDAP/Whois Terms of Use',
                                      'links': ['https://www.arin.net/resources/registry/whois/tou/'],
                                      'title': 'Terms of Service'},
                                     {'description': 'If you see inaccuracies '
                                                     'in the results, please '
                                                     'visit: ',
                                      'links': ['https://www.arin.net/resources/registry/whois/inaccuracy_reporting/'],
                                      'title': 'Whois Inaccuracy Reporting'},
                                     {'description': 'Copyright 1997-2019, '
                                                     'American Registry for '
                                                     'Internet Numbers, Ltd.',
                                      'links': None,
                                      'title': 'Copyright Notice'}],
                         'parent_handle': 'NET-129-0-0-0-0',
                         'raw': None,
                         'remarks': None,
                         'start_address': '129.42.0.0',
                         'status': ['active'],
                         'type': 'DIRECT ASSIGNMENT'},
             'nir': None,
             'objects': {'IBM-1': {'contact': {'address': [{'type': None,
                                                            'value': '3039 '
                                                                     'Cornwallis '
                                                                     'Road\n'
                                                                     'Research '
                                                                     'Triangle '
                                                                     'Park\n'
                                                                     'NC\n'
                                                                     '27709-2195\n'
                                                                     'United '
                                                                     'States'}],
                                               'email': None,
                                               'kind': 'org',
                                               'name': 'IBM',
                                               'phone': None,
                                               'role': None,
                                               'title': None},
                                   'entities': ['RAIN-ARIN'],
                                   'events': [{'action': 'last changed',
                                               'actor': None,
                                               'timestamp': '2017-11-30T14:46:26-05:00'},
                                              {'action': 'registration',
                                               'actor': None,
                                               'timestamp': '1992-02-08T00:00:00-05:00'}],
                                   'events_actor': None,
                                   'handle': 'IBM-1',
                                   'links': ['https://rdap.arin.net/registry/entity/IBM-1',
                                             'https://whois.arin.net/rest/org/IBM-1'],
                                   'notices': None,
                                   'raw': None,
                                   'remarks': None,
                                   'roles': ['registrant'],
                                   'status': None}},
             'query': '129.42.38.10',
             'raw': None},
 'inputs': {'rdap_depth': 0, 'rdap_query': 'https://www.ibm.com'},
 'metrics': {'execution_time_ms': 337,
             'host': 'your@hostname.com',
             'package': 'fn-whois-rdap',
             'package_version': '1.0.0',
             'timestamp': '2019-09-26 15:52:48',
             'version': '1.0'},
 'raw': '{"nir": null, "asn_registry": "arin", "asn": "16807", "asn_cidr": '
        '"129.42.38.0/24", "asn_country_code": "US", "asn_date": "1987-07-29", '
        '"asn_description": "IBM-EI - IBM - Events Infrastructure, US", '
        '"query": "129.42.38.10", "network": {"handle": "NET-129-42-0-0-1", '
        '"status": ["active"], "remarks": null, "notices": [{"title": "Terms '
        'of Service", "description": "By using the ARIN RDAP/Whois service, '
        'you are agreeing to the RDAP/Whois Terms of Use", "links": '
        '["https://www.arin.net/resources/registry/whois/tou/"]}, {"title": '
        '"Whois Inaccuracy Reporting", "description": "If you see inaccuracies '
        'in the results, please visit: ", "links": '
        '["https://www.arin.net/resources/registry/whois/inaccuracy_reporting/"]}, '
        '{"title": "Copyright Notice", "description": "Copyright 1997-2019, '
        'American Registry for Internet Numbers, Ltd.", "links": null}], '
        '"links": ["https://rdap.arin.net/registry/ip/129.42.0.0", '
        '"https://whois.arin.net/rest/net/NET-129-42-0-0-1"], "events": '
        '[{"action": "last changed", "timestamp": "2015-10-20T16:09:08-04:00", '
        '"actor": null}, {"action": "registration", "timestamp": '
        '"1987-07-28T23:00:00-04:00", "actor": null}], "raw": null, '
        '"start_address": "129.42.0.0", "end_address": "129.42.255.255", '
        '"cidr": "129.42.0.0/16", "ip_version": "v4", "type": "DIRECT '
        'ASSIGNMENT", "name": "IBM-RSCH-NET2", "country": null, '
        '"parent_handle": "NET-129-0-0-0-0"}, "entities": ["IBM-1"], '
        '"objects": {"IBM-1": {"handle": "IBM-1", "status": null, "remarks": '
        'null, "notices": null, "links": '
        '["https://rdap.arin.net/registry/entity/IBM-1", '
        '"https://whois.arin.net/rest/org/IBM-1"], "events": [{"action": "last '
        'changed", "timestamp": "2017-11-30T14:46:26-05:00", "actor": null}, '
        '{"action": "registration", "timestamp": "1992-02-08T00:00:00-05:00", '
        '"actor": null}], "raw": null, "roles": ["registrant"], "contact": '
        '{"name": "IBM", "kind": "org", "address": [{"type": null, "value": '
        '"3039 Cornwallis Road\\nResearch Triangle '
        'Park\\nNC\\n27709-2195\\nUnited States"}], "phone": null, "email": '
        'null, "role": null, "title": null}, "events_actor": null, "entities": '
        '["RAIN-ARIN"]}}, "raw": null, "dns_zone": '
        '"10.38.42.129.origin.asn.cymru.com", "display_content": "{ '
        '\\"nir\\":false,\\"asn_registry\\":\\"arin\\",\\"asn\\":\\"16807\\",\\"asn_cidr\\":\\"129.42.38.0/24\\",\\"asn_country_code\\":\\"US\\",\\"asn_date\\":\\"1987-07-29\\",\\"asn_description\\":\\"IBM-EI '
        '- IBM - Events Infrastructure, '
        'US\\",\\"query\\":\\"129.42.38.10\\",\\"network\\":{ '
        '\\"handle\\":\\"NET-129-42-0-0-1\\",\\"remarks\\":false,\\"raw\\":false,\\"start_address\\":\\"129.42.0.0\\",\\"end_address\\":\\"129.42.255.255\\",\\"cidr\\":\\"129.42.0.0/16\\",\\"ip_version\\":\\"v4\\",\\"type\\":\\"DIRECT '
        'ASSIGNMENT\\",\\"name\\":\\"IBM-RSCH-NET2\\",\\"country\\":false,\\"parent_handle\\":\\"NET-129-0-0-0-0\\" '
        '},\\"objects\\":{ \\"IBM-1\\":{ '
        '\\"handle\\":\\"IBM-1\\",\\"status\\":false,\\"remarks\\":false,\\"notices\\":false,\\"raw\\":false,\\"contact\\":{ '
        '\\"name\\":\\"IBM\\",\\"kind\\":\\"org\\",\\"phone\\":false,\\"email\\":false,\\"role\\":false,\\"title\\":false '
        '},\\"events_actor\\":false } '
        '},\\"raw\\":false,\\"dns_zone\\":\\"10.38.42.129.origin.asn.cymru.com\\" '
        '}"}',
 'reason': None,
 'success': True,
 'version': '1.0'}
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
inputs.rdap_query = artifact.value
inputs.rdap_depth = 0
```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
try:
  des = artifact.description.content
except Exception:
  des = None

if results["success"]:
  if des is None:
    note = u"""<div><p><br><b>RDAP threat intelligence at {2}:</b></br>\n\n
    <br><b>{0}</b></br></div></p>\n\n
    <div><p><br><b> Possible accessible keys:</b></br>\n\n
    <br><b>{1}</b></br>\n\n""".format(results["content"]["display_content"],results["content"].keys(),results["metrics"]["timestamp"])
    artifact.description = helper.createRichText(note)
  else:
    note =des +u"""<div><p><br><b>RDAP threat intelligence at {2}:</b></br>\n\n
    <br><b>{0}</b></br></div></p>\n\n
    <div><p><br><b> Possible accessible keys:</b></br>\n\n
    <br><b>{1}</b></br>\n\n""".format(results["content"]["display_content"],results["content"].keys(),results["metrics"]["timestamp"])
    artifact.description = helper.createRichText(note)
else:
  note = u"""RDAP threat intelligence at {}:\n\n  This Artifact has no ans registry information, \n\n so no intelligence was gathered.  \n\n""".format(results["metrics"]["timestamp"])
  artifact.description = helper.createRichText(note)
```

</p>
</details>

---
## Function - WHOIS: query
Using ipwhois library to make general queries in whois format

 ![screenshot: fn-whois-query ](./screenshots/fn-rdap-query.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `whois_query` | `text` | Yes | `ibm.com` | IP, URL or DNS value |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

```python
results = {'content': {'asn': '16807',
             'asn_cidr': '129.42.38.0/24',
             'asn_country_code': 'US',
             'asn_date': '1987-07-29',
             'asn_description': 'IBM-EI - IBM - Events Infrastructure, US',
             'asn_registry': 'arin',
             'display_content': '{ '
                                '"nir":false,"asn_registry":"arin","asn":"16807","asn_cidr":"129.42.38.0/24","asn_country_code":"US","asn_date":"1987-07-29","asn_description":"IBM-EI '
                                '- IBM - Events Infrastructure, '
                                'US","query":"129.42.38.10","raw":false,"referral":false,"raw_referral":false,"dns_zone":"10.38.42.129.origin.asn.cymru.com" '
                                '}',
             'dns_zone': '10.38.42.129.origin.asn.cymru.com',
             'nets': [{'address': '3039 Cornwallis Road',
                       'cidr': '129.42.0.0/16',
                       'city': 'Research Triangle Park',
                       'country': 'US',
                       'created': '1987-07-28',
                       'description': 'IBM',
                       'emails': ['ipreg@us.ibm.com'],
                       'handle': 'NET-129-42-0-0-1',
                       'name': 'IBM-RSCH-NET2',
                       'postal_code': '27709-2195',
                       'range': '129.42.0.0 - 129.42.255.255',
                       'state': 'NC',
                       'updated': '2015-10-20'}],
             'nir': None,
             'query': '129.42.38.10',
             'raw': None,
             'raw_referral': None,
             'referral': None},
 'inputs': {'whois_query': 'https://www.ibm.com'},
 'metrics': {'execution_time_ms': 2362,
             'host': 'your@hostname.com',
             'package': 'fn-whois-rdap',
             'package_version': '1.0.0',
             'timestamp': '2019-09-26 15:57:35',
             'version': '1.0'},
 'raw': '{"nir": null, "asn_registry": "arin", "asn": "16807", "asn_cidr": '
        '"129.42.38.0/24", "asn_country_code": "US", "asn_date": "1987-07-29", '
        '"asn_description": "IBM-EI - IBM - Events Infrastructure, US", '
        '"query": "129.42.38.10", "nets": [{"cidr": "129.42.0.0/16", "name": '
        '"IBM-RSCH-NET2", "handle": "NET-129-42-0-0-1", "range": "129.42.0.0 - '
        '129.42.255.255", "description": "IBM", "country": "US", "state": '
        '"NC", "city": "Research Triangle Park", "address": "3039 Cornwallis '
        'Road", "postal_code": "27709-2195", "emails": ["ipreg@us.ibm.com"], '
        '"created": "1987-07-28", "updated": "2015-10-20"}], "raw": null, '
        '"referral": null, "raw_referral": null, "dns_zone": '
        '"10.38.42.129.origin.asn.cymru.com", "display_content": "{ '
        '\\"nir\\":false,\\"asn_registry\\":\\"arin\\",\\"asn\\":\\"16807\\",\\"asn_cidr\\":\\"129.42.38.0/24\\",\\"asn_country_code\\":\\"US\\",\\"asn_date\\":\\"1987-07-29\\",\\"asn_description\\":\\"IBM-EI '
        '- IBM - Events Infrastructure, '
        'US\\",\\"query\\":\\"129.42.38.10\\",\\"raw\\":false,\\"referral\\":false,\\"raw_referral\\":false,\\"dns_zone\\":\\"10.38.42.129.origin.asn.cymru.com\\" '
        '}"}',
 'reason': None,
 'success': True,
 'version': '1.0'}
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
inputs.whois_query = artifact.value
```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
try:
  des = artifact.description.content
except Exception:
  des = None

if results["success"]:
  if des is None:
    note = u"""<div><p><br><b>WHOIS threat intelligence at {2}:</b></br>\n\n
    <br><b>{0}</b></br></div></p>\n\n
    <div><p><br><b> Possible accessible keys:</b></br>\n\n
    <br><b>{1}</b></br>\n\n""".format(results["content"]["display_content"],results["content"].keys(),results["metrics"]["timestamp"])
    artifact.description = helper.createRichText(note)
  else:
    note =des +u"""<div><p><br><b>WHOIS threat intelligence at {2}:</b></br>\n\n
    <br><b>{0}</b></br></div></p>\n\n
    <div><p><br><b> Possible accessible keys:</b></br>\n\n
    <br><b>{1}</b></br>\n\n""".format(results["content"]["display_content"],results["content"].keys(),results["metrics"]["timestamp"])
    artifact.description = helper.createRichText(note)
else:
  note = u"""WHOIS threat intelligence at {}:\n\n  This Artifact has no ans registry information, \n\n so no intelligence was gathered.  \n\n""".format(results["metrics"]["timestamp"])
  artifact.description = helper.createRichText(note)
```

</p>
</details>

---





<!--
## Inform Resilient Users
  Use this section to optionally provide additional information so that Resilient playbook 
  designer can get the maximum benefit of your integration.
-->