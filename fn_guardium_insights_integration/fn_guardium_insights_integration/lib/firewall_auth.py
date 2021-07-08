# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
import time

import requests
from requests import packages

from fn_guardium_insights_integration.util.constants import F_URL, F_LOGIN_URL

packages.urllib3.disable_warnings()


# noinspection StrFormat
def firewall_authenticate(bso_ip, bso_user, bso_password, log, cert=False):
    """
    A Method to Authenticate BSO firewall.
    :param bso_ip: Firewall IP Address/DNS
    :param bso_user: Firewall Auth User
    :param bso_password: Firewall Auth Password
    :param log: logger object
    :param cert: by default `False`, otherwise give certificate path if firewall needs SSL certificate.
    :return:
    """
    try:
        get_response = requests.get(F_URL.format(bso_ip=bso_ip), verify=cert)
        redirected_url = get_response.url
        redirected_ip_dns = redirected_url.split("/")[2].split(":")[0]
        if get_response.ok:
            if redirected_url.find("sid=") != -1:
                sid = redirected_url.split('=')[-1]
                log.debug(u"Firewall Redirected URL: {}, Session ID: {}".format(redirected_url, sid))
                res2 = requests.post(F_URL.format(bso_ip=redirected_ip_dns), data={"sid": sid, "login": "Log+In+Now"},
                                     verify=cert)
                if res2.ok:
                    try:
                        res3 = requests.post(F_LOGIN_URL.format(bso_ip=redirected_ip_dns),
                                             data={"sid": sid, "username": bso_user, "password": bso_password},
                                             verify=cert)
                        if res3.ok:
                            log.debug(res3.text)
                    except Exception:
                        log.debug(u"Firewall Authentication successful.")
                else:
                    log.debug(u"Error While logging to firewall: {} {}".format(res2.status_code, res2.reason))
            else:
                log.debug("Firewall is authenticating with second type authentication mechanism")
                _payload = "au_pxytimetag={}&uname={}&pwd={}&ok=OK".format(int(time.time()), bso_user, bso_password)
                _headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                try:
                    response = requests.post("https://{}/".format(redirected_ip_dns), headers=_headers, data=_payload,
                                             verify=cert)
                    log.debug(response.content)
                except Exception as er_msg:
                    log.debug("Firewall Authentication : {}".format(er_msg))
        else:
            log.debug(
                u"Error while connecting to firewall: {} {}".format(get_response.status_code, get_response.reason))
    except Exception as firwall_err:
        log.debug(u"Either Firewall is not reachable or Already authenticated. - {}".format(firwall_err))
