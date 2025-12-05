# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .chunk_search_result import ChunkSearchResult

__all__ = ["ChunkSearchResponse"]


class ChunkSearchResponse(BaseModel):
    results: List[ChunkSearchResult]
