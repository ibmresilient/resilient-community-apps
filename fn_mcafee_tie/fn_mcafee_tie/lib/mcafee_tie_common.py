# -*- coding: utf-8 -*-
# Copyright IBM Corp. 2010, 2020 - Confidential Information
# pragma pylint: disable=unused-argument, no-self-use

import logging
from dxlclient.client_config import DxlClientConfig
from dxlclient.client import DxlClient
from dxltieclient import TieClient
from dxltieclient.constants import HashType
from dxltieclient.callbacks import ReputationChangeCallback

LOG = logging.getLogger(__name__)
PACKAGE_NAME = "fn_mcafee_tie"
CONFIG_FILE = "dxlclient_config"

TRUST_LEVELS = {
    "Known Trusted Installed": 100,
    "Known Trusted": 99,
    "Most Likely Trusted": 85,
    "Might be Trusted": 70,
    "Unknown": 50,
    "Might be Malicious": 30,
    "Most Likely Malicious": 15,
    "Known Malicious": 1,
    "Not Set": 0
}

def get_trust_level_value(label):
    # determine if the trust level is a string encoded number
    try:
        return int(label)
    except ValueError:
        pass

    # try to find the value as a label
    if label in TRUST_LEVELS:
        return TRUST_LEVELS[label]

    raise ValueError("Trust Level not found: %s", label)

def get_mcafee_hash_type(hash_type):
    # convert resilient hash type information to mcafee hash type
    lookup = {
        HashType.MD5: ["md5"],
        HashType.SHA1: ["sha1", "sha-1"],
        HashType.SHA256: ["sha256", "sha-256"]
    }

    for mcafee_type, type_list in lookup.items():
        for type_item in type_list:
            if type_item in hash_type.lower():
                return mcafee_type

    return None

def get_mcafee_client(options):
    # Pass in the file containing the dxlclient configuration file to start communication
    try:
        config = options.get(CONFIG_FILE)
        if config is None:
            msg = "{} is not set. You must set this path to run this function".format(CONFIG_FILE)
            raise ValueError(msg)

        LOG.info("Using %s to create configuration for DxlClient", config)

        # Create configuration from file for DxlClient
        config = DxlClientConfig.create_dxl_config_from_file(config)
    except AttributeError:
        LOG.error("There is no [fn_mcafee_tie] section in the config file, "
                  "please set that by running resilient-circuits config -u")
        raise AttributeError("[fn_mcafee_tie] section is not set in the config file")

    return DxlClient(config)

def get_tie_client(client):
    # get TIE Connect client
    if not client.connected:
        client.connect()

    return TieClient(client)

class MyReputationChangeCallback(ReputationChangeCallback):
    """
    My reputation change callback. Used to populate information about the set file reputation action
    """
    def __init__(self):
        self.result = None

    def on_reputation_change(self, rep_change_dict, original_event):
        # return the result information into the class 'result' variable
        LOG.debug("Reputation change on topic: " + original_event.destination_topic)
        # Dump the dictionary
        LOG.debug(rep_change_dict)

        self.result = rep_change_dict
