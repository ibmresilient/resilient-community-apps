# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
"""Function implementation"""

import logging
import json
import re
from .resilient_common import Resilient
from data_feeder_plugins.resilientfeed.lib.filters import Filters, parse_matching_criteria, MatchError
from data_feeder_plugins.resilientfeed.lib.db_sync_common import SyncRowError
from rc_data_feed.lib.feed import FeedDestinationBase, CriticalPluginError
from resilient_lib import str_to_bool

LOG = logging.getLogger(__name__)

# used for parsing owner or member values to return email addr: First Last (a@example.com)
USER_REGEX = re.compile(r".*\((.*\@.*)\)")
# remove xml identifier
XML_REGEX = re.compile(r"^<\?xml.*\?>(.*)")

# sync properties for an incident
DF_INC_ID = "df_inc_id"
DF_ORG_ID = "df_org_id"
DF_HOST = "df_host"
DF_ORIGINAL_CREATE_DATE = "df_create_date"

# number of errors to sync to the db before we close down the app
MAX_SYNC_ROW_ERRORS = 5

"""
This module contains the ResilientFeedDestination for writing Resilient data
to an instance of Resilient.
"""

class ResilientFeedDestination(FeedDestinationBase):  # pylint: disable=too-few-public-methods
    """Feed destination for writing Resilient data to a local directory."""
    def __init__(self, rest_client_helper, options):   # pylint: disable=unused-argument
        super(ResilientFeedDestination, self).__init__()
        self.options = options

        # incident fields to exclude
        self.exclude_fields = options.get("exclude_incident_fields", "").replace(" ", "").split(";")
        self.sync_references = str_to_bool(options.get("sync_reference_fields", "false"))
        self.delete_incidents = str_to_bool(options.get("delete_incidents", "false"))

        self.match_list, self.match_operator_and = parse_matching_criteria(options.get("matching_incident_fields", None),
                                                                           options.get("matching_operator", None))
        # role
        self.is_source = str_to_bool(options.get("sync_role_source", "true"))
        LOG.info(f"Sync role: {'source' if self.is_source else 'target'}")

        self.resilient_source = Resilient(options, rest_client_helper, self.is_source)
        self.resilient_target = Resilient(options, None, self.is_source)

        self.sync_error_count = 0

        # ensure that this combination of source and target do not represent a source/source relationship
        if self.is_source and not self.resilient_target.register_configuration(self.resilient_source.rest_client.base_url,
                                                                               self.resilient_source.rest_client.org_name):
            raise CriticalPluginError("source and destination environments are both configured to 'sync_role_source=true'")

    def send_data(self, context, payload):
        """
        synchronize an object between SOAR instances. Steps performed are:
        1) Convert id references to values
        2) Match incident filter criteria
        3) cleanup loads, removing fields identified
        4) Perform synchronization, create or update
        :param context:
        :param payload:
        :return: None
        """
        try:
            type_name = context.type_info.get_pretty_type_name()

            orig_type_id = payload.get('id', None)
            if context.is_deleted:
                _type_id = self.resilient_target.delete_type(self.resilient_source.rest_client.org_id, context.inc_id,
                                                             type_name, payload, orig_type_id, delete=self.delete_incidents)

                return

            # set up the criteria to accept incident synchronizing, if any
            matching_criteria = Filters(self.match_list, self.match_operator_and)

            # check for attachments and artifacts with attachments
            if type_name == "attachment" or (type_name == "artifact" and payload.get("attachment", None)):
                cleaned_payload = self.clean_payload(context.inc_id, type_name, payload)

                # determine if this is a task attachment
                _orig_task_id, _sync_task_id, mapped_type_name, _is_child_note = self.resilient_target._map_parent(self.resilient_source.rest_client.org_id, 
                                                                                                                   context.inc_id, type_name, payload)

                self.resilient_target.upload_attachment(self.resilient_source.rest_client,
                                                        self.resilient_source.rest_client.org_id, context.inc_id,
                                                        mapped_type_name, cleaned_payload, orig_type_id)
                return

            src_field_names = self.build_field_names(context, self._is_datatable(payload))
            # get target org field names
            target_field_names = self.resilient_target.get_type_info(type_name)

            # convert selection lists and multi-selection lists to values, not id's
            try:
                # make sure datatables exist in new org
                if self._is_datatable(payload) and not target_field_names:
                    LOG.warning("Discarding datatable not found in target org: %s", type_name)
                    return

                if self._is_datatable(payload):
                    new_payload = self.convert_datatable_values(src_field_names, payload)
                    discard_list = None
                else:
                    # get the fields for the target resilient
                    new_payload, discard_list = self.convert_values(matching_criteria, type_name,
                                                                    src_field_names, target_field_names,
                                                                    None, payload)

                # remove fields unrelated to creating/upgrading an object
                cleaned_payload = self.clean_payload(context.inc_id, type_name, new_payload)

                # convert artifact types so that always using the programmatic_name value
                if type_name == "artifact":
                    new_value = self.resilient_target.lookup_artifact_type(cleaned_payload["type"])
                    LOG.debug(f"Artifact type: {cleaned_payload['type']} -> {new_value}")
                    cleaned_payload["type"] = new_value

                # perform the creation or update in the new resilient org
                new_id, opr_type = self.resilient_target.create_update_type(self.resilient_source.rest_client.org_id, context.inc_id,
                                                                            type_name, cleaned_payload, orig_type_id)

                addl_create_list = []
                # create a note for the downstream incident when created
                if new_id and opr_type == "created" and type_name == "incident":
                    note = f"Incident created from \nHost:{self.resilient_source.get_source_host()}\nOrg {self.resilient_source.rest_client.org_id}\nIncident {context.inc_id}"
                    if discard_list:
                        discard_fields = '\n'.join(discard_list)
                        note = f"{note}\n\nDiscarded fields: \n{discard_fields}"

                    payload = {
                        "text": {
                            "format": "text",
                            "content": note
                        }
                    }
                    sync_inc_id, new_type_id = self.resilient_target._create_type(new_id, None, "note", payload)
                    if sync_inc_id:
                        addl_create_list.append(f"note:{new_type_id}")

                # retry any types which are dependent on this created object
                if new_id:
                    retry_create_list = self.retries(self.resilient_source.rest_client.org_id,
                                                    context.inc_id,
                                                    type_name)
                    addl_create_list.extend(retry_create_list)

                new_id and LOG.debug("%s:%s %s, additional updates: %s", type_name, new_id, opr_type, addl_create_list)
            except MatchError as err:
                LOG.info("%s on Incident %s", err, context.inc_id)

                # create a sync entry so we know we skipped this incident
                self.resilient_target.dbsync.create_sync_row(self.resilient_source.rest_client.org_id, context.inc_id,
                                                            type_name, orig_type_id,
                                                            None, None, "filtered")
            self.sync_error_count = 0 # reset the consecutive counter
        except SyncRowError as err:
            self.sync_error_count += 1  # track consecutive errors
            # critical issue when app fails db updates. This is remove the plugin
            # from execution.
            if self.sync_error_count > MAX_SYNC_ROW_ERRORS:
                raise CriticalPluginError(err) from err

    def retries(self, orig_org_id, orig_inc_id, type_name):
        """This function performs retries against incident objects, tasks, artifacts, notes, etc.
        which were requeued until the incident object was successfully sync'd to the target SOAR.
        Syncing of these objects will continue for all objects related to that incident. Requeueing
        is possible if synchronization fails for any reason.

        :param orig_org_id: original org_id
        :type orig_org_id: int
        :param orig_inc_id: original incident_id
        :type orig_inc_id: int
        :param type_name: 'incident' or 'task' as tasks can have notes which require the task to be in place first
        :type type_name: str
        :return: list of all objects sync'd with their related target object_id
        :rtype: list
        """
        retry_create_list = []
        # determine if there are any retries needed
        retry_list = self.resilient_target.dbsync.find_retry_rows(orig_org_id, orig_inc_id,
                                                                  self.resilient_target.return_type_parent(type_name, type_name))
        # retry any object queued for retry based on a dependency
        # this can occur when tasks show up in msg destination before the incident
        #   and artifacts that have parent artifacts
        for retry_item in retry_list:
            # org1_type_id(0), org2_inc_id, org1_dep_type_name, org1_dep_type_id, payload, retry_count
            retry_orig_id = retry_item[0]
            retry_sync_inc_id = retry_item[1]
            retry_type_name = retry_item[2]

            retry_payload = json.loads(retry_item[4]) # deserialize the payload back to json
            retry_count = retry_item[5]

            LOG.info('retrying %s:%s->%s to %s:%s (%s)',
                     orig_inc_id, retry_type_name, retry_orig_id,
                     self.resilient_target.rest_client.org_id, retry_sync_inc_id,
                     retry_count)
            if "attachment" in retry_type_name:
                new_type_id = self.resilient_target.upload_attachment(self.resilient_source.rest_client,
                                                            orig_org_id, orig_inc_id,
                                                            retry_type_name, retry_payload, retry_orig_id)
            else:
                # org1_type_id, org2_inc_id, org1_dep_type_name, org1_dep_type_id, payload
                new_type_id, _ = self.resilient_target.create_update_type(orig_org_id, orig_inc_id,
                                                            retry_type_name, retry_payload,
                                                            retry_orig_id, retry_count=retry_count)

            if new_type_id:
                retry_create_list.append(f"{retry_type_name}:{new_type_id}")

        return retry_create_list

    def _is_datatable(self, payload):
        """
        Return boolean regarding object if a datatable
        :param payload:
        :return: True if datatable
        """
        return bool(payload.get("table_name", None))

    def convert_datatable_values(self, src_field_names, payload):
        # Assisted by WCA@IBM
        # Latest GenAI contribution: ibm/granite-20b-code-instruct-v2
        """
        This function converts numeric Ids (such as owner_id) the related value.

        :param src_field_names: A dictionary containing information about the
                                incident, task, note, etc. fields, 
                                including their names and input types.
        :param payload: The payload containing the values of Ids.
        :type: dict

        :return: A dictionary containing the converted values 
        :rtype: dict
        """
        new_fields = {}
        cells = payload['cells']
        for field in cells:
            # datatable column names need to be looked up differently based on cell Id
            if src_field_names.get(field, {}).get('name', None):
                field_key = src_field_names[field]['name']
                if src_field_names[field]['input_type'] in ('select', 'multiselect'):
                    new_value = {"value": self.convert_selects(field_key, cells[field].get('value', None),
                                                               src_field_names[field])}
                else:
                    new_value = {"value": cells[field].get('value', None)}

                new_fields[field_key] = new_value

        return {"cells": new_fields}

    def clean_mismatched_values(self, src_field_names, target_field_names, field_key, new_value):
        """Make sure all values from source org exist in the target org.
        For value not found, return None. If a multiselect field, the value(s) not found are removed.

        :param src_field_names: all fields in the source org
        :type src_field_names: dict
        :param target_field_names: all fields in the target org
        :type target_field_names: dict
        :param field_key: field to review
        :type field_key: str
        :param new_value: value intended for 'field_key' in target org
        :type new_value: [str, bool, int]
        :return: new values
        :rtype: [str, bool, int, list]
        """
        if field_key != "plan_status":
            if src_field_names[field_key]['input_type'] == 'select':
                matched_value = next((item['label'] \
                    for item in target_field_names.get(field_key, {}).get('values', []) if item['label'] == new_value), None)
                if matched_value != new_value:
                    LOG.warning("Select field/value %s/%s does not exist in target organization, replacing it with None", field_key, new_value)
                    return None

            elif src_field_names[field_key]['input_type'] == 'multiselect':
                new_values = []
                for val in new_value:
                    new_val = next((item['label'] for item in target_field_names.get(field_key, {}).get('values', []) if item['label'] == val), None)
                    if new_val == val:
                        new_values.append(val)
                    else:
                        LOG.warning("Multiselect field/value %s/%s does not exist in target organization, replacing it with None", field_key, val)
                return new_values

        return new_value

    def convert_values(self, matching_criteria, type_name,
                       src_field_names, target_field_names,
                       prefix, payload):
        """
        recursive function to convert Ids to values for a given object
        raise MatchError if the matching criteria for an incident fails
        :param matching_criteria: criteria to determine if this incident is allowed
        :param type_name: type of object converting
        :param src_field_names: type definition for the source org
        :param target_field_names: type definition for the target org
        :param prefix: hierarchical fields have prefixes (incident)
        :param payload:
        :return: converted payload, discard_list of custom fields not sync'd
        """
        new_payload = {}

        # walk the payload, converting any list or ID based field with the appropriate value(s)
        discarded_fields = []
        for field in payload:
            field_key = field
            new_value = payload[field]

            if field in src_field_names:
                if src_field_names[field]['input_type'] in ('select', 'multiselect', 'select_owner', 'multiselect_members') \
                    and src_field_names[field].get('prefix', prefix) == prefix:
                    new_value = self.convert_selects(field_key, payload[field], src_field_names[field])

                    # remove select/multi-select fields which don't exist in the new org
                    if type_name == "incident":
                        new_value = self.clean_mismatched_values(src_field_names, target_field_names, field_key, new_value)
            # category header (pii, properties, gdpr, etc.)?
            elif isinstance(payload[field], dict):
                # recurse over this dictionary
                new_value, discarded = self.convert_values(matching_criteria, type_name,
                                                           src_field_names, target_field_names,
                                                           field, payload[field])
                discarded_fields.extend(discarded)

            if type_name == "incident":
                # apply logic to determine if the incident should be created
                if not matching_criteria.match_payload_value(field_key, new_value):
                    msg = f"Match exclusion for field: '{field_key}', value: {new_value}"
                    raise MatchError(msg)
                # ensure custom fields exist
                if prefix == "properties" and field_key not in target_field_names:
                    # field not found on target org, we will discard
                    LOG.warning("Discarding custom field not found in target org: %s", field_key)
                    discarded_fields.append(field_key)
                    continue

            new_payload[field_key] = new_value

        return new_payload, discarded_fields

    def convert_selects(self, field_key, orig_values, type_info):
        """
        convert select and mutliselects IDs into values
        :param field_key: name of field
        :param orig_values: list or value
        :param type_info: schema for field with all values possible
        :return: converted list or value
        """
        # plan_status is special as the value "C|A" should not be converted
        if field_key == "plan_status":
            return orig_values

        if field_key == "members":
            # members need to be looked up against the list of users in the system
            if isinstance(orig_values, dict):
                member_list = orig_values["values"].keys()
            elif isinstance(orig_values, list):
                member_list = orig_values
            else:
                member_list = []

            new_members = []
            for member_id in member_list:
                email_member = self.resilient_source.get_users_by_user_id(int(member_id))
                if email_member:
                    new_members.append(email_member)

            return new_members

        # recreate the list of values, dropping any not found
        if isinstance(orig_values, list):
            new_value = []
            for item in orig_values:
                found = False
                for value in type_info['values']:
                    if value['value'] == item:
                        replacement_value = self._clean_assignee_value(type_info['input_type'], capture_email(value['label']))
                        new_value.append(replacement_value)
                        found = True
                        break

                if not found and item:
                    LOG.warning("Substitute value: %s not found for field: %s, omitting", item, field_key)

        # recurse over dictionaries
        elif isinstance(orig_values, dict):
            if orig_values.get('name', None):
                new_value = self._clean_assignee_value(type_info['input_type'], orig_values.get('name'))

        else:
            found = False
            new_value = orig_values
            for value in type_info['values']:
                if value['value'] == orig_values:
                    new_value = self._clean_assignee_value(type_info['input_type'], capture_email(value['label']))
                    found = True
                    break

            if not found and new_value:
                LOG.warning("Substitute value: %s not found for field: %s, omitting", new_value, field_key)
                new_value = None

        return new_value

    def clean_payload(self, orig_inc_id, type_name, payload):
        """
        remove fields which will be problematic if passed on and perform clean up for API submission
        :param orig_inc_id: original incident id
        :param type_name: type of object
        :param payload: dictionary
        :return: dictionary of cleaned payload
        """
        orig_org_id = payload.get("org_id", None)
        _orig_type_id = payload.pop("id", None)

        # incident
        for pop_field in ["org", "org_name", "workspace"]:
            payload.pop(pop_field, None)

        if payload.get("assessment"):
            payload["assessment"] = clean_xml(payload["assessment"])

        if payload.get("pii", {}).get("assessment"):
            payload["pii"]["assessment"] = clean_xml(payload["pii"]["assessment"])

        # Task
        for pop_field in ["inc_owner_id", "reng_version", "at_id", "creator_principal", "creator"]:
            payload.pop(pop_field, None)

        if isinstance(payload.get("phase_id", None), dict):
            payload["phase_id"].pop("id", None)
        if isinstance(payload.get("category_id", None), dict):
            payload["category_id"].pop("id", None)

        # fields which are rich text requiring new formats
        for field_name in ["instructions", "description"]:
            if payload.get(field_name) and not isinstance(payload.get(field_name), dict):
                payload[field_name] = {
                    "format": "html",
                    "content": payload.get(field_name)
                }

        if type_name == "incident":
            payload = exclude_incident_fields(self.exclude_fields, payload)

            if self.sync_references and self.is_source:
                self.add_sync_fields(orig_org_id, orig_inc_id, payload)

        elif type_name in ("artifact", "note") and payload.get("parent_id", None):
            # make the artifact type an api style name as custom artifact types are only supported this way
            #todo custom artifact types do not sync as the api name of the artifact is not visible in /types

            # find the parent Id as it's been moved
            # failures to find parent_id will requeue for retry later
            _, target_parent_id, sync_state, _sync_source_role = \
                self.resilient_target.dbsync.find_sync_row(self.resilient_source.rest_client.org_id, orig_inc_id,
                                                           type_name, payload.get("parent_id"))

            if target_parent_id and sync_state == "active":
                payload["parent_id"] = target_parent_id

        return payload

    def add_sync_fields(self, orig_org_id, orig_inc_id, payload):
        """Certain tracking fields should be added to every incident
    
        :param orig_org_id: source
        :type orig_org_id: int
        :param orig_inc_id: source org incident id
        :type orig_inc_id: int
        :param payload: incident fields to sync to destination org
        :type payload: dict

        :return updated payload with tracking fields added
        :rtype dict
        """
        payload["properties"][DF_ORG_ID] = orig_org_id
        payload["properties"][DF_INC_ID] = orig_inc_id
        payload["properties"][DF_HOST] = self.resilient_source.get_source_host()
        payload["properties"][DF_ORIGINAL_CREATE_DATE] = payload.get("create_date", 0)

        return payload

    def _clean_assignee_value(self, input_type, email):
        """
        parse out the string "First Last (a@example.com)" to return only email portion.
        This applies only to select_owner and multiselect_members
        :param input_type:
        :param email:
        :return: value if not input type match or email address
        """
        if input_type not in ('select_owner', 'multiselect_members', 'user'):
            return email

        # confirm that this user is in the target organization, if not return none
        target_users = self.resilient_target.get_users_and_groups()
        if email not in target_users:
            LOG.warning("User/Group '%s' does not exist in target organization: %s", email, target_users)
            return None

        return email

    def filter_nulls(self, payload):
        """
        instance method
        remove key values pairs where value is null, resilient cannot index these
        :param payload:
        :return: new_payload
        """
        new_payload = dict((key, value) for key, value in payload.items() if value)
        return new_payload

    def build_field_names(self, context, is_datatable):
        """return all object field definitions in a key/value format

        :param context: _description_
        :type context: object
        :param is_datatable: true if returning information about a datatable
        :type is_datatable: bool
        :return: all object schema field definitions
        :rtype: dict
        """
        # get all the field definitions from the source environment
        all_fields = context.type_info.get_all_fields(refresh=False)

        # invert the list into a dictionary for faster review
        # data tables use the cell id for the column name. So we need to create the index list differently
        if is_datatable:
            src_field_names = {str(field['id']):field for field in all_fields}
        else:
            src_field_names = {field['name']:field for field in all_fields}

        return src_field_names

# S T A T I C
def capture_email(value):
    # select_owner or multiselect_members
    match = USER_REGEX.match(value)
    if match:
        return match.group(1)       # just email address

    return value

def clean_xml(value):
    # remove xml header for data that follows
    match = XML_REGEX.match(value)
    if match:
        return match.group(1)

    return value

def exclude_incident_fields(exclude_fields, payload):
    """
    exclude incident fields from an incident
    :param exclude_fields - list of fields to exclude
    :param payload:
    :return: payload with excluded fields removed
    """
    new_payload = {}

    for field in payload.keys():
        if field not in exclude_fields:
            if isinstance(payload[field], dict):
                new_payload[field] = exclude_incident_fields(exclude_fields, payload[field])
            else:
                new_payload[field] = payload[field]
        else:
            LOG.debug("Excluding field: %s", field)

    return new_payload
