# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MemoryListChunksParams"]


class MemoryListChunksParams(TypedDict, total=False):
    include_vectors: Optional[bool]
    """Whether to include vector embeddings in the response."""

    limit: int
    """Specifies a limit on the number of objects to return, ranging between 1 and 100.

    Defaults to 100.
    """

    offset: int
    """Specifies the number of objects to skip. Defaults to 0."""
