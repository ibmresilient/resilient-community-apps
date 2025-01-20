import pytest
from fn_watsonx_analyst.util.chunking.chunking import Chunking
import random
import json


class TestChunking:
    """Tests the Chunking Class"""

    text: str
    max_tokens: int
    chunking: Chunking

    def setup_method(self):
        self.text = "This is a sample text to test the split_data_into_token_chunks function."
        self.max_tokens = 10
        self.chunking = Chunking()

    def test_empty_text(self):
        # Test if empty chunks are created.
        chunks = Chunking.split_data_into_token_chunks(self.chunking, "", self.max_tokens)
        assert not chunks

    def test_single_word(self):
        # Test if a single chunk is created.
        chunks = Chunking.split_data_into_token_chunks(self.chunking, "This ", self.max_tokens)
        assert chunks == ["This"]

    def test_multiple_words(self):
        # Test if multiple chunks are created
        chunks = Chunking.split_data_into_token_chunks(self.chunking, self.text, self.max_tokens)
        assert len(chunks) <= self.max_tokens

    def test_max_tokens_exceeded(self):
        # Test if max tokens are exceeded.
        chunks = Chunking.split_data_into_token_chunks(self.chunking, self.text, 5)
        assert len(chunks) <= 5

    def test_estimate_tokens(self):
        # Test for estimate tokens method.
        assert Chunking.estimate_tokens(self.chunking, "This") == 1
        assert Chunking.estimate_tokens(self.chunking, "is") == 1
        assert Chunking.estimate_tokens(self.chunking, "a") == 1
        assert Chunking.estimate_tokens(self.chunking, "sample") == 1
        assert Chunking.estimate_tokens(self.chunking, "text") == 1

    def test_random_chunks(self):
        # Test for random chunks
        chunks = ["chunk1", "chunk2", "chunk3", "chunk4", "chunk5"]
        k = 3
        expected_result = [True, True, True, False, True]
        random.seed(42)  # Set the seed for reproducibility
        result = [chunk in Chunking.random_chunks(self.chunking, chunks, k) for chunk in chunks]
        assert result == expected_result

    def test_split_text_to_tokens_chunks(self):
        # Testing conversion of string to chunks based on size
        description = "During a routine audit of logs, the HSE Ireland's security information and event management (SIEM) system detected unusual network activity. The incident was identified at 14:45 IST, but the cause and nature of the activity are currently unknown."
        max_chunk_size = 10
        chunks = Chunking.split_text_to_token_chunks(self.chunking, description, max_chunk_size)
        assert isinstance(chunks, list)

    def test_tokens_for_model(self):
        model_name = "ibm/granite-guardian-3-8b"
        length = Chunking.max_tokens_for_model(model_name)
        assert length==4096

    def test_retrieve_top_chunks_tfidf(self):
        # Test to retrive top chunks throught TF-IDF.
        query = "example query"
        chunks = ["chunk 1", "chunk 2", "chunk 3"]
        total_tokens = 1000
        threshold = 0.6

        selected_chunks = Chunking.retrieve_top_chunks_tfidf(
            self.chunking, query, chunks, "mistralai/mistral-large", total_tokens, threshold
        )

        assert len(selected_chunks) <= len(chunks)
        assert len(selected_chunks) >= 1

        for chunk in selected_chunks:
            assert chunk in chunks

        total_tokens_selected = sum(
            [
                Chunking.estimate_tokens(self.chunking, json.dumps(chunk, ensure_ascii=False))
                for chunk in selected_chunks
            ]
        )
        assert total_tokens_selected <= total_tokens * threshold

    def test_simple_split(self):
        # test if a simple JSON spit is working.
        data = {"key1": "value1", "key2": "value2", "key3": "value3"}
        expected_chunks = ["key1: value1", "key2: value2", "key3: value3"]
        chunks = Chunking.split_json_to_chunks_prompts(self.chunking, data)
        assert expected_chunks == chunks

    def test_long_text_split(self):
        # test if JSON chunking works for longer text.
        data = {"key1": "This is a long text that needs to be split into chunks", "key2": "value2", "key3": "value3"}
        expected_chunks = [
            "key1: This is a long text that needs to be split into chunks",
            "key2: value2",
            "key3: value3",
        ]
        chunks = Chunking.split_json_to_chunks_prompts(self.chunking, data)
        assert expected_chunks == chunks

    def test_max_chunk_size(self):
        # Test if max chunk size changes the overall output.
        data = {"key1": "value1", "key2": "value2", "key3": "value3"}
        expected_chunks = ["key1: value1", "key2: value2", "key3: value3"]
        chunks = Chunking.split_json_to_chunks_prompts(self.chunking, data, max_chunk_size=100)
        assert expected_chunks == chunks
    
    def test_split_json_to_chunks(self):
        # Test to see exact chunk values 
        data = {
            "incident": {
                "name": "Test Incident",
                "description": "This is a test incident",
                "start_date": "2023-01-01",
                "inc_start": "2023-01-01",
                "discovered_date": "2023-01-01",
                "creator_principal": {"id": "12345", "type": "user", "name": "John Doe", "display_name": "John Doe"},
                "reporter": "john.doe@example.com",
                "state": "open",
                "country": "US",
                "zip": "12345",
                "workspace": "test_workspace",
                "members": ["user1", "user2"],
                "negative_pr_likely": True,
                "assessment": "low",
                "properties": {"severity": "low"},
                "inc_last_modified_date": "2023-01-01",
                "incident_disposition": "resolved",
                "artifacts": [
                    {
                        "value": "artifact1",
                        "type": "file",
                        "inc_name": "artifact1",
                        "related_incident_count": 1,
                        "summary": "This is artifact 1",
                    }
                ],
                "playbook_executions": [
                    {
                        "status": "success",
                        "object": {
                            "parent": {
                                "parent": {
                                    "parent": None,
                                    "object_id": "12345",
                                    "object_name": "Parent Object",
                                    "type_id": "12345",
                                    "type_name": "Parent Type",
                                },
                                "object_id": "67890",
                                "object_name": "Child Object",
                                "type_id": "67890",
                                "type_name": "Child Type",
                            },
                            "object_id": "98765",
                            "object_name": "Grandchild Object",
                            "type_id": "98765",
                            "type_name": "Grandchild Type",
                        },
                        "elapsed_time": 60,
                        "playbook": {"display_name": "Playbook 1", "description": "This is playbook 1"},
                    }
                ],
                "tasktree": [
                    {
                        "phase_name": "phase1",
                        "tasks": [
                            {"name": "task1", "active": True, "required": True, "complete": True},
                            {"name": "task2", "active": False, "required": False, "complete": False},
                        ],
                    }
                ],
            }
        }
        expected_chunks = [
            "incident: {'name': 'Test Incident', 'description': 'This is a test incident', 'start_date': '2023-01-01', 'inc_start': '2023-01-01', 'discovered_date': '2023-01-01', 'creator_principal': {'id': '12345', 'type': 'user', 'name': 'John Doe', 'display_name': 'John Doe'}, 'reporter': 'john.doe@example.com', 'state': 'open', 'country': 'US', 'zip': '12345', 'workspace': 'test_workspace', 'members': ['user1', 'user2'], 'negative_pr_likely': True, 'assessment': 'low', 'properties': {'severity': 'low'}, 'inc_last_modified_date': '2023-01-01', 'incident_disposition': 'resolved', 'artifacts': [{'value': 'artifact1', 'type': 'file', 'inc_name': 'artifact1', 'related_incident_count': 1, 'summary': 'This is artifact 1'}], 'playbook_executions': [{'status': 'success', 'object': {'parent': {'parent': {'parent': None, 'object_id': '12345', 'object_name': 'Parent Object', 'type_id': '12345', 'type_name': 'Parent Type'}, 'object_id': '67890', 'object_name': 'Child Object', 'type_id': '67890', 'type_name': 'Child Type'}, 'object_id': '98765', 'object_name': 'Grandchild Object', 'type_id': '98765', 'type_name': 'Grandchild Type'}, 'elapsed_time': 60, 'playbook': {'display_name': 'Playbook 1', 'description': 'This is playbook 1'}}], 'tasktree': [{'phase_name': 'phase1', 'tasks': [{'name': 'task1', 'active': True, 'required': True, 'complete': True}, {'name': 'task2', 'active': False, 'required': False, 'complete': False}]}]}" # pylint: disable=line-too-long
        ]
        actual_chunks = Chunking.split_json_to_chunks_prompts(self.chunking, data)
        assert actual_chunks == expected_chunks


    def test_split_description_properties(self):
        # Test to see if properties and descrptions are chunked properly
        data = {
            "incident": {
            "name": "Test Incident",
            "description": "During a routine audit of logs, the HSE Ireland's security information and event management (SIEM) system detected unusual network activity. The incident was identified at 14:45 IST, but the cause and nature of the activity are currently unknown.",
            "start_date": "2023-01-01",
            "inc_start": "2023-01-01",
            "discovered_date": "2023-01-01",
            "creator_principal": {"id": "12345", "type": "user", "name": "John Doe", "display_name": "John Doe"},
            "reporter": "john.doe@example.com",
            "state": "open",
            "country": "US",
            "zip": "12345",
            "workspace": "test_workspace",
            "members": ["user1", "user2"],
            "negative_pr_likely": True,
            "assessment": "low",
            'properties': {'internal_customizations_field': None,
   'blah1': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec quis venenatis mauris. Etiam id mi vel lectus malesuada placerat quis sed nisl. Nullam blandit, non magna in ultrices. Pellentesque sodales ultricies risus eget ornare. Nulla facilisi. Proin ultricies vestibulum auctor. Suspendisse eget nisl quam. Duis blandit viverra feugiat. Nunc sit amet imperdiet nibh, eget mollis sapien. Maecenas congue odio eu nulla iaculis, non rutrum quam ullamcorper.Ut ac egestas urna, id porta justo. Nunc nec magna dignissim, blandit libero in, ultrices nunc. Aliquam dapibus quis dolor sed scelerisque. Quisque condimentum tellus non magna ornare, ac maximus lacus varius. Curabitur vestibulum.'},
            "inc_last_modified_date": "2023-01-01",
            "incident_disposition": "resolved",
            "artifacts": [
                {
                    "value": "artifact1",
                    "type": "file",
                    "inc_name": "artifact1",
                    "related_incident_count": 1,
                    "summary": "This is artifact 1",
                }
            ],
            "playbook_executions": [
                {
                    "status": "success",
                    "object": {
                        "parent": {
                            "parent": {
                                "parent": None,
                                "object_id": "12345",
                                "object_name": "Parent Object",
                                "type_id": "12345",
                                "type_name": "Parent Type",
                            },
                            "object_id": "67890",
                            "object_name": "Child Object",
                            "type_id": "67890",
                            "type_name": "Child Type",
                        },
                        "object_id": "98765",
                        "object_name": "Grandchild Object",
                        "type_id": "98765",
                        "type_name": "Grandchild Type",
                    },
                    "elapsed_time": 60,
                    "playbook": {"display_name": "Playbook 1", "description": "This is playbook 1"},
                }
            ],
            "tasktree": [
                {
                    "phase_name": "phase1",
                    "tasks": [
                        {"name": "task1", "active": True, "required": True, "complete": True},
                        {"name": "task2", "active": False, "required": False, "complete": False},
                    ],
                }
            ],
        }
    }
        expected_chunks = ['{"properties": {"index": 0, "properties": "\'internal_customizations_field\': None"}}', '{"properties": {"index": 1, "properties": "\'blah1\': \'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec quis venenatis mauris. Etiam id mi vel lectus malesuada placerat quis sed nisl. Nullam blandit, non magna in ultrices. Pellentesque sodales ultricies risus eget ornare. Nulla facilisi. Proin ultricies vestibulum auctor. Suspendisse eget nisl quam. Duis blandit viverra feugiat. Nunc sit amet imperdiet nibh, eget\'"}}', '{"properties": {"index": 2, "properties": "\'blah1\': \' mollis sapien. Maecenas congue odio eu nulla iaculis, non rutrum quam ullamcorper.Ut ac egestas urna, id porta justo. Nunc nec magna dignissim, blandit libero in, ultrices nunc. Aliquam dapibus quis dolor sed scelerisque. Quisque condimentum tellus non magna ornare, ac maximus lacus varius. Curabitur vestibulum.\'"}}', '{"incident": {"name": "Test Incident", "start_date": "2023-01-01", "inc_start": "2023-01-01", "discovered_date": "2023-01-01", "creator_principal": {"type": "user", "display_name": "John Doe"}, "reporter": "john.doe@example.com", "state": "open", "country": "US", "zip": "12345", "workspace": "test_workspace", "members": ["user1", "user2"], "negative_pr_likely": true, "inc_last_modified_date": "2023-01-01", "incident_disposition": "resolved", "description": "During a routine audit of logs, the HSE Ireland\'s security information and event management (SIEM) system detected unusual network activity. The incident was identified at 14:45 IST, but the cause and nature of the activity are currently unknown."}}', '{"artifact": {"value": "artifact1", "type": "file", "inc_name": "artifact1", "related_incident_count": 1, "summary": "This is artifact 1"}}', '{"playbook_execution": {"status": "success", "object": {"parent": {"object_name": "Child Object", "type_name": "Child Type"}, "object_name": "Grandchild Object", "type_name": "Grandchild Type"}, "elapsed_time": 60, "playbook": {"display_name": "Playbook 1", "description": "This is playbook 1"}}}', '{"task": {"phase": "phase1", "name": "task1", "active": true, "required": true, "complete": "complete"}}', '{"task": {"phase": "phase1", "name": "task2", "active": false, "required": false, "complete": "incomplete"}}']
        actual_chunks = Chunking.split_json_to_chunks(self.chunking, data, 100)
        print(actual_chunks)
        assert actual_chunks == expected_chunks
    def test_flatten_dict_single_level(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        expected = {'a': 1, 'b': 2, 'c': 3}
        actual = Chunking.flatten_dict(self.chunking, d)
        assert actual==expected

    def test_flatten_dict_nested_dict(self):
        d = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
        expected = {'a': 1, 'b.c': 2, 'b.d': 3, 'e': 4}
        actual = Chunking.flatten_dict(self.chunking, d)
        assert actual==expected

    def test_flatten_dict_nested_dict_with_custom_separator(self):
        d = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
        expected = {'a': 1, 'b:c': 2, 'b:d': 3, 'e': 4}
        actual = Chunking.flatten_dict(self.chunking, d, sep=':')
        assert actual==expected
   