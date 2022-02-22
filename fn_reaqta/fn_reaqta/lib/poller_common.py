# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import base64
import datetime
import functools
import logging
import os
import traceback
from ast import Return, literal_eval
from threading import Event
from resilient import SimpleHTTPException, Patch
from resilient_lib import IntegrationError, get_file_attachment, get_file_attachment_name
from cachetools import cached, LRUCache

LOG = logging.getLogger(__name__)

IBM_SOAR = "IBM SOAR" # common label
SOAR_HEADER = "Created by {}".format(IBM_SOAR)

TYPES_URI = "/types"
INCIDENTS_URI = "/incidents"
ARTIFACTS_URI = "/artifacts"
ARTIFACT_FILE_URI = "/".join([ARTIFACTS_URI, "files"])

# Directory of default templates
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "data")

def get_template_dir():
    # quick property to get template directory
    return TEMPLATE_DIR

# P O L L E R   L O G I C
def poller(named_poller_interval, named_last_poller_time, package_name):
    """[decorator for poller, manage poller time, calling the customized method for getting the next entities]

    Args:
        named_poller_interval ([str]): [name of instance variable containing the poller interval in seconds]
        named_last_poller_time ([datetime]): [name of instance variable containing the lookback value in mseconds]
        package_name ([str]: [name of package for loggging]
    """
    def poller_wrapper(func):
        # decorator for running a function forever, passing the ms timestamp of
        #  when the last poller run to the function it's calling
        @functools.wraps(func)
        def wrapped(self):
            last_poller_time = getattr(self, named_last_poller_time)
            exit_event = Event()

            while not exit_event.is_set():
                try:
                    LOG.info(u"%s polling start.", package_name)
                    poller_start = datetime.datetime.now()
                    # function execution with the last poller time in ms
                    func(self, last_poller_time=int(last_poller_time.timestamp()*1000))

                except Exception as err:
                    LOG.error(str(err))
                    LOG.error(traceback.format_exc())
                finally:
                    LOG.info(u"%s polling complete.", package_name)
                    # set the last poller time for next cycle
                    last_poller_time = poller_start

                    # sleep before the next poller execution
                    exit_event.wait(getattr(self, named_poller_interval))
            exit_event.set() # loop complete

        return wrapped
    return poller_wrapper

class SOARCommon():
    """ common methods for accessing IBM SOAR cases and their entities: comment, attachments, etc. """
    def __init__(self, rest_client):
        self.rest_client = rest_client

    def get_soar_case(self, search_fields, open_cases=True):
        """Find a SOAR case which contains custom field(s) associated with the associated endpoint

        Args:
            search_fields [dict]: [dictionary containing key/value pairs to search for a case match]
                                  field values can be True/False for 'has_a_value' or 'does_not_have_a_value'
                                  Otherwise a field will use 'equals' for the value
            NOTE: search_fields only supports custom fields
            open_cases [bool]: [true if only querying open cases]

        Returns:
            case_info [dict]: [API results of the first case found or None]
            error_msg [str]: [error message if the query failed]
        """
        r_cases, error_msg = self.get_soar_cases(search_fields, open_cases=open_cases)
        if error_msg:
            return None, error_msg

        # return first case
        return (r_cases[0] if r_cases else None, None)

    def get_soar_cases(self, search_fields, open_cases=True):
        """ find all IBM SOAR cases which are associated with the endpoint platform
        Args:
            search_fields [dict]: list of field(s) used to track the relationship with a SOAR case
                                 field values can be True/False for 'has_a_value' or 'does_not_have_a_value'
                                 Otherwise a field will use 'equals' for the value
            NOTE: search_fields only supports custom fields

        Returns:
            soar_cases [list]: returned list of cases
            error_msg [str]: any error during the query or None
        """
        query = self._build_search_query(search_fields, open_cases=open_cases)

        return self._query_cases(query)

    def _build_search_query(self, search_fields, open_cases=True):
        """[Build the json structure needed to search for cases]

        Args:
            search_fields ([dict/list]): [key/value pairs to search custom fields with specific values. If
                                         a value contains "*" then a search is used with 'has_a_value']
            NOTE: search_fields works on custom fields

        Returns:
            query_string ([dict]): [json stucture used for cases searching]
        """
        query = {
            "filters": [{
                "conditions": [
                 ]
            }],
            "sorts": [{
                "field_name": "create_date",
                "type": "desc"
            }]
        }

        if open_cases:
            field_search = {
                            "field_name": "plan_status",
                            "method": "equals",
                            "value": "A"
                          }
            query['filters'][0]['conditions'].append(field_search)

        if isinstance(search_fields, dict):
            for search_field, search_value in search_fields.items():
                field_search = {
                            "field_name": "properties.{0}".format(search_field)
                        }
                if isinstance(search_value, bool):
                    field_search['method'] = "has_a_value" if search_value else "does_not_have_a_value"
                else:
                    field_search['method'] = "equals"
                    field_search['value'] = search_value

                query['filters'][0]['conditions'].append(field_search)

        return query

    def _query_cases(self, query):
        """ run a query to find case(s) which match the query string

        Args:
            query [str]: query string to find cases

        Returns:
            query_results [list]: List of query results
        """
        query_uri = "/".join([INCIDENTS_URI, "query?return_level=normal"])

        try:
            return self.rest_client.post(query_uri, query), None
        except SimpleHTTPException as err:
            LOG.error(str(err))
            LOG.error(query)
            return None, str(err)

    def create_soar_case(self, case_payload):
        """
        Create a new IBM SOAR case based on a payload formatted for the API call
        Args:
            case_payload [dict]: fields to use for creating a SOAR case

        Returns:
            case [dict]: created case
        """
        try:
            # Post case to IBM SOAR
            case = self.rest_client.post(INCIDENTS_URI, case_payload)
            return case
        except Exception as err:
            LOG.error(str(err))
            raise IntegrationError from err

    def update_soar_case(self, case_id, case_payload):
        """
        Update a IBM SOAR case by rendering a jinja2 template
        :param case_payload: inciednt fields to update (json object)
        :return: IBM SOAR case
        """
        try:
            result = self._patch_case(case_id, case_payload)
            return result

        except Exception as err:
            LOG.error(str(err))
            raise IntegrationError from err

    def _patch_case(self, case_id, case_payload):
        """ _patch_case will update an case with the specified json payload.
        :param case_id: case ID of case to be updated.
        ;param case_payload: case fields to be updated.
        :return:
        """
        try:
            # Update case
            case_url = "/".join([INCIDENTS_URI, str(case_id)])
            case = self.rest_client.get(case_url)
            patch = Patch(case)

            # Iterate over payload dict.
            for name, _ in case_payload.items():
                if name == 'properties':
                    for field_name, field_value in case_payload['properties'].items():
                        patch.add_value(field_name, field_value)
                else:
                    payload_value = case_payload.get(name)
                    patch.add_value(name, payload_value)

            patch_result = self.rest_client.patch(case_url, patch)
            result = self._chk_status(patch_result)
            # add back the case id
            result['id'] = case_id
            return result

        except Exception as err:
            LOG.error(str(err))
            raise IntegrationError from err

    def create_case_comment(self, case_id, entity_comment_id, entity_comment_header, note):
        """
        Add a comment to the specified SOAR case by ID
        :param case_id:  SOAR case ID
        :param entity_comment_id: entity comment id (or None)
        :param entity_comment_header: identifier for comment as synchronized from another system
        :param note: Content to be added as note
        :return: Response from SOAR
        """
        try:
            uri = "/".join([INCIDENTS_URI, str(case_id), "comments"])
            if entity_comment_header:
                comment = "<b>{} ({}):</b><br>{}".format(entity_comment_header, entity_comment_id, note)
            else:
                comment = note

            note_json = {
                'format': 'html',
                'content': comment
            }
            payload = {'text': note_json}

            return self.rest_client.post(uri=uri, payload=payload)

        except Exception as err:
            LOG.error(str(err))
            raise IntegrationError from err

    def create_datatable_row(self, case_id, datatable, rowdata):
        """create a row in a SOAR case datatable

        Args:
            case_id (int): case containing the datatable
            datatable (str): name of datatable
            rowdata (dict): columns and values to add

        Returns:
            None
        """
        uri = "/".join([INCIDENTS_URI, str(case_id), "table_data", datatable, "row_data"])
        return self.rest_client.post(uri=uri, payload=rowdata)

    def create_artifact(self, rest_client, incident_id, artifact_type, artifact_value, description, send_file=False):
        """create an artifact"""
        try:
            artifact_uri = "/".join([INCIDENTS_URI, incident_id, ARTIFACTS_URI])

            # set up Artifact payload skeleton
            artifact_payload = {
                'type': {
                    'name': artifact_type,
                },
                'description': {
                    'format': description,
                }
            }

            if send_file:
                artifact_uri = "/".join([artifact_uri, "files"])
                files=(
                    ('foo', (None, 'bar')),
                    ('foo', (None, 'baz')),
                    ('spam', (None, 'eggs')),
                )
            else:
                rest_client.post(artifact_uri, )



            # find artifacts that are already associated with this Incident
            existing_artifacts = self._find_resilient_artifacts_for_incident(incident_id)

            # loop through Artifacts provided with this Threat
            for artifact_id, artifact_type in artifacts.items():
                # if this Artifact doesn't match an existing value and type
                if artifact_id not in existing_artifacts or existing_artifacts[artifact_id] != artifact_type:
                    # populate payload with ID and type
                    artifact_payload['value'] = artifact_id
                    artifact_payload['type']['name'] = ARTIFACT_TYPE_API_NAME.get(artifact_type, "String")
                    artifact_payload['description']['content'] = artifact_type
                    # attach new Artifact to Incident
                    resilient_client.post(uri=artifact_uri, payload=artifact_payload)

        except SimpleHTTPException as ex:
            log.info(u'Something went wrong when attempting to create the Incident: {}'.format(ex))
            raise ex

    def get_case(self, case_id):
        """ get an SOAR case based on the case id """
        case = self._get_case_info(case_id, None)
        # create a new field of the incident_type_ids in label form
        case['case_types'] = self.lookup_incident_types(case['incident_type_ids'])
        return case

    def get_case_attachment(self, case_id, artifact_id=None, task_id=None, attachment_id=None, return_base64=True):
        """ get contents of a file attachment """
        file_content = get_file_attachment(self.rest_client, case_id, artifact_id=artifact_id, task_id=task_id, attachment_id=attachment_id)
        if return_base64:
            file_content = b_to_s(base64.b64encode(file_content))

        file_name = get_file_attachment_name(self.rest_client, case_id, artifact_id=artifact_id, task_id=task_id, attachment_id=attachment_id)
        return file_name, file_content

    def get_case_artifacts(self, case_id):
        """ get all case artifacts """
        return self._get_case_info(case_id, "artifacts")

    def get_case_comments(self, case_id):
        """ get all case comments """
        return self._get_case_info(case_id, "comments")

    def get_case_attachments(self, case_id):
        """ get all case attachments """
        attachments =  self._get_case_info(case_id, "attachments")
        for attachment in attachments:
            _, attachment['content'] = self.get_case_attachment(case_id, attachment_id=attachment['id'])

        return attachments

    def lookup_artifact_type(self, artifact_type):
        """ return an artifact type based on it's ID. If not found, return None """
        types = self._get_artifact_types()
        if artifact_type in types:
            return types[artifact_type]
        return None

    def lookup_incident_types(self, incident_type_ids):
        """ return an incident type based on it's ID. If not found, return None """
        if not incident_type_ids:
            return incident_type_ids

        types = self._get_incident_types()

        return [types[incident_type] for incident_type in incident_type_ids if incident_type in types]

    def _get_artifact_types(self):
        """ get all artifact types labels """
        return self._get_type("artifact", "type")

    def _get_incident_types(self):
        """ get all case_type_id labels """
        return self._get_type("incident", "incident_type_ids")

    def _get_resolution_types(self):
        """ get case resolution_types labels """
        return self._get_type("incident", "resolution_id")

    def _get_type(self, obj_type, lookup_field):
        """ get a specified SOAR field set of values, based on their ID (ex. status, incident_type_ids) """
        type_info = self._get_types(obj_type)

        # create a lookup table based on field name
        return { type['value']: type['label'] for type in type_info['fields'][lookup_field]['values'] }

    @cached(cache=LRUCache(maxsize=100))
    def _get_types(self, res_type):
        """ cached API call to get types information for a given type: case, artifact, etc. """
        uri = "/".join([TYPES_URI, res_type])
        return self.rest_client.get(uri)

    def _get_case_info(self, case_id, child_uri):
        """ API call for a given case and it's child objects: tasks, notes, attachments, etc. """
        try:
            uri = "/".join([INCIDENTS_URI, str(case_id)])
            if child_uri:
                uri = "/".join([uri, child_uri])

            response = self.rest_client.get(uri=uri)
            return response

        except Exception as err:
            raise IntegrationError from err

    def filter_soar_comments(self, case_id, entity_comments, soar_header=SOAR_HEADER):
        """
            need to avoid creating same IBM SOAR case comments over and over
              this logic will read all SOAR comments from a case
              and remove those comments which have already sync using soar_header as a filter

        Args:
            case_id ([str]): [IBM SOAR case id]
            entity_comments ([list]): [list comments which the endpoint's entity contains.
                                       This will be a mix of comments sync'd from SOAR and new comments]
            soar_header ([str]): [title added to SOAR comments to be filtered]
        Returns:
            new_comments ([list])
        """
        # get the SOAR case comments and capture only the text
        soar_comments = self.get_case_comments(case_id)
        soar_comment_list = [comment['text'] for comment in soar_comments]

        # filter entity comments with our SOAR header
        return self._filter_comments(self, soar_comment_list, entity_comments, filter_soar_header=soar_header)

    def _filter_comments(self, soar_comment_list, entity_comments, filter_soar_header=None):
        """
            need to avoid creating same IBM SOAR case comments over and over
              this logic will read all SOAR comments from a case
              and remove those comments which have already sync using soar_header as a filter

        Args:
            soar_comment_list ([list]): [list of text portion of a case's comments]
            entity_comments ([list]): [list comments which the endpoint's entity contains.
                                       This will be a mix of comments sync'd from SOAR and new comments]
            filter_soar_header ([str]): [title added to SOAR comments to be filtered]
        Returns:
            new_comments ([list])
        """

        if filter_soar_header:
            # filter entity comments with our SOAR header
            staged_entity_comments = [comment for comment in entity_comments \
                                        if filter_soar_header not in comment]
        else:
            staged_entity_comments = entity_comments.copy()

        # filter out the comments already sync'd to SOAR
        if soar_comment_list:
            new_entity_comments = [comment for comment in staged_entity_comments \
                if not any([comment in already_syncd for already_syncd in soar_comment_list])]

        return new_entity_comments

    def _chk_status(self, resp, rc=200):
        """
        check the return status. If return code is not met, raise IntegrationError,
        if success, return the json payload
        :param resp:
        :param rc:
        :return:
        """
        if hasattr(resp, "status_code"):
            if isinstance(rc, list):
                if resp.status_code < rc[0] or resp.status_code > rc[1]:
                    raise IntegrationError(u"status code failure: {0}".format(resp.status_code))
            elif resp.status_code != rc:
                raise IntegrationError(u"status code failure: {0}".format(resp.status_code))

            return resp.json()

        return {}


def s_to_b(value):
    """ string to bytes """
    try:
        return bytes(value, 'utf-8')
    except Exception:
        return value

def b_to_s(value):
    """ bytes to string """
    try:
        return value.decode()
    except Exception:
        return value

@cached(cache=LRUCache(maxsize=100))
def eval_mapping(eval_value, wrapper=None):
    """
    Args:
            eval_value ([str]): [json fragment to evaluate]
            wrapper ([str]): [values such as '[{}]' or '{{ {} }}']
        Returns:
            mapping ([list or dict]): converted data
    """
    if not eval_value:
        return None

    try:
        if wrapper:
            eval_value = wrapper.format(eval_value)

        # Try converting input to a dict or array
        result = literal_eval(eval_value)
        # expecting the result to be a list or dictionary
        if not isinstance(result, (list, dict)):
            raise IndentationError("Unexpected result: %s", result)

        return result

    except Exception as err:
        LOG.error(str(err))
        LOG.error(traceback.format_exc())
        LOG.error("""mapping eval_value must be a string representation of a (partial) array or dictionary e.g. "'value1', 'value2'" or "'key':'value'" """)

    return None
