# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ChunkSearchResult"]


class ChunkSearchResult(BaseModel):
    id: str

    collection_ids: List[str]

    engram_id: str

    metadata: Dict[str, object]

    owner_id: Optional[str] = None

    text: str

    score: Optional[float] = None

    timestamp: Optional[datetime] = None
