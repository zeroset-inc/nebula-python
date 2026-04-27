# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import builtins
from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "MemorySearchParams",
    "SearchSettings",
    "Snapshot",
    "SnapshotGraph",
    "SnapshotGraphEntity",
    "SnapshotGraphEntityDescriptionEmbeddings",
    "SnapshotGraphRelationshipDescriptionEmbeddings",
    "SnapshotGraphRelationshipRelationEmbeddings",
    "SnapshotGraphRelationship",
]


class MemorySearchParams(TypedDict, total=False):
    collection_ids: Optional[SequenceNotStr[str]]
    """Optional list of collection UUIDs or names to scope the search."""

    effort: Optional[Literal["auto", "low", "medium", "high"]]
    """Compute effort budget for memory search.

    Effort controls traversal compute (exploration budgets, depth, fanout), not the
    size of the returned MemoryRecall projection.
    """

    filters: Optional[Dict[str, object]]
    """Optional filters to apply to the search."""

    nql: Optional[str]
    """Pre-written NQL script.

    Executes directly without planner compilation. Mutually exclusive with `query`.
    """

    query: Optional[str]
    """Natural-language search query. Mutually exclusive with `nql`."""

    search_settings: Optional[SearchSettings]
    """Advanced search settings for fine-tuning search behavior.

    Note: Core parameters (query, collection_ids, filters) are now top-level API
    parameters. This class contains advanced tuning options plus internal fields
    used by the retrieval service.

    Memory search uses `effort` (auto/low/medium/high) to control compute.
    """

    snapshot: Optional[Snapshot]
    """Portable full snapshot owned by the client."""


class SearchSettings(TypedDict, total=False):
    """Advanced search settings for fine-tuning search behavior.

    Note: Core parameters (query, collection_ids, filters) are now top-level API parameters.
    This class contains advanced tuning options plus internal fields used by the retrieval service.

    Memory search uses `effort` (auto/low/medium/high) to control compute.
    """

    effort: Literal["auto", "low", "medium", "high"]
    """Compute effort budget (auto/low/medium/high).

    Controls traversal compute for memory search, not MemoryRecall size.
    """

    enable_conceptual_expansion: bool
    """
    Enable conceptual expansion for cross-domain discovery through overlapping
    concepts
    """

    filters: Dict[str, object]
    """Internal: Filters populated by the API router"""

    fulltext_weight: float
    """Weight for fulltext search in hybrid mode (0-1).

    Set to 0 for pure semantic search.
    """

    graph_settings: Dict[str, object]
    """Internal: Graph traversal settings (bfs_max_depth, semantic_threshold, etc.)"""

    has_pruning_gate: bool
    """
    Internal: Set by select_search_filters when an owner_id $in partition-pruning
    wrapper has been added around the filter tree. Used by the in-memory graph read
    engine to strip the Postgres-only wrapper before evaluating delegation.
    """

    include_scores: bool
    """Whether to include search score values in the search results"""

    semantic_weight: float
    """Weight for semantic search in hybrid mode (0-1).

    Set to 0 for pure fulltext search.
    """

    verbose: bool
    """
    Include full internal metadata, UUIDs, and confidence fields in MemoryRecall
    responses. When False, returns compact LLM-optimized format.
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
