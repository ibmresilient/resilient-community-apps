from boxsdk import Client, JWTAuth
import os
import glob
import sys
import json
import logging


log = logging.getLogger(__name__)


def upload_run_file(config):

    # ID of the "Resilient-integration.run upload" folder
    # Can be found here: https://ibm.box.com/v/resilient-int-run-file
    folder_id = "64205016338"

    # Convert config to a dict
    config_dict = json.loads(config)

    # Authenticate and create client
    sdk = JWTAuth.from_settings_dictionary(config_dict)
    client = Client(sdk)

    run_file_list = glob.glob(os.path.dirname(os.path.realpath(__file__)) + "/result/resilient-circuits_*.run")
    # List will only contain one item so choose the first item
    client.folder(folder_id).upload(run_file_list[0])

    file_path_list = run_file_list[0].split('/')
    log.info("{} file uploaded to Box".format(file_path_list[-1]))


if __name__ == '__main__':
    upload_run_file(sys.argv[1])
