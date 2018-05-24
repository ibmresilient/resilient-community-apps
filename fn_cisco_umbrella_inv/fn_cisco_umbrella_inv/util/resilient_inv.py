# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Investigate class for Resilient circuits Functions supporting Cisco Umbrella Investigate """

from __future__ import print_function
try:
    from urllib.parse import urljoin
except:
    from urlparse import urljoin
import logging
import datetime, time
import json
import sys
from investigate import Investigate

log = logging.getLogger(__name__)

class DATETIME_ERR(ValueError):
    def __init__(self, value):
        self.err_msg = value

    def __str__(self):
        return repr(self.err_msg)

class ResilientInv(Investigate):
    """ Extend base Investigate Class to add support for unsupported and buggy methods.

    """
    def __init__(self, api_key, base_url, proxies={}):
        """ New initialization parameters added.

        :param api_key: Thw api_kewy value from config.
        :param base_url: The base_url value from config.

        """
        super(ResilientInv, self).__init__(api_key, proxies)

        # If python version 2 convert existing uris to unicode object instead of string.
        if sys.version_info.major == 2:
            for k, v in self._uris.items():
                self._uris[k] = v.decode('unicode-escape')

        # Extend _uris dict of Investigate instance.
        self._uris.update({
            "categories": u"domains/categories/",
            "timeline":  u"timeline/{}",
            "classifiers_classifiers": u"url/{}/classifiers",
            "classifiers_info": u"url/{}/info",
            "domain_volume": u"domains/volume/{}",
            "sample_behaviors": u"sample/{}/behaviors"
        })
        # Over-ride Investigate BASE_URL class attribute with version
        # from config file.
        setattr(Investigate, "BASE_URL", base_url)

    @staticmethod
    def _process_datetime(dt, type):
        """Process datetime parameters for start and stop.

        :param dt: The datetime value from Function parameter.
        :param type: Type of dt (stop or start).
        :return dt: Updated datetime.

        """
        if dt is None:
            dt = datetime.timedelta(days=30)

        if isinstance(dt, datetime.timedelta):
            dt = int(time.mktime((datetime.datetime.utcnow() - dt).timetuple()) * 1000)
        elif isinstance(dt, datetime.datetime):
            dt = int(time.mktime(dt.timetuple()) * 1000)
        else:
            raise DATETIME_ERR("{} argument must be a datetime or a timedelta".format(type))

        return dt

    def categories(self):
        """Get the category map for domain status and categorization.

        For more detail, see https://docs.umbrella.com/developer/investigate-api/domain-status-and-categorization-1/

        :param: None.
        :return Result in json format.

        """
        uri = self._uris["categories"]
        return self.get_parse(uri)

    def _get_categorization(self, domain, labels):
        """ Over-ride base method because not working for showLabels.

        For more detail, see https://docs.umbrella.com/developer/investigate-api/domain-status-and-categorization-1/

        :param domain: Domain name parameter.
        :param labels: Optional parameter.
        :return Result in json format.

        """
        uri = urljoin(self._uris['categorization'], domain)
        params = {'showLabels': ''} if labels else {}
        return self.get_parse(uri, params)

    def _post_categorization(self, domains, labels):
        """ Over-ride base method because not working for showLabels.

        For more detail, see https://docs.umbrella.com/developer/investigate-api/domain-status-and-categorization-1/

        :param domain: Domain name parameter.
        :param labels: Optional parameter.
        :return Result in json format.

        """
        params = {'showLabels': ''} if labels else {}
        return self.post_parse(self._uris['categorization'], params,
            json.dumps(domains)
        )

    def timeline(self, resource):
        """Get the timeline Information for the given domain, ip or url.

        :param resource: The resource name parameter (domain, ip address or url).
        :return Result in json format.

        For details, see https://docs.umbrella.com/developer/investigate-api/timeline/
        """
        uri = self._uris["timeline"].format(resource)
        return self.get_parse(uri)

    def classifiers_classifiers(self, domain):
        """Get the Classifiers classifiers Information for the given domain.

        For details, see https://docs.umbrella.com/developer/investigate-api/timeline/

        :param domain: Domain name parameter.
        :return Result in json format.

        """
        uri = self._uris["classifiers_classifiers"].format(domain)
        return self.get_parse(uri)

    def classifiers_info(self, domain):
        """Get the Classifiers info Information for the given domain.

        For details, see https://docs.umbrella.com/developer/investigate-api/timeline/

        :param domain: Domain name parameter.
        :return Result in json format.

        """
        uri = self._uris["classifiers_info"].format(domain)
        return self.get_parse(uri)

    def domain_volume(self, domain, start=None, stop=None, match=None):
        """Get the Domain volume.

        For details, see https://investigate-api.readme.io/docs/domain-volume

        :param domain: Domain name parameter.
        :param start: Optional parameter.
        :param stop: Optional parameter.
        :param match: Optional parameter.
        :return Result in json format.

        """
        params = dict()

        start = self._process_datetime(start, "start")
        stop = self._process_datetime(stop, "stop")

        if stop <= start:
            raise DATETIME_ERR("The {} parameter must be great than the {} parameter".format("stop", "start"))
        else:
            params['start'] = start
            params['stop'] = stop

        if match is not None and isinstance(match, str):
            params['match'] = match

        uri = self._uris["domain_volume"].format(domain)

        return self.get_parse(uri, params)

    def ns_whois(self, nameservers, limit=None, offset=None, sort_field=None):
        """ Gets the domains that have been registered with a nameserver or nameservers.

        Over-ride base method because not working for nameServerList.

        :param nameserver: The nameserver(s) parameter as string or list.
        :param limit: Optional parameter.
        :param offset: Optional parameter.
        :param sort_field: Optional parameter.
        :return Result in json format.

        """
        if not isinstance(nameservers, list):
            uri = self._uris["whois_ns"].format(nameservers)
            params = {'limit': limit, 'offset': offset, 'sortField': sort_field}
        else:
            uri = self._uris["whois_ns"].format('')
            params = {'nameServerList' : ','.join(nameservers), 'limit': limit, 'offset': offset, 'sortField': sort_field}

        resp_json = self.get_parse(uri, params=params)
        return resp_json

    def sample_behaviors(self, hash, limit=None, offset=None):
        """Return an object representing behaviours associated with an input hash

        For details, see https://investigate-api.readme.io/docs/threat-grid-integration-cisco-amp-threat-grid

        :param hash: The hash value parameter (md5, sha1, sha256).
        :param limit: Optional parameter.
        :param offset: Optional parameter.
        :return Result in json format.

        """

        uri = self._uris['sample_behaviors'].format(hash)
        params = {'limit': limit, 'offset': offset}

        return self.get_parse(uri, params)