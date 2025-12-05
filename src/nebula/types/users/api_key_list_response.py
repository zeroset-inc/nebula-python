# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["APIKeyListResponse", "Result"]


class Result(BaseModel):
    key_id: str

    public_key: str

    updated_at: datetime

    description: Optional[str] = None

    name: Optional[str] = None


class APIKeyListResponse(BaseModel):
    results: List[Result]

    total_entries: int
