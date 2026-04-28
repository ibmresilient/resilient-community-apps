"""
Request state management contextvar.

This will hold state in memory for the current thread.
If forking processes, construct new app_state and set the pre-existing values.
"""
import contextvars

from fn_watsonx_analyst.types import AppState

app_state = contextvars.ContextVar("request_id", default=AppState())
