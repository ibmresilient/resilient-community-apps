#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#

import resilient
import requests
import os
from fn_resilient_ml.lib.file_manage import FileManage
import logging
import csv
import json
"""
    ResUtils:
    --------
    Encapsulate methods to download incidents and artifacts
"""
RESILIENT_SECTION = "resilient"

class ResUtils:
    def __init__(self, in_log=None):
        self.log = in_log if in_log else logging.getLogger(__name__)
        self.res_client = None

    def connect(self, opt_parser):
        res_opt = opt_parser.opts.get(RESILIENT_SECTION)
        host = res_opt.get("host", None)
        email = res_opt.get("email", None)
        password = res_opt.get("password", None)
        org = res_opt.get("org", None)
        api_key_id = res_opt.get("api_key_id", None)
        api_key_secret = res_opt.get("api_key_secret", None)

        if host and org and ((email and password) or (api_key_id and api_key_secret)):
            url = "https://{}:443".format(host)
            verify = True
            try:
                cafile = opt_parser.getopt(RESILIENT_SECTION, "cafile")
                if cafile == "false" or cafile == "False":
                    #
                    #   This is a security related feature. The user has to explicitly enter false or False to
                    #   turn it off. We don't accept anything else.
                    #
                    self.log.debug("HTTPS certificate validation has been turned off.")

                    requests.packages.urllib3.disable_warnings()
                    verify = False
                elif os.path.isfile(cafile):
                    #
                    #   User specified a cafile for trusted certificate
                    #
                    verify = cafile
            except:
                verify = True

            args = {"base_url": url,
                    "verify": verify,
                    "org_name": org}

            self.res_client = resilient.SimpleClient(**args)
            if email is not None and password is not None:
                session = self.res_client.connect(email, password)

                if session is not None:
                    user_name = session.get("user_displayname", "Not found")
                    print("User display name is : {}".format(user_name))

                print("Done")
            else:
                self.res_client.set_api_key(api_key_id=api_key_id,
                                            api_key_secret=api_key_secret)

    def download_incidents(self, file_name=None):
        """

        :param file_name:
        :return:
        """
        csv_file = file_name if file_name else FileManage.DEFAULT_INCIDENT_FILE
        self.get_incidents(csv_file)
        return csv_file

    def download_artifacts(self, file_name=None):
        """
        Download artifacts and save them into the output file.
        Use the search_ex endpoint.
        :param file_name: Output file name
        :return:
        """
        json_file = file_name if file_name else FileManage.DEFAULT_ARTIFACT_FILE

        body = {
            "org_id": self.res_client.org_id,
            "query": "*",
            "types": [
                "artifact"
            ],
            "min_required_results": 0
        }

        url = u"{0}/rest/search_ex".format(self.res_client.base_url)
        payload = json.dumps(body)

        response = self.res_client._execute_request(self.res_client.session.post,
                                                    url,
                                                    data=payload,
                                                    proxies=self.res_client.proxies,
                                                    headers=self.res_client.make_headers(),
                                                    verify=self.res_client.verify)

        artifacts = response.json()

        with open(json_file, "w") as outfile:
            json.dump(artifacts, outfile)

    def get_incidents(self, filename, max_count=None, filter=None):
        """
        Convert JSON into CSV and save, since scikit-learn uses CSV.

        :param filename:    CSV file to save to
        :param max_count:   max count of incidents/samples to handle
        :param filter:      filter for incidents/sample
        :return:            incidents/samples count
        """

        # Read the fields of an incident
        inc_fields = self.res_client.get("/types/incident")

        fields_dict = inc_fields.get("fields", {})
        self.log.debug("Incident Fields: " + str(fields_dict))

        # Get all the incidents
        ret = self.query_incidents(max_count=max_count)

        inc_count = self.write_to_csv(incidents=ret,
                                      fields_dict=fields_dict,
                                      filename=filename,
                                      max_count=max_count,
                                      filter=filter)
        return inc_count

    def query_incidents(self, max_count=None, page_size=1000):
        """
        Use the query endpoint since we are going to down load
        large number of incidents.

        :param res_client:  Resilient client used to download incidents
        :param max_count:   Max count for incidents to handle
        :param page_size:   Number of incident to download for each call
        :return:            All downloaded incidents in json
        """
        incidents = []
        url = "/incidents/query_paged?field_handle=-1&return_level=full"
        num_incidents = 0
        ret_num = 0
        done = False
        while not done:
            body = {
                "start": num_incidents,
                "length": page_size,
                "recordsTotal": page_size
            }
            ret = self.res_client.post(uri=url,
                                       payload=body)

            data = ret.get("data", [])
            ret_num = len(data)
            if ret_num > 0:
                self.log.debug("Downloaded {} incidents, total now {} ...".format(ret_num, ret_num + num_incidents))
                incidents.extend(data)
            else:
                #
                # No more to read.
                #
                done = True

            num_incidents = num_incidents + ret_num

            if max_count:
                if num_incidents >= max_count:
                    #
                    # Reach max_count set by user, stop now
                    #
                    done = True

        return incidents

    def write_to_csv(self, incidents, fields_dict, filename, max_count=None, filter=None):
        """
        Write incidents to a CSV file according to the field definition.
        This function is factorized out intentionally for better unit test.

        :param incidents:       list of incidents in json
        :param fields_dict:     field definitions in json dict
        :param filename:        filename for CSV file to save samples
        :param max_count:       max count for incidents to save
        :param filter:          filter for incidents
        :return:                number of incidents saved to the CSV file
        """
        #
        #   Keep a count for samples
        #
        inc_count = 0
        with open(filename, "w") as outfile:
            #
            #   Write everything into a CSV file, since scikit-learn uses CSV format for samples
            #
            fields = list(fields_dict.keys())
            csv_writer = csv.DictWriter(outfile,
                                        fieldnames=fields,
                                        dialect="excel")
            csv_writer.writeheader()

            for inc in incidents:
                #
                #   Call filter to figure if we want to keep this incident/sample
                #
                if filter is not None:
                    shall_include = filter.shall_include_incident(inc)
                    if not shall_include:
                        #
                        #   Filter it out. Continue to the next
                        #
                        continue

                new_dict = {}
                for field in fields:
                    try:
                        #
                        #   The field could be a custom field, if so read from properties.
                        #
                        val = inc.get(field, inc["properties"].get(field, None))
                        #
                        # Note val can be False, so "if not val" does not work
                        #
                        if val is None:
                            gdpr_dict = inc.get("gdpr", None)
                            pii_dict = inc.get("pii", None)
                            hipaa_dict = inc.get("hipaa", None)
                            reg_risk = inc.get("regulator_risk", None)

                            if gdpr_dict:
                                val = gdpr_dict.get(field, None)

                            if val is None and pii_dict:
                                val = pii_dict.get(field, None)

                            if val is None and hipaa_dict:
                                val = hipaa_dict.get(field, None)

                            if val is None and reg_risk:
                                val = reg_risk.get(field, None)

                        #
                        #   Since we are writing it to a CSV file, we convert it into string
                        #   Later on we will use pandas to read the CSV file, and pandas will
                        #   convert things back anyway.
                        #
                        try:
                            value = str(val)
                        except UnicodeEncodeError:
                            value = val.encode("ascii", "ignore").decode("ascii")
                    except Exception as e:
                        self.log.exception("Exception in reading incident field {}: {}".format(field, str(e)))
                        value = ""
                    new_dict[field] = value

                csv_writer.writerow(new_dict)

                inc_count = inc_count + 1
                if max_count and inc_count >= max_count:
                    self.log.info("Truncated samples at " + str(max_count))
                    break

        return inc_count
