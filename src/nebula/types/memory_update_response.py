# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemoryUpdateResponse", "Results", "ResultsConversation", "ResultsDocument"]


class ResultsConversation(BaseModel):
    """Conversation-specific typed fields.

    Present iff ``Engram.kind == CONVERSATION``. Holds the platform-written
    fields that previously lived on ``metadata`` (``conversation_id``,
    ``episode_type``) so they have a typed home and are not co-mingled with
    user-supplied metadata.
    """

    conversation_id: Optional[str] = None

    episode_type: Optional[str] = None


class ResultsDocument(BaseModel):
    """Document-specific typed fields.

    Present iff ``Engram.kind == DOCUMENT``. ``document_type`` is required
    because every document needs an extension/format classifier for parsing.
    ``original_extension`` records the source filename's extension when it
    differs from the canonical ``document_type`` (e.g. user uploaded ``.JPG``
    normalized to ``jpeg``).
    """

    document_type: Literal[
        "mp3",
        "csv",
        "eml",
        "msg",
        "p7s",
        "epub",
        "xls",
        "xlsx",
        "html",
        "htm",
        "bmp",
        "heic",
        "jpeg",
        "png",
        "tiff",
        "jpg",
        "svg",
        "md",
        "org",
        "odt",
        "pdf",
        "txt",
        "json",
        "ppt",
        "pptx",
        "rst",
        "rtf",
        "tsv",
        "gif",
        "doc",
        "docx",
        "py",
        "js",
        "ts",
        "css",
    ]
    """Types of file formats that can be stored as engrams."""

    original_extension: Optional[str] = None


class Results(BaseModel):
    """The unified engram model: typed kind + per-kind substructure.

    ``kind`` is the canonical discriminator. The per-kind ``conversation``
    and ``document`` substructures hold typed fields known to the
    platform; ``metadata`` is reserved for user-supplied annotations and
    must never carry platform-written discriminators or routing markers.

    Construction enforces shape consistency via a model validator:
    ``kind=conversation`` must not carry document fields, ``kind=document``
    must carry a ``DocumentFields`` substructure (``document_type`` is
    required), and vice versa.
    """

    kind: Literal["document", "conversation"]
    """The canonical engram discriminator.

    A single source of truth: every engram is either a `document` or a
    `conversation`. The kind drives which typed substructure (`Engram.document` /
    `Engram.conversation`) carries kind-specific fields. The free-form `metadata`
    dict is reserved for user-supplied annotations and is never inspected for
    routing.
    """

    owner_id: str

    id: Optional[str] = None

    chunks: Optional[List[object]] = None

    collection_ids: Optional[List[str]] = None

    conversation: Optional[ResultsConversation] = None
    """Conversation-specific typed fields.

    Present iff `Engram.kind == CONVERSATION`. Holds the platform-written fields
    that previously lived on `metadata` (`conversation_id`, `episode_type`) so they
    have a typed home and are not co-mingled with user-supplied metadata.
    """

    created_at: Optional[datetime] = None

    document: Optional[ResultsDocument] = None
    """Document-specific typed fields.

    Present iff `Engram.kind == DOCUMENT`. `document_type` is required because every
    document needs an extension/format classifier for parsing. `original_extension`
    records the source filename's extension when it differs from the canonical
    `document_type` (e.g. user uploaded `.JPG` normalized to `jpeg`).
    """

    extraction_status: Optional[Literal["pending", "processing", "success", "failed"]] = None
    """Status of graph creation per document."""

    ingestion_attempt_number: Optional[int] = None

    ingestion_status: Optional[
        Literal[
            "pending", "parsing", "extracting", "chunking", "embedding", "augmenting", "storing", "failed", "success"
        ]
    ] = None
    """Status of document processing."""

    merkle_root: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    search_ready_seq: Optional[int] = None

    size_in_bytes: Optional[int] = None

    text: Optional[str] = None

    title: Optional[str] = None

    total_tokens: Optional[int] = None

    updated_at: Optional[datetime] = None

    version: Optional[str] = None

    workflow_run_id: Optional[str] = None


class MemoryUpdateResponse(BaseModel):
    results: Results
    """The unified engram model: typed kind + per-kind substructure.

    `kind` is the canonical discriminator. The per-kind `conversation` and
    `document` substructures hold typed fields known to the platform; `metadata` is
    reserved for user-supplied annotations and must never carry platform-written
    discriminators or routing markers.

    Construction enforces shape consistency via a model validator:
    `kind=conversation` must not carry document fields, `kind=document` must carry a
    `DocumentFields` substructure (`document_type` is required), and vice versa.
    """
