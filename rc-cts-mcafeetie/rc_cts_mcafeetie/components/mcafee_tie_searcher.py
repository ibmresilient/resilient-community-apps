# -*- coding: utf-8 -*-
# pylint: disable=unused-argument

import logging
from fnmatch import fnmatch

from dxlclient.client_config import DxlClientConfig
from dxlclient.client import DxlClient
from dxltieclient import TieClient
from dxltieclient.constants import HashType, ReputationProp, FileProvider, FileEnterpriseAttrib, TrustLevel, \
    FileGtiAttrib, AtdAttrib, AtdTrustLevel, EpochMixin

from circuits import BaseComponent, handler
from rc_cts import searcher_channel, Hit, StringProp


LOG = logging.getLogger(__name__)


def config_section_data():
    return '''[mcafee]
dxlclient_config=/home/resilient/.resilient/mcafee_tie/dxlclient.config
'''


class McAfeeTieSearcher(BaseComponent):
    """
    McAfee TIE custom threat searcher component

    Test using 'curl':
        curl -v -X OPTIONS 'http://127.0.0.1:9000/cts/mcafee_tie_searcher'
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"hash.md5",
        "value":"1CF5B6CC0E6B742F6DEF8BF96D847A25"}' 'http://127.0.0.1:9000/cts/mcafee_tie_searcher'
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"hash.sha1",
        "value":"19A82049C4336E8A5A30426FEC3F560358FAB6ED"}' 'http://127.0.0.1:9000/cts/mcafee_tie_searcher'
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"hash.sha256",
        "value":"A8B03AD33BC6D7A7F376B943F763EEDD1CDAF125D012F9018F2F56678AE67EA4"}'
        'http://127.0.0.1:9000/cts/mcafee_tie_searcher'

    """

    # Register this as an async searcher for the URL /<root>/mcafee_tie_searcher
    channel = searcher_channel("mcafee_tie_searcher")

    config_file = "dxlclient_config"

    def __init__(self, opts):
        super(McAfeeTieSearcher, self).__init__(opts)
        LOG.debug(opts)

        try:
            config = opts.get("mcafee").get(self.config_file)
            if config is None:
                LOG.error(self.config_file + " is not set. You must set this path to run this threat service")
                raise ValueError(self.config_file + " is not set. You must set this path to run this threat service")

            # Create configuration from file for DxlClient
            self.config = DxlClientConfig.create_dxl_config_from_file(config)
        except AttributeError:
            LOG.error("There is no [mcafee] section in the config file,"
                      "please set that by running resilient-circuits config -u")
            raise AttributeError("[mcafee] section is not set in the config file")

        # Create client
        self.client = DxlClient(self.config)
        self.client.connect()

    # Handle lookup for artifacts of type md5, sha1, and sha256 hashes
    @handler("hash.md5", "hash.sha1", "hash.sha256")
    def _lookup_hash(self, event, *args, **kwargs):
        artifact_type = event.artifact["type"]
        artifact_value = event.artifact["value"]
        LOG.debug("_lookup_hash started for Artifact Type {0} - Artifact Value {1}".format(
            artifact_type, artifact_value))

        tie_client = TieClient(self.client)

        if artifact_type == "hash.md5":
            resilient_hash = {HashType.MD5: artifact_value}
        elif artifact_type == "hash.sha1":
            resilient_hash = {HashType.SHA1: artifact_value}
        elif artifact_type == "hash.sha256":
            resilient_hash = {HashType.SHA256: artifact_value}
        else:
            raise ValueError("Something went wrong setting the hash value")

        reputations_dict = \
            tie_client.get_file_reputation(
                    resilient_hash
            )

        hits = self._query_mcafee_tie(reputations_dict)

        yield hits

    def _query_mcafee_tie(self, reputations_dict):
        hit = Hit()

        # Check Enterprise File Provider
        hit = self._get_enterprise_info(reputations_dict, hit)

        # Check GTI File Provider
        hit = self._get_gti_info(reputations_dict, hit)

        # Check ATD File Provider
        hit = self._get_atd_info(reputations_dict, hit)

        # Check MWG File Provider
        hit = self._get_mwg_info(reputations_dict, hit)

        # Verifies a trust level was set before returning a hit
        for prop in hit["props"]:
            if fnmatch(prop["name"], "*Trust Level"):
                return hit
        return []

    def _get_enterprise_info(self, reputations_dict, hit):
        # Information for Enterprise file provider
        if FileProvider.ENTERPRISE in reputations_dict:
            ent_rep = reputations_dict[FileProvider.ENTERPRISE]
            trust_level = self._get_trust_level(ent_rep[ReputationProp.TRUST_LEVEL])

            if trust_level:
                # Not a hit until trust level has been verified to less than or equal to MIGHT BE MALICIOUS
                hit.append(StringProp(name="Enterprise Trust Level", value=trust_level))

            # Retrieve the enterprise reputation attributes
            ent_rep_attribs = ent_rep[ReputationProp.ATTRIBUTES]

            # Get Average Local Rep
            if FileEnterpriseAttrib.AVG_LOCAL_REP in ent_rep_attribs:
                local_rep = self._get_trust_level(int(ent_rep_attribs[FileEnterpriseAttrib.AVG_LOCAL_REP]))
                if local_rep:
                    hit.append(StringProp(name="Enterprise Avg Local Trust Level", value=local_rep))

            # Get prevalence (if it exists)
            if FileEnterpriseAttrib.PREVALENCE in ent_rep_attribs:
                hit.append(StringProp(name="Enterprise Prevalence",
                                      value=ent_rep_attribs[FileEnterpriseAttrib.PREVALENCE]))

            # Get Enterprise Size (if it exists)
            if FileEnterpriseAttrib.ENTERPRISE_SIZE in ent_rep_attribs:
                hit.append(StringProp(name="Enterprise Size",
                                      value=ent_rep_attribs[FileEnterpriseAttrib.ENTERPRISE_SIZE]))

            # Get First Contact Date (if it exists)
            if FileEnterpriseAttrib.FIRST_CONTACT in ent_rep_attribs:
                hit.append(StringProp(name="Enterprise First Contact",
                                      value=FileEnterpriseAttrib.to_localtime_string(
                                          ent_rep_attribs[FileEnterpriseAttrib.FIRST_CONTACT])))

        return hit

    def _get_gti_info(self, reputations_dict, hit):
        # Information for GTI file provider
        if FileProvider.GTI in reputations_dict:
            gti_rep = reputations_dict[FileProvider.GTI]
            trust_level = self._get_trust_level(gti_rep[ReputationProp.TRUST_LEVEL])

            if trust_level:
                # Not a hit until trust level has been verified to less than or equal to MIGHT BE MALICIOUS
                hit.append(StringProp(name="GTI Trust Level", value=trust_level))

            # Retrieve the GTI reputation attributes
            gti_rep_attribs = gti_rep[ReputationProp.ATTRIBUTES]

            # Get prevalence (if it exists)
            if FileGtiAttrib.PREVALENCE in gti_rep_attribs:
                hit.append(StringProp(name="GTI Prevalence", value=gti_rep_attribs[FileGtiAttrib.PREVALENCE]))

            # Get First Contact Date (if it exists)
            if FileGtiAttrib.FIRST_CONTACT in gti_rep_attribs:
                hit.append(StringProp(name="GTI First Contact", value=EpochMixin.to_localtime_string(
                    gti_rep_attribs[FileGtiAttrib.FIRST_CONTACT])))

        return hit

    def _get_atd_info(self, reputations_dict, hit):
        # Information for Advanced Threat Defense file provider
        if FileProvider.ATD in reputations_dict:
            atd_rep = reputations_dict[FileProvider.ATD]
            trust_level = self._get_trust_level(atd_rep[ReputationProp.TRUST_LEVEL])

            if trust_level:
                # Not a hit until trust level has been verified to less than or equal to MIGHT BE MALICIOUS
                hit.append(StringProp(name="ATD Trust Level", value=trust_level))

        return hit

    def _get_mwg_info(self, reputations_dict, hit):
        # Information for  file provider
        if FileProvider.MWG in reputations_dict:
            mwg_rep = reputations_dict[FileProvider.MWG]
            trust_level = self._get_trust_level(mwg_rep[ReputationProp.TRUST_LEVEL])

            if trust_level:
                # Not a hit until trust level has been verified to less than or equal to MIGHT BE MALICIOUS
                hit.append(StringProp(name="MWG Trust Level", value=trust_level))

        return hit

    @staticmethod
    def _get_trust_level(trust_level_number):
        trust_level = ""
        if TrustLevel.MIGHT_BE_MALICIOUS is trust_level_number:
            trust_level = "Might be Malicious"
        elif TrustLevel.MOST_LIKELY_MALICIOUS is trust_level_number:
            trust_level = "Most Likely Malicious"
        elif TrustLevel.KNOWN_MALICIOUS is trust_level_number:
            trust_level = "Known Malicious"

        return trust_level
