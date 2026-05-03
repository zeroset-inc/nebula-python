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

    min_applied_wal_seq: Optional[int]
    """
    Read-your-writes assertion: the WAL-tail overlay path waits for at least this
    seq to be applied before serving (or returns 503 Unavailable on timeout).
    REQUIRES exactly one collection_ids entry — without a collection scope the
    request returns 422 (the per-WAL-shard scalar applied_wal_seq is meaningless
    across collections). When the served shard has not been migrated to
    wal_compaction_enabled, the field is accepted but the served path is the legacy
    overlay (the assertion has no effect — the response's applied_wal_seq will be
    0). Pass back the value the matching upload response surfaced.
    """

    offset: int
    """Specifies the number of objects to skip. Defaults to 0."""

    owner_only: bool
    """If true, only returns engrams owned by the user, not all accessible engrams."""
