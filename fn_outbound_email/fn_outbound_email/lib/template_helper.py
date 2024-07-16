# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=line-too-long

from logging import getLogger
from re import compile, split
from time import time
from jinja2 import Environment, FileSystemLoader
from os import path
from datetime import datetime
from operator import itemgetter
from six import string_types
from resilient_lib import build_incident_url, build_task_url

LOG = getLogger(__name__)

CONFIG_DATA_SECTION = 'fn_outbound_email'
TEMPLATES_SECTION = f"{CONFIG_DATA_SECTION}:templates"

class TemplateHelper(object):
    def __init__(self, resilient_component):
        """Initialize the Template services."""

        self.component = resilient_component
        self.rest_client = self.component.rest_client()

        self.choices = {}
        self.extends = None
        self.field_defs = None

    def get_datatable(self, datatable_name, incident_id, html=True):
        """datatable jinja template"""
        LOG.info('get_datatable: (%s) (%s)', datatable_name, incident_id)
        try:
            datatable = self.rest_client.get(
                f"/incidents/{incident_id}/table_data/{datatable_name}?"
                "handle_format=names&text_content_output_format=objects_no_convert")
        except:
            LOG.error("The datatable %s doesn't exist", datatable_name)
            return '-'

        if not datatable:
            # failed to find the datatable with that name
            LOG.error("The datatable name %s doesn't match", datatable_name)
            return

        table_def = self.rest_client.get(
            f"/types/{datatable.get('id')}?handle_format=objects&text_content_output_format=objects_no_convert")

        # sort the fields by their display order
        field_list = []
        for _field_def_key, field_def in table_def.get("fields", []).items():
            field_list.append(field_def)
        table_def["fields"] = sorted(field_list, key=itemgetter('order'))

        if html:
            #Create path to data/templates on local system
            cpath = path.dirname(__file__)
            local_template_file_path = path.join(cpath[0:len(cpath) - cpath[::-1].index(path.normpath("/")) - 1], path.normpath('data/templates/'))

            #Create dictionary named tables that stores the datatable
            tables = { str(field_name.get("text")): [] for field_name in table_def.get('fields', []) }

            for header in tables:
                for row in datatable.get('rows', []):
                    rows = row.get('cells')
                    for cells in rows:
                        for field_name in field_list:
                            if str(header) == str(field_name.get('text')):
                                if str(field_name.get('name')) == str(cells).lower():
                                    tables[header].insert(datatable.get('rows').index(row), self.get_value_as_string(field_name, rows[cells].get("value")))

            #Load the path to the datatable.jinja file
            env = Environment(loader=FileSystemLoader(searchpath=local_template_file_path), autoescape=True)
            template = env.get_template('datatable.jinja')
            return template.render(table_name=table_def.get('display_name'), headers=table_def.get('fields'), rows=datatable.get('rows'), table=tables)

        return datatable

    # returns an HTML-formatted table based on the query result
    def get_query_result(self, query_conditions, want_fields_list, exclude_incidents):
        LOG.info('get_query_result')
        conditions = {"filters": [{"conditions": query_conditions}],
                      "sorts": [{"field_name": "create_date", "type": "desc"}]}

        query_result = self.rest_client.post(
            "/incidents/query_paged?handle_format=objects&text_content_output_format=objects_no_convert", conditions)

        row_list = []

        for incident in query_result.get("data", []):
            if incident.get("id") not in exclude_incidents:
                incident = self.rest_client.get(f"/incidents/{incident.get('id')}")
                row = {}
                for want_field in want_fields_list:
                    field_value = self.get_incident_value(incident, want_field)
                    row[want_field] = field_value

                row_list.append(row)

        mytemplate = self.component.jinja_env.get_template("query_result.jinja")
        field_defs = dict((field.get("name"), field) for field in self.component.get_incident_fields())
        return mytemplate.render(row_list=row_list,
                                 want_field_list=want_fields_list,
                                 field_defs=field_defs)

    def get_field_defs(self, type_name):
        if not self.field_defs:
            self.field_defs = self.rest_client.get('/types?handle_format=names')

        return self.field_defs.get(type_name, {}).get('fields')

    def get_incident_value(self, incident, field_name):

        field_def = self.get_field_defs('incident').get(field_name)

        if not field_def:
            LOG.error("Tried to get invalid field value: %s", field_name)
            return

        if field_def.get("prefix"):
            field_value = incident.get(field_def.get("prefix"), {}).get(field_name)
        else:
            field_value = incident.get(field_name)

        return self.get_value_as_string(field_def, field_value)

    def get_artifacts(self, artifacts):
        # return list of artifacts
        return artifacts.get("data")

    # helper function to get child notes recursively
    # takes top level comment and returns a list of all the children and nested children
    def notes_helper(self, p, ret):
        # base case: comment has no children
        if not p.get("children"):
            return ret

        # for each note, get all the children
        for c in p.get("children"):
            ret.append(c)
            self.notes_helper(c, ret)

    def get_notes(self, notes, get_children):
        # returns a list of note objects
        all_notes = []
        # get the top level comments
        for root_parent in notes.get("root_comments"):
            str_to_check = "email sent if mail server is valid"     # gets added in post-processing script note
            if str_to_check not in root_parent.get("text", "").lower():
                all_notes.append(root_parent)
                # to get nested child notes, execute recursive function
                if get_children:
                    self.notes_helper(root_parent, all_notes)
        return all_notes

    # gets the values for the specified field across all rows and returns as comma-separated list
    def get_datatable_value_array(self, inc_id, datatable_name, field_name):
        LOG.info('get_datatable_value_array (%s) (%s) (%s)', inc_id, datatable_name, field_name)
        try:
            datatable = self.rest_client.get(
                f"/incidents/{inc_id}/table_data/{datatable_name}?"
                "handle_format=names&text_content_output_format=objects_no_convert")
        except:
            # if the datatable doesn't "exist", it returns error
            LOG.error("The datatable %s doesn't exist", datatable_name)
            return '-'

        table_def = self.rest_client.get(
            f"/types/{datatable.get('id')}?handle_format=objects&text_content_output_format=objects_no_convert")

        result = set()
        for table_row in datatable["rows"]:
            result.add(self.get_datatable_value(field_def=table_def.get("fields", {}).get(field_name),
                                                          table_row=table_row))

        return ', '.join(result)

    def get_datatable_value(self, field_def, table_row):
        field_value = table_row.get("cells", {}).get(field_def.get('name'), {}).get('value')

        return self.get_value_as_string(field_def, field_value)

    def get_value_as_string(self, field_def, field_value):
        if not field_value and not isinstance(field_value, (int, float)):
            return

        if field_def['input_type'] == 'multiselect':
            # join the values, and escape it
            simple_list = list(
                (select_val.get("name") if isinstance(select_val, dict) else select_val) for select_val in field_value)
            ret_value = ', '.join(simple_list)
        elif field_def.get('input_type') in ['datepicker', 'datetimepicker']:
            # format the date and escape it
            ret_value = self.format_timestamp(field_value)
        elif field_def.get('input_type') == "textarea":
            if not isinstance(field_value, dict):
                ret_value = field_value
            elif field_value.get('format') == "text":
                # plain text, escape it
                ret_value = field_value.get("content")
            else:
                # HTML value, so return it without escaping
                return field_value.get("content")
        elif field_def.get('input_type') == "number":
            ret_value = str(field_value)
        else:
            # unknown field type, or type which doesn't require special handling
            ret_value = str(field_value)

        # html escape the return value
        return ret_value

    @staticmethod
    def regex_replace(string, pattern, replace):
        p = compile(pattern)
        return p.sub(replace, string)

    @staticmethod
    def get_timestamp(offset=0):
        return int(round(time() + offset))

    # format_timestamp() has changed in version 1.0.7.
    # This function now takes EPOCH time in seconds as an argument. If formatting a Resilient date/time field,
    # divide it by 1000, first, in the JINJA template.
    def format_timestamp(self, value: int):
        # converts resilient epoch timestamp to string
        # 2018-06-03T11:57:02Z
        # https://en.wikipedia.org/wiki/ISO_8601
        date_format = self.component.options.get('date_format')
        date_object = datetime.fromtimestamp(value / 1000)
        if not date_format:
            return date_object.isoformat()

        return date_object.strftime(date_format)

    def get_action_field_value(self, action_data, field_name):
        field_def = self.get_field_defs('actioninvocation').get(field_name)
        if not field_def:
            LOG.error('action field name (%s) invalid', field_name)
            return

        action_def_value_list = field_def.get('values')
        if not action_def_value_list:
            LOG.error('action field not a list type: (%s)', field_name)
            return

        for action_def_value in action_def_value_list:
            if action_def_value.get('value') == action_data.get('properties', {}).get(field_name):
                return action_def_value.get('label')

    @staticmethod
    def get_list_from_string(str_value):
        if not str_value:
            return []

        if isinstance(str_value, string_types):
            list_result = set()
            for list_value in split(r'[,; ]', str_value):
                list_value = list_value.strip()
                if list_value:
                    list_result.add(list_value)
        elif isinstance(str_value, (list, tuple)):
            list_result = str_value
        else:
            LOG.warning('Unexpected list type (%s) for (%s)', type(str_value).__name__, str_value)
            list_result = str_value

        return list_result

    def generate_incident_url(self, inc_id):
        org_id = self.rest_client.org_id
        return build_incident_url(self.rest_client.base_url, inc_id, org_id)


    def generate_task_url(self, inc_id, task_id):
        org_id = self.rest_client.org_id
        return build_task_url(self.rest_client.base_url, inc_id, task_id, org_id)

def get_template(app_config, template_name):
    """_summary_

    Args:
        app_config (dict): all sections in app.config
        template_name (str): name of template to use

    Returns:
        str: entire template to use read from disk
    """
    template_path = _get_template_path(app_config.get(TEMPLATES_SECTION, {}), template_name)
    LOG.debug("Template name: %s = %s", template_name, template_path)
    if template_path:
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()

def _get_template_path(app_config, template_name):
    """_summary_

    Args:
        app_config (dict): template section in app.config
        template_name (str): name of template to use

    Returns:
        str: path to template file on disk
    """
    template_name = template_name.lower()
    template_file_path = None
    if app_config and template_name:
        if template_name not in app_config:
            LOG.error("Template name '%s' not found.", template_name)
            return

        # determine if a relative path or an absolute path
        template_file_path = app_config.get(template_name)
        if not path.isabs(template_file_path): # absolute
            cpath = path.dirname(__file__)
            template_file_path = path.join(cpath[0:len(cpath) - cpath[::-1].index(path.normpath("/")) - 1], path.normpath(template_file_path))

        if not path.exists(template_file_path):
            LOG.error("Template file path '%s' not found.", template_file_path)
            return

    return template_file_path

def get_template_names(opts):
    """get template names from the app.config file

    Args:
        opts (dict): all sections within app.config
    """
    templates = opts.get(TEMPLATES_SECTION)

    if templates:
        return templates.keys()
