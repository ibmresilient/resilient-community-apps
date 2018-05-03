import os
import base64
import requests
import logging
import json

log = logging.getLogger(__name__)


def _get_atd_session_headers(g):
    login_string = "{}:{}".format(g.atd_username, g.atd_password)
    base64_login = base64.b64encode(login_string)
    session_url = "{}/php/session.php".format(g.atd_url)

    headers = {
        "Accept": "application/vnd.ve.v1.0+json",
        "Content-Type": "application/json",
        "VE-SDK-API": base64_login
    }
    r = requests.get(session_url, headers=headers, verify=g.trust_cert)
    _check_status_code(r)
    log.debug("User logged in successfully")
    content = r.json()
    session_string = "{}:{}".format(content["results"]["session"], content["results"]["userId"])
    base64_session = base64.b64encode(session_string)

    session_headers = {
        "Accept": "application/vnd.ve.v1.0+json",
        # "Content-Type": "application/json",
        "VE-SDK-API": base64_session
    }

    return session_headers


def _file_upload(g, f, file_name, type):
    file_upload_url = "{}/php/fileupload.php".format(g.atd_url)

    data_dict = {
            "data": {
                "xMode": g.xMode,
                "overrideOS": g.overrideOS,
                "vmProfileList": g.vm_profile_list,
                "submitType": type
            },
            "filePriorityQ": g.filePriority
        }
    data_dict = json.dumps(data_dict)
    post_data = {'data': data_dict}

    files = {'amas_filename': (file_name, f)}

    response = requests.post(file_upload_url, post_data, files=files, headers=_get_atd_session_headers(g), verify=g.trust_cert)
    _check_status_code(response)

    return response


def _check_status_code(response):
    if response.status_code > 299 or response.status_code < 200:
        raise ValueError("Call was not successful")


def create_report_file(name):
    path = os.path.dirname(os.path.abspath(__file__))
    report_file_name = "{}_report.pdf".format(name)
    report_file = os.path.join(path, report_file_name)
    file_location = {
        "report_file_name": report_file_name,
        "report_file": report_file
    }

    return file_location


def remove_file(file_location):
    os.remove(file_location)


def submit_file(g, f, file_name):
    # Submit type = regular file upload
    return _file_upload(g, f, file_name, '0')


# A loop to check if the analysis for a job has completed - need to add handling for -1 which is failed analysis
def check_atd_status(g, task_id):
    status_url = "{}/php/samplestatus.php?iTaskId={}".format(g.atd_url, task_id)
    submission_status = requests.get(status_url, headers=_get_atd_session_headers(g), verify=g.trust_cert)
    submit_json = json.loads(submission_status.text)
    if submit_json['results']['istate'] == 4:
        return False
    elif submit_json['results']['istate'] == 3:
        return False
    elif submit_json['results']['istate'] == 1:
        log.debug("ATD Analysis Status: {}".format(submit_json['results']['status']))
        return True
    elif submit_json['results']['istate'] == 2:
        log.debug("ATD Analysis Status: {}".format(submit_json['results']['status']))
        return True


# Gets the report from ATD
def get_atd_report(g, taskId, report_type, report_file):
    headers = _get_atd_session_headers(g)
    report_url = "{}/php/showreport.php?iTaskId={}&iType={}".format(g.atd_url, taskId, report_type)
    response = requests.get(report_url, headers=headers, verify=g.trust_cert)
    _check_status_code(response)

    with open(report_file, 'wb') as f:
        f.write(response.content)
        log.info("Saved ATD report")
