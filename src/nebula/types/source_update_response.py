# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SourceUpdateResponse", "Results"]


class Results(BaseModel):
    id: str

    collection_ids: List[str]

    engram_id: str

    metadata: Dict[str, object]

    owner_id: str

    text: str

    content_hash: Optional[str] = None

    created_at: Optional[datetime] = None

    next_utterance_id: Optional[str] = None

    parent_utterance_id: Optional[str] = None

    prev_utterance_id: Optional[str] = None

    sequence_number: Optional[float] = None

    source_type: Optional[str] = None

    speaker_id: Optional[str] = None

    speaker_name: Optional[str] = None

    timestamp: Optional[datetime] = None

    token_count: Optional[int] = None

    vector: Optional[List[float]] = None


class SourceUpdateResponse(BaseModel):
    results: Results
