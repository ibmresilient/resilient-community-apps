# Copyright IBM Corp. - Confidential Information

import base64
import requests
import logging
import json
import tempfile
import shutil
import time
from resilient_circuits import FunctionError
import configparser
import io
from fn_mcafee_atd.util.config import config_section_data

log = logging.getLogger(__name__)


def check_config(opts):
    # Read from default config file
    buf = io.StringIO(config_section_data())
    parser = configparser.RawConfigParser(allow_no_value=True)
    parser.read_file(buf)
    default_config = dict(parser.items("fn_mcafee_atd"))

    options = opts.get("fn_mcafee_atd", {})
    if options == {}:
        log.error("There is no [fn_mcafee_atd] section in the config file, "
                  "please set that by running resilient-circuits config -u")
        raise ValueError("[fn_mcafee_atd] section is not set in the config file")
    else:
        atd_url = options.get("atd_url")
        atd_username = options.get("atd_username")
        atd_password = options.get("atd_password")
        timeout_mins = int(options.get("timeout", 30))
        polling_interval = int(options.get("polling_interval", 60))
        filePriority = options.get("filePriority", "add_to_q")
        trust_cert = options.get("trust_cert")

        if atd_url is None:
            log.error("atd_url is not set. You must set this value to run this function")
            raise ValueError("atd_url is not set. You must set this value to run this function")
        elif atd_url == default_config["atd_url"]:
            log.error("atd_url is still the default value, this must be changed to run this function")
            raise ValueError("atd_url is still the default value, this must be changed to run this function")

        if atd_username is None:
            log.error("atd_username is not set. You must set this value to run this function")
            raise ValueError("atd_username is not set. You must set this value to run this function")
        elif atd_username == default_config["atd_username"]:
            log.error("atd_username is still the default value, this must be changed to run this function")
            raise ValueError("atd_username is still the default value, this must be changed to run this function")

        if atd_password is None:
            log.error("atd_password is not set. You must set this value to run this function")
            raise ValueError("atd_password is not set. You must set this value to run this function")
        elif atd_password == default_config["atd_password"]:
            log.error("atd_password is still the default value, this must be changed to run this function")
            raise ValueError("atd_password is still the default value, this must be changed to run this function")

        if trust_cert != "True" and trust_cert != "False":
            log.error("trust_cert is not set correctly, please set to True or False to run this function")
            raise ValueError("trust_cert is not set correctly, please set to True or False to run this function")
        else:
            if trust_cert == "True":
                trust_cert = True
            else:
                trust_cert = False

        ret_dict = {
            "atd_url": atd_url,
            "atd_username": atd_username,
            "atd_password": atd_password,
            "timeout_mins": timeout_mins,
            "polling_interval": polling_interval,
            "filePriority": filePriority,
            "trust_cert": trust_cert
        }
        return ret_dict


def _get_atd_session_headers(g):
    login_string = "{}:{}".format(g.atd_username, g.atd_password)
    base64_login = base64.b64encode(str.encode(login_string))
    session_url = "{}/php/session.php".format(g.atd_url)

    headers = {
        "Accept": "application/vnd.ve.v1.0+json",
        "Content-Type": "application/json",
        "VE-SDK-API": base64_login
    }
    r = requests.get(session_url, headers=headers, verify=g.trust_cert)
    try:
        check_status_code(r)
    log.debug("User logged in successfully")
    content = r.json()
    session_string = "{}:{}".format(content["results"]["session"], content["results"]["userId"])
    base64_session = base64.b64encode(str.encode(session_string))

    session_headers = {
        "Accept": "application/vnd.ve.v1.0+json",
        "VE-SDK-API": base64_session
    }

    return session_headers


def _file_upload(g, submit_type, f=None, file_name=None, url=""):
    file_upload_url = "{}/php/fileupload.php".format(g.atd_url)

    data_dict = {
            "data": {
                "submitType": submit_type,
                "url": url
            },
            "filePriorityQ": g.filePriority
        }
    data_dict = json.dumps(data_dict)
    post_data = {'data': data_dict}

    response = None
    headers = _get_atd_session_headers(g)

    if f is not None:
        files = {'amas_filename': (file_name, f)}
        response = requests.post(file_upload_url, post_data, files=files, headers=headers,
                                 verify=g.trust_cert)
        log.debug("File submitted")
    elif url != "":
        response = requests.post(file_upload_url, post_data, headers=headers, verify=g.trust_cert)
        log.debug("url submitted")
    else:
        raise ValueError("Either file or url must be set")

    check_status_code(response)
    atd_logout(g.atd_url, headers, g.trust_cert)

    return response


def check_status_code(response):
    log.debug(response.content)
    if response.status_code > 299 or response.status_code < 200:
        if response.status_code == 401:
            log.error("Request refused, consider McAfee latency")
        raise ValueError("Request not successful. Status code: {}".format(str(response.status_code)))


def create_report_file(name, type):
    temp_d = tempfile.mkdtemp("tmp")
    temp_f = tempfile.mkstemp(dir=temp_d)
    report_file = temp_f[1]

    # If it is a URL change certain characters as file names won't be uploaded correctly
    for c in [":", "/", "https", "http"]:
        if name.find(c) > -1:
            name = name.replace(c, '')
    report_file_name = "McAfeeATD_{}.{}".format(name, type)
    file_location = {
        "report_file_name": report_file_name,
        "report_file": report_file,
        "tmp_dir": temp_d
    }

    return file_location


def remove_dir(dir):
    shutil.rmtree(dir)
    log.debug("Tmp directory removed")


def submit_file(g, f, file_name):
    # Submit type = regular file upload
    return _file_upload(g, '0', f=f, file_name=file_name)


def submit_url(g, url, submit_type=None):
    # Submit url to atd
    return _file_upload(g, submit_type, url=url)


def get_task_id_list(g, jobId):
    headers = _get_atd_session_headers(g)
    try:
        task_list_url = "{}/php/getTaskIdList.php?jobId={}".format(g.atd_url, jobId)
        task_list_status = requests.get(task_list_url, headers=headers, verify=g.trust_cert)
        check_status_code(task_list_status)
        task_list_json = task_list_status.json()
        task_list_string = task_list_json["result"]["taskIdList"]
        return task_list_string.split(',')

    finally:
        atd_logout(g.atd_url, headers, g.trust_cert)


# A loop to check if the analysis for a job has completed - need to add handling for -1 which is failed analysis
def check_job_status(g, jobId):
    headers = _get_atd_session_headers(g)

    try:
        status_url = "{}/php/samplestatus.php?jobId={}".format(g.atd_url, jobId)
        submission_status = requests.get(status_url, headers=headers, verify=g.trust_cert)
        check_status_code(submission_status)
        submit_json = submission_status.json()
        if submit_json["status"] == -1:
            raise ValueError
        elif submit_json["status"] in [0, 2, 3]:
            return False
        elif submit_json["status"] == 5:
            return True
    finally:
        atd_logout(g.atd_url, headers, g.trust_cert)


# A loop to check if the analysis for a job has completed - need to add handling for -1 which is failed analysis
def check_task_status(g, taskId):
    headers = _get_atd_session_headers(g)

    try:
        status_url = "{}/php/samplestatus.php?iTaskId={}".format(g.atd_url, taskId)
        submission_status = requests.get(status_url, headers=headers, verify=g.trust_cert)
        log.debug(submission_status.content)
        check_status_code(submission_status)
        submit_json = submission_status.json()
        if submit_json['results']['istate'] == 4:
            log.debug("Waiting in queue")
            return False
        elif submit_json['results']['istate'] == 3:
            log.debug("Being analyzed")
            return False
        elif submit_json['results']['istate'] == 1:
            status = submit_json['results']['status']
            log.debug("ATD Analysis Status: {}".format(status))
            job_id = submit_json['results']['jobid']
            jobid_url = "{}/php/samplestatus.php?jobId={}".format(g.atd_url, job_id)
            res = requests.get(jobid_url, headers=headers, verify=g.trust_cert)
            res_json = res.json()
            log.debug("Task istate = 1, response is: {}".format(res_json))
            severity = res_json.get("severity")
            if severity < 0:
                log.error("Severity is {}".format(str(severity)))
                raise ValueError
            else:
                return True
        elif submit_json['results']['istate'] == 2:
            status = submit_json['results']['status']
            log.debug("ATD Analysis Status: {}".format(status))
            job_id = submit_json['results']['jobid']
            jobid_url = "{}/php/samplestatus.php?jobId={}".format(g.atd_url, job_id)
            res = requests.get(jobid_url, headers=headers, verify=g.trust_cert)
            res_json = res.json()
            log.debug("Task istate = 2, response is: {}".format(res_json))
            severity = res_json.get("severity")
            if severity < 0:
                log.error("Severity is {}".format(str(severity)))
                raise ValueError
            else:
                atd_logout(g.atd_url, headers, g.trust_cert)
                return True
        elif submit_json['results']['istate'] == -1:
            raise ValueError
    finally:
        atd_logout(g.atd_url, headers, g.trust_cert)


# Gets the report from ATD
def get_atd_report(g, taskId, report_type, report_file):
    headers = _get_atd_session_headers(g)
    url = "{}/php/showreport.php?iTaskId={}&iType={}"
    # Download pdf or html report if specified, otherwise just return JSON
    if report_type == "pdf" or report_type == "html":
        report_url = url.format(g.atd_url, taskId, report_type)
        response = requests.get(report_url, headers=headers, verify=g.trust_cert)
        check_status_code(response)

        content = response.content

        # Check if task does not have a report associated with it
        # Check for bytes, if not then check with string
        if isinstance(content, bytes):
            if b'Description: File type not supported' in content or \
                    b'Description: Report not available' in content:
                log.debug(content)
                log.info("No report available")
                return False
        else:
            if "Description: File type not supported" in content or \
                    "Description: Report not available" in content:
                log.debug(content)
                return False

        with open(report_file.get("report_file"), 'wb') as f:
            f.write(response.content)
            log.info("Saved ATD report")

    json_url = url.format(g.atd_url, taskId, "json")
    json_response = requests.get(json_url, headers=headers, verify=g.trust_cert)
    check_status_code(json_response)
    atd_logout(g.atd_url, headers, g.trust_cert)

    json_content = json_response.content

    # Check if task does not have a report associated with it
    # Check for bytes, if not then check with string
    if isinstance(json_content, bytes):
        if b'Description: File type not supported' in json_content or \
                b'Description: Report not available' in json_content:
            log.debug(json_content)
            return False
    else:
        if "Description: File type not supported" in json_content or \
                "Description: Report not available" in json_content:
            log.debug(json_content)
            return False

    return json_response.json()


# Logout of ATD session
def atd_logout(url, headers, cert):
    url = url + "/php/session.php"
    requests.delete(url, headers=headers, verify=cert)


def check_timeout(start, polling_interval, timeout):
    end = time.time()
    t = end - start
    if t >= timeout:
        raise FunctionError("Timeout limit reached")
    else:
        # Sleep is used to wait for the polling interval so ATD is not constantly getting checked if the
        # analysis is not complete
        time.sleep(polling_interval)
        return True


def get_incident_id(**kwargs):
    incident_id = kwargs.get("incident_id")
    if not incident_id:
        raise FunctionError("incident_id is required")
    else:
        return incident_id
