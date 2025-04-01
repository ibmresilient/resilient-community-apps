import json
from typing import List
from fn_watsonx_analyst.types.pbx_detail import PBExecDetail
from fn_watsonx_analyst.types.playbook import Playbook
from fn_watsonx_analyst.util.ContextHelper import ContextHelper, Templates
from .generic_summarizer import GenericSummarizer

from resilient import SimpleClient


class PlaybookExecutionsSummarizer(GenericSummarizer):
    pbx_details: List[PBExecDetail]
    pb_details: List[Playbook]

    instruction = ""
    name = "playbook_executions"

    def __init__(
        self,
        pbx_data: List[PBExecDetail],
        model_id: str,
        res_client: SimpleClient,
        opts: dict,
    ):
        (_, data, _, _) = ContextHelper().cleanse_data(None, pbx_data, [], [])
        self.instruction = ContextHelper().get_prompt(
            Templates.SUMM_PBEXEC, data=json.dumps(data, indent=2)
        )
        self.pre_process()
        super().__init__(self.name, self.instruction, model_id, res_client, opts)

    def pre_process(self):
        # impute the description of the playbook into each execution
        pass
