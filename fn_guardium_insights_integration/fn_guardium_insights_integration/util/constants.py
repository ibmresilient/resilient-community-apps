# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

# Guardium Insights
API_VERSION = "v3"
ANAMOLIES = "https://{host}:{port}/api/" + API_VERSION + "/events"
ANAMOLIES_DETAILS = "https://{host}:{port}/api/" + API_VERSION + "/events/{event_id}/detail"
BLOCK_USER = "https://{host}:{port}/api/" + API_VERSION + "/block_user"
LIST_REPORTS = "https://{host}:{port}/api/" + API_VERSION + "/reports"
RUN_REPORT = "https://{host}:{port}/api/" + API_VERSION + "/reports/run"

# Resilient Incident Restful Endpoints
ADD_INCIDENT = "/incidents?want_full_data=false&want_tasks=false&handle_format=names"
INCIDENT_URL = "/incidents/{}?handle_format=names"
# Resilient Table Restful Endpoints
GET_TABLE_DATA = '/incidents/{inc_id}/table_data?handle_format=names'
TABLE_ADD_ROW = "/incidents/{inc_id}/table_data/{table_id}/row_data?handle_format=names"
DELETE_TABLE_ROW = "/incidents/{inc_id}/table_data/{table_id}/row_data/{row_id}?handle_format=names"
GET_TABLE_DATA_BY_ID = "/incidents/{inc_id}/table_data/{table_id}?handle_format=names"
ASSETS = "https://{host}:{port}/api/v3/assets?user_type=all_user_type"

# BSO firewall
F_URL = "https://{bso_ip}/netaccess/connstatus.html"
F_LOGIN_URL = "https://{bso_ip}/netaccess/loginuser.html"

CLASSIFICATION_REPORT_BODY = {
    "fetch_size": 0,
    "offset": 0,
    "report_definition": {
        "report_id": "000000000000000000001101",
        "category_id": "000000000000000000000006",
        "report_name": "Classification",
        "report_description": "This report details incoming classification data.",
        "report_tags": [
            {
                "nls_key": "REPORT_TYPE_CLASSIFICATION",
                "nls_value": "Classification"
            }
        ],
        "report_headers": [
            {
                "header_id": "911",
                "header_name": "StartDateTimeUTC",
                "header_description": {
                    "nls_key": "STARTDATETIMEUTC_DESCRIPTION",
                    "nls_value": "Date and time the classification process started running (local time)."
                },
                "field_name": {
                    "nls_key": "CLASSIFICATION_STARTDATETIMEUTC",
                    "nls_value": "Start date (local time)"
                },
                "header_type": "DATE_UTC",
                "header_type_length": 10,
                "table_name": "CLASSIFICATION",
                "sequence": 1,
                "aggregation_type": "VALUE",
                "header_data_type": "TABLE_HEADER"
            },
            {
                "header_id": "916",
                "header_name": "DataSourceIP",
                "header_description": {
                    "nls_key": "DATASOURCEIP_DESCRIPTION",
                    "nls_value": "The datasource server IP"
                },
                "field_name": {
                    "nls_key": "CLASSIFICATION_DATASOURCEIP",
                    "nls_value": "Datasource IP"
                },
                "header_type": "STRING",
                "header_type_length": 50,
                "table_name": "CLASSIFICATION",
                "sequence": 2,
                "aggregation_type": "VALUE",
                "header_data_type": "TABLE_HEADER"
            },
            {
                "header_id": "914",
                "header_name": "DataSourceName",
                "header_description": {
                    "nls_key": "DATASOURCENAME_DESCRIPTION",
                    "nls_value": "Full name of the data source."
                },
                "field_name": {
                    "nls_key": "CLASSIFICATION_DATASOURCENAME",
                    "nls_value": "Datasource name"
                },
                "header_type": "STRING",
                "header_type_length": 255,
                "table_name": "CLASSIFICATION",
                "sequence": 3,
                "aggregation_type": "VALUE",
                "header_data_type": "TABLE_HEADER"
            },
            {
                "header_id": "915",
                "header_name": "DataSourceType",
                "header_description": {
                    "nls_key": "DATASOURCETYPE_DESCRIPTION",
                    "nls_value": "Database type."
                },
                "field_name": {
                    "nls_key": "CLASSIFICATION_DATASOURCETYPE",
                    "nls_value": "Datasource type"
                },
                "header_type": "STRING",
                "header_type_length": 255,
                "table_name": "CLASSIFICATION",
                "sequence": 4,
                "aggregation_type": "VALUE",
                "header_data_type": "TABLE_HEADER"
            },
            {
                "header_id": "919",
                "header_name": "Port",
                "header_description": {
                    "nls_key": "PORT_DESCRIPTION",
                    "nls_value": "Port on the data source that the assessment runs on."
                },
                "field_name": {
                    "nls_key": "CLASSIFICATION_PORT",
                    "nls_value": "Port"
                },
                "header_type": "INTEGER",
                "header_type_length": 4,
                "table_name": "CLASSIFICATION",
                "sequence": 5,
                "aggregation_type": "VALUE",
                "header_data_type": "TABLE_HEADER"
            },
            {
                "header_id": "917",
                "header_name": "ServiceName",
                "header_description": {
                    "nls_key": "SERVICENAME_DESCRIPTION",
                    "nls_value": "Service name for the interaction (or alias that is used until the service is connected)."
                },
                "field_name": {
                    "nls_key": "CLASSIFICATION_SERVICENAME",
                    "nls_value": "Service name"
                },
                "header_type": "STRING",
                "header_type_length": 255,
                "table_name": "CLASSIFICATION",
                "sequence": 6,
                "aggregation_type": "VALUE",
                "header_data_type": "TABLE_HEADER"
            },
            {
                "header_id": "904",
                "header_name": "Schema",
                "header_description": {
                    "nls_key": "SCHEMA_DESCRIPTION",
                    "nls_value": "Displays if the data source includes schema details."
                },
                "field_name": {
                    "nls_key": "CLASSIFICATION_SCHEMA",
                    "nls_value": "Schema"
                },
                "header_type": "STRING",
                "header_type_length": 255,
                "table_name": "CLASSIFICATION",
                "sequence": 7,
                "aggregation_type": "VALUE",
                "header_data_type": "TABLE_HEADER"
            },
            {
                "header_id": "903",
                "header_name": "Catalog",
                "header_description": {
                    "nls_key": "CATALOG_DESCRIPTION",
                    "nls_value": "Displays if the data source includes catalog details."
                },
                "field_name": {
                    "nls_key": "CLASSIFICATION_CATALOG",
                    "nls_value": "Catalog"
                },
                "header_type": "STRING",
                "header_type_length": 255,
                "table_name": "CLASSIFICATION",
                "sequence": 8,
                "aggregation_type": "VALUE",
                "header_data_type": "TABLE_HEADER"
            },
            {
                "header_id": "905",
                "header_name": "TableName",
                "header_description": {
                    "nls_key": "TABLENAME_DESCRIPTION",
                    "nls_value": "Table name in the data source."
                },
                "field_name": {
                    "nls_key": "CLASSIFICATION_TABLENAME",
                    "nls_value": "Table"
                },
                "header_type": "STRING",
                "header_type_length": 255,
                "table_name": "CLASSIFICATION",
                "sequence": 9,
                "aggregation_type": "VALUE",
                "header_data_type": "TABLE_HEADER"
            },
            {
                "header_id": "906",
                "header_name": "ColumnName",
                "header_description": {
                    "nls_key": "COLUMNNAME_DESCRIPTION",
                    "nls_value": "Column name in the data source."
                },
                "field_name": {
                    "nls_key": "CLASSIFICATION_COLUMNNAME",
                    "nls_value": "Column"
                },
                "header_type": "STRING",
                "header_type_length": 255,
                "table_name": "CLASSIFICATION",
                "sequence": 10,
                "aggregation_type": "VALUE",
                "header_data_type": "TABLE_HEADER"
            },
            {
                "header_id": "902",
                "header_name": "ProcessDescription",
                "header_description": {
                    "nls_key": "PROCESSDESCRIPTION_DESCRIPTION",
                    "nls_value": "Classification process description."
                },
                "field_name": {
                    "nls_key": "CLASSIFICATION_PROCESSDESCRIPTION",
                    "nls_value": "Description"
                },
                "header_type": "STRING",
                "header_type_length": 255,
                "table_name": "CLASSIFICATION",
                "sequence": 11,
                "aggregation_type": "VALUE",
                "header_data_type": "TABLE_HEADER"
            },
            {
                "header_id": "908",
                "header_name": "ClassificationName",
                "header_description": {
                    "nls_key": "CLASSIFICATIONNAME_DESCRIPTION",
                    "nls_value": "Classification of the policy rule as defined by the user."
                },
                "field_name": {
                    "nls_key": "CLASSIFICATION_CLASSIFICATIONNAME",
                    "nls_value": "Classification name"
                },
                "header_type": "STRING",
                "header_type_length": 255,
                "table_name": "CLASSIFICATION",
                "sequence": 12,
                "aggregation_type": "VALUE",
                "header_data_type": "TABLE_HEADER"
            },
            {
                "header_id": "907",
                "header_name": "RuleDescription",
                "header_description": {
                    "nls_key": "RULEDESCRIPTION_DESCRIPTION",
                    "nls_value": "Classification rules use regular expressions, Luhn algorithms, and other criteria to define rules for matching content when applying a classification policy."
                },
                "field_name": {
                    "nls_key": "CLASSIFICATION_RULEDESCRIPTION",
                    "nls_value": "Classification rule"
                },
                "header_type": "STRING",
                "header_type_length": 32000,
                "table_name": "CLASSIFICATION",
                "sequence": 13,
                "aggregation_type": "VALUE",
                "header_data_type": "TABLE_HEADER"
            },
            {
                "header_id": "909",
                "header_name": "Category",
                "header_description": {
                    "nls_key": "CATEGORY_DESCRIPTION",
                    "nls_value": "Categories are used to group policy violations for both reporting and incident management."
                },
                "field_name": {
                    "nls_key": "CLASSIFICATION_CATEGORY",
                    "nls_value": "Category"
                },
                "header_type": "STRING",
                "header_type_length": 255,
                "table_name": "CLASSIFICATION",
                "sequence": 14,
                "aggregation_type": "VALUE",
                "header_data_type": "TABLE_HEADER"
            },
            {
                "header_id": "920",
                "header_name": "Comprehensive",
                "header_description": {
                    "nls_key": "COMPREHENSIVE_DESCRIPTION",
                    "nls_value": "Classification based on random sampling of data"
                },
                "field_name": {
                    "nls_key": "CLASSIFICATION_COMPREHENSIVE",
                    "nls_value": "Comprehensive"
                },
                "header_type": "STRING",
                "header_type_length": 50,
                "table_name": "CLASSIFICATION",
                "sequence": 15,
                "aggregation_type": "VALUE",
                "header_data_type": "TABLE_HEADER"
            }
        ],
        "runtime_parameters": [
            {
                "key": "QUERY_FROM_DATE",
                "label": "Time From",
                "runtime_parameter_type": "DATE_UTC",
                "runtime_parameter_type_length": 10,
                "operator_type": "GREATER_THAN_OR_EQUAL"
            },
            {
                "key": "QUERY_TO_DATE",
                "label": "Time To",
                "runtime_parameter_type": "DATE_UTC",
                "runtime_parameter_type_length": 10,
                "operator_type": "LESS_THAN_OR_EQUAL"
            }
        ],
        "report_filters": {
            "option_type": "AND",
            "filters_array": [
                {
                    "condition": {
                        "filter_id": 1,
                        "sequence": -1,
                        "header_id": "911",
                        "header_name": "StartDateTimeUTC",
                        "field_nls_translation_key": "CLASSIFICATION_STARTDATETIMEUTC",
                        "table_name": "CLASSIFICATION",
                        "parameter_type": "PARAMETER",
                        "operator_type": "GREATER_THAN_OR_EQUAL",
                        "values": [
                            "QUERY_FROM_DATE"
                        ]
                    }
                },
                {
                    "condition": {
                        "filter_id": 2,
                        "sequence": -1,
                        "header_id": "911",
                        "header_name": "StartDateTimeUTC",
                        "field_nls_translation_key": "CLASSIFICATION_STARTDATETIMEUTC",
                        "table_name": "CLASSIFICATION",
                        "parameter_type": "PARAMETER",
                        "operator_type": "LESS_THAN_OR_EQUAL",
                        "values": [
                            "QUERY_TO_DATE"
                        ]
                    }
                }
            ]
        },
        "default_timestamp_header_id": "911",
        "selected_timestamp_header_id": "911"
    },
    "runtime_parameter_list": [
        {
            "key": "QUERY_FROM_DATE",
            "label": "Enter Period From",
            "runtime_parameter_type": "DATE_UTC",
            "runtime_parameter_type_length": 10,
            "operator_type": "GREATER_THAN_OR_EQUAL",
            "value": ""
        },
        {
            "key": "QUERY_TO_DATE",
            "label": "Enter Period To",
            "runtime_parameter_type": "DATE_UTC",
            "runtime_parameter_type_length": 10,
            "operator_type": "LESS_THAN_OR_EQUAL",
            "value": ""
        }
    ],
    "without_limit": False
}
