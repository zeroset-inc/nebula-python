# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "MemoryAppendParams",
    "IngestionConfig",
    "IngestionConfigChunkEnrichmentSettings",
    "Message",
    "MessageContentUnionMember1",
    "MessageContentUnionMember1TextContentRequest",
    "MessageContentUnionMember1FileContentRequest",
    "MessageContentUnionMember1S3FileReferenceRequest",
]


class MemoryAppendParams(TypedDict, total=False):
    collection_id: Required[str]
    """Target collection ID for the appended content."""

    chunks: Optional[SequenceNotStr[str]]
    """Pre-processed text chunks to append for document memories."""

    ingestion_config: Optional[IngestionConfig]
    """Public ingestion config accepted by memory-ingestion endpoints.

    This mirrors the supported request payload shape while staying independent from
    the runtime provider config, which also carries internal-only fields such as
    `app` and `extra_fields`.
    """

    ingestion_mode: Literal["hi-res", "ocr", "fast", "custom"]
    """Ingestion mode for document content."""

    messages: Optional[Iterable[Message]]
    """Messages to append for conversation memories.

    Each message has content, role, and optional metadata.
    """

    metadata: Optional[Dict[str, object]]
    """Additional metadata for the appended content."""

    raw_text: Optional[str]
    """Raw text content to append for document memories."""


class IngestionConfigChunkEnrichmentSettings(TypedDict, total=False):
    """Settings for chunk enrichment.

    Model selection for the enrichment LLM call lives in
    ``app.task_llms.chunk_enrichment``; the legacy ``generation_config``
    field was removed in the per-task LLM cleanup pass.
    """

    chunk_enrichment_prompt: Optional[str]
    """The prompt to use for chunk enrichment"""

    enable_chunk_enrichment: bool
    """Whether to enable chunk enrichment or not"""

    n_chunks: int
    """The number of preceding and succeeding chunks to include. Defaults to 2."""


class IngestionConfig(TypedDict, total=False):
    """Public ingestion config accepted by memory-ingestion endpoints.

    This mirrors the supported request payload shape while staying independent
    from the runtime provider config, which also carries internal-only fields
    such as ``app`` and ``extra_fields``.
    """

    audio_transcription_model: Optional[str]

    automatic_extraction: bool

    chunk_enrichment_settings: IngestionConfigChunkEnrichmentSettings
    """Settings for chunk enrichment.

    Model selection for the enrichment LLM call lives in
    `app.task_llms.chunk_enrichment`; the legacy `generation_config` field was
    removed in the per-task LLM cleanup pass.
    """

    chunk_overlap: int

    chunk_size: int

    chunking_strategy: str

    excluded_parsers: SequenceNotStr[str]

    extra_parsers: Dict[str, object]

    max_concurrent_vlm_tasks: int

    parser_overrides: Dict[str, str]

    provider: str

    vlm: Optional[str]

    vlm_batch_size: int

    vlm_max_tokens_to_sample: int

    vlm_ocr_one_page_per_chunk: bool


class MessageContentUnionMember1TextContentRequest(TypedDict, total=False):
    """Text content block."""

    text: Required[str]
    """Text content"""

    type: Literal["text"]


class MessageContentUnionMember1FileContentRequest(TypedDict, total=False):
    """Unified file content for multimodal messages."""

    data: Required[str]
    """Base64 encoded file data"""

    duration_seconds: Optional[float]
    """Duration in seconds (for audio)"""

    filename: Optional[str]
    """Original filename"""

    media_type: str
    """MIME type"""

    type: Literal["file", "image", "audio", "document"]
    """Content kind: file, image, audio, or document."""


class MessageContentUnionMember1S3FileReferenceRequest(TypedDict, total=False):
    """Reference to a file uploaded to S3 (for large files)."""

    s3_key: Required[str]
    """S3 object key"""

    bucket: Optional[str]
    """S3 bucket (uses default if not specified)"""

    filename: Optional[str]
    """Original filename"""

    media_type: str
    """MIME type"""

    size_bytes: Optional[int]
    """File size in bytes"""

    type: Literal["s3_ref"]


MessageContentUnionMember1: TypeAlias = Union[
    MessageContentUnionMember1TextContentRequest,
    MessageContentUnionMember1FileContentRequest,
    MessageContentUnionMember1S3FileReferenceRequest,
]


class Message(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageContentUnionMember1]]]
    """Message content.

    Use a string for text-only messages or a list of content parts for multimodal
    content.
    """

    role: Required[Literal["user", "assistant", "system"]]
    """Role: 'user', 'assistant', or 'system'"""

    authority: Optional[float]
    """Optional authority score"""

    metadata: Optional[Dict[str, object]]
    """Optional message-level metadata"""

    parent_id: Optional[str]
    """Optional parent message ID"""

    source_role_id: Optional[str]
    """Optional SourceRole entity ID"""

    timestamp: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Semantic timestamp for when the message was authored.

    Drives chunk timestamps, the extraction LLM's temporal anchor, and episodic
    grouping. Without it, relative phrases ('this morning') resolve against
    ingestion wall-clock and episodes collapse.
    """
