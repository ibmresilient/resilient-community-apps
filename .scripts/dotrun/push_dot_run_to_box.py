from boxsdk import Client, JWTAuth
import os
import glob
import sys
import json
import logging


log = logging.getLogger(__name__)


def upload_run_file(config_file, result_dir):
    # ID of the "Resilient-integration.run upload" folder
    # Can be found here: https://ibm.box.com/v/resilient-int-run-file
    folder_id = "64205016338"

    with open(config_file) as f:
        config_content = f.read()
        config_dict = json.loads(config_content)

        # Authenticate and create client
        sdk = JWTAuth.from_settings_dictionary(config_dict)
        client = Client(sdk)

        run_file_list = glob.glob(os.path.dirname(os.path.realpath(__file__)) +
                                  "/{}/resilient-circuits_*.run".format(result_dir))
        # List will only contain one item so choose the first item
        client.folder(folder_id).upload(run_file_list[0])

        file_path_list = run_file_list[0].split('/')
        log.info("{} file uploaded to Box".format(file_path_list[-1]))


if __name__ == '__main__':
    # Pass config file and result directory
    upload_run_file(sys.argv[1], sys.argv[2])
