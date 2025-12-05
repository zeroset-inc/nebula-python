# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["ChunkResponse"]


class ChunkResponse(BaseModel):
    id: str

    collection_ids: List[str]

    engram_id: str

    metadata: Dict[str, object]

    owner_id: str

    text: str

    vector: Optional[List[float]] = None
