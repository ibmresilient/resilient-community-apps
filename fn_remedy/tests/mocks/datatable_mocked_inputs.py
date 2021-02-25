# (c) Copyright IBM Corp. 2021. All Rights Reserved.
GET_ROW_MOCKED_INPUT = {
    "incident_id": 1001,
    "datatable_datatable_api_name": "mock_data_table",
    "datatable_row_id": None,
    "datatable_search_column": "dt_col_email",
    "datatable_search_value": "joe@example.com"
}
GET_ROW_MOCKED_OUTPUT = {
    u'id': 1,
    u'cells': {
        u'dt_col_email': {u'id': u'dt_col_email', u'row_id': 1, u'value': u'joe@example.com'},
        u'dt_col_id': {u'id': u'dt_col_id', u'row_id': 1, u'value': 3001},
        u'dt_col_name': {u'id': u'dt_col_name', u'row_id': 1, u'value': u'Joe Blogs'},
        u'dt_col_status': {u'id': u'dt_col_status', u'row_id': 1, u'value': u'In Progress'}
    }
}

GET_ROWS_MOCKED_INPUT = {
    'incident_id': 1001,
    'datatable_datatable_api_name': 'mock_data_table',
    'datatable_sort_by': 'dt_col_status',
    'datatable_sort_direction': {'name': 'ASC'},
    'datatable_max_rows': 1,
    'datatable_search_column': 'dt_col_name',
    'datatable_search_value': 'Mary Blogs'
}

GET_ROWS_MOCKED_OUTPUT = [
        {
            u'id': 3,
            u'cells': {
                u'dt_col_name': {
                    u'id': u'dt_col_name',
                    u'value': u'Mary Blogs',
                    u'row_id': 3
                },
                u'dt_col_email': {
                    u'id': u'dt_col_email',
                    u'value': u'mary@example.com',
                    u'row_id': 3
                },
                u'dt_col_status': {
                    u'id': u'dt_col_status',
                    u'value': u'Active',
                    u'row_id': 3
                },
                u'dt_col_id': {
                    u'id': u'dt_col_id',
                    u'value': 3003,
                    u'row_id': 3
                }
            }
        }
    ]


UPDATE_ROW_MOCKED_INPUT = {
    "incident_id": 1001,
    "datatable_datatable_api_name": "mock_data_table",
    "datatable_row_id": 2,
    "datatable_cells_to_update": {
        "dt_col_status": "Complete"
    }
}

UPDATE_ROW_MOCKED_OUTPUT = {
    u'id': 1,
    u'cells': {
        u'dt_col_email': {u'id': u'dt_col_email', u'row_id': 1, u'value': u'mary@example.com'},
        u'dt_col_id': {u'id': u'dt_col_id', u'row_id': 1, u'value': 3002},
        u'dt_col_name': {u'id': u'dt_col_name', u'row_id': 1, u'value': u'Mary Blogs'},
        u'dt_col_status': {u'id': u'dt_col_status', u'row_id': 1, u'value': u'Complete'}
    }
}


DELETE_ROW_MOCKED_INPUT = {
    "incident_id": 1001,
    "datatable_datatable_api_name": "mock_data_table",
    "datatable_row_id": None,
    "datatable_search_column": "dt_col_email",
    "datatable_search_value": "joe@example.com"
}

DELETE_ROW_MOCKED_OUTPUT = {
    u'id': 1,
    u'cells': {
        u'dt_col_email': {u'id': u'dt_col_email', u'row_id': 1, u'value': u'joe@example.com'},
        u'dt_col_id': {u'id': u'dt_col_id', u'row_id': 1, u'value': 3001},
        u'dt_col_name': {u'id': u'dt_col_name', u'row_id': 1, u'value': u'Joe Blogs'},
        u'dt_col_status': {u'id': u'dt_col_status', u'row_id': 1, u'value': u'In Progress'}
    }
}
