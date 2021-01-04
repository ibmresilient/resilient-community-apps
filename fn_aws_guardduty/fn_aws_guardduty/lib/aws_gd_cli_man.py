# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" AWS GuardDuty client manager support class. """
import re
from  datetime import datetime
import logging
from sys import version_info
from resilient_lib import RequestsCommon
from resilient_lib import validate_fields
from fn_aws_guardduty.lib.aws_gd_client import AwsGdClient
from fn_aws_guardduty.lib.helpers import is_regex
import fn_aws_guardduty.util.config as config

LOG = logging.getLogger(__name__)


class AwsGdCliMan():
    """
    Client manager class for AWS GuardDuty.
    Creates a hash of client objects for accessible GuardDuty regions.
    """
    def __init__(self, opts=None, function_options=None):
        """
        Class constructor.
        """
        if not isinstance(opts, dict) and not opts:
            raise ValueError("The 'opts' parameter is not set correctly.")
        if not isinstance(function_options, dict) and not function_options:
            raise ValueError("The 'function_options' parameter is not set correctly.")

        validate_fields(config.REQUIRED_CONFIG_SETTINGS, function_options)

        self.opts = opts
        self.function_opts = function_options
        self.aws_gd_master_region = function_options.get("aws_gd_master_region")
        # Strip quotes from self.aws_gd_regions regex
        self.aws_gd_regions = function_options.get("aws_gd_regions").strip("'\"")
        # Test self.aws_gd_regions is a valid regex expression.
        self.proxies = RequestsCommon(opts, function_options).get_proxies()
        if not is_regex(self.aws_gd_regions):
            raise ValueError("The query filter '{}' is not a valid regular expression."
                             .format(repr(self.aws_gd_regions)))
        self._get_clients()

    def _get_clients(self):
        """ Create a hash of GuardDuty clients for accessible regions.

        :return clients: Hash of client objects.
        """
        self.timestamp = datetime.now()
        self.clients = {}

        if version_info.major < 3:
            regex = r'{}'.format(self.aws_gd_regions.encode('utf-8'))
        else:
            regex = r'{}'.format(self.aws_gd_regions)

        for region in [r for r in self.get_regions()
                       if re.search(regex, r, re.IGNORECASE)]:
            aws_gd = AwsGdClient(self.opts, self.function_opts, region=region)
            try:
                detectors = aws_gd.get("list_detectors")

            except aws_gd.gd.exceptions.ClientError as invalid_ex:
                if "The security token included in the request is invalid" in invalid_ex.__repr__():
                    LOG.warning("Invalid security token for region %s, Got exception: %s. "
                                "GuardDuty may need to be enabled for the user in the AWS region.",
                                region, str(invalid_ex))
                    continue
                raise invalid_ex

            self.clients.update({
                region: {
                    "client": aws_gd,
                    "detectors": detectors
                }
            })

    def get_regions(self):
        """ Get a list of regions.

        Use the ec2 service, which has the 'describe_regions' method, as a proxy to get available regions.

        :return regions: List of region names.
        """
        regions = []
        ec2 = AwsGdClient(self.opts, self.function_opts, service_name="ec2", region=self.aws_gd_master_region)

        regions = [region['RegionName'] for region in ec2.get("describe_regions")]

        return regions

    def refresh_clients(self):
        """ Refresh hash of Clients for accessible GuardDuty regions.

        :return: Update hash of clients.
        """
        self._get_clients()
