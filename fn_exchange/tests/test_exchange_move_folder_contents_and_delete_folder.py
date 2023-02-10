# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import get_mock_config, mocked_exchange_utils

PACKAGE_NAME = "fn_exchange"
FUNCTION_NAME = "exchange_move_folder_contents_and_delete_folder"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_exchange_move_folder_contents_and_delete_folder_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("exchange_move_folder_contents_and_delete_folder", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("exchange_move_folder_contents_and_delete_folder_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestExchangeMoveFolderContentsAndDeleteFolder:
    """ Tests for the exchange_move_folder_contents_and_delete_folder function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_exchange.components.exchange_move_folder_contents_and_delete_folder.exchange_utils', side_effect=mocked_exchange_utils)
    @pytest.mark.parametrize("exchange_email, exchange_delete_if_no_subfolders, exchange_folder_path, exchange_destination_folder_path, expected_results", [
        ("user@exch.com", False, "Top of Information Store/TESTFOLDER_1", "Top of Information Store/TESTFOLDER_2",
         {'email_ids': ['<ed6f175b4ef84ceaa921ba8bfdd37739@exch.exch.com>'], 'emails': {
             '<ed6f175b4ef84ceaa921ba8bfdd37739@exch.exch.com>': {
                 'body': '<html>\r\n<head>\r\n<meta http-equiv="Content-Type" content="text\\/html; charset=utf-8">\r\n<\\/head>\r\n<body>\r\nExample Body\r\n<\\/body>\r\n<\\/html>\r\n',
                 'attachments': {}, 'attachment_ids': [], 'sender_name': 'John Doe',
                 'mime_content': u'Received: from exch.exch.com (2002:925:1d2d::925:1d2d) by\r\n exch.exch.com (2002:925:1d2d::925:1d2d) with Microsoft SMTP Server\r\n (TLS) id 15.0.1395.4 via Mailbox Transport; Tue,\n       10 Nov 2020 11:52:21 +0000\r\nReceived: from exch.exch.com (2002:925:1d2d::925:1d2d) by\r\n exch.exch.com (2002:925:1d2d::925:1d2d) with Microsoft SMTP Server\r\n (TLS) id 15.0.1395.4; Tue,\n       10 Nov 2020 11:46:35 +0000\r\nReceived: from exch.exch.com ([\n        fe80::4f8:e4ed:8276:c2c7\n      ]) by\r\n exch.exch.com ([\n        fe80::4f8:e4ed:8276:c2c7%12\n      ]) with mapi id\r\n 15.00.1395.000; Tue,\n       10 Nov 2020 11:46:35 +0000\r\nFrom: "John Doe" <jdoe@exch.com>\r\nTo: "User" <user@exch.com>\r\nSubject: Example Subject\r\nThread-Topic: Example Subject\r\nThread-Index: AQHWt1Wr3ksBSsdJkUatZX7q6rcC3A==\r\nDate: Tue,\n       10 Nov 2020 11:36:02 +0000\r\nMessage-ID: <ed6f175b4ef84ceaa921ba8bfdd37739@exch.exch.com>\r\nAccept-Language: en-US\r\nContent-Language: en-US\r\nX-MS-Exchange-Organization-AuthAs: Internal\r\nX-MS-Exchange-Organization-AuthMechanism: 04\r\nX-MS-Exchange-Organization-AuthSource: exch.exch.com\r\nX-MS-Has-Attach:\r\nX-MS-Exchange-Organization-SCL: -1\r\nX-MS-TNEF-Correlator:\r\nContent-Type: multipart\\/alternative;\r\n\tboundary="_000_ed6f175b4ef84ceaa921ba8bfdd37739exchexchcom_"\r\nMIME-Version: 1.0\r\n\r\n--_000_ed6f175b4ef84ceaa921ba8bfdd37739exchexchcom_\r\nContent-Type: text\\/plain; charset="us-ascii"\r\n\r\nTest\r\n\r\n--_000_ed6f175b4ef84ceaa921ba8bfdd37739exchexchcom_\r\nContent-Type: text\\/html; charset="us-ascii"\r\n\r\n<html>\r\n<head>\r\n<meta http-equiv="Content-Type" content="text\\/html; charset=us-ascii">\r\n<\\/head>\r\n<body>\r\nTest\r\n<\\/body>\r\n<\\/html>\r\n\r\n--_000_ed6f175b4ef84ceaa921ba8bfdd37739exchexchcom_--\r\n',
                 'sender_email': 'jdoe@exch.com', 'subject': 'Example Subject'}}}),
        ("user@exch.com", True, "Top of Information Store/TESTFOLDER_1", "Top of Information Store/TESTFOLDER_2",
         {'email_ids': ['<ed6f175b4ef84ceaa921ba8bfdd37739@exch.exch.com>'], 'emails': {
             '<ed6f175b4ef84ceaa921ba8bfdd37739@exch.exch.com>': {
                 'body': '<html>\r\n<head>\r\n<meta http-equiv="Content-Type" content="text\\/html; charset=utf-8">\r\n<\\/head>\r\n<body>\r\nExample Body\r\n<\\/body>\r\n<\\/html>\r\n',
                 'attachments': {}, 'attachment_ids': [], 'sender_name': 'John Doe',
                 'mime_content': u'Received: from exch.exch.com (2002:925:1d2d::925:1d2d) by\r\n exch.exch.com (2002:925:1d2d::925:1d2d) with Microsoft SMTP Server\r\n (TLS) id 15.0.1395.4 via Mailbox Transport; Tue,\n       10 Nov 2020 11:52:21 +0000\r\nReceived: from exch.exch.com (2002:925:1d2d::925:1d2d) by\r\n exch.exch.com (2002:925:1d2d::925:1d2d) with Microsoft SMTP Server\r\n (TLS) id 15.0.1395.4; Tue,\n       10 Nov 2020 11:46:35 +0000\r\nReceived: from exch.exch.com ([\n        fe80::4f8:e4ed:8276:c2c7\n      ]) by\r\n exch.exch.com ([\n        fe80::4f8:e4ed:8276:c2c7%12\n      ]) with mapi id\r\n 15.00.1395.000; Tue,\n       10 Nov 2020 11:46:35 +0000\r\nFrom: "John Doe" <jdoe@exch.com>\r\nTo: "User" <user@exch.com>\r\nSubject: Example Subject\r\nThread-Topic: Example Subject\r\nThread-Index: AQHWt1Wr3ksBSsdJkUatZX7q6rcC3A==\r\nDate: Tue,\n       10 Nov 2020 11:36:02 +0000\r\nMessage-ID: <ed6f175b4ef84ceaa921ba8bfdd37739@exch.exch.com>\r\nAccept-Language: en-US\r\nContent-Language: en-US\r\nX-MS-Exchange-Organization-AuthAs: Internal\r\nX-MS-Exchange-Organization-AuthMechanism: 04\r\nX-MS-Exchange-Organization-AuthSource: exch.exch.com\r\nX-MS-Has-Attach:\r\nX-MS-Exchange-Organization-SCL: -1\r\nX-MS-TNEF-Correlator:\r\nContent-Type: multipart\\/alternative;\r\n\tboundary="_000_ed6f175b4ef84ceaa921ba8bfdd37739exchexchcom_"\r\nMIME-Version: 1.0\r\n\r\n--_000_ed6f175b4ef84ceaa921ba8bfdd37739exchexchcom_\r\nContent-Type: text\\/plain; charset="us-ascii"\r\n\r\nTest\r\n\r\n--_000_ed6f175b4ef84ceaa921ba8bfdd37739exchexchcom_\r\nContent-Type: text\\/html; charset="us-ascii"\r\n\r\n<html>\r\n<head>\r\n<meta http-equiv="Content-Type" content="text\\/html; charset=us-ascii">\r\n<\\/head>\r\n<body>\r\nTest\r\n<\\/body>\r\n<\\/html>\r\n\r\n--_000_ed6f175b4ef84ceaa921ba8bfdd37739exchexchcom_--\r\n',
                 'sender_email': 'jdoe@exch.com', 'subject': 'Example Subject'}}}),

    ])
    def test_success(self, mock_utils, circuits_app, exchange_email, exchange_delete_if_no_subfolders, exchange_folder_path, exchange_destination_folder_path, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "exchange_email": exchange_email,
            "exchange_delete_if_no_subfolders": exchange_delete_if_no_subfolders,
            "exchange_folder_path": exchange_folder_path,
            "exchange_destination_folder_path": exchange_destination_folder_path
        }
        results = call_exchange_move_folder_contents_and_delete_folder_function(circuits_app, function_params)
        assert(expected_results == results)