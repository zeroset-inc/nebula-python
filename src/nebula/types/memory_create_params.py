# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .ingestion_mode import IngestionMode
from .ingestion_config_param import IngestionConfigParam

__all__ = ["MemoryCreateParams", "Message"]


class MemoryCreateParams(TypedDict, total=False):
    collection_ref: Required[str]
    """Collection UUID or name"""

    engram_type: Required[Literal["conversation", "document"]]
    """Type of memory to create"""

    chunks: Optional[SequenceNotStr[str]]
    """Pre-chunked text for document type"""

    ingestion_config: Optional[IngestionConfigParam]
    """Custom ingestion config for documents"""

    ingestion_mode: Optional[IngestionMode]
    """Ingestion mode for documents"""

    messages: Optional[Iterable[Message]]
    """Messages for conversation type"""

    metadata: Optional[Dict[str, object]]
    """Metadata for the memory"""

    name: Optional[str]
    """Optional name for the memory"""

    raw_text: Optional[str]
    """Raw text content for document type"""


class Message(TypedDict, total=False):
    """A message in a conversation."""

    content: Required[str]
    """Message content"""

    role: Required[str]
    """Role: 'user', 'assistant', or 'system'"""

    authority: Optional[float]
    """Optional authority score"""

    metadata: Optional[Dict[str, object]]
    """Optional message-level metadata"""
