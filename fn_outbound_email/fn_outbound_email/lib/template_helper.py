# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

import logging
from re import compile, split
from time import time
from jinja2 import Environment, FileSystemLoader
from os import path
from datetime import datetime
from operator import itemgetter
from six import string_types

LOG = logging.getLogger(__name__)

class TemplateHelper(object):
    def __init__(self, resilient_component):
        """Initialize the Template services."""

        self.component = resilient_component

        self.choices = {}
        self.extends = None
        self.field_defs = None

    def get_datatable(self, datatable_name, incident_id, html=True):
        """datatable jinja template"""
        LOG.info(
            'get_datatable: ({}) ({})'.format(datatable_name, incident_id))
        try:
            datatable = self.component.rest_client().get(
                "/incidents/{}/table_data/{}?"
                "handle_format=names&text_content_output_format=objects_no_convert".format(
                    incident_id, datatable_name))
        except:
            LOG.error("The datatable {} doesn't exist".format(datatable_name))
            return '-'

        if not datatable:
            # failed to find the datatable with that name
            LOG.error("The datatable name {} doesn't match".format(datatable_name))
            return

        table_def = self.component.rest_client().get(
            "/types/{}?handle_format=objects&text_content_output_format=objects_no_convert".format(
                datatable['id']))

        # sort the fields by their display order
        field_list = []
        for field_def_key, field_def in table_def["fields"].items():
            field_list.append(field_def)
        table_def["fields"] = sorted(field_list, key=itemgetter('order'))

        if html:
            #Create path to data/templates on local system
            cpath = path.dirname(__file__)
            local_template_file_path = path.join(cpath[0:len(cpath) - cpath[::-1].index("/") - 1], 'data/templates/')

            #Create dictionary named tables that stores the datatable
            tables = { str(field_name.get("text")): [] for field_name in table_def['fields'] }

            for header in tables:
                for row in datatable['rows']:
                    rows = row.get('cells')
                    for cells in rows:
                        for field_name in field_list:
                            if str(header) == str(field_name['text']):
                                if str(field_name['name']) == str(cells).lower():
                                    tables[header].insert(datatable['rows'].index(row), self.get_value_as_string(field_name, rows[cells].get("value")))

            #Load the path to the datatable.jinja file
            env = Environment(loader=FileSystemLoader(searchpath=local_template_file_path), autoescape=True)
            template = env.get_template('datatable.jinja')
            return template.render(table_name=table_def['display_name'], headers=table_def['fields'], rows=datatable['rows'], table=tables)
        else:
            return datatable

    # returns an HTML-formatted table based on the query result
    def get_query_result(self, query_conditons, want_fields_list, exclude_incidents):
        LOG.info('get_query_result')
        conditions = {"filters": [{"conditions": query_conditons}],
                      "sorts": [{"field_name": "create_date", "type": "desc"}]}

        query_result = self.component.rest_client().post(
            "/incidents/query_paged?handle_format=objects&text_content_output_format=objects_no_convert", conditions)

        row_list = []

        for incident in query_result["data"]:
            if incident["id"] not in exclude_incidents:
                incident = self.component.rest_client().get("/incidents/{}".format(incident["id"]))
                row = {}
                for want_field in want_fields_list:
                    field_value = self.get_incident_value(incident, want_field)
                    row[want_field] = field_value

                row_list.append(row)

        mytemplate = self.component.jinja_env.get_template("query_result.jinja")
        field_defs = dict((field["name"], field) for field in self.component.get_incident_fields())
        return mytemplate.render(row_list=row_list,
                                 want_field_list=want_fields_list,
                                 field_defs=field_defs
                                 )

    def get_field_defs(self, type_name):
        if not self.field_defs:
            self.field_defs = self.component.rest_client().get('/types?handle_format=names')

        return self.field_defs[type_name]['fields']

    def get_incident_value(self, incident, field_name):

        field_def = self.get_field_defs('incident').get(field_name)

        if not field_def:
            LOG.error("Tried to get invalid field value: " + field_name)
            return None

        if field_def.get("prefix"):
            field_value = incident[field_def["prefix"]].get(field_name)
        else:
            field_value = incident.get(field_name)

        return self.get_value_as_string(field_def, field_value)

    # gets the values for the specified field across all rows and returns as comma-separated list
    def get_datatable_value_array(self, inc_id, datatable_name, field_name):
        LOG.info(
            'get_datatable_value_array ({}) ({}) ({})'.format(inc_id, datatable_name,
                                                                                 field_name))
        try:
            datatable = self.component.rest_client().get(
                "/incidents/{}/table_data/{}?"
                "handle_format=names&text_content_output_format=objects_no_convert".format(
                    inc_id, datatable_name))
        except:
            # if the datatable doesn't "exist", it returns error
            LOG.error("The datatable {} doesn't exist".format(datatable_name))
            return '-'

        table_def = self.component.rest_client().get(
            "/types/{}?handle_format=objects&text_content_output_format=objects_no_convert".format(
                datatable['id']))

        result = set()
        for table_row in datatable["rows"]:
            result.add(self.get_datatable_value(field_def=table_def["fields"][field_name],
                                                          table_row=table_row))

        return ', '.join(result)

    def get_datatable_value(self, field_def, table_row):
        field_value = table_row["cells"][field_def['name']]['value']

        return self.get_value_as_string(field_def, field_value)

    def get_value_as_string(self, field_def, field_value):
        if not field_value and not isinstance(field_value, (int, float)):
            return None

        if field_def['input_type'] == 'multiselect':
            # join the values, and escape it
            simple_list = list(
                (select_val["name"] if isinstance(select_val, dict) else select_val) for select_val in field_value)
            ret_value = ', '.join(simple_list)
        elif field_def['input_type'] in ['datepicker', 'datetimepicker']:
            # format the date and escape it
            ret_value = self.format_timestamp(field_value)
        elif field_def['input_type'] == "textarea":
            if not isinstance(field_value, dict):
                ret_value = field_value
            elif field_value['format'] == "text":
                # plain text, escape it
                ret_value = field_value["content"]
            else:
                # HTML value, so return it without escaping
                return field_value["content"]
        elif field_def['input_type'] == "number":
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
    def format_timestamp(self, value):
        # converts resilient epoch timestamp to string
        # 2018-06-03T11:57:02Z
        # https://en.wikipedia.org/wiki/ISO_8601
        date_format = self.component.options.get('date_format')
        value = value / 1000
        date_object = datetime.utcfromtimestamp(value)
        if not date_format:
            return date_object.isoformat()
        else:
            return date_object.strftime(date_format)

    def get_action_field_value(self, action_data, field_name):
        field_def = self.get_field_defs('actioninvocation').get(field_name)
        if not field_def:
            logging.error('action field name (%s) invalid' % field_name)
            return None

        action_def_value_list = field_def.get('values')
        if not action_def_value_list:
            logging.error('action field not a list type: (%s)' % field_name)
            return None

        for action_def_value in action_def_value_list:
            if action_def_value['value'] == action_data['properties'][field_name]:
                return action_def_value['label']

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
            logging.warning('Unexpected list type (%s) for (%s)' % (type(str_value).__name__, str_value))
            list_result = str_value

        return list_result
