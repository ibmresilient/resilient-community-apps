# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import json
class AmqpFacadeMock:

    """
    When a response comes in, check if the correlation_ids match
    If they do, the body will contain our search request
    """
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body
            self.status = props.headers.get('status')
    """
    Call is used to submit a query to the ICDX AMQP API. 
    It performs these steps:
    + Init a response and setup a correlation_id
    + Publish a request to the ICDX Platform with a reply_to queue for response
    + Wait for response and return    
    """
    def call(*args, **kwargs):

        try:
            is_json(kwargs.get('payload'))
        except Exception:
            # Invalid JSON, raise a descriptive error
            raise ValueError("AMQP Request failed. Received a non-json Payload")

        if "id" not in json.loads(kwargs.get('payload')):
            raise ValueError("No ID Field found on payload")

        if kwargs.get('success') == True:
            return json.dumps(
                [{"path": "default", "name": "Default Archive"}, {"path": "system", "name": "System Archive"}]), 200
        else:
            return json.dumps({}), 204

def mocked_call(*args, **kwargs):
    try:
        is_json(kwargs.get('payload'))
    except Exception:
        # Invalid JSON, raise a descriptive error
        raise ValueError("AMQP Request failed. Received a non-json Payload")

    if "id" not in json.loads(kwargs.get('payload')):
        raise ValueError("No ID Field found on payload")

    # Mocked responses for the get archive list function
    if kwargs.get('operation') == 'get_archive_list':
        if kwargs.get('success') == True:
            return json.dumps([{"path": "default", "name": "Default Archive"}, {"path": "system", "name": "System Archive"}]).encode('utf-8'), 200
        else:
            return (json.dumps({}).encode('utf-8'), 204)

    # Mocked responses for the find events function
    if kwargs.get('operation') == 'find_events':
        if kwargs.get('success') == True:
            return json.dumps(
                {
                    "result": [{
                   "time":"2018-04-04T13:55:38.724-07:00",
                   "device_name":u"dn_3000000267328",
                   "device_ip":u"41.255.173.40",
                   "uuid":"0dfaba40-0afc-11e5-ea25-00000000e69b"
                }, {
                   "time":"2018-04-04T13:56:20.839-07:00",
                   "device_name":"dn_3000000892759",
                   "device_ip":"91.128.1.62",
                   "uuid":"2714f770-0afc-11e5-d069-00000000f734"
                }, {
                   "time":"2018-04-04T13:56:25.844-07:00",
                   "device_name":u"dn_3000000892759",
                   "device_ip":u"91.128.1.62",
                   "uuid":"2a10ab40-0afc-11e5-dcda-00000000f8d8"
                 }]
                }).encode('utf-8'), 200
        else:
            return (json.dumps({}), 204)
    # Mocked responses for the get event function
    if kwargs.get('operation') == 'get_event':
        if kwargs.get('success') == True:
            if json.loads(kwargs.get('payload'))['uuid'] ==  "ec6167c0-1c2e-11e8-c000-000000000022":
                return json.dumps({
                    "device_os_type_id": 0,
                    "timezone": 0,
                    "type": "MBIN",
                    "seq_num": 145,
                    "ref_uid": 2449263,
                    "product_ver": u"6.6.0.758",
                    "collector_device_ip": "10.7.100.25",
                    "proxy_product_ver": u"1.2.3",
                    "device_end_time": 1491548212290,
                    "device_time": 1491548212290,
                    "device_ref_uid": 1515,
                    "count": 1,
                    "end_time": "2017-04-07T06:56:52.290Z",
                    "message": "	Љ	Щ	щ	Ӄ",
                    "version": "1.0",
                    "collector_device_name": "ICDx-CREST-25",
                    "product_name": "Symantec Data Center Security",
                    "device_ip": "10.69.0.44",
                    "actor": {
                        "session": {
                            "id": 2601
                        }, "file": {
                            "name": "SDCS_ProcessEvent",
                            "path": "SDCS_ProcessEvent"
                        }
                    },
                    "device_post_time": 1491548212290,
                    "proxy_product_name": "Data Center Security",
                    "proxy_product_uid": "UUID based on (name + version)",
                    "dcs_remediated": False,
                    "device_alias_name": "rh67-66mp1",
                    "severity_id": 1,
                    "time": "2018-04-07T06:56:52.290Z",
                    "log_time": "2018-04-07T18:27:29.468-08:00",
                    "uuid": "ec6167c0-1c2e-11e8-c000-000000000022"
                }).encode('utf-8'),200
            elif json.loads(kwargs.get('payload'))['uuid'] == "ec6167c0-1c2e-11e8-c000-000000000022":
                return json.dumps({
               "device_os_type_id": 0,
               "timezone": 0,
               "type": "MBIN",
               "seq_num": 145,
               "ref_uid": 2449263,
               "product_ver": "6.6.0.758",
               "collector_device_ip": "10.7.100.25",
               "proxy_product_ver": "1.2.3",
               "device_end_time": 1491548212290,
               "device_time": 1491548212290,
               "device_ref_uid": 1515,
               "count": 1,
               "end_time": "2017-04-07T06:56:52.290Z",
               "message": "	Љ	Щ	щ	Ӄ",
               "version": "1.0",
               "collector_device_name": "ICDx-CREST-25",
               "product_name": "Symantec Data Center Security",
               "device_ip": "10.69.0.44",
               "actor$session$id": 2601,
               "actor$file$name": "SDCS_ProcessEvent",
               "actor$file$path": "SDCS_ProcessEvent",
               "device_post_time": 1491548212290,
               "proxy_product_name": "Data Center Security",
               "proxy_product_uid": "UUID based on (name + version)",
               "dcs_remediated": False,
               "device_alias_name": "rh67-66mp1",
               "severity_id": 1,
               "time": "2018-04-07T06:56:52.290Z",
               "log_time": "2018-04-27T18:27:29.468-08:00",
               "uuid": "ec6167c0-1c2e-11e8-c000-000000000022"
               }).encode('utf-8'),200

        else:
            return(json.dumps({}).encode('utf-8'),204)



def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError:
        return False
    return True