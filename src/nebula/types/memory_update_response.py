# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemoryUpdateResponse", "Results"]


class Results(BaseModel):
    """Base class for engram information handling."""

    id: str

    collection_ids: List[str]

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

    engram_type: Literal["document", "conversation"]
    """Types of engrams - broader categories that include documents and conversations."""

    metadata: Dict[str, object]

    owner_id: str

    chunks: Optional[List[object]] = None

    created_at: Optional[datetime] = None

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

    search_ready_seq: Optional[int] = None

    size_in_bytes: Optional[int] = None

    summary: Optional[str] = None

    summary_embedding: Optional[List[float]] = None

    text: Optional[str] = None

    title: Optional[str] = None

    total_tokens: Optional[int] = None

    updated_at: Optional[datetime] = None

    version: Optional[str] = None

    workflow_run_id: Optional[str] = None


class MemoryUpdateResponse(BaseModel):
    results: Results
    """Base class for engram information handling."""
