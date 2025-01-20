from typing import List

from resilient import SimpleClient

from fn_watsonx_analyst.summarizers.contents_summarizer import ContentsSummarizer
from fn_watsonx_analyst.summarizers.document_summarizer import DocumentSummarizer
from fn_watsonx_analyst.types.ai_response import AIResponse
from fn_watsonx_analyst.types.artifact import Artifact

from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose, ModelTag
from fn_watsonx_analyst.util.chunking.chunking import Chunking
from fn_watsonx_analyst.util.parallel.parallel import ParallelRunnableRunner
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls
from fn_watsonx_analyst.util.util import create_logger

MAX_THRESHOLD = 2000000  # bytes

log = create_logger(__name__)

class ArtifactSummaryGenerator:
    """Generate a summary of an artifact in layers of summaries"""

    res_client: SimpleClient

    inc_id: int
    artifact: Artifact
    content_type: str
    artifact_contents: bytes

    model_id: str
    model_tag: ModelTag

    opts: dict

    def __init__(
        self,
        res_client: SimpleClient,
        inc_id: int,
        artifact: Artifact,
        model_id: str,
        opts: dict,
    ):
        self.res_client = res_client

        self.inc_id = inc_id
        self.artifact = artifact
        self.content_type = artifact["attachment"]["content_type"]

        self.model_id = model_id
        self.opts = opts

        self.model_tag = ModelTag(model_id, AiResponsePurpose.ARTIFACT_SUMMARY)

    def generate(self) -> AIResponse:
        """Generate a random sample-based summary of the artifact, truncate if over max threshold"""
        data = self.__get_contents()

        # don't spend too long chunking
        if len(data) > MAX_THRESHOLD:
            data = data[:MAX_THRESHOLD]

        chunker = Chunking()
        chunks = chunker.split_data_into_token_chunks(data, max_tokens=1500)
        chunks = chunker.random_chunks(chunks, 12)

        contents_summarizers: List[ContentsSummarizer] = []
        for chunk in chunks:
            if len(chunk) > 0:
                contents_summarizers.append(
                    ContentsSummarizer(
                        chunk,
                        self.artifact["attachment"]["content_type"],
                        self.model_id,
                        self.res_client,
                        self.opts,
                    )
                )

        summaries: List[AIResponse] = ParallelRunnableRunner(contents_summarizers).run()
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
            summaries[0]["tag"] = str(self.model_tag)
            return summaries[0]

        return

    def __summarize_layer(self, summaries: List[AIResponse]):
        log.debug("Summarizing layer")
        chunks: List[str] = []
        doc_summarizers: List[DocumentSummarizer] = []

        if len(summaries) == 1:
            return summaries

        chunker = Chunking()
        summaries_text = [x["generated_text"] for x in summaries]
        chunks = chunker.split_data_into_token_chunks(
            "\n---\n".join(summaries_text), 2000
        )

        for chunk in chunks:
            doc_summarizers.append(
                DocumentSummarizer(
                    chunk, "text", self.model_id, self.res_client, self.opts
                )
            )

        summaries: List[AIResponse] = ParallelRunnableRunner(doc_summarizers).run()
        return summaries

    def __get_contents(self):
        return RestHelper().do_request(
            self.res_client,
            RestUrls.ARTIFACT_CONTENTS,
            inc_id=self.inc_id,
            art_id=self.artifact["id"],
        )
