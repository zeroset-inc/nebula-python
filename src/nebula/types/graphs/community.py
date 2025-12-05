# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Community"]


class Community(BaseModel):
    id: Union[int, str, None] = None

    attributes: Optional[Dict[str, object]] = None

    collection_id: Optional[str] = None

    community_id: Optional[str] = None

    created_at: Optional[datetime] = None

    description_embedding: Optional[List[float]] = None

    findings: Optional[List[str]] = None

    graph_snapshot_id: Optional[str] = None

    level: Optional[int] = None

    name: Optional[str] = None

    rating: Optional[float] = None

    rating_explanation: Optional[str] = None

    summary: Optional[str] = None

    updated_at: Optional[datetime] = None
