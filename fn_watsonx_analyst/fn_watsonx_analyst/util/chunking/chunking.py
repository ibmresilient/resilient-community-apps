"""Chunking class to generate segmented data, which can be used in the RAG system."""

import json
import random
import logging
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fn_watsonx_analyst.types.incident_full_data import IncidentFullData
import tiktoken

from fn_watsonx_analyst.util.util import get_model_config

logger = logging.getLogger(__name__)


class Chunking:
    """Class for Chunking and picking most relevant chunk for GenAI use cases"""

    def __init__(self) -> None:
        pass

    def split_json_to_chunks(self, data: IncidentFullData) -> List[str]:
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
                try:
                    return {k: v for k, v in d.items() if v is not None}
                except Exception as e:
                    logger.exception(
                        "An error occurred while running filter_null_fields method in split_json_to_chunks method: %s",
                        e,
                    )
                    raise

            # Chunk incident details
            incident_chunk = {
                "incident": filter_null_fields(
                    {
                        "name": data["incident"]["name"],
                        "description": data["incident"]["description"],
                        "addr": data["incident"].get("addr", None),
                        "city": data["incident"].get("city", None),
                        "start_date": data["incident"]["start_date"],
                        "inc_start": data["incident"]["inc_start"],
                        "discovered_date": data["incident"]["discovered_date"],
                        "creator_principal": filter_null_fields(
                            {
                                "id": data["incident"]["creator_principal"]["id"],
                                "type": data["incident"]["creator_principal"]["type"],
                                "name": data["incident"]["creator_principal"]["name"],
                                "display_name": data["incident"]["creator_principal"][
                                    "display_name"
                                ],
                            }
                        ),
                        "reporter": data["incident"].get("reporter", None),
                        "state": data["incident"].get("state", None),
                        "country": data["incident"].get("country", None),
                        "zip": data["incident"].get("zip", None),
                        "workspace": data["incident"]["workspace"],
                        "members": data["incident"].get("members", []),
                        "negative_pr_likely": data["incident"].get(
                            "negative_pr_likely", None
                        ),
                        "assessment": data["incident"]["assessment"],
                        "properties": data["incident"].get("properties", {}),
                        "inc_last_modified_date": data["incident"][
                            "inc_last_modified_date"
                        ],
                        "incident_disposition": data["incident"][
                            "incident_disposition"
                        ],
                    }
                )
            }

            chunks.append(json.dumps(incident_chunk))

            # Chunk artifacts
            for artifact in data["incident"]["artifacts"]:
                logger.debug("Chunking artifact %s", artifact["value"])
                artifact_chunk = {
                    "artifact": filter_null_fields(
                        {
                            "value": artifact["value"],
                            "created": artifact.get("created", None),
                            "last_modified_time": artifact.get(
                                "last_modified_time", None
                            ),
                            "description": artifact.get("description", None),
                            "type": artifact["type"],
                            "related_incident_count": artifact.get(
                                "related_incident_count", None
                            ),
                        }
                    )
                }
                chunks.append(json.dumps(artifact_chunk))

            # Chunk playbook executions
            for execution in data["incident"]["playbook_executions"]:
                playbook_chunk = {
                    "playbook_execution": filter_null_fields(
                        {
                            "status": execution["status"],
                            "object": filter_null_fields(
                                {
                                    "parent": (
                                        filter_null_fields(
                                            {
                                                "parent": execution["object"]
                                                .get("parent", {})
                                                .get("parent", None),
                                                "object_id": execution["object"]
                                                .get("parent", {})
                                                .get("object_id", None),
                                                "object_name": execution["object"]
                                                .get("parent", {})
                                                .get("object_name", None),
                                                "type_id": execution["object"]
                                                .get("parent", {})
                                                .get("type_id", None),
                                                "type_name": execution["object"]
                                                .get("parent", {})
                                                .get("type_name", None),
                                            }
                                        )
                                        if execution["object"].get("parent")
                                        else None
                                    ),
                                    "object_id": execution["object"].get(
                                        "object_id", None
                                    ),
                                    "object_name": execution["object"].get(
                                        "object_name", None
                                    ),
                                    "type_id": execution["object"].get("type_id", None),
                                    "type_name": execution["object"].get(
                                        "type_name", None
                                    ),
                                }
                            ),
                            "elapsed_time": execution["elapsed_time"],
                            "playbook": filter_null_fields(
                                {
                                    "display_name": execution["playbook"][
                                        "display_name"
                                    ],
                                    "description": execution["playbook"].get(
                                        "description", None
                                    ),
                                }
                            ),
                        }
                    )
                }
                chunks.append(json.dumps(playbook_chunk))

            # Chunk tasks
            for phase in data["incident"]["tasktree"]:
                for task in phase["tasks"]:
                    task_chunk = {
                        "task": filter_null_fields(
                            {
                                "phase": phase["phase_name"],
                                "name": task["name"],
                                "active": task.get("active", None),
                                "required": task.get("required", None),
                                "complete": (
                                    "complete" if task["complete"] else "incomplete"
                                ),
                            }
                        )
                    }
                    chunks.append(json.dumps(task_chunk))

            return chunks
        except Exception as e:
            logger.exception(
                "An error occurred while running split_json_to_chunks method: %s", e
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
                "An error occurred while running max_tokens_for_model method: %s", e
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
                "An error occurred while running split_data_into_token_chunks method: %s",
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
                "An error occurred while running estimate_tokens method: %s", e
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
                "An error occurred while running split_data_into_token_chunks_overlap method: %s",
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
                "An error occurred while running random_chunks method: %s", e
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
                "An error occurred while running retrieve_top_chunks_tfidf method: %s",
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
                "An error occurred while running split_json_to_chunks_prompts method: %s",
                e,
            )
            raise
