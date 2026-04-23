# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import builtins
from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "SnapshotImportParams",
    "Snapshot",
    "SnapshotGraph",
    "SnapshotGraphEntity",
    "SnapshotGraphEntityDescriptionEmbeddings",
    "SnapshotGraphRelationshipDescriptionEmbeddings",
    "SnapshotGraphRelationshipRelationEmbeddings",
    "SnapshotGraphRelationship",
]


class SnapshotImportParams(TypedDict, total=False):
    snapshot: Required[Snapshot]
    """Portable full snapshot owned by the client."""


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
