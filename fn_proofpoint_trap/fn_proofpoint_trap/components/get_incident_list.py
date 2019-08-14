# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

""" Helper functions for Resilient circuits Functions supporting ProofPoint TRAP """

import requests
import json
import datetime


def timestamp_minutes_ago(minutes):
    """
    Return ISO 8601 Timestamp of X minutes ago
    :param minutes:
    :return:
    """
    now = datetime.datetime.now()
    past = now - datetime.timedelta(minutes=minutes)
    return past.isoformat()


def get_incident_list(options, lastupdate, bundle):
    """
    Grab incident list from TRAP
    :param options: - Configuration Options pulled from app.config
    :param lastupdate: - Minutes since last update
    :param bundle: - Pass bundle options or False
    :return:
    """
    base_url = options['base_url']
    api_key = options['api_key']
    headers = {'Authorization': api_key }
    # TODO: Possibly break out into different STATEs
    params = {}
    url = '{0}/incidents'.format(base_url)
    if type(lastupdate) is int:
        params['created_after'] = timestamp_minutes_ago(lastupdate)
    else:
        if lastupdate is None:
            # first run, fetch all
            # TODO: Logger instead of print
            print("First Run in progress - this may take a while")

    try:
        res = requests.get(url, headers=headers, params=params, verify=bundle)

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
            except json.decoder.JSONDecodeError:
                return {'error': 'JSON decode error {}'.format(err)}
            return custom_error_content
        return {'error': 'HTTP error {}'.format(err)}

    except requests.exceptions.RequestException as ex:
        return {'error': 'request exception {}'.format(ex)}




