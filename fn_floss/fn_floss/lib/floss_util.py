# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
import os
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

def call_floss(str_floss_options, temp_file_binary):
    """Helper routine to get call Floss."""
    try:
        # Floss writes output to stdout so redirect stdout to temporary file.
        # Store stdout so we can restore when we are done.
        floss_call_complete = True
        save_stdout = sys.stdout
        with tempfile.NamedTemporaryFile('w+b', bufsize=0) as temp_file_strings:
            sys.stdout = temp_file_strings

            # Call Floss to extract strings from the file.
            # See floss documentation for other options you can pass to floss.
            # https://github.com/fireeye/flare-floss/blob/master/doc/usage.md
            # Create the list of commandline options to pass to floss main.
            list_floss_params = get_floss_params(str_floss_options, temp_file_binary.name.encode('utf-8'))

            # main.main is the actual call to Floss.
            # The flag floss_call_complete is a hack used to indicate whether the call to floss
            # actually completes.  If the commandline options passed into floss are invalid in some
            # cases it will call down to the python option parser library which will write an error message
            # to stderr and exit.  In this case there is no error raised and the function and workflow
            # do not terminate properly.
            floss_call_complete = False
            result_floss = main.main(list_floss_params)
            floss_call_complete = True

            # Floss returns 0 for success
            if result_floss != 0:
                raise RuntimeError("Error running Floss. Return code: {}".format(str(result_floss)))

            # Set read pointer to beginning of the file and make a list of strings
            temp_file_strings.seek(0)
            list_string = temp_file_strings.read().splitlines()
    except Exception as err:
        raise err
    finally:
        # Restore sys.output 
        sys.output = save_stdout
        # See comments above about the use of floss_call_complete flag. This raise will only be
        # executed if invalid commandline options are passed to floss.
        if floss_call_complete == False:
            raise RuntimeError("Error running Floss. Floss did not complete. Check input options are valid in app.config file.")

    return list_string
        


def extract_strings(str_options, data):
    """extract_strings_from_binary writes binary data to a file and calls get_strings to extract
       the encoded strings"""
    # Create a temporary file to write the binary data to.
    with tempfile.NamedTemporaryFile('w+b', bufsize=0, delete=False) as temp_file_binary:
        # Write binary data to a temporary file. Make sure to close the file here...this
        # code must work on Windows and on Windows the file cannot be opened a second time
        # While open.  Floss will open the file again to read the data, so close before
        # calling Floss.
        temp_file_binary.write(data)
        temp_file_binary.close()
        try:
            # Get the list of string from Floss.
            list_string = call_floss(str_options, temp_file_binary)
        except Exception as err:
            raise err
        finally:
            os.unlink(temp_file_binary.name)
    return list_string

