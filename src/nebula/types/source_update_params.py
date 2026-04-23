# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SourceUpdateParams"]


class SourceUpdateParams(TypedDict, total=False):
    content: Required[str]

    collection_id: Optional[str]
    """Collection context for copy-on-write.

    If provided and the parent engram is shared across multiple collections, a
    collection-specific copy will be created before applying the update.
    """

    metadata: Optional[Dict[str, object]]
