# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TemporalEventListParams"]


class TemporalEventListParams(TypedDict, total=False):
    event_type: Optional[str]
    """Filter by event_type"""

    limit: int

    offset: int

    since: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter events created after this timestamp (inclusive)"""

    target_relationship_id: Optional[str]
    """Filter by relationship UUID"""

    until: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter events created before this timestamp (inclusive)"""
