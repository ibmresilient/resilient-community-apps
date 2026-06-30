import mock
from fn_elasticsearch.components.fn_elasticsearch_query import FunctionComponent

class TestMockVersionInputs(object):
    """
        [Class for version check differences]
    """
    def test_perform_search_old(self):
        """
        [Test 6.0.0 with doctype]
        """
        es_instance_info = {'cluster_name': 'elasticsearch', 'cluster_uuid': 'kPjOcrpMQaWWm4neFdzLrw', 'name': 'f492663fbfa2', 'tagline': 'You Know, for Search', 'version': {'build_date': '2019-04-05T22:55:32.697037Z', 'build_flavor': 'oss', 'build_hash': 'b7e28a7', 'build_snapshot': False, 'build_type': 'tar', 'lucene_version': '8.0.0', 'minimum_index_compa...y_version': '6.0.0-beta1', 'minimum_wire_compat...y_version': '6.7.0', 'number': '6.0.0'}}
        es_query = None
        es_index = None
        es_doc_type = 4
        es_mock = mock.Mock()
        FunctionComponent.perform_search(es_instance_info, es_mock, es_query, es_index, es_doc_type)
        es_mock.search.assert_called_with(doc_type=4, body=None, ignore=[400, 404, 500], index=None)

    def test_perform_search_new(self):
        """
        [Test 7.0.0 with doctype]
        """
        es_instance_info = {'cluster_name': 'elasticsearch', 'cluster_uuid': 'kPjOcrpMQaWWm4neFdzLrw', 'name': 'f492663fbfa2', 'tagline': 'You Know, for Search', 'version': {'build_date': '2019-04-05T22:55:32.697037Z', 'build_flavor': 'oss', 'build_hash': 'b7e28a7', 'build_snapshot': False, 'build_type': 'tar', 'lucene_version': '8.0.0', 'minimum_index_compa...y_version': '6.0.0-beta1', 'minimum_wire_compat...y_version': '6.7.0', 'number': '7.0.0'}}
        es_query = None
        es_index = None
        es_doc_type = 4

        es_mock = mock.Mock()
        FunctionComponent.perform_search(es_instance_info, es_mock, es_query, es_index, es_doc_type)
        es_mock.search.assert_called_with(body=None, ignore=[400, 404, 500], index=None)
