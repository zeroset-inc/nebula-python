# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..memories.engram_response import EngramResponse

__all__ = ["PaginatedNebulaResultListEngramResponse"]


class PaginatedNebulaResultListEngramResponse(BaseModel):
    results: List[EngramResponse]

    total_entries: int
