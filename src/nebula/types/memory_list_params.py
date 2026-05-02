# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["MemoryListParams"]


class MemoryListParams(TypedDict, total=False):
    chunks_limit: Optional[int]
    """Maximum chunks to inline per engram.

    Defaults to all chunks for backwards compatibility; pass 0 to skip chunk
    hydration.
    """

    collection_ids: Optional[SequenceNotStr[str]]
    """Optional list of collection IDs to filter engrams by.

    If provided, exactly one collection ID must be specified.
    """

    ids: SequenceNotStr[str]
    """A list of engram IDs to retrieve.

    If not provided, all engrams will be returned.
    """

    limit: int
    """Specifies a limit on the number of objects to return, ranging between 1
    and 1000.

    Defaults to 100.
    """

    metadata_filters: Optional[str]
    """JSON string for metadata filtering.

    Example: '{"metadata.source": {"$eq": "playground"}}'
    """

    offset: int
    """Specifies the number of objects to skip. Defaults to 0."""

    owner_only: bool
    """If true, only returns engrams owned by the user, not all accessible engrams."""
