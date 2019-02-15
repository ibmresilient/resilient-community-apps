# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

from qradar_http_info import HttpInfo


class TacticsTokenError(Exception):
    """ Exception in getting csrf token"""
    def __init__(self, url, message):
        fail_msg = "Requests to url [{}] throws exception. Error [{}]".format(url, message)
        super(TacticsTokenError, self).__init__(fail_msg)


class GetAllMappingsError(Exception):
    """ Exception in getting all mappings from CFMA"""
    def __init__(self, url, message):
        fail_msg = "Requests to url [{}] throws exception. Error [{}]".format(url, message)
        super(GetAllMappingsError, self).__init__(fail_msg)


class QRadarCfmaClient(object):
    """
    QRadar Cyber Adversary Framework Mapping Client
    """
    def __init__(self, qradar_host, cfma_app_id, cfma_token, cafile, log):
        self.http_info = HttpInfo(qradar_host=qradar_host,
                                  advisor_app_id=cfma_app_id,
                                  qradar_token=cfma_token,
                                  cafile=cafile,
                                  log=log)
        self.log = log

    def get_tactics_token(self):
        """
        According to QRAW, there is no /about endpoint right now for getting the
        XSRF token. One walkaround is to use the /api/config/tuning endpoint
        to get the XSFR token.
        :return:
        """
        url = self.http_info.get_tuning_url()

        try:
            session = self.http_info.get_session()
            response = session.get(url=url,
                                   verify=self.http_info.get_cafile())
            #
            # The CSRF token is in the cookie. Add it to the
            # session header
            #
            if response.status_code == 200:
                self.http_info.update_session_tactics(session.cookies.get_dict())
            else:
                self.log.error("the about endpoint returns status {}".format(str(response.status_code)))
                raise TacticsTokenError(url, "Status {}".format(str(response.status_code)))
        except Exception as e:
            self.log.error("Get token failed with exception:")
            self.log.error(str(e))
            raise TacticsTokenError(url, e.message)

    def get_all_mapping(self):
        """
        Note this is only necessary by now since there is a QRAW bug that we
        can't look for mapping for a particular rule directly. We need to
        get all the mappings and then go through them one by one
        :return:
        """
        if not self.http_info.xsrf_token:
            self.get_tactics_token()

        url = self.http_info.get_all_mappings()
        session = self.http_info.get_session()

        try:
            response = session.get(url=url,
                                   data=None,
                                   verify=self.http_info.get_cafile())
            if response.status_code != 200:
                error_msg = "Offense insights using {} returns error {}".format(url, str(response))
                self.log.error(error_msg)
                raise GetAllMappingsError(url, error_msg)
        except Exception as e:
            self.log.error("Offense insights failed with exception:")
            self.log.error(str(e))
            raise GetAllMappingsError(url, e.message)

        return response.json()




