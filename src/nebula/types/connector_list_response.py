# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectorListResponse", "Result", "ResultErrorDetail"]


class ResultErrorDetail(BaseModel):
    message: str

    retryable: bool


class Result(BaseModel):
    id: str

    collection_id: str

    created_at: datetime

    provider: str

    status: Literal["active", "pending", "revoked"]

    updated_at: datetime

    user_id: str

    config: Optional[Dict[str, object]] = None

    error_detail: Optional[ResultErrorDetail] = None

    external_account_id: Optional[str] = None

    health: Optional[Literal["ok", "error"]] = None

    items_synced: Optional[int] = None

    last_error: Optional[str] = None

    last_synced_at: Optional[datetime] = None

    next_sync_at: Optional[datetime] = None

    sync_cursor: Optional[Dict[str, object]] = None

    token_expires_at: Optional[datetime] = None


class ConnectorListResponse(BaseModel):
    results: List[Result]
