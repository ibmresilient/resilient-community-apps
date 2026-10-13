# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
from pytest_resilient_circuits import BasicResilientMock, resilient_endpoint
import requests_mock
import json
import six

mock_data_connector_queues = {
    "queues": [
        {
            "queue_name": "low_code"
        }
    ]
}

class ConnectorResilientMock(BasicResilientMock):
    @resilient_endpoint("GET", r"/connectors/queues")
    def mock_connector_queues_get(self, request):
        """ Handle GET request for connector queues """
        data = mock_data_connector_queues

        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=six.b(json.dumps(data)))
