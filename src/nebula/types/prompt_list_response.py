# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .prompt_response import PromptResponse

__all__ = ["PromptListResponse"]


class PromptListResponse(BaseModel):
    results: List[PromptResponse]

    total_entries: int
