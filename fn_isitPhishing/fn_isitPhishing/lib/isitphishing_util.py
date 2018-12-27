import sys
import base64

def get_license_key(name, license):

    # Compute the base64 license key. This key will be provided to you by Vade Secure,
    # and has the following format: <CUSTOMER_NAME>:<CUSTOMER_LICENSE>.
    url_key = u'{0}:{1}'.format(name, license)

    # It must be Base64-encoded. Handled different on Python 2 vs 3.
    if sys.version_info[0] == 2:
        auth_token = base64.b64encode(bytes(url_key).encode("utf-8"))
    else:
        auth_token = base64.b64encode(bytes(url_key, 'ascii')).decode('ascii')
 
    return auth_token

def get_filename_attachment(client, incident_id, artifact_id, task_id, attachment_id):

    # return the filename of an attachment.
    if attachment_id:
        if task_id:
            metadata_uri = "/tasks/{0}/attachments/{1}".format(task_id, attachment_id)
        else:
            metadata_uri = "/incidents/{0}/attachments/{1}".format(incident_id, attachment_id)
    elif artifact_id:
        metadata_uri = "/incidents/{0}/artifacts/{1}".format(incident_id, artifact_id)
    else:
        raise ValueError("Attachment or Artifact id must be specified")


    metadata = client.get(metadata_uri)

    # Return the filename
    if attachment_id:
        return metadata["name"]
    elif artifact_id:
        return metadata["attachment"]["name"]