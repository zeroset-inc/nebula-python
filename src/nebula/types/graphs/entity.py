# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["Entity"]


class Entity(BaseModel):
    """An entity extracted from a engram."""

    name: str

    id: Optional[str] = None

    category: Optional[str] = None

    chunk_ids: Optional[List[str]] = None

    collection_id: Optional[str] = None

    description: Optional[str] = None

    description_embedding: Optional[List[float]] = None

    engram_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
