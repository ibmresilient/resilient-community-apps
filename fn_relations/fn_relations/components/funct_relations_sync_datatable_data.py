# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_relations.lib.utilities import list_children
import re
import ast

PACKAGE_NAME = "fn_relations"
FN_NAME = "relations_sync_datatable_data"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'relations_sync_datatable_data'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: A Function used to Sync DataTable Data from the incident where it resides to the parent or child.
        Inputs:
            -   fn_inputs.relations_row_data
            -   fn_inputs.incident_id
            -   fn_inputs.relations_datatables
            -   fn_inputs.relations_exclude_datatables
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["relations_datatables", "incident_id"], fn_inputs)

        incident_id = fn_inputs.incident_id
        relations_datatables =  fn_inputs.relations_datatables
        relations_exclude_datatables =  getattr(fn_inputs, "relations_exclude_datatables", None)
        relations_row_data = getattr(fn_inputs, "relations_row_data", None)
        self.LOG.info("incident_id: {}".format(incident_id))
        self.LOG.info("relations_datatables: {}".format(relations_datatables))
        self.LOG.info("relations_exclude_datatables: {}".format(relations_exclude_datatables))
        self.LOG.info("relations_row_data: {}".format(relations_row_data))


        def remove_row_id(row_list):
            stripped_rows = []
            for row in row_list:
                stripped_cells = {}
                for column in row['cells']:
                    stripped_column = {}
                    for key in row['cells'][column]:
                        if key != 'row_id':
                            stripped_column[key] = row['cells'][column][key]
                    stripped_cells[column] = stripped_column
                stripped_rows.append(stripped_cells)
            return(stripped_rows)


        incident = self.rest_client().get("/incidents/{}?handle_format=names".format(incident_id))

        if incident['properties']['relations_level'] == 'Child':
            self.LOG.info('Parsing Parent Incident ID')
            id_regex = re.compile(r'#incidents/(\d+)"')
            parent_id = int(re.findall(id_regex,incident['properties']['relations_parent_id'])[0])
            self.LOG.debug('Parent ID: {}'.format(parent_id))
        elif incident['properties']['relations_level'] == 'Parent':
            self.LOG.info('Collecting Children Incidents.')
            children_incidents = list_children(self.rest_client().get("/incidents/{}/table_data/dt_relations_child_incidents?handle_format=names".format(incident_id)))
            self.LOG.debug('Child Incidents Found: {}'.format(str(children_incidents)))
        else:
            raise IntegrationError("Incident does not have a relation level. Unable to sync datatable(s).")

        if not relations_row_data:
            if 'All' in relations_datatables.split(','):
                self.LOG.info('Collecting All Table Data')
                all_dataTable_data = self.rest_client().get('/incidents/{}/table_data?handle_format=names'.format(incident_id))
                self.LOG.debug('DataTables Collected: {}'.format(all_dataTable_data))

                for datatable in all_dataTable_data:
                    if datatable not in relations_exclude_datatables.split(','):
                        self.LOG.info('Sanatizing DataTable of Row IDs')
                        sanatized_datatable_rows = remove_row_id(all_dataTable_data[datatable]['rows'])
                        self.LOG.debug('Sanatized Rows: {}'.format(sanatized_datatable_rows))
                        if incident['properties']['relations_level'] == 'Child':
                            self.LOG.info('Collecting Parent DataTable')
                            parent_datatable = self.rest_client().get('/incidents/{}/table_data/{}?handle_format=names'.format(parent_id, datatable))
                            self.LOG.debug('DataTable Collected: {}'.format(parent_datatable))
                            self.LOG.info('Sanatizing DataTable of Row IDs')
                            sanatized_parent_rows = remove_row_id(parent_datatable['rows'])
                            self.LOG.debug('Sanatized Rows: {}'.format(sanatized_parent_rows))
                            for sanatized_row in sanatized_datatable_rows:
                                if sanatized_row not in sanatized_parent_rows:
                                    self.LOG.info('Posting Row to Parent Incident')
                                    posted_row = self.rest_client().post('/incidents/{}/table_data/{}/row_data?handle_format=names'.format(parent_id, datatable), {'cells': sanatized_row})
                                    self.LOG.debug('Posted Row: {}'.format(posted_row))
                                else:
                                    self.LOG.info('Row already exists in Parent Incident')

                        else:
                            for child in children_incidents:
                                self.LOG.info('Collecting Child DataTable')
                                child_datatable = self.rest_client().get('/incidents/{}/table_data/{}?handle_format=names'.format(child, datatable))
                                self.LOG.debug('DataTable Collected: {}'.format(child_datatable))
                                self.LOG.info('Sanatizing DataTable of Row IDs')
                                sanatized_child_rows = remove_row_id(child_datatable['rows'])
                                self.LOG.debug('Sanatized Rows: {}'.format(sanatized_child_rows))
                                for sanatized_row in sanatized_datatable_rows:
                                    if sanatized_row not in sanatized_child_rows:
                                        self.LOG.info('Posting Row to Child Incident')
                                        posted_row = self.rest_client().post('/incidents/{}/table_data/{}/row_data?handle_format=names'.format(child, datatable), {'cells': sanatized_row})
                                        self.LOG.debug('Posted Row: {}'.format(posted_row))
                                    else:
                                        self.LOG.info('Row already exists in Child Incident')
                    else:
                        self.LOG.info('DataTable {} skipped because of Exclude List'.format(datatable))
                if incident['properties']['relations_level'] == 'Child':
                    results = {'datatables': ["All"], 'rows': None, 'incidents': [parent_id]}
                else:
                    results = {'datatables': ["All"], 'rows': None, 'incidents': children_incidents}

            else:
                for datatable in relations_datatables.split(','):
                    self.LOG.info('Collecting Table Data')
                    dataTable_data = self.rest_client().get('/incidents/{}/table_data/{}?handle_format=names'.format(incident_id, datatable))
                    self.LOG.debug('DataTable Collected: {}'.format(dataTable_data))
                    self.LOG.info('Sanatizing DataTable of Row IDs')
                    sanatized_datatable_rows = remove_row_id(dataTable_data['rows'])
                    self.LOG.debug('Sanatized Rows: {}'.format(sanatized_datatable_rows))
                    if incident['properties']['relations_level'] == 'Child':
                        self.LOG.info('Collecting Parent DataTable')
                        parent_datatable = self.rest_client().get('/incidents/{}/table_data/{}?handle_format=names'.format(parent_id, datatable))
                        self.LOG.debug('DataTable Collected: {}'.format(parent_datatable))
                        self.LOG.info('Sanatizing DataTable of Row IDs')
                        sanatized_parent_rows = remove_row_id(parent_datatable['rows'])
                        self.LOG.debug('Sanatized Rows: {}'.format(sanatized_parent_rows))
                        for sanatized_row in sanatized_datatable_rows:
                            if sanatized_row not in sanatized_parent_rows:
                                self.LOG.info('Posting Row to Parent Incident')
                                posted_row = self.rest_client().post('/incidents/{}/table_data/{}/row_data?handle_format=names'.format(parent_id, datatable), {'cells': sanatized_row})
                                self.LOG.debug('Posted Row: {}'.format(posted_row))
                            else:
                                self.LOG.info('Row already exists in Parent Incident')

                    else:
                        for child in children_incidents:
                            self.LOG.info('Collecting Child DataTable')
                            child_datatable = self.rest_client().get('/incidents/{}/table_data/{}?handle_format=names'.format(child, datatable))
                            self.LOG.debug('DataTable Collected: {}'.format(child_datatable))
                            self.LOG.info('Sanatizing DataTable of Row IDs')
                            sanatized_child_rows = remove_row_id(child_datatable['rows'])
                            self.LOG.debug('Sanatized Rows: {}'.format(sanatized_child_rows))
                            for sanatized_row in sanatized_datatable_rows:
                                if sanatized_row not in sanatized_child_rows:
                                    self.LOG.info('Posting Row to Child Incident')
                                    posted_row = self.rest_client().post('/incidents/{}/table_data/{}/row_data?handle_format=names'.format(child, datatable), {'cells': sanatized_row})
                                    self.LOG.debug('Posted Row: {}'.format(posted_row))
                                else:
                                    self.LOG.info('Row already exists in Child Incident')
                if incident['properties']['relations_level'] == 'Child':
                    results = {'datatables': relations_datatables.split(','), 'rows': None, 'incidents': [parent_id]}
                else:
                    results = {'datatables': relations_datatables.split(','), 'rows': None, 'incidents': children_incidents}

        else:
            if len(relations_datatables.split(',')) > 1:
                raise IntegrationError("Multiple Tables added for single row. Please only supply 1 DataTabe when specifying a specific row.")
            else:
                self.LOG.info('Converting Row Data from Postable Format')
                dataTable_row = {}
                for column in ast.literal_eval(relations_row_data):
                    if ast.literal_eval(relations_row_data)[column]:
                        dataTable_row[column] = {'id': column, 'value': ast.literal_eval(relations_row_data)[column]}
                    else:
                        dataTable_row[column] = {'id': column}
                self.LOG.info('Converted DataTable Row: {}'.format(dataTable_row))
                if incident['properties']['relations_level'] == 'Child':
                    self.LOG.info('Collecting Parent DataTable')
                    parent_datatable = self.rest_client().get('/incidents/{}/table_data/{}?handle_format=names'.format(parent_id, relations_datatables.split(',')[0]))
                    self.LOG.debug('DataTable Collected: {}'.format(parent_datatable))
                    self.LOG.info('Sanatizing DataTable of Row IDs')
                    sanatized_parent_rows = remove_row_id(parent_datatable['rows'])
                    self.LOG.debug('Sanatized Rows: {}'.format(sanatized_parent_rows))
                    if dataTable_row not in sanatized_parent_rows:
                        self.LOG.info('Posting Row to Parent Incident')
                        posted_row = self.rest_client().post('/incidents/{}/table_data/{}/row_data?handle_format=names'.format(parent_id, relations_datatables.split(',')[0]), {'cells': dataTable_row})
                        self.LOG.debug('Posted Row: {}'.format(posted_row))
                    else:
                        self.LOG.info('Row already exists in Parent Incident')
                    results = {'datatables': None, 'rows': [dataTable_row], 'incidents': [parent_id]}

                else:
                    for child in children_incidents:
                        self.LOG.info('Collecting Child DataTable')
                        child_datatable = self.rest_client().get('/incidents/{}/table_data/{}?handle_format=names'.format(child, relations_datatables.split(',')[0]))
                        self.LOG.debug('DataTable Collected: {}'.format(child_datatable))
                        self.LOG.info('Sanatizing DataTable of Row IDs')
                        sanatized_child_rows = remove_row_id(child_datatable['rows'])
                        self.LOG.debug('Sanatized Rows: {}'.format(sanatized_child_rows))
                        if dataTable_row not in sanatized_child_rows:
                            self.LOG.info('Posting Row to Child Incident')
                            posted_row = self.rest_client().post('/incidents/{}/table_data/{}/row_data?handle_format=names'.format(child, relations_datatables.split(',')[0]), {'cells': dataTable_row})
                            self.LOG.debug('Posted Row: {}'.format(posted_row))
                        else:
                            self.LOG.info('Row already exists in Child Incident')
                    results = {'datatables': None, 'rows': [dataTable_row], 'incidents': children_incidents}


        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Note this is only used for demo purposes! Put your own key/value pairs here that you want to access on the Platform

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
