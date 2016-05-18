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
        if message_dest['programmatic_name']==queue_name:
            return message_dest['id']
    return -1


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

    # Create a new message destination with the names defined in the config
    LOG.info("Creating new message destination...")
    message_destination={"programmatic_name": credentials["queue_prog_name"],
                         "name": credentials["queue_name"],
                         "expect_ack": True,
                         "destination_type": 0,
                         "users": []}
    resilient_client.post("/message_destinations", message_destination)

    # Create automatic action that triggers whenever the task is changed from
    # active to closed or vice-versa. This automatic action will be
    # pointed at the message destination we just created earlier.
    LOG.info("Creating new action...")
    LOG.info("Pointing action at message destination...")
    queue_id = get_queue_id(resilient_client, credentials["queue_name"])
    automatic_action={"object_type": 0,
                      "name": "Task Tracker",
                      "message_destinations": [queue_id],
                      "conditions":[{"method": "changed",
                                    "field_name": "task.active"
                                    }]
                      }
    resilient_client.post("/actions", automatic_action)

if __name__ == "__main__":
    setup()
