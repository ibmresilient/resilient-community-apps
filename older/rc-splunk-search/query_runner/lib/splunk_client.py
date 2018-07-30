# -*- coding: utf-8 -*-
"""# A simple client for the Splunk SIEM"""

import requests
import urllib
import ssl
import base64
import time
import tempfile
import csv
from datetime import datetime
import splunklib.client as splunk
import splunklib.results as results
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

import logging

import sys
if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf-8')

LOG = logging.getLogger(__name__)

# For details of the Splunk API, see:
# <>

EVENT_FIELDS = ["*"]

# The default set of fields we want from an offense
OFFENSE_FIELDS = ["id",
                  "status",
                  "start_time",
                  "description",
                  "offense_type",
                  "offense_source",
                  "magnitude",
                  "source_network",
                  "destination_networks",
                  "categories",
                  "event_count",
                  "assigned_to"]

class TLSHttpAdapter(HTTPAdapter):
    """Adapter that ensures that we use best-available TLS version."""
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       assert_hostname=False,
                                       ssl_version=ssl.PROTOCOL_SSLv23)


class SimpleHTTPException(Exception):
    """Exception for HTTP errors."""
    def __init__(self, response):
        """
        Args:
          response - the Response object from the get/put/etc.
        """
        super(SimpleHTTPException, self).__init__("{0}".format(response.text))
        LOG.error("SimpleHTTPException %s", response.status_code)
        self.response = response


def _raise_if_error(response):
    """raise error for failed GET request"""
    if response.status_code != 200:
        raise SimpleHTTPException(response)


def _raise_if_posterror(response):
    """raise error for failed POST request"""
    if response.status_code not in [200, 201]:
        raise SimpleHTTPException(response)


class SplunkClient(object):
    """A simple client class wrapper for Splunk"""

    def __init__(self, host, port, username, password):
        # Set up connection to Splunk services
        self.splunk_service = splunk.connect(host=host,
                                             port=port,
                                             username=username,
                                             password=password)

    def search(self, query, max_results=None, job_ttl=None):
        """Start a search in splunk"""

        # Create the job
        query_args = {"search_mode": "normal",
                      "enable_lookups": True}

        if max_results:
            query_args["max_count"] = max_results

        job = None
        try:
            job = self.splunk_service.jobs.create(query, **query_args)
            if job_ttl:
                job.set_ttl(job_ttl)
        except Exception as e:
            LOG.exception("Search job creation failed")

        return job
    # end search


    @staticmethod
    def search_complete(job):
        """Return True if search job has finished, else False"""
        job.refresh()
        return job["dispatchState"] in ("FAILED", "DONE")

    @staticmethod
    def write_results(job):
        """Writes results to a tempfile"""
        reader = results.ResultsReader(job.results())
        temp_filename = ""

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_filename = temp_file.name
            writer = None
            for result in reader:
                if isinstance(result, dict):
                    if not writer:
                        writer = csv.DictWriter(temp_file, fieldnames=result.keys(), dialect='excel')
                        writer.writeheader()
                    writer.writerow(result)
        return temp_filename
    #end write_results

    @staticmethod
    def get_results(job, limit):
        """Return a collection of results"""
        reader = results.ResultsReader(job.results(count=limit))
        return {"results": [row for row in reader]}
    #end get_results

    @staticmethod
    def cancel_search(job):
        """Cancel a search job"""
        job.cancel()



def test():
    """Some tests"""
    client = SplunkClient("https://localhost", 8089, "admin", "Pass4Admin")

    query_string = ""
    client.search(query_string)

if __name__ == "__main__":
    test()
