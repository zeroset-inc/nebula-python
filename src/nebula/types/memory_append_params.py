# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .ingestion_mode import IngestionMode
from .ingestion_config_param import IngestionConfigParam

__all__ = ["MemoryAppendParams"]


class MemoryAppendParams(TypedDict, total=False):
    collection_id: Required[str]
    """Target collection ID for the appended content."""

    chunks: Optional[SequenceNotStr[str]]
    """Pre-processed text chunks to append (for document engrams)."""

    ingestion_config: Optional[IngestionConfigParam]
    """Optional ingestion configuration override (for document engrams)."""

    ingestion_mode: IngestionMode
    """Ingestion mode for document content (ignored for conversations)."""

    messages: Optional[Iterable[Dict[str, object]]]
    """List of messages to append (for conversation engrams).

    Each has content, role, optional parent_id, metadata, authority.
    """

    metadata: Optional[Dict[str, object]]
    """Additional metadata for the appended content."""

    raw_text: Optional[str]
    """Raw text content to append (for document engrams)."""
