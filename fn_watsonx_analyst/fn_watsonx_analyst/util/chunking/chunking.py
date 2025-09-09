"""Chunking class to generate segmented data, which can be used in the RAG system."""

import json
import re
from typing import List

import numpy as np
import faiss
from bs4 import BeautifulSoup
import tiktoken

from fn_watsonx_analyst.types.incident_full_data import IncidentFullData
from fn_watsonx_analyst.util.model_helper import ModelHelper
from fn_watsonx_analyst.util.logging_helper import create_logger
from fn_watsonx_analyst.config import load_model_config
from fn_watsonx_analyst.util.QueryHelper import QueryHelper
from fn_watsonx_analyst.util.state_manager import app_state

logger = create_logger(__name__)


class Chunking:
    """Class for Chunking and picking most relevant chunk for GenAI use cases"""

    query_helper: QueryHelper

    def __init__(
        self, init_query_helper=True
    ) -> None:
        if init_query_helper:
            self.query_helper = QueryHelper()

    def clamped_chunks_for_model(self, data: List[str], model_id: str, threshold: float) -> List[str]:
        """
        Returns the maximum chunks that can be fit in the model with the given threshold percentage

        data: List of string chunks
        model_id: Model which we use to find maximum tokens for input. Will default to 32k tokens if unkown model
        threshold: Fraction of input to use for this chunk data - e.g., 0.4
        """
        max_tokens: int
        try:
            max_tokens = self.max_tokens_for_model(model_id)
        except:
            max_tokens = 32000 # fallback

        max_tokens = int(max_tokens * threshold)

        cumulative_tokens = 0
        output = []

        for chunk in data:
            chunk_tokens = self.estimate_tokens(chunk)

            if cumulative_tokens + chunk_tokens < max_tokens:
                output.append(chunk)
                cumulative_tokens += chunk_tokens
            else:
                break
        return output

    def extract_key_value_pairs(self, data: dict, parent_key: str = '') -> list[tuple[str, any]]:
        """Recursively extracts key-value pairs from nested JSON-like data, including lists.
        Args:
            data (dict): Input Data

        Returns:
            List[str]: all the key-value data

        Calling function(s): process_json_data
        """
        try:
            results = []
            if isinstance(data, dict):
                for key, value in data.items():
                    if value is not None:
                        new_key = f"{parent_key}.{key}" if parent_key else key
                        if isinstance(value, (dict, list)):
                            results.extend(self.extract_key_value_pairs(value, parent_key=new_key))
                        else:
                            results.append((new_key, value))
            elif isinstance(data, list):
                for index, item in enumerate(data):
                    if item is not None:
                        new_key = f"{parent_key}[{index}]"
                        if isinstance(item, (dict, list)):
                            results.extend(self.extract_key_value_pairs(item, parent_key=new_key))
                        else:
                            results.append((new_key, item))
            return results
        except Exception as e:
            logger.exception(
                "An error occurred while extracting key-value pairs from json data: %s", e
            )
            raise

    def process_json_data(self, data: dict) -> dict:
        """This method groups the json data based on first 3 keys.
        It also keeps the subgroup key-value in the group so that
        the data makes more sense

        input: json data.
        returns: a dictionary of new and modified key-valu pairs that are more meaningful.
        """
        try:
            key_value_pairs = self.extract_key_value_pairs(data)

            # Group by the third key if nested keys > 3; otherwise, group by the second key
            grouped_results = {}
            for key, value in key_value_pairs:
                key_parts = key.split(".")
                if len(key_parts) > 3:
                    subgroup_key = ".".join(
                        key_parts[:-2]
                    )  # Extract the key before the last one
                    group_key = ".".join(
                        key_parts[:3]
                    )  # Use the first 3 keys as the group

                elif len(key_parts) > 1:
                    subgroup_key = ".".join(
                        key_parts[:0]
                    )  # Extract the key before the last one
                    group_key = key_parts[1]  # Use the second key as the group
                else:
                    subgroup_key = None
                    group_key = key_parts[0]  # Fallback to the first key

                if group_key not in grouped_results:
                    grouped_results[group_key] = []
                grouped_results[group_key].append((key, value))

                # Add the phase_key and its value
                if subgroup_key:
                    subgroup_key_value = next(
                        (
                            (k, v)
                            for k, v in key_value_pairs
                            if k.startswith(subgroup_key) and k != key
                        ),
                        None,
                    )
                    if (
                        subgroup_key_value
                        and subgroup_key_value not in grouped_results[group_key]
                    ):
                        # Ensure this key is at the top
                        grouped_results[group_key].insert(0, subgroup_key_value)
            return grouped_results
        except Exception as e:
            logger.exception("An error occurred while grouping json data: %s", e)
            raise

    def replace_commas_in_brackets(self, text):
        """ 

        Replace commas with colons, but only inside top-level square brackets 
        (e.g., turn [a, b] into [a: b], but leave [x[1, 2], y] as [x[1, 2]: y]).
        1. Ignore square brackets nested within other square brackets.
        2. Only change the commas that are not inside those nested brackets.
        3. Leave anything outside square brackets untouched.

        result: final list of characters to build the output string.
        inside_brackets: flag to tell if we’re inside the outermost square brackets.
        bracket_depth: tracks how deep inside brackets we are. Depth = 0 → outside any [].
        buffer: temporarily holds characters within square brackets, for processing.

        """
        try:
            result = []
            inside_brackets = False
            bracket_depth = 0
            buffer = []

            for char in text:
                if char == '[':
                    bracket_depth += 1
                    if bracket_depth == 1:
                        inside_brackets = True
                        buffer = ['[']
                        continue
                elif char == ']':
                    bracket_depth -= 1
                    if bracket_depth == 0:
                        inside_brackets = False
                        buffer.append(']')
                        # Process content of outermost brackets
                        content = ''.join(buffer[1:-1])
                        # Replace commas only at top level (i.e., not nested)
                        processed = []
                        level = 0
                        for c in content:
                            if c == '[':
                                level += 1
                            elif c == ']':
                                level -= 1
                            if c == ',' and level == 0:
                                processed.append(':')
                            else:
                                processed.append(c)
                        result.append('[' + ''.join(processed) + ']')
                        continue

                if inside_brackets:
                    buffer.append(char)
                else:
                    result.append(char)

            return ''.join(result)
        
        except Exception as e:
            logger.exception("An error occurred while replacing commas in brackets: %s", e)
            return text  # also fallback to original text if something goes wrong
    
    def clean_text(self, chunk: str) -> str:
        """Preprocessing chunks"""
        try:
            # Remove " (including double quotes)
            text = re.sub(r'"', "", chunk)

            # Remove HTML tags
            text = BeautifulSoup(text, "html.parser").get_text()

            # Extract key-value pairs inside curly braces
            def process_match(match):
                key, value = match.groups()
                key = key.split('.')[-2:]
                return f"{key}: {value}"

            # Process occurrences like "incident.artifacts[2].value: Pay 500 000 in Bitcoin.txt"
            text = re.sub(
                r"([\w\[\]{}_/\\]+(?:\.[\w\[\]{}_/\\]+)+): ([^,}]*)",
                process_match,
                text,
            )

            # Remove extra spaces, newlines, and tabs
            text = re.sub(r"\s+", " ", text).strip()

            # Remove non-ASCII characters
            text = text.encode("ascii", "ignore").decode()

            # Remove unwanted special characters but KEEP [], {}, /, \, and _
            text = re.sub(r'[^a-zA-Z0-9.,!?;:()\[\]{}_/\\@ -]', '', text)

            # Transform bracketed content with commas into colon-separated
            text = self.replace_commas_in_brackets(text)

            # Remove the final square brackets and the numbers within them
            text = re.sub(r'\[\d+\]', '', text)

            # Convert [word1: word2: ...]: value -> {word1.word2...: value}
            return re.sub(r'\[([\w\s:]+?)\]: ([^,}]+)', lambda m: "{" + m.group(1).replace(": ", ".") + ": " + m.group(2) + "}", text)

        except Exception as e:
            logger.exception("An error occurred while cleaning chunk: %s", e)
            raise

    def remove_duplicate_value(self, text: str) -> str:
        """
        Removes redundant value text if it is a reformatted duplicate of the path.
        Example: path: incident.description, value: incident: description: --> value:
        """
        try:
            pattern = r'path: ([\w\.]+), value: ([\w\s:]+):'
            if text:
                matches = re.findall(pattern, text)

                for path, value in matches:
                    path_parts = path.split('.')[-2:]  # Last two tokens from path
                    value_parts = [v.strip() for v in value.strip().split(':') if v]

                    if path_parts == value_parts:
                        # Remove redundant value content
                        redundant = f"value: {value.strip()}:"
                        text = text.replace(redundant, "value:")

            return text
        except Exception as e:
            logger.exception("Error in remove_duplicate_value: %s", e)
            return text

    def preprocess_chunks(self, chunks: List[str])-> List[str]:
        """calling clean_text to preprocess all the chunks"""
        try:
            return [self.remove_duplicate_value(self.clean_text(chunk)) for chunk in chunks]
        except Exception as e:
            logger.exception("An error occurred while pre-processing the chunks: %s", e)
            raise

    def split_json_to_chunks(self, data:dict= IncidentFullData, max_tokens_per_chunk:int=400)-> list[str]:
        """ Splits the Indcident data into  meanignful chunks"""
        try:
            processed_data = self.process_json_data(data)
            chunks = []
            chunk_index = 0
            for _, value in processed_data.items():
                if value is not None:
                    if isinstance(value[0], tuple):  # Only split string values
                        result = ', '.join(f"{k}: {v}" for k, v in value)
                        result_tag = result.split(':', maxsplit=1)[0].strip()
                        if self.estimate_tokens(result) > max_tokens_per_chunk:
                            property_chunks = self.split_text_to_token_chunks(
                                result, max_tokens_per_chunk
                            )
                            for prop_chunk in property_chunks:
                                chunks.append(json.dumps({
                                        "path": result_tag ,
                                        "value": prop_chunk
                                    }))
                                chunk_index += 1
                        else:
                            # Handle non-string values as-is (e.g., None or numeric values)
                            chunks.append(json.dumps({
                                   # "path": chunk_index,
                                    "value": result
                            }))
                            chunk_index += 1
            return self.preprocess_chunks(chunks)
        except Exception as e:
            logger.exception(
                "An error occurred while chunking processed json data: %s", e
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
            model_config = load_model_config()

            # Find the configuration for the given model
            model_conf = next(
                (config for config in model_config if config["name"] == model_id),
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

    def split_data_into_token_chunks(self, text: str, max_tokens=400) -> List[str]:
        """
        Return a list of chunks of data, with each chunk not exceeding max_tokens
        """
        newline_placeholder = '<newline/>'

        try:
            chunks: List[str] = []
            current_chunk = ""
            current_token_count = 0

            text = text.replace('\n', f' {newline_placeholder} ') # add spaces so is a separate word
            # Split the text into words
            words = text.split()

            for word in words:
                if word == newline_placeholder:
                    word = '\n'

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
            num_tokens = len(encoding.encode(text, disallowed_special=()))
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
            tokens = encoding.encode(text, disallowed_special=())
            token_chunks = [
                tokens[i : i + max_tokens] for i in range(0, len(tokens), max_tokens)
            ]
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

    def create_faiss_index(self, embeddings: List[list]) -> faiss.IndexFlatL2:
        """Create a Faiss index which stores the embedded chunks for retrieval

        Args:
            embeddings (List[list]): List of embeddings

        Returns:
            _type_: _description_
        """
        try:
            # Convert embeddings to numpy array
            embeddings_array = np.array(embeddings)

            # Initialize FAISS index
            index = faiss.IndexFlatL2(embeddings_array.shape[1])

            # Add the embeddings to the FAISS index
            # suppress error
            # pylint: disable=no-value-for-parameter
            index.add(embeddings_array)

            return index
        except Exception as e:
            logger.exception(
                "An error occurred while creating Faiss Index: %s",
                e,
            )
            raise

    def normalize_l2_distances(self, distances: np.array) -> np.array:
        """normalizes the L2 scores that we generate in Faiss index search
        Args:
            distances(array)
        returns:
            normalized_scores(array)

        """
        try:
            min_val = np.min(distances)
            max_val = np.max(distances)

            # Avoid division by zero
            if max_val == min_val:
                return np.ones_like(distances)

            normalized_scores = 1 - (distances - min_val) / (max_val - min_val)
            return normalized_scores
        except Exception as e:
            logger.exception(
                "An error occurred while normalizing distance scores in index search: %s",
                e,
            )
            raise

    def retrieve_relevant_chunks_watsonx(
        self, query: str, chunks: List[str], total_tokens=None, threshold=0.7, score_threshold=0.2
    ) -> List[str]:
        """Retrieve relevant chunks from Faiss Index semantically using emedding models from WatsonX API

        Args:
            query (str): Query by the user
            chunks (List[str]): Chunks Generated by split_json_to_chunks method
            total_tokens (_type_): total context length for the model
            threshold (_type_): Fraction of tokens to delegate for chunk data

        Returns:
            _type_: _description_
        """
        try:
            # get total tokens
            total_tokens = total_tokens or ModelHelper.context_length_for_model(
                app_state.get().model_id
            )
            logger.debug(
                "Total tokens: %d for model_id: %s",
                total_tokens,
                app_state.get().model_id,
            )

            # Create embeddings of Chunks
            payload_chunk_embeddings = self.query_helper.generate_embeddings(
                data=chunks
            )

            # Create Faiss Index
            payload_index = self.create_faiss_index(payload_chunk_embeddings)
            
            # Create embedding for the query
            query_embedding = self.query_helper.generate_embeddings(data=[query])

            # Search the index for top K most relevant chunks (set a high enough top_k initially)
            top_k = len(chunks)  # Search all chunks to evaluate token limit
            distances, indices = payload_index.search(np.array(query_embedding), top_k)

            # Select the indexes that have the distance greater than .2
            distances = self.normalize_l2_distances(distances)
            selected_indices = [
                idx for score, idx in zip(distances[0], indices[0]) if score >= score_threshold
            ]

            selected_chunks = [chunks[idx] for idx in selected_indices]

            return self.clamped_chunks_for_model(selected_chunks, app_state.get().model_id, threshold)
    
        except Exception as e:
            logger.exception(
                "An error occurred while retrieving relevant chunks: %s",
                e,
            )
            raise

    def split_json_to_chunks_prompts(
        self, data: dict, max_chunk_size=400
    ) -> List[str]:
        """
        Splits a JSON-like dictionary prompt into chunks of string prompts, each limited to a specified maximum size.
        Args:
            data (dict): A dict where each header description pair will be processed and converted to a string chunk.
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

    def flatten_dict(self, d: dict, parent_key="", sep=".") -> dict:
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
