# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["WebhookListEventsResponse"]


class WebhookListEventsResponse(BaseModel):
    """Response model for webhook events list"""

    events: List[Dict[str, object]]

    total_count: int
