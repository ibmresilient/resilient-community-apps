from typing import List
import concurrent

from fn_watsonx_analyst.types.ai_response import AIResponse
from fn_watsonx_analyst.util.util import create_logger

log = create_logger(__name__)

class ParallelRunnable:
    name: str = "unkown"

    def run(**kwargs):
        raise NotImplementedError("not implemented")


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
            log.debug(f"Iteration {i+1} of {len(groups)}")
            results += self._run_impl(group)

        return results

    def _run_impl(self, runnables: List[ParallelRunnable]) -> AIResponse:
        """
        Runs the provided runnables in parallel
        """
        results: List[AIResponse] = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_runnale = {
                executor.submit(runnable.run): runnable for runnable in runnables
            }
            for future in concurrent.futures.as_completed(future_to_runnale):
                r = future_to_runnale[future]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    import traceback

                    log.error(traceback.format_exc())
                    log.error(f"Failed to run runnable '{r.name}'")
                    continue
        return results
