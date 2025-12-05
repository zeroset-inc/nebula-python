# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .chunk_response import ChunkResponse

__all__ = ["NebulaResultsChunkResponse"]


class NebulaResultsChunkResponse(BaseModel):
    results: ChunkResponse
