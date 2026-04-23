# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SourceDeleteParams"]


class SourceDeleteParams(TypedDict, total=False):
    collection_id: Optional[str]
    """Collection context for copy-on-write.

    If provided and the parent engram is shared across multiple collections, a
    collection-specific copy will be created before applying the delete.
    """
