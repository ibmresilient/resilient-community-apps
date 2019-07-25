# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

import requests
import json
from requests.auth import HTTPBasicAuth
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError


def get_threat_list(options, lastupdate, bundle):
    base_url = options['base_url']
    username = options['username']
    password = options['password']
    basic_auth = HTTPBasicAuth(username, password)
    url = '{0}/siem/all?format=JSON'.format(base_url, lastupdate)
    if type(lastupdate) is str:
        url += '&sinceTime={}'.format(lastupdate)
    else:
        if lastupdate is None:
            # first run, fetch for time span equivalent to polling interval
            lastupdate = int(options['polling_interval']) * 60
        url += '&sinceSeconds={}'.format(lastupdate)

    try:
        res = requests.get(url, auth=basic_auth, verify=bundle)

        res.raise_for_status()

        if res.status_code == 200:
            data = json.loads(res.text)
            return data
        else:
            return {'error': 'request to {0} failed with code {1}'.format(url, res.status_code)}

    except requests.exceptions.Timeout:
        return {'error': 'request to {0} timed out'.format(url)}

    except requests.exceptions.TooManyRedirects:
        return {'error': 'URL redirection loop?'}

    except requests.exceptions.HTTPError as err:
        if err.response.content is not None:
            try:
                custom_error_content = json.loads(err.response.content)
            except JSONDecodeError:
                return {'error': 'JSON decode error {}'.format(err)}
            return custom_error_content
        return {'error': 'HTTP error {}'.format(err)}

    except requests.exceptions.RequestException as ex:
        return {'error': 'request exception {}'.format(ex)}
