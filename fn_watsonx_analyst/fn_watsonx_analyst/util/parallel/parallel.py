from typing import List
import concurrent
import traceback


from fn_watsonx_analyst.types.ai_response import AIResponse
from fn_watsonx_analyst.util.util import create_logger, get_request_id, set_request_id

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
            results += self._run_impl(group, get_request_id())

        return results

    def _run_impl(self, runnables: List[ParallelRunnable], req_id: str) -> AIResponse:
        """
        Runs the provided runnables in parallel
        """
        results: List[AIResponse] = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_runnale = {
                executor.submit(context_wrapper, runnable, req_id): runnable for runnable in runnables
            }
            for future in concurrent.futures.as_completed(future_to_runnale):
                r = future_to_runnale[future]
                inner_log = create_logger(__name__)
                set_request_id(req_id)
                try:
                    result = future.result()
                    results.append(result)
                except:
                    inner_log.error(traceback.format_exc())
                    inner_log.error("Failed to run runnable %s", r.name)
                    continue
        return results
