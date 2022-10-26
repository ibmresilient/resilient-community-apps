# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import datetime
import hashlib
import re
import time
from email.utils import parsedate_to_datetime

SUBJECT_PREFIX = "IBM SOAR Approval Requested"
# pattern used to find and extract the email message-id
MESSAGE_PATTERN = re.compile(r"([^<>]+)")

ID_PATTERN_LIST = {
  'msg-id': re.compile(r"msg-id: ([a-zA-z0-9-]*)"),
  'inc-id': re.compile(r"incident (\d*):"),
  'task-id': re.compile(r"task (\d*):"),
  'task-name': re.compile(r"task \d*: (.*)$"),
  'expiration-ts': re.compile(r"expiration (\d*):")
}

APPROVE_LIST = ['yes', 'ok', 'okay', 'approve', 'approved', 'allow', 'proceed', 'continue', 'accept']
DENY_LIST = ['no', 'disapprove', 'reject', 'rejected', 'deny', 'denied', 'stop', 'pause', 'defer', 'deferred']
STRIP_RESPONSE = re.compile(r'(\w*)') # pattern to strip white space and special characters like '.'

# delimeter for sections within the approval message
RETAIN_COMMENTS = "##- retain"
ORIGINAL_EMAIL = [re.compile(r"^> "), re.compile(r"^On "), re.compile(r"wrote:", re.IGNORECASE), re.compile(r"From:", re.IGNORECASE)] # characters associated with the start of the original message

# F U N C T I O N S
def generate_msg_hash(expiration_ts, incident_id, incident_create_date, task_id):
    m = hashlib.sha256()
    m.update(str(expiration_ts).encode())
    m.update(str(incident_id).encode())
    m.update(str(incident_create_date).encode())
    m.update(str(task_id).encode())

    uuid_hash = m.hexdigest()
    return "{}-{}-{}-{}-{}".format(uuid_hash[0:12], uuid_hash[12:24], uuid_hash[24:36], uuid_hash[36:48], uuid_hash[48:])
    
def handle_list(value):
  # convert a list to comma separate list, if neccessary
  if value and isinstance(value, list):
    return ", ".join(value)

  return value

def get_content():
  # return all content found in the email messagew
  """
  approved
  msg1
  msg2
  ##- Please type your reply "approved" or "denied" above this line. Add additional detail on separate line(s), as necessary.  -##
  
  Approval is requested to perform this activity. Additional detail follows:
  checkpoint fw
  ip ban
  
  ##- retain this data -##
  msg-id: d9ef3d54103f-03cb756ce84b-805eab0bff8c-8030b0796977-a47d83a5f0c391d4
  incident 2142: Incident generated from email "Approval Requested for Task: Remote wipe/lock" via mailbox outlook (<a target='_blank' href='https://9.30.55.116:443/#incidents/2142?orgId=201'>link</a>)
  task 1066: Interview key individuals (<a target='_blank' href='https://9.30.55.116:443/#incidents/2142?orgId=201&amp;taskId=1066&amp;tabName=details'>link</a>)
  expiration 123456789: 2022-08-29 12:00:00 IST
  """

  if (emailmessage.body.content is not None):
    return emailmessage.body.content

  log.error("Email message has no content!")

def get_response(content):
  # parse the message body to collect:
  #  - the response
  #  - any comments
  #  - msg-id, incident-id, task-id
  
  id_list_response = {}
  comments = []
  response = None

  # sections are separators between user response and information about the incident
  retain_section = False
  original_msg = False
  for line in content.split('\n'):
    # find the section where all the incident data is retained
    if RETAIN_COMMENTS in line.strip():
      retain_section = True
      continue
      
    if retain_section:
      for key, ptrn in ID_PATTERN_LIST.items():
        match = ptrn.search(line.strip())
        if match:
          id_list_response[key] = match.group(1)
      continue
        
    # parse the approval response and comments
    if not retain_section and response is not None and line.strip():
      if "<br>" not in line and not original_msg:
        # make sure we haven't started looking through the original email
        for matcher in ORIGINAL_EMAIL:
            if matcher.search(line):
                original_msg = True
                break
            
        if not original_msg:
          comments.append(line)
    elif not retain_section and response is None:
      match = STRIP_RESPONSE.search(line.strip().lower())
      reply = match.group(0) if match else line.strip().lower()

      # find approval response
      if bool(reply in APPROVE_LIST):
        response = True
      elif bool(reply in DENY_LIST):
        response = False
      else:
        log.info(f"extraneous: {line}")

  log.info(f"response {response} id_list_response {id_list_response} comments {comments}")
  return response, id_list_response, comments

def find_incident(inc_id):
  # find the cooresponding incident
  query_builder.equals(fields.incident.id, int(inc_id))
  query_builder.equals(fields.incident.plan_status, "Active")
  query = query_builder.build()
  incidents = helper.findIncidents(query)

  if len(incidents) == 0:
    return None

  return incidents[0]

def is_valid_msg_id(incident, id_list_response):
  # confirm if the msg-id matches the incident
  confirm_msg_id = generate_msg_hash(id_list_response['expiration-ts'],
                                     id_list_response['inc-id'],
                                     incident.create_date,
                                     id_list_response['task-id']
                                     )

  return bool(id_list_response['msg-id'] == confirm_msg_id)

def get_attachments(attachments):
  return [attachment.suggested_filename for attachment in attachments]

def get_msg_sent_date(msg_date):
  # Date: Sat, 27 Aug 2022 20:30:30 +0000 (UTC)
  dt = parsedate_to_datetime(msg_date[0].replace("Date: ", ""))
  return int(dt.timestamp()*1000)
  
def get_expiration_ts(expiration):
    if expiration != '0':
        dt = datetime.strptime(expiration, '%Y-%m-%d %H:%M:%S %Z')
        if dt:
            return dt.timestamp()*1000
        
    return 0
  

# S T A R T
# bail if subject doesn't match
if SUBJECT_PREFIX in emailmessage.subject:

  # loop through the message, starting at the 2nd comment section
  content = get_content()
  
  # collect all the data
  response, id_list_response, comments = get_response(content)
  
  if response is None:
    log.error("No response was recognized")
  
  # do not continue if all ids are not found
  if id_list_response.keys() != ID_PATTERN_LIST.keys():
    log.warn("This does not appear to be an approval email")
    log.warn(emailmessage.body.content)
    for k,v in id_list_response.items():
        log.warn(f"{k}:{v}")
  else:
    # get the expiration timeframe in millisec
    #id_list_response['expiration-ts'] = get_expiration_ts(id_list_response['expiration'])
    log.info(f"Finding incident {id_list_response.get('inc-id')}")
    # find the cooresponding incident
    found_incident = find_incident(id_list_response.get('inc-id'))
    if not found_incident:
      helper.fail(f"Unable to locate incident: {id_list_response.get('inc-id')}")

    # this populates the incident object
    log.info(f"Associating approval with incident: {id_list_response.get('inc-id')}")
    emailmessage.associateWithIncident(found_incident)
    
    # determine if msg id is the same
    if not is_valid_msg_id(incident, id_list_response):
      helper.fail(f"msg-id mismatch for incident: {id_list_response.get('inc-id')} {id_list_response}")
      
    # store the email in the email approval table
    row = incident.addRow('email_approval_process')
    row['date'] = int(emailmessage.sent_date)
     # determine if the expiration value has expired
    if int(id_list_response.get('expiration-ts')) != 0 and int(id_list_response.get('expiration-ts')) < int(time.time()*1000):
      row['status'] = 'Expired'
    elif response:
      row['status'] = 'Approved'
    elif response is None:
      row['status'] = 'Unknown'
    else:
      row['status'] = 'Denied'

    row['recipients'] = f"To: {emailmessage.to[0].get('address')}\nFrom: {emailmessage.sender.get('address')}"
    row['comments'] = "\n".join(comments)
    row['message_id'] = id_list_response.get('msg-id')
    row['expiration'] = int(id_list_response.get('expiration-ts'))
    row['task_id'] = int(id_list_response.get('task-id'))
    row['task_name'] = id_list_response.get('task-name')
