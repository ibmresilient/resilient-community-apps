# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Investigate class for Resilient circuits Functions supporting Cisco Umbrella Investigate """

from __future__ import print_function
import urlparse, urllib
import logging
import datetime, time
import re
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
        super(ResilientInv, self).__init__(api_key, proxies)
        # Extend _uris dict of Investigate instance.
        self._uris.update({
            "categories": "domains/categories/",
            "timeline":  "timeline/{}",
            "classifiers_classifiers": "url/{}/classifiers",
            "classifiers_info": "url/{}/info",
            "domain_volume": "domains/volume/{}",
            "sample_behaviors": "sample/{}/behaviors"
        })
        # Over-ride Investigate BASE_URL class attribute with version
        # from config file.
        setattr(Investigate, "BASE_URL", base_url)

    @staticmethod
    def _process_datetime(dt, type):
        """Process datetime parameters for start and stop.

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
        """
        uri = self._uris["categories"]
        return self.get_parse(uri)

    def _get_categorization(self, domain, labels):
        """ Over-ride base method because not working for showLabels.

        """
        uri = urlparse.urljoin(self._uris['categorization'], domain)
        params = {'showLabels': ''} if labels else {}
        return self.get_parse(uri, params)

    def timeline(self, resource):
        """Get the timeline Information for the given domain, ip or url.

        For details, see https://docs.umbrella.com/developer/investigate-api/timeline/
        """
        uri = self._uris["timeline"].format(resource)
        return self.get_parse(uri)

    def classifiers_classifiers(self, domain):
        """Get the Classifiers classifiers Information for the given domain.

        For details, see https://docs.umbrella.com/developer/investigate-api/timeline/
        """
        uri = self._uris["classifiers_classifiers"].format(domain)
        return self.get_parse(uri)

    def classifiers_info(self, domain):
        """Get the Classifiers info Information for the given domain.

        For details, see https://docs.umbrella.com/developer/investigate-api/timeline/
        """
        uri = self._uris["classifiers_info"].format(domain)
        return self.get_parse(uri)

    def domain_volume(self, domain, start=None, stop=None, match=None):
        """Get the Domain volume.

        For details, see https://investigate-api.readme.io/docs/domain-volume
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

        """

        uri = self._uris['sample_behaviors'].format(hash)
        params = {'limit': limit, 'offset': offset}

        return self.get_parse(uri, params)