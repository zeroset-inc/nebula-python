# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "MemoryCreateResponse",
    "Results",
    "ResultsSnapshot",
    "ResultsSnapshotGraph",
    "ResultsSnapshotGraphEntity",
    "ResultsSnapshotGraphEntityDescriptionEmbeddings",
    "ResultsSnapshotGraphRelationshipDescriptionEmbeddings",
    "ResultsSnapshotGraphRelationshipRelationEmbeddings",
    "ResultsSnapshotGraphRelationship",
]


class ResultsSnapshotGraphEntity(BaseModel):
    """Canonical entity record used in snapshots, WAL ops, and segments."""

    id: str

    created_at: datetime

    engram_id: str

    name: str

    updated_at: datetime

    category: Optional[str] = None

    chunk_ids: Optional[List[str]] = None

    collection_id: Optional[str] = None

    description: Optional[str] = None

    fts_terms: Optional[Dict[str, int]] = None

    metadata: Optional[Dict[str, object]] = None

    relationship_count: Optional[int] = None


class ResultsSnapshotGraphEntityDescriptionEmbeddings(BaseModel):
    """A positionally-aligned masked embedding matrix."""

    dim: Optional[int] = None

    encoding: Optional[Literal["npy-base64"]] = None

    mask_b64: Optional[str] = None

    values_b64: Optional[str] = None


class ResultsSnapshotGraphRelationshipDescriptionEmbeddings(BaseModel):
    """A positionally-aligned masked embedding matrix."""

    dim: Optional[int] = None

    encoding: Optional[Literal["npy-base64"]] = None

    mask_b64: Optional[str] = None

    values_b64: Optional[str] = None


class ResultsSnapshotGraphRelationshipRelationEmbeddings(BaseModel):
    """A positionally-aligned masked embedding matrix."""

    dim: Optional[int] = None

    encoding: Optional[Literal["npy-base64"]] = None

    mask_b64: Optional[str] = None

    values_b64: Optional[str] = None


class ResultsSnapshotGraphRelationship(BaseModel):
    """Canonical relationship record used in snapshots, WAL ops, and segments."""

    id: str

    created_at: datetime

    object_id: str

    subject_id: str

    updated_at: datetime

    category: Optional[str] = None

    chunk_ids: Optional[List[str]] = None

    collection_id: Optional[str] = None

    description: Optional[str] = None

    engram_id: Optional[str] = None

    inference_metadata: Optional[Dict[str, object]] = None

    metadata: Optional[Dict[str, object]] = None

    object: Optional[str] = None

    predicate: Optional[str] = None

    relationship_type: Optional[str] = None

    subject: Optional[str] = None

    temporal_precision: Optional[str] = None

    valid_span: Optional[Dict[str, builtins.object]] = None

    weight: Optional[float] = None


class ResultsSnapshotGraph(BaseModel):
    """A complete graph payload or a context subgraph payload."""

    entities: Optional[List[ResultsSnapshotGraphEntity]] = None

    entity_description_embeddings: Optional[ResultsSnapshotGraphEntityDescriptionEmbeddings] = None
    """A positionally-aligned masked embedding matrix."""

    relationship_description_embeddings: Optional[ResultsSnapshotGraphRelationshipDescriptionEmbeddings] = None
    """A positionally-aligned masked embedding matrix."""

    relationship_relation_embeddings: Optional[ResultsSnapshotGraphRelationshipRelationEmbeddings] = None
    """A positionally-aligned masked embedding matrix."""

    relationships: Optional[List[ResultsSnapshotGraphRelationship]] = None


class ResultsSnapshot(BaseModel):
    """Portable full snapshot owned by the client."""

    collection_id: str

    root_hash: str

    created_at: Optional[datetime] = None

    format_version: Optional[int] = None

    generation: Optional[int] = None

    graph: Optional[ResultsSnapshotGraph] = None
    """A complete graph payload or a context subgraph payload."""


class Results(BaseModel):
    """Updated snapshot returned by snapshot-mode memory writes."""

    snapshot: ResultsSnapshot
    """Portable full snapshot owned by the client."""


class MemoryCreateResponse(BaseModel):
    results: Results
    """Updated snapshot returned by snapshot-mode memory writes."""
