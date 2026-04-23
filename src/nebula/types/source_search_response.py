# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SourceSearchResponse", "Result"]


class Result(BaseModel):
    """Result of a search operation."""

    id: str

    collection_ids: List[str]

    engram_id: str

    metadata: Dict[str, object]

    owner_id: Optional[str] = None

    text: str

    score: Optional[float] = None

    speaker_id: Optional[str] = None

    speaker_name: Optional[str] = None

    timestamp: Optional[datetime] = None


class SourceSearchResponse(BaseModel):
    results: List[Result]
