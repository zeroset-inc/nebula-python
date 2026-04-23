# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["MemoryUpdateParams"]


class MemoryUpdateParams(TypedDict, total=False):
    collection_id: Optional[str]
    """Collection context for copy-on-write.

    If provided and engram is shared, creates a copy before modification.
    """

    collection_ids: Optional[SequenceNotStr[str]]
    """New collection associations"""

    merge_metadata: bool
    """Merge with existing metadata"""

    metadata: Optional[Dict[str, object]]
    """Metadata to update"""

    name: Optional[str]
    """New name for the memory"""
