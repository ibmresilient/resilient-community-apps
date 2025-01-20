"""Chunking class to generate segmented data, which can be used in the RAG system."""

import json
import random
from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tiktoken

from fn_watsonx_analyst.types.incident_full_data import IncidentFullData
from fn_watsonx_analyst.util.util import create_logger
from fn_watsonx_analyst.util.util import get_model_config

logger = create_logger(__name__)

class Chunking:
    """Class for Chunking and picking most relevant chunk for GenAI use cases"""

    def __init__(self) -> None:
        pass

    def split_json_to_chunks(self, data: IncidentFullData, max_tokens_per_chunk = 500) -> List[str]:
        """This is a custom chunking method of JSON payload for Case QnA via Notes

        Args:
            data (dict): Input Data

        Returns:
            List[str]: Chunks - the sections of input
        """
        try:
            chunks = []

            # Helper function to filter out null fields
            def filter_null_fields(d):
                return {k: v for k, v in d.items() if v is not None}

            # Chunk incident details excluding description and properties
            incident_data = filter_null_fields({
                "name": data['incident'].get('name', None),
                "addr": data['incident'].get('addr', None),
                "city": data['incident'].get('city', None),
                "start_date": data['incident'].get('start_date', None),
                "inc_start": data['incident'].get('inc_start', None),
                "discovered_date": data['incident'].get('discovered_date', None),
                "creator_principal": filter_null_fields({
                    "type": data['incident']['creator_principal'].get('type', None) if data['incident'].get('creator_principal') else None,
                    "display_name": data['incident']['creator_principal'].get('display_name', None) if data['incident'].get('creator_principal') else None,
                }),
                "reporter": data['incident'].get('reporter', None),
                "state": data['incident'].get('state', None),
                "country": data['incident'].get('country', None),
                "zip": data['incident'].get('zip', None),
                "workspace": data['incident'].get('workspace', None),
                "members": data['incident'].get('members', []),
                "negative_pr_likely": data['incident'].get('negative_pr_likely', None),
                "inc_last_modified_date": data['incident'].get('inc_last_modified_date', None),
                "incident_disposition": data['incident'].get('incident_disposition', None)
            })

            description = data['incident'].get('description', None)
            if description:  # Check if description is not None before processing
                if self.estimate_tokens(description) > max_tokens_per_chunk:
                    description_chunks = self.split_text_to_token_chunks(description, max_tokens_per_chunk)
                    for idx, desc_chunk in enumerate(description_chunks):
                        chunks.append(json.dumps({
                            "incident_description": {
                                "index": idx,
                                "description": desc_chunk
                            }
                        }))
                else:
                    # Add the description as a single chunk if it fits
                    incident_data["description"] = description

            # Check if properties is not None before proceeding
            properties = data['incident'].get('properties', {})
            if properties:  # Only process if properties is not None or empty
                flat_properties = self.flatten_dict(properties)

                # Flatten the nested dictionary
                chunk_index = 0
                for key, value in flat_properties.items():
                    if isinstance(value, str):  # Only split string values
                        property_chunks = self.split_text_to_token_chunks(value, max_tokens_per_chunk)
                        for prop_chunk in property_chunks:
                            chunks.append(json.dumps({
                                "properties": {
                                    "index": chunk_index,
                                    "properties": f"'{key}': '{prop_chunk}'"
                                }
                            }))
                            chunk_index += 1
                    else:
                        # Handle non-string values as-is (e.g., None or numeric values)
                        chunks.append(json.dumps({
                            "properties": {
                                "index": chunk_index,
                                "properties": f"'{key}': {value}"
                            }
                        }))
                        chunk_index += 1

            chunks.append(json.dumps({"incident": incident_data}))

            # Chunk artifacts
            for artifact in data['incident'].get('artifacts', []):
                artifact_chunk = {
                    "artifact": filter_null_fields({
                        "value": artifact.get('value', None),
                        "description": artifact.get('description', None),
                        "type": artifact.get('type', None),
                        "inc_name": artifact.get('inc_name', None),
                        "related_incident_count": artifact.get('related_incident_count', None),
                        "summary": artifact.get('summary', None)
                    })
                }
                chunks.append(json.dumps(artifact_chunk))

            # Chunk playbook executions
            for execution in data['incident'].get('playbook_executions', []):
                playbook_chunk = {
                    "playbook_execution": filter_null_fields({
                        "status": execution.get('status', None),
                        "object": filter_null_fields({
                            "parent": filter_null_fields({
                                "object_name": execution['object'].get('parent', {}).get('object_name', None),
                                "type_name": execution['object'].get('parent', {}).get('type_name', None)
                            }) if execution['object'].get('parent') else None,
                            "object_name": execution['object'].get('object_name', None),
                            "type_name": execution['object'].get('type_name', None)
                        }),
                        "elapsed_time": execution.get('elapsed_time', None),
                        "playbook": filter_null_fields({
                            "display_name": execution['playbook'].get('display_name', None),
                            "description": execution['playbook'].get('description', None)
                        })
                    })
                }
                chunks.append(json.dumps(playbook_chunk))

            # Chunk tasks
            for phase in data['incident'].get('tasktree', []):
                for task in phase.get('tasks', []):
                    task_chunk = {
                        "task": filter_null_fields({
                            "phase": phase.get('phase_name', None),
                            "name": task.get('name', None),
                            "active": task.get('active', None),
                            "required": task.get('required', None),
                            "complete": "complete" if task.get('complete', False) else "incomplete"
                        })
                    }
                    chunks.append(json.dumps(task_chunk))
            return chunks
        except Exception as e:
            logger.exception(
                "An error occurred while running pre-processing json data into chunks: %s", e
            )
            raise

    @staticmethod
    def max_tokens_for_model(model_id: str) -> int:
        """
        Returns the maximum number of tokens for a given model.

        Args:
            model_id (str): The name of the model.

        Returns:
            int: The maximum number of tokens for the given model.
        """
        try:
            # Get the list of models from the model_config.json file
            model_config = get_model_config()

            # Find the configuration for the given model
            model_conf = next(
                (config for config in model_config if config["model_name"] == model_id),
                None,
            )

            if not model_conf:
                # default
                return 4000

            return model_conf["context_length"]

        except Exception as e:
            logger.exception(
                "An error occurred while deciding max tokens for the model: %s", e
            )
            raise

    def split_data_into_token_chunks(self, text: str, max_tokens=500) -> List[str]:
        """
        Return a list of chunks of data, with each chunk not exceeding max_tokens
        """
        try:
            chunks: List[str] = []
            current_chunk = ""
            current_token_count = 0

            # Split the text into words
            words = text.split()

            for word in words:
                # Estimate tokens for the current word
                word_token_count = self.estimate_tokens(word)

                # Check if adding this word would exceed the max token count
                if current_token_count + word_token_count <= max_tokens:
                    current_chunk += word + " "
                    current_token_count += word_token_count
                else:
                    # Append the current chunk to the chunks list and reset
                    chunks.append(current_chunk.strip())
                    current_chunk = word + " "
                    current_token_count = word_token_count

            # Append the last chunk if any remaining
            if current_chunk:
                chunks.append(current_chunk.strip())

            return chunks
        except Exception as e:
            logger.exception(
                "An error occurred while pre-processing textual data into token chunks: %s",
                e,
            )
            raise

    def estimate_tokens(self, text: str) -> int:
        """
        Provide an approximation of the number of tokens in the input text
        """
        try:
            encoding = tiktoken.get_encoding("cl100k_base")
            num_tokens = len(encoding.encode(text))
            return num_tokens
        except Exception as e:
            logger.exception(
                "An error occurred while calculating tokens for a string text: %s", e
            )
            raise

    def split_text_to_token_chunks(self, text: str, max_tokens: int) -> list:
        """
        Splits a given text into chunks based on token size and chunk size limit
        """
        try:
            encoding = tiktoken.get_encoding("cl100k_base")
            tokens = encoding.encode(text)
            token_chunks = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]
            return [encoding.decode(chunk) for chunk in token_chunks]
        except Exception as e:
            logger.exception(
                "An error occurred while splitting text into token chunks: %s", e
            )
            raise

    def split_data_into_token_chunks_overlap(
        self, text: str, max_chunk_size=1000, overlap_size=200, min_chunk_size=400
    ) -> List[str]:
        """Create Overlapping Chunks

        Args:
            text str: Payload Text
            max_chunk_size (int, optional): _description_. Defaults to 1000.
            overlap_size (int, optional): _description_. Defaults to 200.
            min_chunk_size (int, optional): _description_. Defaults to 400.

        Returns:
            List[str]: Return chunks of size min_chunk_size
        """
        try:
            chunks = []
            temp_chunk = ""  # Temporary chunk for accumulating words until minimum size is reached

            # Split the text into words
            words = text.split()
            word_buffer = []  # Buffer to hold words until chunk size limits are reached

            for word in words:
                # Add the word to the current buffer and calculate the potential new chunk size
                word_buffer.append(word)
                current_chunk = " ".join(word_buffer)

                # If the accumulated chunk is smaller than max size but meets min size, add to chunks
                if len(current_chunk) >= min_chunk_size:
                    if len(current_chunk) >= max_chunk_size:
                        # Add the chunk to chunks
                        chunks.append(current_chunk)
                        # Reset buffer, adding overlap words
                        word_buffer = (
                            word_buffer[-(overlap_size // len(word)) :]
                            if overlap_size
                            else []
                        )
                    else:
                        temp_chunk = current_chunk

            # If there's any leftover temp_chunk after the loop, append it
            if temp_chunk:
                chunks.append(temp_chunk)

            return chunks
        except Exception as e:
            logger.exception(
                "An error occurred while creating overlapping chunks: %s",
                e,
            )
            raise

    def random_chunks(self, chunks: List[str], k=3) -> List[str]:
        """
        Returns a simple random sample of the input chunks, with up to k chunks
        """
        try:
            k = min(k, len(chunks))
            return random.sample(chunks, k)
        except Exception as e:
            logger.exception(
                "An error occurred while retieving random chunks: %s", e
            )
            raise

    def retrieve_top_chunks_tfidf(
        self,
        query: str,
        chunks: List[str],
        model_id: str,
        total_tokens=None,
        threshold=0.6,
    ) -> List[str]:
        """
        Using cosine similarity, retrieve the most similar chunks to the provided query, such that
        N ~<= total_tokens * threshold

        Args:
            query (str): "chunk" to use cosine similarity with data
            chunks (List[str]): Chunks of string data
            total_tokens (int): Maximum input *and* output chunks
            threshold (float): Fraction of tokens to delegate for chunk data
        """
        try:
            total_tokens = total_tokens or self.max_tokens_for_model(model_id)
            logger.debug("Total tokens: %d for model_id: %s", total_tokens, model_id)

            token_limit = total_tokens * threshold

            # Convert chunks to a list of strings for TF-IDF processing
            chunk_strings = [json.dumps(chunk, ensure_ascii=False) for chunk in chunks]

            # Create a TF-IDF Vectorizer and fit it on the chunks and query combined
            vectorizer = TfidfVectorizer(
                stop_words="english"
            )  # Use the stopwords filter from TF-IDF
            tfidf_matrix = vectorizer.fit_transform(chunk_strings + [query])

            # Compute cosine similarity between the query (last entry in matrix) and all chunks
            query_vector = tfidf_matrix[-1]
            chunk_vectors = tfidf_matrix[:-1]
            similarity_scores = cosine_similarity(query_vector, chunk_vectors).flatten()

            # Combine chunks and their similarity scores
            chunk_scores = [
                (chunks[i], similarity_scores[i]) for i in range(len(chunks))
            ]

            # Sort chunks based on similarity score (descending order)
            sorted_chunks = sorted(chunk_scores, key=lambda x: x[1], reverse=True)

            # Select chunks within the token limit
            selected_chunks = []
            token_count = 0

            for chunk, _ in sorted_chunks:
                chunk_str = json.dumps(chunk, ensure_ascii=False)
                chunk_token_count = self.estimate_tokens(chunk_str)

                # If adding this chunk exceeds the token limit, stop
                if token_count + chunk_token_count <= token_limit:
                    selected_chunks.append(chunk)
                    token_count += chunk_token_count
                else:
                    break  # Stop if we reach the token limit

            return selected_chunks
        except Exception as e:
            logger.exception(
                "An error occurred while retrieving top chunks using TF-IDF: %s",
                e,
            )
            raise

    def split_json_to_chunks_prompts(
        self, data: dict, max_chunk_size=2000
    ) -> List[str]:
        """
        Splits a JSON-like dictionary prompt into chunks of string prompts, each limited to a specified maximum size.
        Args:
            data (dict): A JSON-like prompt dict where each header description pair will be processed and converted to a string chunk.
            max_chunk_size (int) optional: The maximum allowed character length for each chunk (default is 2000).
        Returns:
            chunks (list): A list of string chunks, each representing a portion of the original data dictionary
        """
        try:
            chunks = []
            # Example: Splitting based on keys or sections within the JSON
            for key, value in data.items():
                # For simplicity, treating each key-value pair as a chunk
                chunk = f"{key}: {value}"
                if len(chunk) <= max_chunk_size:
                    chunks.append(chunk)
                else:
                    # Further split long text if needed
                    sub_chunks = []
                    chunks.extend(sub_chunks)
            return chunks
        except Exception as e:
            logger.exception(
                "An error occurred while retrieving best chunk prompts: %s",
                e,
            )
            raise
    def flatten_dict(self, d:dict, parent_key='', sep='.')->dict:
        """Recursively flatten a nested dictionary and prepend parent keys to maintain hierarchy.
        Args:
            d (dict): give a dictionary
            parent_key (str, optional): _description_. Defaults to ''.
            sep (str, optional): _description_. Defaults to '.'.

        Returns:
            dict: flattens the nested dictionary and returns it.
        """
        try:
            items = []
            for k, v in d.items():
                new_key = f"{parent_key}{sep}{k}" if parent_key else k
                if isinstance(v, dict):
                    items.extend(self.flatten_dict(v, new_key, sep=sep).items())
                else:
                    items.append((new_key, v))
            return dict(items)
        except Exception as e:
            logger.exception(
                "An error occurred while flattening a nested json: %s",
                e,
            )
            raise
