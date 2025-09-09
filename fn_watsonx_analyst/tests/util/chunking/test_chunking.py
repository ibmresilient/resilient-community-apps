import random
import pytest
import json
import faiss

from unittest.mock import Mock, patch

from fn_watsonx_analyst.util.chunking.chunking import Chunking
from fn_watsonx_analyst.util.QueryHelper import QueryHelper
from fn_watsonx_analyst.util.state_manager import app_state
from tests import helper


class TestChunking:
    """Tests the Chunking Class"""

    text: str
    max_tokens: int
    chunking: Chunking

    def setup_method(self):
        """
        Sets up the necessary parameters and initializes Chunking and QueryHelper classes.
        """
        self.text = "This is a sample text to test the split_data_into_token_chunks function."
        self.max_tokens = 10
        self.chunking = Chunking(init_query_helper=False)

    def test_special_token_encoding(self):
        self.chunking.split_data_into_token_chunks("<|endoftext|>", self.max_tokens)


    def test_empty_text(self):
        """Test if empty chunks are created."""
        chunks = self.chunking.split_data_into_token_chunks("", self.max_tokens)
        assert not chunks

    def test_single_word(self):
        """Test if a single chunk is created."""
        chunks = Chunking.split_data_into_token_chunks(self.chunking, "This ", self.max_tokens)
        assert chunks == ["This"]

    def test_multiple_words(self):
        """Test if multiple chunks are created"""
        chunks = Chunking.split_data_into_token_chunks(self.chunking, self.text, self.max_tokens)
        assert len(chunks) <= self.max_tokens

    def test_max_tokens_exceeded(self):
        """Test if max tokens are exceeded."""
        chunks = Chunking.split_data_into_token_chunks(self.chunking, self.text, 5)
        assert len(chunks) <= 5

    def test_estimate_tokens(self):
        """Test for estimate tokens method."""
        assert Chunking.estimate_tokens(self.chunking, "This") == 1
        assert Chunking.estimate_tokens(self.chunking, "is") == 1
        assert Chunking.estimate_tokens(self.chunking, "a") == 1
        assert Chunking.estimate_tokens(self.chunking, "sample") == 1
        assert Chunking.estimate_tokens(self.chunking, "text") == 1

    def test_split_text_to_tokens_chunks(self):
        """Testing conversion of string to chunks based on size"""
        description = "During a routine audit of logs, the HSE Ireland's security information and event management (SIEM) system detected unusual network activity. The incident was identified at 14:45 IST, but the cause and nature of the activity are currently unknown."
        max_chunk_size = 10
        chunks = Chunking.split_text_to_token_chunks(self.chunking, description, max_chunk_size)
        assert isinstance(chunks, list)

    def test_tokens_for_model(self):
        """Tests the token langth of the model"""
        model_name = "ibm/granite-guardian-3-8b"
        length = Chunking.max_tokens_for_model(model_name)
        assert length==8192

    def test_relevant_chunks_watsonx(self):
        """Test the retrieval of relevant chunks from a list of chunks based on a query and a similarity threshold."""
        # Mock the query_helper
        mock_query_helper = Mock()
        
        # Define the mock behavior for generate_embeddings
        mock_query_helper.generate_embeddings.side_effect = lambda data: [
            [0.1, 0.2, 0.3] if d == "example query" else [0.3, 0.2, 0.1] for d in data
        ]
        
        # Inject the mock query_helper
        self.chunking.query_helper = mock_query_helper
        
        # Define the test inputs
        query = "example query"
        chunks = ["chunk 1", "chunk 2", "chunk 3"]
        total_tokens = 1000
        threshold = 0.6

        app_state.get().set_model("mistralai/mistral-large",)
        
        # Call the method under test
        selected_chunks = self.chunking.retrieve_relevant_chunks_watsonx(
            query, chunks,  total_tokens, threshold
        )
        
        # Assert conditions
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
        """test if a simple JSON spit is working."""
        data = {"key1": "value1", "key2": "value2", "key3": "value3"}
        expected_chunks = ["key1: value1", "key2: value2", "key3: value3"]
        chunks = Chunking.split_json_to_chunks_prompts(self.chunking, data)
        assert expected_chunks == chunks

    def test_long_text_split(self):
        """test if JSON chunking works for longer text."""
        data = {"key1": "This is a long text that needs to be split into chunks", "key2": "value2", "key3": "value3"}
        expected_chunks = [
            "key1: This is a long text that needs to be split into chunks",
            "key2: value2",
            "key3: value3",
        ]
        chunks = Chunking.split_json_to_chunks_prompts(self.chunking, data)
        assert expected_chunks == chunks

    def test_max_chunk_size(self):
        """Test if max chunk size changes the overall output."""
        data = {"key1": "value1", "key2": "value2", "key3": "value3"}
        expected_chunks = ["key1: value1", "key2: value2", "key3: value3"]
        chunks = Chunking.split_json_to_chunks_prompts(self.chunking, data, max_chunk_size=100)
        assert expected_chunks == chunks
    
    def test_split_json_to_chunks(self):
        """Test to see exact chunk values """
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
                        "created": "2023-01-01",
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
        expected_chunks = ['{value: {incident.name: Test Incident}}', '{value: {incident.description: This is a test incident}}', '{value: {incident.start_date: 2023-01-01}}', '{value: {incident.inc_start: 2023-01-01}}', '{value: {incident.discovered_date: 2023-01-01}}', '{value: {creator_principal.id: 12345}, {creator_principal.type: user}, {creator_principal.name: John Doe}, {creator_principal.display_name: John Doe}}', '{value: {incident.reporter: john.doe@example.com}}', '{value: {incident.state: open}}', '{value: {incident.country: US}}', '{value: {incident.zip: 12345}}', '{value: {incident.workspace: test_workspace}}', '{value: {incident.members: user1}}', '{value: {incident.members: user2}}', '{value: {incident.negative_pr_likely: True}}', '{value: {incident.assessment: low}}', '{value: {properties.severity: low}}', '{value: {incident.inc_last_modified_date: 2023-01-01}}', '{value: {incident.incident_disposition: resolved}}', '{value: {artifacts.value: artifact1}, {artifacts.type: file}, {artifacts.inc_name: artifact1}, {artifacts.created: 2023-01-01}, {artifacts.related_incident_count: 1}, {artifacts.summary: This is artifact 1}}', '{value: {playbook_executions.status: success}, {playbook_executions.elapsed_time: 60}}', '{value: {playbook_executions.status: success}, {parent.object_name: Parent Object}, {parent.object_id: 12345}, {parent.object_name: Parent Object}, {parent.type_id: 12345}, {parent.type_name: Parent Type}, {parent.object_id: 67890}, {parent.object_name: Child Object}, {parent.type_id: 67890}, {parent.type_name: Child Type}, {object.object_id: 98765}, {object.object_name: Grandchild Object}, {object.type_id: 98765}, {object.type_name: Grandchild Type}}', '{value: {playbook_executions.status: success}, {playbook.display_name: Playbook 1}, {playbook.description: This is playbook 1}}', '{value: {tasktree.phase_name: phase1}}', '{value: {tasktree.phase_name: phase1}, {tasks.name: task1}, {tasks.active: True}, {tasks.required: True}, {tasks.complete: True}}', '{value: {tasktree.phase_name: phase1}, {tasks.name: task2}, {tasks.active: False}, {tasks.required: False}, {tasks.complete: False}}']
        actual_chunks = Chunking.split_json_to_chunks(self.chunking, data)
        assert actual_chunks == expected_chunks


    def test_split_description_properties(self):
        """Test to see if properties and descrptions are chunked properly"""
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
        expected_chunks = ['{value: {incident.name: Test Incident}}', '{value: {incident.description: During a routine audit of logs}, the HSE Irelands security information and event management (SIEM) system detected unusual network activity. The incident was identified at 14:45 IST, but the cause and nature of the activity are currently unknown.}', '{value: {incident.start_date: 2023-01-01}}', '{value: {incident.inc_start: 2023-01-01}}', '{value: {incident.discovered_date: 2023-01-01}}', '{value: {creator_principal.id: 12345}, {creator_principal.type: user}, {creator_principal.name: John Doe}, {creator_principal.display_name: John Doe}}', '{value: {incident.reporter: john.doe@example.com}}', '{value: {incident.state: open}}', '{value: {incident.country: US}}', '{value: {incident.zip: 12345}}', '{value: {incident.workspace: test_workspace}}', '{value: {incident.members: user1}}', '{value: {incident.members: user2}}', '{value: {incident.negative_pr_likely: True}}', '{value: {incident.assessment: low}}', '{path: incident.properties.blah1, value: {properties.blah1: Lorem ipsum dolor sit amet}, consectetur adipiscing elit. Donec quis venenatis mauris. Etiam id mi vel lectus malesuada placerat quis sed nisl. Nullam blandit, non magna in ultrices. Pellentesque sodales ultricies risus eget ornare. Nulla facilisi. Proin ultricies vestibulum auctor. Suspendisse eget nisl quam. Duis blandit viverra feugiat. Nunc sit amet}', '{path: incident.properties.blah1, value: imperdiet nibh, eget mollis sapien. Maecenas congue odio eu nulla iaculis, non rutrum quam ullamcorper.Ut ac egestas urna, id porta justo. Nunc nec magna dignissim, blandit libero in, ultrices nunc. Aliquam dapibus quis dolor sed scelerisque. Quisque condimentum tellus non magna ornare, ac maximus lacus varius. Curabitur vestibulum.}', '{value: {incident.inc_last_modified_date: 2023-01-01}}', '{value: {incident.incident_disposition: resolved}}', '{value: {artifacts.value: artifact1}, {artifacts.type: file}, {artifacts.inc_name: artifact1}, {artifacts.related_incident_count: 1}, {artifacts.summary: This is artifact 1}}', '{value: {playbook_executions.status: success}, {playbook_executions.elapsed_time: 60}}', '{path: incident.playbook_executions.status, value: {playbook_executions.status: success}, {parent.object_name: Parent Object}, {parent.object_id: 12345}, {parent.object_name: Parent Object}, {parent.type_id: 12345}, {parent.type_name: Parent Type}, incident}', '{path: incident.playbook_executions.status, value: .{parent.object_id: 67890}, {parent.object_name: Child Object}, {parent.type_id: 67890}, {parent.type_name: Child Type}, {object.object_id: 98765}, {object.object_name: Grandchild Object}, incident.playbook}', '{path: incident.playbook_executions.status, value: {object.type_id: 98765}, {object.type_name: Grandchild Type}}', '{value: {playbook_executions.status: success}, {playbook.display_name: Playbook 1}, {playbook.description: This is playbook 1}}', '{value: {tasktree.phase_name: phase1}}', '{value: {tasktree.phase_name: phase1}, {tasks.name: task1}, {tasks.active: True}, {tasks.required: True}, {tasks.complete: True}}', '{value: {tasktree.phase_name: phase1}, {tasks.name: task2}, {tasks.active: False}, {tasks.required: False}, {tasks.complete: False}}']
        actual_chunks = Chunking.split_json_to_chunks(self.chunking, data, 100)
        assert actual_chunks == expected_chunks

    def test_flatten_dict_single_level(self):
        """Tests Flattening of a dictionary with single level."""
        d = {'a': 1, 'b': 2, 'c': 3}
        expected = {'a': 1, 'b': 2, 'c': 3}
        actual = Chunking.flatten_dict(self.chunking, d)
        assert actual==expected

    def test_flatten_dict_nested_dict(self):
        """Tests Flattening of a dictionary with nested level."""
        d = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
        expected = {'a': 1, 'b.c': 2, 'b.d': 3, 'e': 4}
        actual = Chunking.flatten_dict(self.chunking, d)
        assert actual==expected

    def test_flatten_dict_nested_dict_with_custom_separator(self):
        """Tests Flattening of a dictionary with custom separator."""
        d = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
        expected = {'a': 1, 'b:c': 2, 'b:d': 3, 'e': 4}
        actual = Chunking.flatten_dict(self.chunking, d, sep=':')
        assert actual==expected

    def test_create_faiss_index(self):
        """Tests FAISS INDEX and its dimentionality"""
        embeddings = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index = Chunking.create_faiss_index(self.chunking, embeddings)
        assert isinstance(index, faiss.IndexFlatL2), f"Expected index to be instance of faiss.IndexFlatL2, got {type(index)}"

        # Replace self.assertEqual with plain assert
        assert index.ntotal == 3, f"Expected index.ntotal to be 3, got {index.ntotal}"
        assert index.d == 3, f"Expected index.d to be 3, got {index.d}"

    def test_extract_key_value_pairs_dict(self):
        """Test the extract_key_value_pairs function with a dictionary input. """
        data = {
            "name": "John",
            "age": 30,
            "address": {
                "street": "123 Main St",
                "city": "Anytown"
            }
        }
        expected_results = [('name', 'John'),
                            ('age', 30),
                            ('address.street', '123 Main St'),
                            ('address.city', 'Anytown')]

        actual_results = Chunking.extract_key_value_pairs(self.chunking, data)
        assert actual_results == expected_results

    def test_extract_key_value_pairs_list(self):
        """Test the extract_key_value_pairs function with a dictionary input. """
        data = [
            {
                "name": "John",
                "age": 30
            },
            {
                "name": "Jane",
                "age": 25
            }
        ]
        expected_results = [
            ("[0].name", "John"),
            ("[0].age", 30),
            ("[1].name", "Jane"),
            ("[1].age", 25)
        ]
        actual_results = Chunking.extract_key_value_pairs(self.chunking, data)
        assert actual_results == expected_results

    def test_extract_key_value_pairs_nested_dict(self):
        """Test the extract_key_value_pairs function with a dictionary input. """
        data = {
            "name": "John",
            "age": 30,
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "zip": {
                    "code": "12345"
                }
            }
        }
        expected_results = [
            ("name", "John"),
            ("age", 30),
            ("address.street", "123 Main St"),
            ("address.city", "Anytown"),
            ("address.zip.code", "12345")
        ]
        actual_results = Chunking.extract_key_value_pairs(self.chunking, data)
        assert actual_results == expected_results

    def test_extract_key_value_pairs_nested_list(self):
        """Test the extract_key_value_pairs function with a dictionary input. """
        data = {
            "name": "John",
            "age": 30,
            "address": [
                {
                    "street": "123 Main St",
                    "city": "Anytown"
                },
                {
                    "street": "456 Elm St",
                    "city": "Anytown"
                }
            ]
        }
        expected_results = [
            ("name", "John"),
            ("age", 30),
            ("address[0].street", "123 Main St"),
            ("address[0].city", "Anytown"),
            ("address[1].street", "456 Elm St"),
            ("address[1].city", "Anytown")
        ]
        actual_results = Chunking.extract_key_value_pairs(self.chunking, data)
        assert actual_results == expected_results

    def test_dict_with_dict(self):
        """ test to check processing of key value pair in a dict"""
        data = {
            "key1": {
                "key2": "value2",
                "key3": "value3"
            }
        }
        expected_results = [("key1.key2", "value2"), ("key1.key3", "value3")]
        actual_results = Chunking.extract_key_value_pairs(self.chunking,data)
        assert actual_results == expected_results

    def test_nested_list_with_dict(self):
        """ test to check processing of key value pairs in a list of dicts"""
        data = [
            [
                {
                    "key1": "value1",
                    "key2": "value2"
                },
                {
                    "key3": "value3",
                    "key4": "value4"
                }
            ]
        ]
        expected_results = [('[0][0].key1', 'value1'), ('[0][0].key2', 'value2'), ('[0][1].key3', 'value3'), ('[0][1].key4', 'value4')]
        actual_results = Chunking.extract_key_value_pairs(self.chunking,data)
        assert actual_results == expected_results


    def test_process_json_data(self):
        """ testing the processing of nested keys correctly """
        data = {
            'key1.subkey1.subsubkey1': 'value1',
            'key1.subkey1.subsubkey2': 'value2',
            'key1.subkey2.subsubkey1': 'value3',
            'key2.subkey1.subsubkey1': 'value4',
            'key2.subkey1.subsubkey2': 'value5',
            'key2.subkey2.subsubkey1': 'value6',
        }
        expected_results = {'subkey1': [('key1.subkey1.subsubkey1', 'value1'), ('key1.subkey1.subsubkey2', 'value2'), ('key2.subkey1.subsubkey1', 'value4'), ('key2.subkey1.subsubkey2', 'value5')], 'subkey2': [('key1.subkey2.subsubkey1', 'value3'), ('key2.subkey2.subsubkey1', 'value6')]}
        actual_results = Chunking.process_json_data(self.chunking,data)
        assert actual_results == expected_results

    def test_process_json_data_with_nested_keys(self):
        """ testing the processing of a mix of different nested keys correctly """
        data = {
            'key1.subkey1.subsubkey1': 'value1',
            'key1.subkey1.subsubkey2': 'value2',
            'key1.subkey2.subsubkey1': 'value3',
            'key2.subkey1.subsubkey1': 'value4',
            'key2.subkey1.subsubkey2': 'value5',
            'key2.subkey2.subsubkey1': 'value6',
            'key3.subkey1.subsubkey1.subsubsubkey1': 'value7',
            'key3.subkey1.subsubkey1.subsubsubkey2': 'value8',
            'key3.subkey1.subsubkey2.subsubsubkey1': 'value9',
            'key3.subkey2.subsubkey1.subsubsubkey1': 'value10',
            'key3.subkey2.subsubkey1.subsubsubkey2': 'value11',
            'key3.subkey2.subsubkey2.subsubsubkey1': 'value12',
        }
        expected_results = {'subkey1': [('key1.subkey1.subsubkey1', 'value1'), ('key1.subkey1.subsubkey2', 'value2'), ('key2.subkey1.subsubkey1', 'value4'), ('key2.subkey1.subsubkey2', 'value5')], 'subkey2': [('key1.subkey2.subsubkey1', 'value3'), ('key2.subkey2.subsubkey1', 'value6')], 'key3.subkey1.subsubkey1': [('key3.subkey1.subsubkey1.subsubsubkey2', 'value8'), ('key3.subkey1.subsubkey1.subsubsubkey1', 'value7'), ('key3.subkey1.subsubkey1.subsubsubkey2', 'value8')], 'key3.subkey1.subsubkey2': [('key3.subkey1.subsubkey1.subsubsubkey1', 'value7'), ('key3.subkey1.subsubkey2.subsubsubkey1', 'value9')], 'key3.subkey2.subsubkey1': [('key3.subkey2.subsubkey1.subsubsubkey2', 'value11'), ('key3.subkey2.subsubkey1.subsubsubkey1', 'value10'), ('key3.subkey2.subsubkey1.subsubsubkey2', 'value11')], 'key3.subkey2.subsubkey2': [('key3.subkey2.subsubkey1.subsubsubkey1', 'value10'), ('key3.subkey2.subsubkey2.subsubsubkey1', 'value12')]}
        actual_results = Chunking.process_json_data(self.chunking,data)
        assert actual_results == expected_results

    def test_process_json_data_with_single_key(self):
        """Testing the results of a single key-value pair for correctness"""
        data = {
            'key1': 'value1',
        }
        expected_results = {
            'key1': [('key1', 'value1')],
        }
        actual_results = Chunking.process_json_data(self.chunking,data)
        assert actual_results == expected_results

    def test_process_json_data_with_no_keys(self):
        """Testing the results of a zero key-value pair for correctness"""
        data = {}
        expected_results = {}
        actual_results = Chunking.process_json_data(self.chunking,data)
        assert actual_results == expected_results

    def test_clean_text(self):
        """Testing the correctness of text cleanup"""
        actual_result = 'This is a "sample" text with <b>HTML</b> tags and "key: value" pairs.'
        expected_result = 'This is a sample text with HTML tags and key: value pairs.'
        assert Chunking.clean_text(self.chunking, actual_result) == expected_result

    def test_clean_text_with_html_tags(self):
        """Testing the correctness of text cleanup with html tags"""
        actual_result = 'This is a <b>sample</b> text with <b>HTML</b> tags and "key: value" pairs.'
        expected_result = 'This is a sample text with HTML tags and key: value pairs.'
        assert Chunking.clean_text(self.chunking, actual_result) == expected_result

    def test_clean_text_with_key_value_pairs(self):
        """Testing the correctness of text cleanup with key-value pairs"""
        actual_result = 'This is a "sample" text with <b>HTML</b> tags and "incident.artifacts[2].value: Pay 500 000 in Bitcoin.txt" pairs.'
        expected_result = 'This is a sample text with HTML tags and {artifacts.value: Pay 500 000 in Bitcoin.txt pairs.}'
        assert Chunking.clean_text(self.chunking, actual_result) == expected_result

    def test_clean_text_with_special_characters(self):
        """Testing the correctness of text cleanup when text has special characters(we retain some like !()_"""
        actual_result = 'This is a "sample" text with <b>HTML</b> tags and "key: value" pairs.!#$%^&*()_+'
        expected_result = 'This is a sample text with HTML tags and key: value pairs.!()_'
        assert Chunking.clean_text(self.chunking, actual_result) == expected_result

    def test_clean_text_with_non_ascii_characters(self):
        """Tests to check if non ascii chars are removed from chunks"""
        actual_result = 'This is a "sample" text with <b>HTML</b> tags and "key: value" pairs. 你好，世界'
        expected_result = 'This is a sample text with HTML tags and key: value pairs. '
        assert Chunking.clean_text(self.chunking, actual_result) == expected_result

    def test_preprocess_chunks(self):
        """Tests to check if chunks are a list and str type"""
        chunks = ['This is a "sample" text with <b>HTML</b> tags and "key: value" pairs. 你好，世界']
        assert isinstance(chunks, list)
        assert all(isinstance(chunk, str) for chunk in chunks)

    def test_ensure_newlines_preserved(self):
        input_str = """a
b
c"""
        assert ' | '.join(Chunking.split_data_into_token_chunks(self.chunking, input_str)).count('\n') == 2
