# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
import resilient_circuits.template_functions as template_functions
from resilient_circuits.template_functions import environment
import datetime
import calendar
# Used for Ipaddress
import ipaddress
import logging
from collections import defaultdict

log = logging.getLogger(__name__)


class ICDXHelper:

    def str_to_bool(self, str):
        """Convert unicode string to equivalent boolean value. Converts a "true" or "false" string to a boolean value , string is case insensitive."""
        try:
            if str.lower() == 'true':
                return True
            elif str.lower() == 'false':
                return False
            else:
                raise ValueError
        except:
            return False

    def get_config_option(self, option_name, optional=False):
        """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
        option = self.options.get(option_name)

        if option is None and optional is False:
            err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function".format(
                option_name)
            raise ValueError(err)
        else:
            return option

    def get_function_input(self, inputs, input_name, optional=False):
        """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""
        input = inputs.get(input_name)

        if input is None and optional is False:
            err = "'{0}' is a mandatory function input".format(input_name)
            raise ValueError(err)
        else:
            return input

    def merge_dicts(*dict_args):
        """
        Given any number of dicts, shallow copy and merge into a new dict,
        precedence goes to key value pairs in latter dicts.
        Example input dicts a,b,c will result in a dict with format c,b,a

        """
        """
                The old way to merge the dicts, 
                Works fine for merging but does not merge in the case of duplicate keys 
                dict1 has attribute item which has value 2
                dict2 has attribute item which has value 3

                I expect the result to include attribute item which has values [2,3]
                result = {}
                for dictionary in dict_args:
                    # If dictionary is non-empty AND of type dict
                    if bool(dictionary) and isinstance(dictionary, dict):
                        result.update(dictionary)
                """
        # Create a defaultdict with a default type of list
        result = defaultdict(list)
        # For each arg in *dict_args
        for dictionary in dict_args:
            # If this arg is a dictionary and not empty
            if bool(dictionary) and isinstance(dictionary, dict):
                # Get a handle on its keys and values
                for k, v in dictionary.items():
                    # And for each item in v append this to the defaultdict
                    for item in v:
                        result[k].append(item)

        # Finally cast the result to a normal dict, encapsulate the fact we are using defaultdicts
        return dict(result)

    def safe_cast(self, val, to_type, default=0):
        try:
            return to_type(val)
        except (ValueError, TypeError):
            return default

    def search_for_artifact_data(self, search_result):
        """Takes an input of an ICDx Search Result in dict format
        Performs these steps :
        1. Check for a file object, if exists parse for artifact data
        2. Check for a connection object, if exists parse for artifact data
        3. Check for a email object, if exists parse for artifact data

        Final step is to merge the above dicts and return as one dict
        """

        formatted_file_dictionary = self.parse_for_file_artifacts(search_result)
        formatted_network_dictionary = self.parse_for_network_artifacts(search_result)
        formatted_email_dictionary = self.parse_for_email_artifacts(search_result)

        """
        Once here is reached, we have 1 or more separate dicts
        
        Before result is returned
        Merge all non None dicts into one dict
        """
        artifact_dictionary = self.merge_dicts(formatted_file_dictionary, formatted_network_dictionary, formatted_email_dictionary)
        return artifact_dictionary

    def parse_for_file_artifacts(self, search_result):
        # Check if the file object is present in result
        if 'file' in search_result:
            file_payload = search_result['file']
            # All the keys we want to extract from the schema
            your_keys = ['md5', 'sha2', 'path', 'name']

            # Using dictionary comprehension to gather the attributes we want into a new dict
            unformatted_artifact_dict = {your_key: file_payload.get(your_key, None) for your_key in your_keys}

            # After first dict comprehension we have a dict of artifacts
            # Next step is to remap the keys to match resilient artifact types
            keys_to_artifact_map = {'md5': 'Malware MD5 Hash', 'sha2': 'Malware SHA-256 Hash', 'path': 'File Path',
                                    'name': 'File Name'}

            """
            Prepare final dict, remap keys to be artifact types
            Remove empty values 
            """

            return self.parse_for_artifacts(keys_to_artifact_map, unformatted_artifact_dict)

    def parse_for_network_artifacts(self, search_result):
        # Check if the network_connection object is present
        if 'connection' in search_result:
            network_conn_payload = search_result['connection']

            # All the keys we want to extract from the schema
            network_keys = ['dst_ip', 'dst_mac', 'dst_port', 'dst_service', 'src_ip', 'src_mac',
                            'src_port', 'src_service']

            # Using dictionary comprehension to gather the attributes we want into a new dict
            unformatted_artifact_dict = {key: network_conn_payload.get(key, None) for key in network_keys}

            # After first dict comprehension we have a dict of artifacts
            # Next step is to remap the keys to match resilient artifact types
            keys_to_artifact_map = {'dst_ip': 'IP Address', 'dst_mac': 'MAC Address', 'dst_port': 'Port',
                                    'dst_service': 'Service', 'src_ip': 'IP Address', 'src_mac': 'MAC Address',
                                    'src_port': 'Port', 'src_service': 'Service'}

            """
            Prepare final dict, remap keys to be artifact types
            Remove empty values 
            """
            return self.parse_for_artifacts(keys_to_artifact_map, unformatted_artifact_dict)

    def parse_for_email_artifacts(self, search_result):
        # Check if the network_connection object is present
        if 'email' in search_result:
            email_payload = search_result['email']

            # All the keys we want to extract from the schema
            email_keys = ['header_subject', 'header_from', 'smtp_to', 'sender_ip']
            # Using dictionary comprehension to gather the attributes we want into a new dict
            unformatted_artifact_dict = {key: email_payload.get(key, None) for key in email_keys}

            # After first dict comprehension we have a dict of artifacts
            # smtp_to is usually a list, convert to a string of all recipients as dict can only have one smtp_to key
            if 'smtp_to' in unformatted_artifact_dict and type(unformatted_artifact_dict['smtp_to']) is list:
                unformatted_artifact_dict['smtp_to'] = ''.join(unformatted_artifact_dict['smtp_to'])
            # Next step is to remap the keys to match resilient artifact types
            keys_to_artifact_map = {'header_subject': 'Email Subject', 'header_from': 'Email Sender',
                                    'smtp_to': 'Email Recipient', 'sender_ip': 'IP Address'}

            """
            Prepare final dict, remap keys to be artifact types
            Remove empty values 
            """
            return self.parse_for_artifacts(keys_to_artifact_map, unformatted_artifact_dict)

    def parse_for_artifacts(self, keys_to_artifact_map, unformatted_artifact_dict):
        """
        A utility function which takes in 2 params and returns a formatted dict with Resilient Artifact names as keys

        :param keys_to_artifact_map:
        :param unformatted_artifact_dict:

        The keys_to_artifact_map contains the ICDx attribute names as keys and their corresponding Resilient Artifact Name as values
        unformatted_artifact_dict contains the event information gathered from ICDx.
        Unused values which wont be mapped are dropped by the time this dict is passed to the function

        Prepare a defaultdict with a value type of list
        This is because there is potentially more than 1 of a given Resilient Artifact type and we need to handle this
        A normal dict will overwrite any Resilient Artifact type with the second value as that is how dicts work
        Defaultdict allows us to continuously add items for a given Artifact type

        Before return, remove any keys which have a fasle-y value i.e empty values
        :return:
        """
        # First create a defaultdict data structure to hold the artifacts
        formatted_artifact_dictionary = defaultdict(list)
        # Set the default value k:v pair in the dict
        for val in keys_to_artifact_map.values():
            formatted_artifact_dictionary.setdefault(val, [])
        # Perform a dict comprehension to append each artifact to its representative key if the value is not null
        {keys_to_artifact_map[key]: formatted_artifact_dictionary[keys_to_artifact_map[key]].append(value) for
         key, value in
         unformatted_artifact_dict.items() if value is not None}

        return {k: v for k, v in formatted_artifact_dictionary.items() if (v)}

    def map_values(self, template_file, message_dict):
        """Map_Values is used to :
        Take in a forwarded Event from ICDx
        Import a Jinja template
        Map Event data to a new Incidents data including artifact data"""
        log.debug("Attempting to map message to an IncidentDTO. Message provided : {}".format(message_dict))
        with open(template_file, 'r') as template:

            incident_template = template.read()
            incident_data = template_functions.render(incident_template, message_dict)
            log.debug(incident_data)
            return incident_data

    def __init__(self, options):
        self.options = options


def add_methods_to_global():
    # Add ds_to_millis to global env so it can be used in filters
    ds_filter = {
        "ds_to_millis": ds_to_millis,
        "is_valid_ipv4_addr": is_valid_ipv4_addr,
        "is_valid_ipv6_addr": is_valid_ipv6_addr,
        "custom_regex_escape": regex_escape,
        "is_list": is_list,
        "represents_int": represents_int
    }
    env = environment()
    env.globals.update(ds_filter)


def ds_to_millis(val):
    """ A custom Jinja filter function which attempts to convert the input from a date/timestamp into milliseconds
    Expects either a full timestamp with Timezone (where the timezone will be stripped)
    or a datetime """
    if not val:
        return val
    try:
        ts = val[:23]

        ts_format = "%Y-%m-%dT%H:%M:%S.%f"
        dt = datetime.datetime.strptime(ts, ts_format)
        return calendar.timegm(dt.utctimetuple()) * 1000
    except Exception as e:
        return 0


def is_valid_ipv4_addr(ip):
    """ A custom Jinja filter function which determines if input is an IPV4 Address"""
    try:
        return isinstance(ipaddress.ip_address(ip), ipaddress.IPv4Address)
    except Exception as e:
        return False


def is_valid_ipv6_addr(ip):
    """ A custom Jinja filter function which determines if input is an IPV6 Address"""
    try:
        return isinstance(ipaddress.ip_address(ip), ipaddress.IPv6Address)
    except Exception as e:
        return False


def is_list(value):
    """ A custom Jinja filter function which determines if input is a list"""
    return isinstance(value, list)


def regex_escape(val):
    """ A custom Jinja filter function which helps to handle Windows FilePaths and escaping"""
    return val.replace('\\', r'\\')


def represents_int(s):
    """ A custom Jinja filter function which determines if a string input represents a number"""
    try:
        int(s)
        return True
    except ValueError:
        return False



