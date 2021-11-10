# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
from resilient_lib import validate_fields

DEFAULT_SENTINELONE_UPDATE_INCIDENT_TEMPLATE = "data/sentinelone_update_incident_template.jinja"
DEFAULT_SENTINELONE_CLOSE_INCIDENT_TEMPLATE = "data/sentinelone_close_incident_template.jinja"

DEFAULT_INCIDENT_CREATION_TEMPLATE = "data/incident_creation_template.jinja"
DEFAULT_INCIDENT_UPDATE_TEMPLATE = "data/incident_update_template.jinja"
DEFAULT_INCIDENT_CLOSE_TEMPLATE = "data/incident_close_template.jinja"

REQUIRED_PROFILE_FIELDS = ["new_incident", "workspace_name", "resource_groupname"]

PACKAGE_NAME = "fn_microsoft_sentinel"

class SentinelProfiles():
    def __init__(self, opts, options):
        self.profiles = self._load_profiles(opts, options)

    def _load_profiles(self, opts, options):
        """load the app.config profiles for sentinel. Each profile represents a different workspace
                to pull incidents from.

        Raises:
            KeyError: [error when a named profile is not found in app.config]
        """
        sentinel_profiles = options["sentinel_profiles"]

        # confirm all profiles are valid
        profiles = {}
        profile_list = [item.strip() for item in sentinel_profiles.split(",")]
        for profile in profile_list:
            profile_name = u"{}:{}".format(PACKAGE_NAME, profile)
            profile_data = opts.get(profile_name)
            if not profile_data:
                raise KeyError(u"Unable to find Sentinel profile: {}".format(profile_name))

            # check each profile for the correct settings
            validate_fields(REQUIRED_PROFILE_FIELDS, profile_data)

            profiles[profile] = profile_data

        return profiles

    def get_profile(self, profile_name):
        """collect the settings for a Sentinel profile: subscription, resource group, workspace

        Args:
            profile_name ([str]): [name of profile in app.config]

        Raises:
            KeyError: [profile not found]

        Returns:
            [dict]: [settings for a sentinel incident environment]
        """
        if not profile_name in self.profiles:
            raise KeyError(u"Unable to find profile: {}".format(profile_name))

        return self.profiles[profile_name]

    def get_profiles(self):
        """
        Return all profiles
        """
        return self.profiles
