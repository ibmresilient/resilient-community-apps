import base64
import hashlib
import re
import time

# get the task_creation property. This script requires the 'create custom task' function to previously run
try:
  dialog_inputs = playbook.inputs
  task_info = playbook.functions.results.task_creation
except:
  dialog_inputs = rule.properties
  task_info = workflow.properties.task_creation

task_id = task_info['content'].get('task', {}).get('id')
task_name = task_info['inputs'].get('task_name')

MESSAGE_ID_DOMAIN = "QRADARSOAR.IBM.COM"
SUBJECT_PREFIX = "IBM SOAR Approval Requested"
# check for any combination of upper/lowercase http/https/news/telnet/file. Characters repeated for readability
DEFANG_PATTERN = re.compile(r"(https|http|ftps|ftp|mailto|news|file|mailto):", re.IGNORECASE)

current_time = int(time.time()*1000)

# generate a message-id
def generate_msg_hash(expiration, incident_id, incident_create_date, task_id):
    m = hashlib.sha256()
    m.update(str(expiration).encode())
    m.update(str(incident_id).encode())
    m.update(str(incident_create_date).encode())
    m.update(str(task_id).encode())

    uuid_hash = m.hexdigest()
    return "{}-{}-{}-{}-{}".format(uuid_hash[0:12], uuid_hash[12:24], uuid_hash[24:36], uuid_hash[36:48], uuid_hash[48:])

def create_msg_id(msg_hash, domain=MESSAGE_ID_DOMAIN):
  return "{}@{}".format(msg_hash, domain)

msg_content = dialog_inputs.email_approval_details.content.replace('\n', '<br>') if dialog_inputs.email_approval_details.content else None

expiration_ts = dialog_inputs.email_approval_expiration if dialog_inputs.email_approval_expiration else 0
# confirm dates in the future
if expiration_ts and expiration_ts < current_time:
    helper.fail("Expiration date is in the past")

expiration = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(expiration_ts/1000)) if expiration_ts else 0

msg_hash = generate_msg_hash(expiration_ts,
                             incident.id,
                             incident.create_date,
                             task_id
                             )
msg_id = create_msg_id(msg_hash)
# defang the artifact if needed
artifact_value = DEFANG_PATTERN.sub(r"x_\1_x:", artifact.value)
body = []
body.append(f"""
##- Please type your reply "approved" or "denied" above this line. Add additional detail on separate line(s), as necessary.  -##
<br><br>
Approval is requested to perform an action on artifact: '{artifact_value}'.
""")
if expiration_ts > 0:
    body.append(f"This approval will expire on: {expiration}")


body.append(f"""<br>
Additional detail follows:
<br>
{msg_content}
<br><br>
##- retain this data -##
<br>
msg-id: {msg_hash}
<br>
incident {incident.id}: {incident.name} (<a target='_blank' href='{{{{ template_helper.generate_incident_url({incident.id}) }}}}'>link</a>)
<br>
task {task_id}: {task_name} (<a target='_blank' href='{{{{ template_helper.generate_task_url({incident.id},{task_id}) }}}}'>link</a>)
<br>
artifact: {artifact.type}: {artifact_value}
<br>
expiration {expiration_ts}: {expiration}
""")

# have the approval details
details = {
  "ts": current_time,
  "expiration": expiration,
  "expiration_ts": expiration_ts,
  "msg_hash": msg_hash,
  "msg_id": msg_id,
  "to": dialog_inputs.email_approval_to,
  "from": None, # change as necessary
  "cc": dialog_inputs.email_approval_cc,
  "bcc": None, # change as necessary
  "subject": f"{SUBJECT_PREFIX} for Task: {task_name}",
  "body": "<br>".join(body),
  "importance": dialog_inputs.email_approval_importance,
  "task_id": task_id,
  "task_name": task_name
}

# add to property for function processing
try:
  workflow.addProperty("email_approval", details)
except:
  playbook.addProperty("email_approval", details)
