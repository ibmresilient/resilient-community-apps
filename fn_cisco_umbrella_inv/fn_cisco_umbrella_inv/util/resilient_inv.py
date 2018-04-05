# -*- coding: utf-8 -*-


from __future__ import print_function
import urlparse, urllib
import logging
import datetime, time
import re
import investigate

log = logging.getLogger(__name__)

class ResilientInv(investigate.Investigate):
    """ Extend base Investigate Class to add support for unsupported and buggy methods.

    """
    def __init__(self, api_key, proxies={}):
        super(ResilientInv, self).__init__(api_key, proxies)
        self._uris.update({
            "categories": "domains/categories/",
            "timeline":  "timeline/{}",
            "classifiers_classifiers": "url/{}/classifiers",
            "classifiers_info": "url/{}/info",
            "domain_volume": "domains/volume/{}"
        })

    def categories(self):
        '''Get the category map for domain status and categorization.

        For more detail, see https://docs.umbrella.com/developer/investigate-api/domain-status-and-categorization-1/
        '''
        uri = self._uris["categories"]
        return self.get_parse(uri)

    def _get_categorization(self, domain, labels):
        """ Over-ride base method because not working for showLabels.

        """
        uri = urlparse.urljoin(self._uris['categorization'], domain)
        params = {'showLabels': ''} if labels else {}
        return self.get_parse(uri, params)

    def timeline(self, resource):
        '''Get the timeline Information for the given domain, ip or url.

        For details, see https://docs.umbrella.com/developer/investigate-api/timeline/
        '''
        uri = self._uris["timeline"].format(resource)
        return self.get_parse(uri)

