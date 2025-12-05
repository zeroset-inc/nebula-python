# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WebhookGetStatsResponse"]


class WebhookGetStatsResponse(BaseModel):
    earliest_event: Optional[datetime] = None

    failed_count: int

    latest_event: Optional[datetime] = None

    processed_count: int

    success_rate: float

    total_events: int

    unique_types: int

    verified_count: int
