# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
import hashlib
import time

try:
  dialog_inputs = rule.properties
except:
  dialog_inputs = None

if not dialog_inputs or not dialog_inputs.get('email_approval_to'):
  try:
    dialog_inputs = playbook.inputs
  except:
    pass
  

MESSAGE_ID_DOMAIN = "QRADARSOAR.IBM.COM"
SUBJECT_PREFIX = "IBM SOAR Approval Requested"

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

msg_content = dialog_inputs.email_approval_details.content.replace('\n', '<br>') if dialog_inputs.get('email_approval_details') else None

expiration_ts = dialog_inputs.email_approval_expiration if dialog_inputs.get('email_approval_expiration') else 0
# confirm dates in the future
if expiration_ts and expiration_ts < current_time:
    helper.fail("Expiration date is in the past")

expiration = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(expiration_ts/1000)) if expiration_ts else 0

msg_hash = generate_msg_hash(expiration_ts,
                             incident.id,
                             incident.create_date,
                             task.id
                             )
msg_id = create_msg_id(msg_hash)

body = []
body.append("""
##- Please type your reply "approved" or "denied" above this line. Add additional detail on separate line(s), as necessary.  -##
<br><br>
Approval is requested to perform this activity.
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
task {task.id}: {task.name} (<a target='_blank' href='{{{{ template_helper.generate_task_url({incident.id},{task.id}) }}}}'>link</a>)
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
  "subject": f"{SUBJECT_PREFIX} for Task: {task.name}",
  "body": "<br>".join(body),
  "importance": dialog_inputs.get('email_approval_importance', 'normal')
}

# add to property for function processing
try:
  workflow.addProperty("email_approval", details)
except:
  pass

try:
  playbook.addProperty("email_approval", details)
except:
  pass

# updates to task
task.due_date = expiration_ts if expiration_ts else task.due_date
task.owner_id = principal.name if not task.owner_id else None