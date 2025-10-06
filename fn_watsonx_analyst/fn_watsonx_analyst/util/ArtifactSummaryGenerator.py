"""Artifact summary generator class"""

from typing import List, Optional
from math import ceil
from datetime import datetime, timezone

from resilient import SimpleClient

from fn_watsonx_analyst.summarizers.contents_summarizer import ContentsSummarizer
from fn_watsonx_analyst.summarizers.document_summarizer import DocumentSummarizer
from fn_watsonx_analyst.types.ai_response import AIResponse
from fn_watsonx_analyst.types.artifact import Artifact

from fn_watsonx_analyst.types.attachment import Attachment
from fn_watsonx_analyst.types.watsonx_responses import WatsonxTextGenerationResponse
from fn_watsonx_analyst.util.FileParser import FileParser
from fn_watsonx_analyst.util.chunking.chunking import Chunking
from fn_watsonx_analyst.util.parallel.parallel import ParallelRunnableRunner
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls
from fn_watsonx_analyst.util.logging_helper import create_logger
from fn_watsonx_analyst.util.state_manager import app_state
from fn_watsonx_analyst.util.response_helper import ResponseHelper


log = create_logger(__name__)


class ArtifactSummaryGenerator:
    """Generate a summary of an artifact in layers of summaries"""

    res_client: SimpleClient
    inc_id: int
    artifact: Artifact
    content_type: str
    contents: bytes

    opts: dict

    def __init__(
        self,
        inc_id: int,
        artifact: Optional[Artifact],
        attachment: Optional[Attachment],
    ):
        state = app_state.get()
        self.res_client = state.res_client
        self.model_id = state.model_id
        self.opts = state.opts

        self.inc_id = inc_id
        self.artifact = artifact
        self.attachment = attachment

        if self.artifact:
            self.content_type = artifact.get("attachment", {}).get("content_type", "")
        else:
            self.content_type = attachment.get("content_type", "")

    def generate(self) -> AIResponse:
        data = self.__get_contents()

        # Guard clause to avoid LLM call if content is empty or failed to parse
        if data == "Parsed content is empty or could not be extracted":
            response = ResponseHelper()
            return response.error_response(data)

        chunker = Chunking()
        model_context_limit = chunker.max_tokens_for_model(self.model_id)
        chunk_size = 0.5 * model_context_limit
        max_data_to_scan = 125000

        total_chunks = chunker.split_data_into_token_chunks(data, chunk_size)
        total_executions = int(ceil(max_data_to_scan / chunk_size))
        total_chunks = total_chunks[:total_executions]

        contents_summarizers: List[ContentsSummarizer] = []
        for chunk in total_chunks:
            if len(chunk) > 0:
                contents_summarizers.append(
                    ContentsSummarizer(
                        chunk,
                        self.content_type,
                    )
                )

        summaries: List[WatsonxTextGenerationResponse] = ParallelRunnableRunner(
            contents_summarizers
        ).run()
        if isinstance(summaries, dict):
            summaries = [summaries]

        cnt = 0
        if len(summaries) < 1:
            raise ValueError("No summaries generated")

        while len(summaries) > 1:
            log.debug(
                "Layer iteration %s, summaries remaining: %d", cnt, len(summaries)
            )
            cnt += 1
            summaries = self.__summarize_layer(summaries)

        if len(summaries) == 0:
            raise ValueError(
                "Failed to generate section summaries for artifact scan. Review the logs for more details."
            )
        if summaries[0] is not None:
            return summaries[0]

        return

    def __summarize_layer(self, summaries: List[AIResponse]):
        log.debug("Summarizing layer")
        chunks: List[str] = []
        doc_summarizers: List[DocumentSummarizer] = []

        if len(summaries) == 1:
            return summaries

        chunker = Chunking()
        summaries_text = [x["results"][0]["generated_text"] for x in summaries]
        chunks = chunker.split_data_into_token_chunks(
            "\n---\n".join(summaries_text), 5000
        )

        for chunk in chunks:
            doc_summarizers.append(DocumentSummarizer(chunk, "text"))

        summaries: List[WatsonxTextGenerationResponse] = ParallelRunnableRunner(
            doc_summarizers
        ).run()
        return summaries

    def __get_contents(self):
        contents: str = None
        if self.artifact:
            contents = RestHelper().do_request(
                RestUrls.ARTIFACT_CONTENTS,
                inc_id=self.inc_id,
                art_id=self.artifact["id"],
            )
        elif self.attachment:
            if not self.attachment["task_id"]:
                contents = RestHelper().do_request(
                    RestUrls.ATTACHMENT_CONTENTS,
                    inc_id=self.inc_id,
                    attach_id=self.attachment["id"],
                )
            else:
                contents = RestHelper().do_request(
                    RestUrls.TASK_ATTACHMENT_CONTENTS,
                    task_id=self.attachment["task_id"],
                    attach_id=self.attachment["id"],
                )

        else:
            raise ValueError("Please provide a valid artifact or attachment")

        parser_instance = FileParser()
        object_name = (
            self.artifact["value"] if self.artifact else self.attachment["name"]
        )
        contents = parser_instance.multi_format_parser(
            data=contents, object_name=object_name
        )
        return contents
