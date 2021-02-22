# **User Guide:** fn_outbound_email

## Table of Contents
- [**User Guide:** fn_outbound_email](#user-guide-fnoutboundemail107)
  - [Table of Contents](#table-of-contents)
  - [History](#history)
  - [Key Features](#key-features)
  - [Function - Send Email HTML](#function---send-email-html)
  - [Function - Send Email Text](#function---send-email-text)
  - [Rules](#rules)

---

## History

| Version | Date | Notes |
| ------- | ---- | ----- |
| v1.1.1  | 2/2021 | Bug fixes associated with sending attachments |
| v1.1.0  | 10/2020 | Bug fixes and send all or specific attachments |
| v1.0.9 | 5/2020 | App Host compatibility |
| v1.0.8 | 4/2020 | Initial Release after internal development by Professional Services, no prior release notes |


## Key Features
* Send a plain text or HTML-formatted email by triggering a Resilient action
* Add incident data to the email body as well as incident attachments to the outgoing email
* TLS cert login on port 589, which is possible by permitting less secure apps by your email provider or giving this application a specific login (recommended)

---

## Function - Send Email

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mail_bcc` | `text` | No | `changeme@email.com` | edit in script or app.config (precedence on smtp_user) |
| `mail_body_html` | `text` | No | `<html>` | template in script |
| `mail_body_text` | `text` | No | `plain_text` | template in script |
| `mail_cc` | `text` | No | `changeme@email.com` | user input |
| `mail_from` | `text` | No | `changeme@email.com` | edit in script or app.config (precedence on smtp_user) |
| `mail_incident_id` | `number` | No | `2085` | Taken from incident  |
| `mail_subject` | `text` | No | `[incident type id]` | Taken from incident |
| `mail_to` | `text` | Yes | `changeme@email.com` | user_input |
| `mail_attachments` | `text` | No | `myattach1.txt, myattachment2.csv` | comma separated attachment list or '*' for all |

</p>
</details>

<details><summary>Outputs:</summary>
<p>


</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
inputs.mail_to = rule.properties.mail_to
inputs.mail_cc = rule.properties.mail_cc
inputs.mail_incident_id = incident.id
inputs.mail_from = "changeme@resilientsystems.com"
inputs.mail_subject = "[{0}] {1}".format(incident.id, incident.name)

inputs.mail_body_html = """
{% set NOT_FOUND = ["Not Found!","-","None",None] %}
{% macro get_row(label,field_name) -%}
	{% set value = template_helper.get_incident_value(incident,field_name) %}
	{% set style = "font-family: Calibri; color: rgb(31,73,125)" %}
    {% if value and value not in NOT_FOUND and not value.startswith('-') %}
    <tr>
        <td width="100" style="{{style}}; font-weight:bold">{{ label }}</td>
        <td style="{{style}}">{{ value | striptags}}</td>
    </tr>
    {% endif %}
{%- endmacro %}
<table width="100%" >
<tr>
    <td colspan="2">
        <h3 style="color: rgb(68,114,196)">INCIDENT DETAILS</h3>
        <hr size="1" width="100%" noshade style="color:#FFDF57" align="center"/>
    </td>
</tr>
    {{ get_row('Severity:','severity_code') }}
    {{ get_row('Status:','status') }}<br>
    {{ get_row('Created:','create_date') }}<br>
    {{ get_row('Category:','incident_type_ids') }}
<tr>
    <td colspan="2">
        <br><h3 style="color: rgb(68,114,196)">INCIDENT DESCRIPTION</h3>
        <hr size="1" width="100%" noshade style="color:#FFDF57" align="center"/>
    </td>
    {{ get_row('Description:','description') }}
</tr>
</table>
<br>
"""
```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
if results.success:
  noteText = u"""Email Sent if mail server is valid/authenticated\n 
  From: {0}<br> To: {1}<br> CC: {2}<br> BCC: {3}<br> Subject: {4} <br> 
  Body: {5} <br>""".format(results.content.inputs[0].strip("u\"[]"), results.content.inputs[1].strip("u\"[]"), results.content.inputs[2].strip("u\"[]"), results.content.inputs[3].strip("u\"[]"), results.content.inputs[4].strip("u\"[]"), results.content.text)
else:
  noteText = u"Email NOT Sent\n From: {0}\n To: {1}".format(results.content.inputs[0].strip("u\"[]"), results.content.inputs[1].strip("u\"[]"))
incident.addNote(helper.createRichText(noteText))

```

```python
results = {
"""2020-03-29 13:23:23,135 DEBUG [actions_component] Result: {'success': True, 'message': 'Content-Type: multipart/mixed; boundary="===============3279704273121734511=="\nMIME-Version: 1.0\nFrom: changeme@resilientsystems.com\nTo: dummy@email.com\nCC: \nBCC: \nSubject: [2095] aueo\n\n--===============3279704273121734511==\nMIME-Version: 1.0\nContent-Type: text/html; charset="utf-8"\nContent-Transfer-Encoding: base64\n\nCgoKPHRhYmxlIHdpZHRoPSIxMDAlIiA+Cjx0cj4KICAgIDx0ZCBjb2xzcGFuPSIyIj4KICAgICAg\nICA8aDMgc3R5bGU9ImNvbG9yOiByZ2IoNjgsMTE0LDE5NikiPklOQ0lERU5UIERFVEFJTFM8L2gz\nPgogICAgICAgIDxociBzaXplPSIxIiB3aWR0aD0iMTAwJSIgbm9zaGFkZSBzdHlsZT0iY29sb3I6\nI0ZGREY1NyIgYWxpZ249ImNlbnRlciIvPgogICAgPC90ZD4KPC90cj4KICAgIAoJCiAgICAKICAg\nIDx0cj4KICAgICAgICA8dGQgd2lkdGg9IjEwMCIgc3R5bGU9ImZvbnQtZmFtaWx5OiBDYWxpYnJp\nOyBjb2xvcjogcmdiKDMxLDczLDEyNSk7IGZvbnQtd2VpZ2h0OmJvbGQiPlNldmVyaXR5PC90ZD4K\nICAgICAgICA8dGQgc3R5bGU9ImZvbnQtZmFtaWx5OiBDYWxpYnJpOyBjb2xvcjogcmdiKDMxLDcz\nLDEyNSkiPkxvdzwvdGQ+CiAgICA8L3RyPgogICAgCiAgICAKCQogICAgCiAgICA8dHI+CiAgICAg\nICAgPHRkIHdpZHRoPSIxMDAiIHN0eWxlPSJmb250LWZhbWlseTogQ2FsaWJyaTsgY29sb3I6IHJn\nYigzMSw3MywxMjUpOyBmb250LXdlaWdodDpib2xkIj5TdGF0dXM8L3RkPgogICAgICAgIDx0ZCBz\ndHlsZT0iZm9udC1mYW1pbHk6IENhbGlicmk7IGNvbG9yOiByZ2IoMzEsNzMsMTI1KSI+QTwvdGQ+\nCiAgICA8L3RyPgogICAgCiAgICAKCQogICAgCiAgICA8dHI+CiAgICAgICAgPHRkIHdpZHRoPSIx\nMDAiIHN0eWxlPSJmb250LWZhbWlseTogQ2FsaWJyaTsgY29sb3I6IHJnYigzMSw3MywxMjUpOyBm\nb250LXdlaWdodDpib2xkIj5DcmVhdGVkPC90ZD4KICAgICAgICA8dGQgc3R5bGU9ImZvbnQtZmFt\naWx5OiBDYWxpYnJpOyBjb2xvcjogcmdiKDMxLDczLDEyNSkiPjIwMTktMTEtMTRUMTQ6MTQ6NDE8\nL3RkPgogICAgPC90cj4KICAgIAogICAgCgkKICAgIAogICAgPHRyPgogICAgICAgIDx0ZCB3aWR0\naD0iMTAwIiBzdHlsZT0iZm9udC1mYW1pbHk6IENhbGlicmk7IGNvbG9yOiByZ2IoMzEsNzMsMTI1\nKTsgZm9udC13ZWlnaHQ6Ym9sZCI+Q2F0ZWdvcnk8L3RkPgogICAgICAgIDx0ZCBzdHlsZT0iZm9u\ndC1mYW1pbHk6IENhbGlicmk7IGNvbG9yOiByZ2IoMzEsNzMsMTI1KSI+Q29tbXVuaWNhdGlvbiBl\ncnJvciAoZmF4OyBlbWFpbCk8L3RkPgogICAgPC90cj4KICAgIAo8dHI+CiAgICA8dGQgY29sc3Bh\nbj0iMiI+CiAgICAgICAgPGJyPjxoMyBzdHlsZT0iY29sb3I6IHJnYig2OCwxMTQsMTk2KSI+SU5D\nSURFTlQgREVTQ1JJUFRJT048L2gzPgogICAgICAgIDxociBzaXplPSIxIiB3aWR0aD0iMTAwJSIg\nbm9zaGFkZSBzdHlsZT0iY29sb3I6I0ZGREY1NyIgYWxpZ249ImNlbnRlciIvPgogICAgPC90ZD4K\nPC90cj4KPC90YWJsZT4KPGJyPg==\n\n--===============3279704273121734511==--\n'}
<Ack[*] ()>
}"""
}
```
</p>
</details>

---


## Rules
| Rule Name | Object | Workflow Triggered |
| --------- | ------ | ------------------ |
| Example: Send Incident Email HTML | incident | `example_send_incident_email_html` |
| Example: Send Incident Email Text | incident | `example_send_incident_email_text` |

---
