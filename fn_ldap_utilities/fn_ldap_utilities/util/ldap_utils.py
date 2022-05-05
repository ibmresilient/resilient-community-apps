# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
#
#   Util classes for LDAP

from . import helper
from resilient_lib import IntegrationError

class LDAPDomains():
    def __init__(self, opts):
        self.domains, self.domain_name_list = self._load_domains(opts)

    def _load_domains(self, opts):
        domains = {}
        domain_name_list = self._get_domain_name_list(opts)
        for domain in domain_name_list:
            domain_name = u"{}".format(domain)
            domain_data = opts.get(domain_name)
            if not domain_data:
                raise KeyError(u"Unable to find ldap domain: {}".format(domain_name))

            domains[domain] = domain_data

        return domains, domain_name_list

    def ldap_domain_name_test(self, ldap_domain_name, domains_list):
        """
        Check if the given ldap_domain_name is in the app.config
        :param ldap_domain_name: User selected domain
        :param domains_list: list of ldap domains
        :return: dictionary of options for choosen domain
        """
        domain_name = helper.PACKAGE_NAME+":"+ldap_domain_name
        if ldap_domain_name and domain_name in domains_list:
            return domains_list[domain_name]
        elif ldap_domain_name == helper.PACKAGE_NAME or len(domains_list) == 1:
            return domains_list[list(domains_list.keys())[0]]
        else:
            raise IntegrationError("{} did not match domain given in the app.config".format(ldap_domain_name))

    def _get_domain_name_list(self, opts):
        """
        Return the list of ldap domain names defined in the app.config in fn_ldap_utilities.
        :param opts: list of options
        :return: list of domains
        """
        domain_list = []
        for key in opts.keys():
            if key.startswith("{}:".format(helper.PACKAGE_NAME)):
                domain_list.append(key)
        return domain_list

    def get_domain_name_list(self):
        """
        Return list of all domain names
        """
        return self.domain_name_list