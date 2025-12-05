# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .chunk_response import ChunkResponse

__all__ = ["PaginatedNebulaResultListChunkResponse"]


class PaginatedNebulaResultListChunkResponse(BaseModel):
    results: List[ChunkResponse]

    total_entries: int
