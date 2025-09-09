from typing import List
import concurrent
import traceback


from fn_watsonx_analyst.types.ai_response import AIResponse
from fn_watsonx_analyst.types.watsonx_responses import WatsonxTextGenerationResponse
from fn_watsonx_analyst.types import AppState
from fn_watsonx_analyst.util.logging_helper import create_logger, get_request_id, set_request_id
from fn_watsonx_analyst.util.state_manager import app_state

log = create_logger(__name__)

class ParallelRunnable:
    name: str = "unkown"

    @staticmethod
    def run(**kwargs):
        raise NotImplementedError("not implemented")

def context_wrapper(runnable: ParallelRunnable, req_id: str):
    set_request_id(req_id)
    return runnable.run()

class ParallelRunnableRunner:
    runnables: List[ParallelRunnable]

    def __init__(self, runnables: List[ParallelRunnable]):
        self.runnables = runnables

    def run(self, workers=3) -> List[AIResponse]:
        """
        Execute the runnables in parallel
        Args:
            workers (int): number of workers to use in parallel
        """
        results = []
        groups = [
            self.runnables[i : i + workers]
            for i in range(0, len(self.runnables), workers)
        ]

        for i, group in enumerate(groups):
            log.debug("Iteration %d of %d", i+1, len(groups))
            results += self._run_impl(group, get_request_id(), app_state.get())

        return results

    def _run_impl(self, runnables: List[ParallelRunnable], req_id: str, state: AppState) -> List[WatsonxTextGenerationResponse]:
        """
        Runs the provided runnables in parallel
        """
        results: List[WatsonxTextGenerationResponse] = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_runnale = {
                executor.submit(context_wrapper, runnable, req_id): runnable for runnable in runnables
            }
            for future in concurrent.futures.as_completed(future_to_runnale):
                r = future_to_runnale[future]
                inner_log = create_logger(__name__)

                set_request_id(req_id)
                app_state.set(state)

                try:
                    result: WatsonxTextGenerationResponse = future.result()
                    results.append(result)
                    try:
                        app_state.get().increment_input_tokens(result["results"][0]["input_token_count"])
                        app_state.get().increment_output_tokens(result["results"][0]["generated_token_count"])
                    except:
                        log.warning("Failed to retrieve token usage from parallel execution.")
                except:
                    inner_log.error(traceback.format_exc())
                    inner_log.error("Failed to run runnable %s", r.name)
                    continue
        return results
