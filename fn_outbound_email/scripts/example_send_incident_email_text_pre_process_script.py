inputs.mail_to = rule.properties.mail_to
inputs.mail_cc = rule.properties.mail_cc
inputs.mail_incident_id = incident.id
inputs.mail_from = "irhub@mail.resilientsystems.com"
inputs.mail_subject = "[{0}] {1}".format(incident.id, incident.name)

inputs.mail_body_text = """
Incident Summary:
    Severity Code: {{ incident.severity_code }}
    Plan Status: {{ incident.plan_status }}
    Created: {{ template_helper.format_timestamp(incident.create_date) }}
    Incident Type: {{ incident.incident_type_ids }}

"""