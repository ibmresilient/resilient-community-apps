# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

import logging
import requests
import json
import base64
import configparser
import io
from fn_mcafee_esm.util.config import config_section_data

log = logging.getLogger(__name__)


def check_config(options):
    # Read from default config file
    buf = io.StringIO(config_section_data())
    parser = configparser.RawConfigParser(allow_no_value=True)
    parser.read_file(buf)
    default_config = dict(parser.items("fn_mcafee_esm"))

    if options == {}:
        log.error("There is no [fn_mcafee_esm] section in the config file, "
                  "please set that by running resilient-circuits config -u")
        raise ValueError("[fn_mcafee_esm] section is not set in the config file")
    else:
        esm_url = options.get("esm_url")
        esm_username = options.get("esm_username")
        esm_password = options.get("esm_password")
        trust_cert = options.get("trust_cert")

        if esm_url is None:
            raise ValueError("esm_url is not set. You must set this value to run this function")
        elif esm_url == default_config["esm_url"]:
            raise ValueError("esm_url is still the default value, this must be changed to run this function")

        if esm_username is None:
            raise ValueError("esm_username is not set. You must set this value to run this function")
        elif esm_username == default_config["esm_username"]:
            raise ValueError("esm_username is still the default value, this must be changed to run this function")

        if esm_password is None:
            raise ValueError("esm_password is not set. You must set this value to run this function")
        elif esm_password == default_config["esm_password"]:
            raise ValueError("esm_password is still the default value, this must be changed to run this function")

        if trust_cert is None:
            raise ValueError("trust_cert is not set. You must set this value to run this function")
        elif trust_cert == default_config["trust_cert"]:
            raise ValueError("trust_cert is still the default value, this must be changed to run this function")
        if not trust_cert or trust_cert.lower() == "false":
            trust_cert = False
        else:
            trust_cert = True

        options["trust_cert"] = trust_cert
        return options


def check_status_code(status_code):
    if status_code > 299 or status_code < 200:
        raise ValueError("Request not successful")


def get_authenticated_headers(address, username, password, verify_cert=True):
    url = address + "/rs/esm/v2/login"
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    data = {
        "username": base64.b64encode(username),
        "password": base64.b64encode(password),
        "locale": "en_US"
    }
    data_string = json.dumps(data)
    r = requests.post(url, data=data_string, headers=headers, verify=verify_cert)
    check_status_code(r.status_code)

    cookies = r.cookies
    jwttoken = cookies.get("JWTToken")

    response_headers = r.headers
    xsrf_token = response_headers.get("Xsrf-Token")

    authenticated_headers = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "Cookie": "JWTToken=" + jwttoken,
        "X-Xsrf-Token": xsrf_token
    }

    return authenticated_headers


def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z
