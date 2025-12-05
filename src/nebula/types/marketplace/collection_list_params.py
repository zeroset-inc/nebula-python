# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CollectionListParams"]


class CollectionListParams(TypedDict, total=False):
    limit: int
    """The maximum number of collections to return"""

    offset: int
    """The number of collections to skip"""

    search: Optional[str]
    """Search query to filter collections by name"""
