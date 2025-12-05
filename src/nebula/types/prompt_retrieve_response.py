# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .prompt_response import PromptResponse

__all__ = ["PromptRetrieveResponse"]


class PromptRetrieveResponse(BaseModel):
    results: PromptResponse
