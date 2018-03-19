# -*- coding: utf-8 -*-
# Copyright IBM Corp. - Confidential Information
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

from dxlclient.client_config import DxlClientConfig
from dxlclient.client import DxlClient
from dxltieclient import TieClient
from dxltieclient.constants import HashType, ReputationProp, FileProvider, FileEnterpriseAttrib, TrustLevel, \
    FileGtiAttrib, AtdAttrib, AtdTrustLevel, EpochMixin

LOG = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_tie_search_hash"""

    config_file = "dxlclient_config"

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        try:
            config = opts.get("mcafee").get(self.config_file)
            if config is None:
                LOG.error(self.config_file + " is not set. You must set this path to run this threat service")
                raise ValueError(self.config_file + " is not set. You must set this path to run this threat service")

            # Create configuration from file for DxlClient
            self.config = DxlClientConfig.create_dxl_config_from_file(config)
        except AttributeError:
            LOG.error("There is no [mcafee] section in the config file, "
                      "please set that by running resilient-circuits config -u")
            raise AttributeError("[mcafee] section is not set in the config file")

        self.client = DxlClient(self.config)
        self._connect_client()

    def _connect_client(self):
        # Connect client
        if not self.client.connected:
            self.client.connect()
            self.tie_client = TieClient(self.client)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("mcafee", {})

    @function("mcafee_tie_search_hash")
    def _mcafee_tie_search_hash_function(self, event, *args, **kwargs):
        """Function: """

        yield StatusMessage("Searching Hash...")
        try:
            response_dict = {}
            # Get the function parameters:
            mcafee_tie_hash_type = kwargs.get("mcafee_tie_hash_type")  # text
            if not mcafee_tie_hash_type:
                yield FunctionError("mcafee_tie_hash_type is required")
            mcafee_tie_hash = kwargs.get("mcafee_tie_hash")  # text
            if not mcafee_tie_hash:
                yield FunctionError("mcafee_tie_hash is required")

            LOG.debug("_lookup_hash started for Artifact Type {0} - Artifact Value {1}".format(
                mcafee_tie_hash_type, mcafee_tie_hash))

            if mcafee_tie_hash_type == "md5":
                resilient_hash = {HashType.MD5: mcafee_tie_hash}
            elif mcafee_tie_hash_type == "sha1":
                resilient_hash = {HashType.SHA1: mcafee_tie_hash}
            elif mcafee_tie_hash_type == "sha256":
                resilient_hash = {HashType.SHA256: mcafee_tie_hash}
            else:
                yield FunctionError("Something went wrong setting the hash value")

            # Make sure client is connected
            self._connect_client()

            reputations_dict = \
                self.tie_client.get_file_reputation(
                    resilient_hash
                )
            system_list = self.tie_client.get_file_first_references(
                resilient_hash
            )

            response_dict["Enterprise"] = self._get_enterprise_info(reputations_dict)
            response_dict["GTI"] = self._get_gti_info(reputations_dict)
            response_dict["ATD"] = self._get_atd_info(reputations_dict)
            response_dict["MWG"] = self._get_mwg_info(reputations_dict)
            response_dict["system_list"] = system_list

            yield StatusMessage("Done...")

            # Produce a FunctionResult with the return value
            yield FunctionResult(response_dict)
        except Exception:
            yield FunctionError()

    def _get_enterprise_info(self, reputations_dict):
        ent_dict = {}
        # Information for Enterprise file provider
        if FileProvider.ENTERPRISE in reputations_dict:
            ent_rep = reputations_dict[FileProvider.ENTERPRISE]
            ent_dict["File Provider"] = "Enterprise"
            ent_dict["Create Date"] = EpochMixin.to_localtime_string(ent_rep[ReputationProp.CREATE_DATE])
            trust_level = self._get_trust_level(ent_rep[ReputationProp.TRUST_LEVEL])

            if trust_level:
                ent_dict["Trust Level"] = trust_level

            # Retrieve the enterprise reputation attributes
            if ReputationProp.ATTRIBUTES in ent_rep:
                ent_rep_attribs = ent_rep[ReputationProp.ATTRIBUTES]
                attribs_dict = {}

                if FileEnterpriseAttrib.PREVALENCE in ent_rep_attribs:
                    attribs_dict["Prevalence"] = ent_rep_attribs[FileEnterpriseAttrib.PREVALENCE]

                if FileEnterpriseAttrib.ENTERPRISE_SIZE in ent_rep_attribs:
                    attribs_dict["Enterprise Size"] = ent_rep_attribs[FileEnterpriseAttrib.ENTERPRISE_SIZE]

                if FileEnterpriseAttrib.FIRST_CONTACT in ent_rep_attribs:
                    attribs_dict["First Contact"] = FileEnterpriseAttrib.to_localtime_string(
                        ent_rep_attribs[FileEnterpriseAttrib.FIRST_CONTACT])

                if FileEnterpriseAttrib.PARENT_AVG_LOCAL_REP in ent_rep_attribs:
                    attribs_dict["Parent Avg Local Rep"] = self._get_trust_level(int(ent_rep_attribs[
                                                                            FileEnterpriseAttrib.PARENT_AVG_LOCAL_REP]))

                if FileEnterpriseAttrib.PARENT_FILE_REPS in ent_rep_attribs:
                    attribs_dict["Parent File Reps"] = FileEnterpriseAttrib.to_aggregate_tuple(ent_rep_attribs[
                        FileEnterpriseAttrib.PARENT_FILE_REPS])

                if FileEnterpriseAttrib.CHILD_FILE_REPS in ent_rep_attribs:
                    attribs_dict["Child File Reps"] = FileEnterpriseAttrib.to_aggregate_tuple(ent_rep_attribs[
                        FileEnterpriseAttrib.CHILD_FILE_REPS])

                if FileEnterpriseAttrib.AVG_LOCAL_REP in ent_rep_attribs:
                    attribs_dict["Average Local Rep"] = self._get_trust_level(int(ent_rep_attribs[
                                                                              FileEnterpriseAttrib.AVG_LOCAL_REP]))

                if FileEnterpriseAttrib.MAX_LOCAL_REP in ent_rep_attribs:
                    attribs_dict["Max Local Rep"] = self._get_trust_level(int(ent_rep_attribs[
                                                                              FileEnterpriseAttrib.MAX_LOCAL_REP]))

                if FileEnterpriseAttrib.MIN_LOCAL_REP in ent_rep_attribs:
                    attribs_dict["Min Local Rep"] = self._get_trust_level(int(ent_rep_attribs[
                                                                              FileEnterpriseAttrib.MIN_LOCAL_REP]))

                if FileEnterpriseAttrib.DETECTION_COUNT in ent_rep_attribs:
                    attribs_dict["Detection Count"] = ent_rep_attribs[FileEnterpriseAttrib.DETECTION_COUNT]

                if FileEnterpriseAttrib.FILE_NAME_COUNT in ent_rep_attribs:
                    attribs_dict["File Name Count"] = ent_rep_attribs[FileEnterpriseAttrib.FILE_NAME_COUNT]

                if FileEnterpriseAttrib.LAST_DETECTION_TIME in ent_rep_attribs:
                    attribs_dict["Last Detection Time"] = FileEnterpriseAttrib.to_localtime_string(
                        ent_rep_attribs[FileEnterpriseAttrib.FIRST_CONTACT])

                if FileEnterpriseAttrib.IS_PREVALENT in ent_rep_attribs:
                    attribs_dict["Is Prevalent"] = ent_rep_attribs[FileEnterpriseAttrib.IS_PREVALENT]

                if FileEnterpriseAttrib.PARENT_MIN_LOCAL_REP in ent_rep_attribs:
                    attribs_dict["Parent Min Local Rep"] = self._get_trust_level(int(ent_rep_attribs[
                                                                            FileEnterpriseAttrib.PARENT_MIN_LOCAL_REP]))

                if FileEnterpriseAttrib.PARENT_MAX_LOCAL_REP in ent_rep_attribs:
                    attribs_dict["Parent Max Local Rep"] = self._get_trust_level(int(ent_rep_attribs[
                                                                            FileEnterpriseAttrib.PARENT_MAX_LOCAL_REP]))

                ent_dict["Attributes"] = attribs_dict

        return ent_dict

    def _get_gti_info(self, reputations_dict):
        gti_dict = {}
        # Information for GTI file provider
        if FileProvider.GTI in reputations_dict:
            gti_rep = reputations_dict[FileProvider.GTI]
            gti_dict["File Provider"] = "GTI"
            gti_dict["Create Date"] = EpochMixin.to_localtime_string(gti_rep[ReputationProp.CREATE_DATE])

            trust_level = self._get_trust_level(gti_rep[ReputationProp.TRUST_LEVEL])

            if trust_level:
                gti_dict["Trust Level"] = trust_level

            # Retrieve the GTI reputation attributes
            if ReputationProp.ATTRIBUTES in gti_rep:
                gti_rep_attribs = gti_rep[ReputationProp.ATTRIBUTES]
                attribs_dict = {}

                # Get prevalence (if it exists)
                if FileGtiAttrib.PREVALENCE in gti_rep_attribs:
                    attribs_dict["Prevalence"] = gti_rep_attribs[FileGtiAttrib.PREVALENCE]

                # Get First Contact Date (if it exists)
                if FileGtiAttrib.FIRST_CONTACT in gti_rep_attribs:
                    attribs_dict["First Contact"] = EpochMixin.to_localtime_string(gti_rep_attribs[
                                                                                       FileGtiAttrib.FIRST_CONTACT])
                gti_dict["Attributes"] = attribs_dict

        return gti_dict

    def _get_atd_info(self, reputations_dict):
        atd_dict = {}
        # Information for Advanced Threat Defense file provider
        if FileProvider.ATD in reputations_dict:
            atd_rep = reputations_dict[FileProvider.ATD]
            atd_dict["File Provider"] = "ATD"
            atd_dict["Create Date"] = EpochMixin.to_localtime_string(atd_rep[ReputationProp.CREATE_DATE])

            trust_level = self._get_trust_level(atd_rep[ReputationProp.TRUST_LEVEL])

            if trust_level:
                atd_dict["Trust Level"] = trust_level

            # Retrieve the ATD reputation attributes
            if ReputationProp.ATTRIBUTES in atd_rep:
                atd_rep_attribs = atd_rep[ReputationProp.ATTRIBUTES]

                attribs_dict = {}
                # Get Trust scores
                if AtdAttrib.GAM_SCORE in atd_rep_attribs:
                    attribs_dict["GAM Score"] = self._get_atd_trust_level(atd_rep, AtdAttrib.GAM_SCORE)
                if AtdAttrib.AV_ENGINE_SCORE in atd_rep_attribs:
                    attribs_dict["AV Engine Score"] = self._get_atd_trust_level(atd_rep, AtdAttrib.AV_ENGINE_SCORE)
                if AtdAttrib.GAM_SCORE in atd_rep_attribs:
                    attribs_dict["Sandbox Score"] = self._get_atd_trust_level(atd_rep, AtdAttrib.SANDBOX_SCORE)
                if AtdAttrib.GAM_SCORE in atd_rep_attribs:
                    attribs_dict["Verdict"] = self._get_atd_trust_level(atd_rep, AtdAttrib.VERDICT)
                if AtdAttrib.BEHAVIORS in atd_rep_attribs:
                    attribs_dict["Behaviors"] = atd_rep_attribs[AtdAttrib.BEHAVIORS]

                atd_dict["Attributes"] = attribs_dict

        return atd_dict

    def _get_mwg_info(self, reputations_dict):
        mwg_dict = {}
        # Information for  file provider
        if FileProvider.MWG in reputations_dict:
            mwg_rep = reputations_dict[FileProvider.MWG]

            mwg_dict["File Provider"] = "MWG"
            mwg_dict["Create Date"] = EpochMixin.to_localtime_string(mwg_rep[ReputationProp.CREATE_DATE])

            trust_level = self._get_trust_level(mwg_rep[ReputationProp.TRUST_LEVEL])

            if trust_level:
                mwg_dict["Trust Level"] = trust_level

        return mwg_dict

    @staticmethod
    def _get_trust_level(trust_level_number):
        trust_level = ""
        if TrustLevel.KNOWN_TRUSTED_INSTALLER is trust_level_number:
            trust_level = "Known Trusted Installer"
        elif TrustLevel.KNOWN_TRUSTED is trust_level_number:
            trust_level = "Known Trusted"
        elif TrustLevel.MOST_LIKELY_TRUSTED is trust_level_number:
            trust_level = "Most Likely Trusted"
        elif TrustLevel.MIGHT_BE_TRUSTED is trust_level_number:
            trust_level = "Might Be Trusted"
        elif TrustLevel.UNKNOWN is trust_level_number:
            trust_level = "Unknown"
        elif TrustLevel.MIGHT_BE_MALICIOUS is trust_level_number:
            trust_level = "Might be Malicious"
        elif TrustLevel.MOST_LIKELY_MALICIOUS is trust_level_number:
            trust_level = "Most Likely Malicious"
        elif TrustLevel.KNOWN_MALICIOUS is trust_level_number:
            trust_level = "Known Malicious"
        elif TrustLevel.NOT_SET is trust_level_number:
            trust_level = "Not Set"

        return trust_level

    @staticmethod
    def _get_atd_trust_level(atd_rep, rep_provider):
        trust_level = ""
        if AtdTrustLevel.KNOWN_TRUSTED is atd_rep[rep_provider]:
            trust_level = "Known Trusted"
        elif AtdTrustLevel.MOST_LIKELY_TRUSTED is atd_rep[rep_provider]:
            trust_level = "Most Likely Trusted"
        elif AtdTrustLevel.MIGHT_BE_TRUSTED is atd_rep[rep_provider]:
            trust_level = "Might Be Trusted"
        elif AtdTrustLevel.UNKNOWN is atd_rep[rep_provider]:
            trust_level = "Unknown"
        elif AtdTrustLevel.MIGHT_BE_MALICIOUS is atd_rep[rep_provider]:
            trust_level = "Might be Malicious"
        elif AtdTrustLevel.MOST_LIKELY_MALICIOUS is atd_rep[rep_provider]:
            trust_level = "Most Likely Malicious"
        elif AtdTrustLevel.KNOWN_MALICIOUS is atd_rep[rep_provider]:
            trust_level = "Known Malicious"
        elif AtdTrustLevel.NOT_SET is atd_rep[rep_provider]:
            trust_level = "Not Set"

        return trust_level
