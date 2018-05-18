# Copyright IBM Corp. - Confidential Information

import base64
import requests
import logging
import json
import tempfile
import shutil

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
    check_status_code(r)
    log.debug("User logged in successfully")
    content = r.json()
    session_string = "{}:{}".format(content["results"]["session"], content["results"]["userId"])
    base64_session = base64.b64encode(session_string)

    session_headers = {
        "Accept": "application/vnd.ve.v1.0+json",
        "VE-SDK-API": base64_session
    }

    return session_headers


def _file_upload(g, submit_type, f=None, file_name=None, url=""):
    file_upload_url = "{}/php/fileupload.php".format(g.atd_url)

    data_dict = {
            "data": {
                "vmProfileList": g.vm_profile_list,
                "submitType": submit_type,
                "url": url
            },
            "filePriorityQ": g.filePriority
        }
    data_dict = json.dumps(data_dict)
    post_data = {'data': data_dict}

    response = None
    if f is not None:
        files = {'amas_filename': (file_name, f)}
        response = requests.post(file_upload_url, post_data, files=files, headers=_get_atd_session_headers(g),
                                 verify=g.trust_cert)
        log.debug("File submitted")
    elif url != "":
        response = requests.post(file_upload_url, post_data, headers=_get_atd_session_headers(g), verify=g.trust_cert)
        log.debug("url submitted")
    else:
        raise ValueError("Either file or url must be set")

    check_status_code(response)
    return response


def _check_url_ending(url):
    file_endings = [
        ".aif", ".cda", ".mid", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl", ".7z", ".arj", ".deb", ".pkg", ".rar",
        ".rpm", ".tar.gz", ".z", ".zip", ".bin", ".dmg", ".iso", ".toast", ".vcd", ".csv", ".dat", ".db", ".dbf",
        ".log", ".mdb", ".sav", ".sql", ".tar", ".xml", ".apk", ".bat", ".jar", ".cgi", ".com", ".exe", ".gadget",
        ".py", ".wsf", ".fnt", ".fon", ".otf", ".ttf", ".ai", ".bmp", ".gif", ".ico", ".jpeg", ".png", ".ps", ".psd",
        ".svg", ".tif", ".tiff", ".asp", ".part", ".cer", ".cfm", ".css", ".key", ".odp", ".pps", ".ppt", ".pptx", ".c",
        ".class", ".cpp", ".cs", ".h", ".java", ".sh", ".swift", ".vb", ".ods", ".xlr", ".xls", ".xlsx", ".bak", ".cab",
        ".cgf", ".cur", ".dll", ".dmp", ".drv", ".icns", ".ini", ".lnk", ".msi", ".sys", ".tmp", ".3g2", ".3gp", ".avi",
        ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv", ".doc",
        ".docx", ".odt", ".pdf", ".rtf", ".tex", ".txt", ".wks", ".wps", ".wpd"
    ]
    e = url.rfind('.')
    potential_file_ending = url[e:]
    # Per the McAfee documentation, 3 is used if the URL includes a file to download, while 1 is used to just analyze
    # a URL
    if potential_file_ending.lower() in file_endings:
        return '3'
    else:
        return '1'


def check_status_code(response):
    if response.status_code > 299 or response.status_code < 200:
        raise ValueError("Request not successful")


def create_report_file(name, type):
    temp_d = tempfile.mkdtemp("tmp")
    temp_f = tempfile.mkstemp(dir=temp_d)
    report_file = temp_f[1]

    # If it is a URL change certain characters as file names won't be uploaded correctly
    for c in [":", "/", "http", "https"]:
        if name.find(c) > -1:
            name = name.replace(c, '')
    report_file_name = "{}_report.{}".format(name, type)
    file_location = {
        "report_file_name": report_file_name,
        "report_file": report_file,
        "tmp_dir": temp_d
    }

    return file_location


def remove_dir(dir):
    shutil.rmtree(dir)


def submit_file(g, f, file_name):
    # Submit type = regular file upload
    return _file_upload(g, '0', f=f, file_name=file_name)


def submit_url(g, url, submit_type=None):
    if submit_type is not None:
        return _file_upload(g, submit_type, url=url)
    else:
        return _file_upload(g, _check_url_ending(url), url=url)


# A loop to check if the analysis for a job has completed - need to add handling for -1 which is failed analysis
def check_atd_status(g, task_id):
    status_url = "{}/php/samplestatus.php?iTaskId={}".format(g.atd_url, task_id)
    submission_status = requests.get(status_url, headers=_get_atd_session_headers(g), verify=g.trust_cert)
    submit_json = submission_status.json()
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
    url = "{}/php/showreport.php?iTaskId={}&iType={}"
    # Download pdf or html report if specified, otherwise just return JSON
    if report_type == "pdf" or report_type == "html":
        report_url = url.format(g.atd_url, taskId, report_type)
        response = requests.get(report_url, headers=headers, verify=g.trust_cert)
        check_status_code(response)

        with open(report_file, 'wb') as f:
            f.write(response.content)
            log.info("Saved ATD report")

    json_url = url.format(g.atd_url, taskId, "json")
    json_response = requests.get(json_url, headers=headers, verify=g.trust_cert)
    check_status_code(json_response)

    return json_response.json()
