# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["GraphResponse"]


class GraphResponse(BaseModel):
    id: str

    collection_id: str

    created_at: datetime

    description: Optional[str] = None

    engram_ids: List[str]

    name: str

    status: str

    updated_at: datetime
