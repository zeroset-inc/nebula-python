# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import builtins
from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "MemoryCreateParams",
    "ContentPart",
    "ContentPartTextContentRequest",
    "ContentPartFileContentRequest",
    "ContentPartS3FileReferenceRequest",
    "IngestionConfig",
    "IngestionConfigChunkEnrichmentSettings",
    "Message",
    "MessageContentUnionMember1",
    "MessageContentUnionMember1TextContentRequest",
    "MessageContentUnionMember1FileContentRequest",
    "MessageContentUnionMember1S3FileReferenceRequest",
    "Snapshot",
    "SnapshotGraph",
    "SnapshotGraphEntity",
    "SnapshotGraphEntityDescriptionEmbeddings",
    "SnapshotGraphRelationshipDescriptionEmbeddings",
    "SnapshotGraphRelationshipRelationEmbeddings",
    "SnapshotGraphRelationship",
]


class MemoryCreateParams(TypedDict, total=False):
    chunks: Optional[SequenceNotStr[str]]
    """Pre-chunked text for document type"""

    collection_id: Optional[str]
    """Collection UUID (mutually exclusive with snapshot)"""

    content_parts: Optional[Iterable[ContentPart]]
    """Multimodal content parts (text, images, audio, documents) for document type."""

    contents: Optional[SequenceNotStr[str]]
    """Batch content strings for snapshot mode"""

    engram_type: Literal["document", "conversation"]
    """Type of memory to create"""

    ingestion_config: Optional[IngestionConfig]
    """Public ingestion config accepted by memory-ingestion endpoints.

    This mirrors the supported request payload shape while staying independent from
    the runtime provider config, which also carries internal-only fields such as
    `app` and `extra_fields`.
    """

    ingestion_mode: Optional[Literal["hi-res", "ocr", "fast", "custom"]]
    """Ingestion mode for documents"""

    messages: Optional[Iterable[Message]]
    """Messages for conversation type"""

    metadata: Optional[Dict[str, object]]
    """Metadata for the memory"""

    name: Optional[str]
    """Optional name for the memory"""

    raw_text: Optional[str]
    """Raw text content for document type"""

    snapshot: Optional[Snapshot]
    """Portable full snapshot owned by the client."""

    speaker_id: Optional[str]
    """UUID of the SourceRole entity creating this memory"""

    speaker_name: Optional[str]
    """Display name of the speaker/agent creating this memory"""


class ContentPartTextContentRequest(TypedDict, total=False):
    """Text content block."""

    text: Required[str]
    """Text content"""

    type: Literal["text"]


class ContentPartFileContentRequest(TypedDict, total=False):
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


class ContentPartS3FileReferenceRequest(TypedDict, total=False):
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


ContentPart: TypeAlias = Union[
    ContentPartTextContentRequest, ContentPartFileContentRequest, ContentPartS3FileReferenceRequest
]


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
    """A message in a conversation with multimodal support."""

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

    timestamp: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Semantic timestamp for when the message was authored.

    Drives chunk timestamps, the extraction LLM's temporal anchor, and episodic
    grouping. Without it, relative phrases ('this morning') resolve against
    ingestion wall-clock and episodes collapse.
    """


class SnapshotGraphEntity(TypedDict, total=False):
    """Canonical entity record used in snapshots, WAL ops, and segments."""

    id: Required[str]

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    engram_id: Required[str]

    name: Required[str]

    updated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    category: Optional[str]

    chunk_ids: SequenceNotStr[str]

    collection_id: str

    description: Optional[str]

    fts_terms: Optional[Dict[str, int]]

    metadata: Dict[str, object]

    relationship_count: int


class SnapshotGraphEntityDescriptionEmbeddings(TypedDict, total=False):
    """A positionally-aligned masked embedding matrix."""

    dim: int

    encoding: Literal["npy-base64"]

    mask_b64: str

    values_b64: str


class SnapshotGraphRelationshipDescriptionEmbeddings(TypedDict, total=False):
    """A positionally-aligned masked embedding matrix."""

    dim: int

    encoding: Literal["npy-base64"]

    mask_b64: str

    values_b64: str


class SnapshotGraphRelationshipRelationEmbeddings(TypedDict, total=False):
    """A positionally-aligned masked embedding matrix."""

    dim: int

    encoding: Literal["npy-base64"]

    mask_b64: str

    values_b64: str


class SnapshotGraphRelationship(TypedDict, total=False):
    """Canonical relationship record used in snapshots, WAL ops, and segments."""

    id: Required[str]

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    object_id: Required[str]

    subject_id: Required[str]

    updated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    category: Optional[str]

    chunk_ids: SequenceNotStr[str]

    collection_id: str

    description: Optional[str]

    engram_id: Optional[str]

    inference_metadata: Optional[Dict[str, object]]

    metadata: Dict[str, object]

    object: Optional[str]

    predicate: str

    relationship_type: Optional[str]

    subject: Optional[str]

    temporal_precision: Optional[str]

    valid_span: Optional[Dict[str, builtins.object]]

    weight: Optional[float]


class SnapshotGraph(TypedDict, total=False):
    """A complete graph payload or a context subgraph payload."""

    entities: Iterable[SnapshotGraphEntity]

    entity_description_embeddings: SnapshotGraphEntityDescriptionEmbeddings
    """A positionally-aligned masked embedding matrix."""

    relationship_description_embeddings: SnapshotGraphRelationshipDescriptionEmbeddings
    """A positionally-aligned masked embedding matrix."""

    relationship_relation_embeddings: SnapshotGraphRelationshipRelationEmbeddings
    """A positionally-aligned masked embedding matrix."""

    relationships: Iterable[SnapshotGraphRelationship]


class Snapshot(TypedDict, total=False):
    """Portable full snapshot owned by the client."""

    collection_id: Required[str]

    root_hash: Required[str]

    created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    format_version: int

    generation: int

    graph: SnapshotGraph
    """A complete graph payload or a context subgraph payload."""
