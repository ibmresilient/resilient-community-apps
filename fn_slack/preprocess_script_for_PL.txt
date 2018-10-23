Example: Post message to Slack - Incident:
-----------------------------------------------------
#####################
# Incident data     #
#####################

# Incident description
description = incident.description.content.replace(u'"', u'\\"') if incident.description is not None else ''

# Slack additional text message
# Additional text message to inlcude with the Incident, Note, Artifact, Attachment or Task data.
rule_additional_text = rule.properties.rule_slack_text if rule.properties.rule_slack_text is not None else ''

# "datetime" fields: Assign 0 if it's None
date_occured = incident.start_date if incident.start_date else 0
date_discovered = incident.discovered_date if incident.discovered_date else 0

# Incident id for the URL
incident_id = str(incident.id)

# Slack text message in JSON format
# ---------------------------------
# Do not remove first 3 elements "Additional Text", "Resilient URL" and "Type of data",
# the information is used to to generate the title of the message.
#
# Add/remove information using the syntax: "label": {{ "type": "[string|richtext|boolean|datetime", "data": "resilient field data" }}
# Make sure to send "datetime" types as int and not str - withouth duble quotes: { "type": "datetime", "data": resilient datetime data}
# watch out of embedded double quotes in text fields and escape with field.replace(u'"', u'\\"')
custom_slack_text = u"""{{
  "Additional Text": {{"type": "string", "data": "{0}" }},
  "Resilient URL": {{"type": "incident", "data": "{1}" }},
  "Type of data": {{"type": "string", "data": "{2}" }},
  "Incident ID": {{"type": "string", "data": "{3}" }},
  "Incident name": {{"type": "string", "data": "{4}" }},
  "Description": {{"type": "richtext", "data": "{5}" }},
  "Incident Types": {{"type": "string", "data": "{6}" }},
  "NIST Attack Vectors": {{"type": "string", "data": "{7}" }},
  "Confirmed": {{"type": "boolean", "data": "{8}" }},
  "Date Created": {{"type": "datetime", "data": {9} }},
  "Date Occurred": {{"type": "datetime", "data": {10} }},
  "Date Discovered": {{"type": "datetime", "data": {11} }},
  "Severity": {{"type": "string", "data": "{12}" }}
}}""".format(
  rule_additional_text,
  incident_id,
  "Incident",
  incident_id,
  incident.name.replace(u'"', u'\\"'),
  description,
  incident.incident_type_ids,
  incident.nist_attack_vectors,
  incident.confirmed,
  incident.create_date,
  date_occured,
  date_discovered,
  incident.severity_code)

# ID of this incident
inputs.incident_id = incident.id

# Slack channel name
# Name of the existing Slack Workspace channel or a new Slack channel you are posting to.
# Channel names can only contain lowercase letters, numbers, hyphens, and underscores, and must be 21 characters or less.
# If you leave this field empty, function will try to use the slack_channel associated with the Incident or Task found in the Slack Conversations datatable.
# It there isn’t one defined, the workflow will terminate.
inputs.slack_channel = rule.properties.rule_slack_channel if rule.properties.rule_slack_channel is not None else inputs.slack_channel

# Is channel private
# Indicate if the channel you are posting to should be private.
inputs.slack_is_channel_private = rule.properties.rule_slack_is_channel_private if rule.properties.rule_slack_is_channel_private is not None else inputs.slack_is_channel_private

# Slack users emails
# A comma separated list of emails belonging to Slack users in your workspace that will be added to the channel you are posting to.
inputs.slack_participant_emails = rule.properties.rule_slack_participant_emails if rule.properties.rule_slack_participant_emails is not None else inputs.slack_participant_emails

# Slack text message
# Container field to retain JSON fields to send to Slack.
inputs.slack_text = custom_slack_text

Example: Post message to Slack - Task :
-----------------------------------------------------
#####################
# Task data         #
#####################

# Incident id for the URL
incident_id = str(incident.id)
if task:
  incident_id += "?task_id="+str(task.id)

# Task due date, send 0 if it's None
task_due_date = task.due_date if task.due_date else 0

# Task Status
task_status = "Open" if task.status == "O" else "Closed"

# Slack additional text message
# Additional text message to inlcude with the Incident, Note, Artifact, Attachment or Task data.
rule_additional_text = rule.properties.rule_slack_text if rule.properties.rule_slack_text is not None else ''

# Slack text message in JSON format
# ---------------------------------
# Do not remove first 3 elements "Additional Text", "Resilient URL" and "Type of data",
# the information is used to to generate the title of the message.
#
# Add/remove information using the syntax: "label": {{ "type": "[string|richtext|boolean|datetime", "data": "resilient field data" }}
# Make sure to send "datetime" types as int and not str - withouth duble quotes: { "type": "datetime", "data": resilient datetime data}
# watch out of embedded double quotes in text fields and escape with field.replace(u'"', u'\\"')
custom_slack_text = u"""{{
  "Additional Text": {{"type": "string", "data": "{0}" }},
  "Resilient URL": {{"type": "incident", "data": "{1}" }},
  "Type of data": {{"type": "string", "data": "{2}" }},
  "Incident ID": {{"type": "string", "data": "{3}" }},
  "Task Name": {{"type": "string", "data": "{4}" }},
  "Task Status": {{"type": "string", "data": "{5}" }},
  "Task Owner": {{"type": "string", "data": "{6}" }},
  "Task Due Date": {{"type": "datetime", "data": {7} }}
}}""".format(
  rule_additional_text,
  incident_id,
  "Task",
  str(incident.id),
  task.name,
  task_status,
  task.owner_id,
  task_due_date)

# Slack username - optional setting
# Set to true and the authenticated user of the Slack App will appear as the author of the message, ignoring any values provided for slack_username.
# Set your bot's name to Task's creator to appear as the author of the message. Must be used in conjunction with slack_as_user set to false, otherwise ignored.
#inputs.slack_as_user = False
#inputs.slack_username = task.creator_id

# ID of this incident
inputs.incident_id = incident.id

# ID of this Task
inputs.task_id = task.id

# Slack channel name
# Name of the existing Slack Workspace channel or a new Slack channel you are posting to.
# Channel names can only contain lowercase letters, numbers, hyphens, and underscores, and must be 21 characters or less.
# If you leave this field empty, function will try to use the slack_channel associated with the Incident or Task found in the Slack Conversations datatable.
# It there isn’t one defined, the workflow will terminate.
inputs.slack_channel = rule.properties.rule_slack_channel if rule.properties.rule_slack_channel is not None else inputs.slack_channel

# Is channel private
# Indicate if the channel you are posting to should be private.
inputs.slack_is_channel_private = rule.properties.rule_slack_is_channel_private if rule.properties.rule_slack_is_channel_private is not None else inputs.slack_is_channel_private

# Slack users emails
# A comma separated list of emails belonging to Slack users in your workspace that will be added to your channel.
inputs.slack_participant_emails = rule.properties.rule_slack_participant_emails if rule.properties.rule_slack_participant_emails is not None else inputs.slack_participant_emails

# Slack text message
# Container field to retain JSON fields to send to Slack
inputs.slack_text = custom_slack_text

Example: Post message to Slack - Note:
-----------------------------------------------------
#####################
# Note data         #
#####################

# Note description
note_description = note.text.content.replace(u'"', u'\\"') if note.text is not None else ''

# Slack additional text message
# Additional text message to inlcude with the Incident, Note, Artifact, Attachment or Task data.
rule_additional_text = rule.properties.rule_slack_text if rule.properties.rule_slack_text is not None else ''

# Incident id for the URL
incident_id = str(incident.id)
type_data = "Incident Note"
if task:
  incident_id += "?task_id="+str(task.id)
  type_data = "Task Note"

# Task name
task_name = task.name if task else ""

# Slack text message in JSON format
# ---------------------------------
# Do not remove first 3 elements "Additional Text", "Resilient URL" and "Type of data",
# the information is used to to generate the title of the message.
#
# Add/remove information using the syntax: "label": {{ "type": "[string|richtext|boolean|incident|datetime", "data": "resilient field data" }}
# Make sure to send "datetime" types as int and not str - withouth duble quotes: { "type": "datetime", "data": resilient datetime data}
# watch out of embedded double quotes in text fields and escape with field.replace(u'"', u'\\"')
custom_slack_text = u"""{{
  "Additional Text": {{"type": "string", "data": "{0}" }},
  "Resilient URL": {{"type": "incident", "data": "{1}" }},
  "Type of data": {{"type": "string", "data": "{2}" }},
  "Incident ID": {{"type": "string", "data": "{3}" }},
  "Task": {{"type": "string", "data": "{4}" }},
  "Note": {{"type": "richtext", "data": "{5}" }}
}}""".format(
  rule_additional_text,
  incident_id,
  type_data,
  str(incident.id),
  task_name,
  note_description)

# Slack username - optional setting
# Set to true and the authenticated user of the Slack App will appear as the author of the message, ignoring any values provided for slack_username.
# Set your bot's name to Note's creator to appear as the author of the message. Must be used in conjunction with slack_as_user set to false, otherwise ignored.
#inputs.slack_as_user = False
#inputs.slack_username = note.user_id

# ID of this incident
inputs.incident_id = incident.id

# ID of this Task
if task:
  inputs.task_id = task.id

# Slack channel name
# Name of the existing Slack Workspace channel or a new Slack channel you are posting to.
# Channel names can only contain lowercase letters, numbers, hyphens, and underscores, and must be 21 characters or less.
# If you leave this field empty, function will try to use the slack_channel associated with the Incident or Task found in the Slack Conversations datatable.
# It there isn’t one defined, the workflow will terminate.
inputs.slack_channel = rule.properties.rule_slack_channel if rule.properties.rule_slack_channel is not None else inputs.slack_channel

# Is channel private
# Indicate if the channel you are posting to should be private.
inputs.slack_is_channel_private = rule.properties.rule_slack_is_channel_private if rule.properties.rule_slack_is_channel_private is not None else inputs.slack_is_channel_private

# Slack users emails
# A comma separated list of emails belonging to Slack users in your workspace that will be added to your channel.
inputs.slack_participant_emails = rule.properties.rule_slack_participant_emails if rule.properties.rule_slack_participant_emails is not None else inputs.slack_participant_emails

# Slack text message
# Container field to retain JSON fields to send to Slack.
inputs.slack_text = custom_slack_text

Example: Post message to Slack - Artifact:
-----------------------------------------------------
#####################
# Artifact data     #
#####################

# Slack additional text message
# Additional text message to inlcude with the Incident, Note, Artifact, Attachment or Task data.
rule_additional_text = rule.properties.rule_slack_text if rule.properties.rule_slack_text is not None else ''

# Incident id for the URL
incident_id = str(incident.id)

# Slack text message in JSON format
# ---------------------------------
# Do not remove first 3 elements "Additional Text", "Resilient URL" and "Type of data",
# the information is used to to generate the title of the message.
#
# Add/remove information using the syntax: "label": {{ "type": "[string|richtext|boolean|datetime", "data": "resilient field data" }}
# Make sure to send "datetime" types as int and not str - withouth duble quotes: { "type": "datetime", "data": resilient datetime data}
# watch out of embedded double quotes in text fields and escape with field.replace(u'"', u'\\"')
custom_slack_text = u"""{{
  "Additional Text": {{"type": "string", "data": "{0}" }},
  "Resilient URL": {{"type": "incident", "data": "{1}" }},
  "Type of data": {{"type": "string", "data": "{2}" }},
  "Incident ID": {{"type": "string", "data": "{3}" }},
  "Artifact Type": {{"type": "string", "data": "{4}" }},
  "Artifact Value": {{"type": "string", "data": "{5}" }},
  "Artifact Created By": {{"type": "string", "data": "{6}" }},
  "Artifact Created on": {{"type": "datetime", "data": {7} }}
}}""".format(
  rule_additional_text,
  incident_id,
  "Artifact",
  incident_id,
  artifact.type,
  artifact.value,
  artifact.creator.display_name,
  artifact.created)

# ID of this incident
inputs.incident_id = incident.id

# Slack channel name
# Name of the existing Slack Workspace channel or a new Slack channel you are posting to.
# Channel names can only contain lowercase letters, numbers, hyphens, and underscores, and must be 21 characters or less.
# If you leave this field empty, function will try to use the slack_channel associated with the Incident or Task found in the Slack Conversations datatable.
# It there isn’t one defined, the workflow will terminate.
inputs.slack_channel = rule.properties.rule_slack_channel if rule.properties.rule_slack_channel is not None else inputs.slack_channel

# Is channel private
# Indicate if the channel you are posting to should be private.
inputs.slack_is_channel_private = rule.properties.rule_slack_is_channel_private if rule.properties.rule_slack_is_channel_private is not None else inputs.slack_is_channel_private

# Slack users emails
# A comma separated list of emails belonging to Slack users in your workspace that will be added to your channel.
inputs.slack_participant_emails = rule.properties.rule_slack_participant_emails if rule.properties.rule_slack_participant_emails is not None else inputs.slack_participant_emails

# Slack text message
# Container field to retain JSON fields to send to Slack.
inputs.slack_text = custom_slack_text