# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
import sys
import tempfile
from floss import main


def get_binary_data_from_file(client, incident_id, task_id, artifact_id, attachment_id):
    """get_binary_data_from_file calls the REST API to get the attachment or artifact data"""

    if artifact_id and incident_id:
        data_uri = "/incidents/{}/artifacts/{}/contents".format(incident_id, artifact_id)
    elif attachment_id:
        if task_id:
            data_uri = "/tasks/{}/attachments/{}/contents".format(task_id, attachment_id)
        elif incident_id:
            data_uri = "/incidents/{}/attachments/{}/contents".format(incident_id, attachment_id)
        else:
            raise ValueError("task_id or incident_id must be specified with attachment")
    else:
        raise ValueError("artifact or attachment or incident id must be specified")

    # Get the data
    data = client.get_content(data_uri)

    return data

def get_floss_params(str_floss_options, filename):
    """Helper routine to build the list of commandline parameters to pass to Floss."""
    # First parameter is the name of the Floss "main" routine.
    list_floss_params = ['main']

    # Add the options from app.config
    list_options = str_floss_options.split(",")
    for option in list_options:
        list_floss_params.append(option)

    # Add the filename of the binary file.
    list_floss_params.append(filename)
    return list_floss_params

def call_floss(str_floss_options, temp_file_binary, temp_file_strings):
    """Helper routine to get call Floss."""
    # Floss writes output to stdout so redirect stdout to temporary file
    try:
        save_stdout = sys.stdout
        with open(temp_file_strings.name.encode('utf-8'), 'w') as output_stream:
            sys.stdout = temp_file_strings

            # Call Floss to extract strings from the file.
            # See floss documentation for other options you can pass to floss.
            # https://github.com/fireeye/flare-floss/blob/master/doc/usage.md
            # Create the list of commandline options to pass to floss main.
            list_floss_params = get_floss_params(str_floss_options, temp_file_binary.name.encode('utf-8'))

            # This is the actual call to Floss.
            result_floss = main.main(list_floss_params)

        if result_floss != 0:
            raise RuntimeError("Error running Floss. Return code: {}".format(str(result_floss)))
    except Exception as err:
        raise err
    finally:
        sys.output = save_stdout

    list_string = []

    # Read the output from floss and make a list of the decoded strings
    try:
        with open(temp_file_strings.name, "r") as floss_output:
            list_string = floss_output.read().splitlines()
    except Exception as err:
        raise err

    return list_string
        


def extract_strings(str_options, data):
    """extract_strings_from_binary writes binary data to a file and calls get_strings to extract
       the encoded strings"""
    list_string = []
    try:
        with tempfile.NamedTemporaryFile('w', bufsize=0) as temp_file_binary:

            # Write binary data to a temporary file.
            temp_file_binary.write(data)
            with tempfile.NamedTemporaryFile(bufsize=0) as temp_file_strings:
                # Get the list of string from Floss.
                list_string = call_floss(str_options, temp_file_binary, temp_file_strings)
    except Exception as err:
        raise err

    return list_string

