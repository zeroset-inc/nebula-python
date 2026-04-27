# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "MemoryCreateResponse",
    "NebulaResultsMemoryCreateAcceptedResponse",
    "NebulaResultsMemoryCreateAcceptedResponseResults",
    "NebulaResultsSnapshotMutationResult",
    "NebulaResultsSnapshotMutationResultResults",
    "NebulaResultsSnapshotMutationResultResultsSnapshot",
    "NebulaResultsSnapshotMutationResultResultsSnapshotGraph",
    "NebulaResultsSnapshotMutationResultResultsSnapshotGraphEntity",
    "NebulaResultsSnapshotMutationResultResultsSnapshotGraphEntityDescriptionEmbeddings",
    "NebulaResultsSnapshotMutationResultResultsSnapshotGraphRelationshipDescriptionEmbeddings",
    "NebulaResultsSnapshotMutationResultResultsSnapshotGraphRelationshipRelationEmbeddings",
    "NebulaResultsSnapshotMutationResultResultsSnapshotGraphRelationship",
]


class NebulaResultsMemoryCreateAcceptedResponseResults(BaseModel):
    """Accepted-response envelope for async memory ingestion."""

    id: str

    message: str

    engram_id: Optional[str] = None

    memory_id: Optional[str] = None

    status: Optional[Literal["parsing", "processing", "queued"]] = None

    task_id: Optional[str] = None


class NebulaResultsMemoryCreateAcceptedResponse(BaseModel):
    results: NebulaResultsMemoryCreateAcceptedResponseResults
    """Accepted-response envelope for async memory ingestion."""


class NebulaResultsSnapshotMutationResultResultsSnapshotGraphEntity(BaseModel):
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


class NebulaResultsSnapshotMutationResultResultsSnapshotGraphEntityDescriptionEmbeddings(BaseModel):
    """A positionally-aligned masked embedding matrix."""

    dim: Optional[int] = None

    encoding: Optional[Literal["npy-base64"]] = None

    mask_b64: Optional[str] = None

    values_b64: Optional[str] = None


class NebulaResultsSnapshotMutationResultResultsSnapshotGraphRelationshipDescriptionEmbeddings(BaseModel):
    """A positionally-aligned masked embedding matrix."""

    dim: Optional[int] = None

    encoding: Optional[Literal["npy-base64"]] = None

    mask_b64: Optional[str] = None

    values_b64: Optional[str] = None


class NebulaResultsSnapshotMutationResultResultsSnapshotGraphRelationshipRelationEmbeddings(BaseModel):
    """A positionally-aligned masked embedding matrix."""

    dim: Optional[int] = None

    encoding: Optional[Literal["npy-base64"]] = None

    mask_b64: Optional[str] = None

    values_b64: Optional[str] = None


class NebulaResultsSnapshotMutationResultResultsSnapshotGraphRelationship(BaseModel):
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


class NebulaResultsSnapshotMutationResultResultsSnapshotGraph(BaseModel):
    """A complete graph payload or a context subgraph payload."""

    entities: Optional[List[NebulaResultsSnapshotMutationResultResultsSnapshotGraphEntity]] = None

    entity_description_embeddings: Optional[
        NebulaResultsSnapshotMutationResultResultsSnapshotGraphEntityDescriptionEmbeddings
    ] = None
    """A positionally-aligned masked embedding matrix."""

    relationship_description_embeddings: Optional[
        NebulaResultsSnapshotMutationResultResultsSnapshotGraphRelationshipDescriptionEmbeddings
    ] = None
    """A positionally-aligned masked embedding matrix."""

    relationship_relation_embeddings: Optional[
        NebulaResultsSnapshotMutationResultResultsSnapshotGraphRelationshipRelationEmbeddings
    ] = None
    """A positionally-aligned masked embedding matrix."""

    relationships: Optional[List[NebulaResultsSnapshotMutationResultResultsSnapshotGraphRelationship]] = None


class NebulaResultsSnapshotMutationResultResultsSnapshot(BaseModel):
    """Portable full snapshot owned by the client."""

    collection_id: str

    root_hash: str

    created_at: Optional[datetime] = None

    format_version: Optional[int] = None

    generation: Optional[int] = None

    graph: Optional[NebulaResultsSnapshotMutationResultResultsSnapshotGraph] = None
    """A complete graph payload or a context subgraph payload."""


class NebulaResultsSnapshotMutationResultResults(BaseModel):
    """Updated snapshot returned by snapshot-mode memory writes."""

    snapshot: NebulaResultsSnapshotMutationResultResultsSnapshot
    """Portable full snapshot owned by the client."""


class NebulaResultsSnapshotMutationResult(BaseModel):
    results: NebulaResultsSnapshotMutationResultResults
    """Updated snapshot returned by snapshot-mode memory writes."""


MemoryCreateResponse: TypeAlias = Union[NebulaResultsMemoryCreateAcceptedResponse, NebulaResultsSnapshotMutationResult]
