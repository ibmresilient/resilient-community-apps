"""
Example script to auto-create custom fields, actions, and message destinations.
"""

import configparser
import co3 as resilient
import logging

LOG = logging.getLogger(__name__)


def get_queue_id(res_client, queue_name):
    """Returns the id of the queue_name in the res_client instance"""
    message_dest_dict = res_client.get('/message_destinations')
    for message_dest in message_dest_dict['entities']:
        if message_dest['programmatic_name'] == queue_name:
            return message_dest['id']
    return -1


def create_table(resilient_client):
    """Creates a table call Task History"""
    # Create a new table
    data_table = {"type_id": 8,
                  "display_name": "Task History",
                  "type_name": "task_history",
                  "parent_types": ["incident"],
                  "fields": {"task_name": {"hide_notification": False,
                                           "values": [],
                                           "text": "Task Name",
                                           "required": None,
                                           "chosen": False,
                                           "blank_option": False,
                                           "input_type": "text",
                                           "name": "task_name",
                                           "tooltip": "Task Name",
                                           "placeholder": "task name",
                                           "order": 0},
                             "task_notes": {"hide_notification": False,
                                            "values": [],
                                            "text": "task_notes",
                                            "required": None,
                                            "chosen": False,
                                            "blank_option": False,
                                            "input_type": "text",
                                            "name": "task_notes",
                                            "tooltip": "Task Notes",
                                            "placeholder": "task changed",
                                            "order": 1},
                             "init_date": {"hide_notification": False,
                                           "values": [],
                                           "text": "Init Date",
                                           "required": None,
                                           "chosen": True,
                                           "blank_option": True,
                                           "input_type": "datetimepicker",
                                           "name": "init_date",
                                           "tooltip": "Task creation date",
                                           "placeholder": "init date",
                                           "order": 2},
                             "closed_date": {"hide_notification": False,
                                             "values": [],
                                             "text": "Closed Date",
                                             "required": None,
                                             "chosen": True,
                                             "blank_option": True,
                                             "input_type": "datetimepicker",
                                             "name": "closed_date",
                                             "tooltip": "Task close date",
                                             "placeholder": "closed date",
                                             "order": 3},
                             "time_to_close": {"hide_notification": False,
                                               "values": [],
                                               "text": "Time to Close",
                                               "required": None,
                                               "chosen": False,
                                               "blank_option": False,
                                               "input_type": "text",
                                               "name": "time_to_close",
                                               "tooltip": "Time taken to close",
                                               "placeholder": "time to close",
                                               "order": 4},
                             "task_id":  {"hide_notification": False,
                                          "values":  [],
                                          "text": "Task ID",
                                          "required": None,
                                          "chosen": False,
                                          "blank_option": True,
                                          "input_type": "text",
                                          "name": "task_id",
                                          "tooltip": "The task ID",
                                          "placeholder": "task ID",
                                          "order": 5}}}
    resilient_client.post('/types', data_table)


def create_message_destination(resilient_client, credentials):
    """Creates a new message destination"""
    # Create a new message destination with the name as defined in the config
    LOG.info("Creating new message destination...")
    users = resilient_client.get('/users')
    queuereaderid = ""
    for user in users:
        if user['email'] == credentials['queue_reader_email']:
            queuereaderid = user['id']
            print(queuereaderid)
    message_destination = {"programmatic_name": credentials["queue_prog_name"],
                           "name": credentials["queue_name"],
                           "expect_ack": True,
                           "destination_type": 0,
                           "users": [queuereaderid]}
    resilient_client.post("/message_destinations", message_destination)


def create_automatic_action(resilient_client, credentials):
    """Creates an automatic action assigned to the user in the config file"""
    # Create automatic action that triggers whenever the task is changed from
    # active to closed or vice-versa. This automatic action will be
    # pointed at the message destination we just created earlier.
    LOG.info("Creating new action...")
    LOG.info("Pointing action at message destination...")
    queue_id = get_queue_id(resilient_client, credentials["queue_name"])
    automatic_action = {"object_type": 1,
                        "name": credentials['action_name'],
                        "message_destinations": [queue_id],
                        "conditions": [{"method": "changed",
                                       "field_name": "task.status"}]
                        }
    resilient_client.post("/actions", automatic_action)


def setup():
    """Logs into resilient and posts necessary fields/actions/message queues"""
    # Import login credentials from config file
    LOG.info("Reading config file...")
    config = configparser.ConfigParser()
    config.read("setup.config")
    credentials = config["setup_credentials"]
    # Set whether on not to verify cert
    verify_cert = True
    if credentials["verify"] == "False":
        verify_cert = False

    # Login to resilient
    LOG.info("Logging in to Resilient...")
    resilient_client = resilient.SimpleClient(credentials["org_name"],
                                              credentials["address"],
                                              verify=verify_cert)
    resilient_client.connect(credentials["username"], credentials["password"])

    # Create table
    create_table(resilient_client)
    # Create message destination
    create_message_destination(resilient_client, credentials)
    # Create automatic action with the specified user in the setup.config file
    create_automatic_action(resilient_client, credentials)


if __name__ == "__main__":
    setup()
