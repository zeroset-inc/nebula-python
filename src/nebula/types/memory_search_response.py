# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "MemorySearchResponse",
    "NebulaResultsCompactMemoryRecallResponse",
    "NebulaResultsCompactMemoryRecallResponseResults",
    "NebulaResultsMemoryRecall",
    "NebulaResultsMemoryRecallResults",
    "NebulaResultsMemoryRecallResultsEntity",
    "NebulaResultsMemoryRecallResultsEpisodic",
    "NebulaResultsMemoryRecallResultsInferenceHint",
    "NebulaResultsMemoryRecallResultsProcedural",
    "NebulaResultsMemoryRecallResultsSemantic",
    "NebulaResultsMemoryRecallResultsSemanticEvidenceRef",
    "NebulaResultsMemoryRecallResultsSource",
    "NebulaResultsMemoryRecallResultsSourceEvidenceRef",
    "NebulaResultsSnapshotSearchResult",
    "NebulaResultsSnapshotSearchResultResults",
    "NebulaResultsSnapshotSearchResultResultsEntity",
    "NebulaResultsSnapshotSearchResultResultsRelationship",
]


class NebulaResultsCompactMemoryRecallResponseResults(BaseModel):
    """Default compact response from /v1/memories/search."""

    query: str

    episodic: Optional[List[Dict[str, object]]] = None

    procedural: Optional[List[Dict[str, object]]] = None

    semantic: Optional[List[Dict[str, object]]] = None

    sources: Optional[List[Dict[str, object]]] = None

    token_count: Optional[int] = None


class NebulaResultsCompactMemoryRecallResponse(BaseModel):
    results: NebulaResultsCompactMemoryRecallResponseResults
    """Default compact response from /v1/memories/search."""


class NebulaResultsMemoryRecallResultsEntity(BaseModel):
    """An entity activated during memory traversal with its profile.

    Represents a conceptual node in memory that was activated by the query.
    Contains the full EntityProfile (gestalt) filtered by relevance.
    """

    id: str

    name: str

    activation_score: Optional[float] = None

    category: Optional[str] = None

    profile: Optional[object] = None


class NebulaResultsMemoryRecallResultsEpisodic(BaseModel):
    """An episodic nodegroup activated during memory traversal.

    Represents a cluster of temporally related facts/events discovered
    during graph traversal.
    """

    id: str

    name: str

    activation_score: Optional[float] = None

    category: Optional[str] = None

    description: Optional[str] = None

    entity_names: Optional[List[str]] = None

    evidence_ids: Optional[List[str]] = None

    member_semantic_ids: Optional[List[str]] = None

    n_facts: Optional[int] = None

    status: Optional[str] = None

    t_last: Optional[str] = None

    t_start: Optional[str] = None


class NebulaResultsMemoryRecallResultsInferenceHint(BaseModel):
    """A lightweight inference artifact returned alongside MemoryRecall.

    These are *not* asserted facts. They are "evidence + weak hints" that may have influenced
    retrieval (e.g. query expansion) or may be useful for UI transparency.
    """

    object: str

    predicate: str

    term: str

    confidence: Optional[float] = None

    inference_metadata: Optional[Dict[str, builtins.object]] = None

    inferred: Optional[bool] = None

    ledger_p_stable: Optional[float] = None

    ledger_p_true: Optional[float] = None

    ledger_p_use: Optional[float] = None

    metadata: Optional[Dict[str, builtins.object]] = None

    object_id: Optional[str] = None

    relationship_id: Optional[str] = None

    subject_id: Optional[str] = None

    usable_for_rewrite: Optional[bool] = None

    used_for_rewrite: Optional[bool] = None


class NebulaResultsMemoryRecallResultsProcedural(BaseModel):
    """A procedure (user preference) activated during memory traversal.

    Procedures are prescriptive -- they describe what the user prefers,
    likes, dislikes, or habitually does. Distinct from facts which are
    descriptive assertions.
    """

    id: str

    statement: str

    activation_score: Optional[float] = None

    belief_kind: Optional[str] = None

    confidence: Optional[float] = None

    derivation_type: Optional[str] = None

    entity_id: Optional[str] = None

    entity_name: Optional[str] = None

    is_negated: Optional[bool] = None

    metadata: Optional[Dict[str, object]] = None


class NebulaResultsMemoryRecallResultsSemanticEvidenceRef(BaseModel):
    """Tagged reference to a source of evidence."""

    ref_type: Literal["chunk", "table_artifact"]

    artifact_id: Optional[str] = None

    chunk_id: Optional[str] = None

    collection_id: Optional[str] = None

    column_names: Optional[List[str]] = None

    row_indices: Optional[List[int]] = None

    table_name: Optional[str] = None


class NebulaResultsMemoryRecallResultsSemantic(BaseModel):
    """A semantic item activated during memory traversal.

    Represents a structured assertion (fact, inference, or task) that was
    found relevant to the query. Links back to its entity and source
    utterances for provenance.
    """

    id: str

    predicate: str

    subject: str

    value: str

    activation_score: Optional[float] = None

    belief_kind: Optional[str] = None

    category: Optional[str] = None

    corroboration_count: Optional[int] = None

    description: Optional[str] = None

    entity_id: Optional[str] = None

    entity_name: Optional[str] = None

    evidence_ids: Optional[List[str]] = None

    evidence_refs: Optional[List[NebulaResultsMemoryRecallResultsSemanticEvidenceRef]] = None

    extraction_confidence: Optional[float] = None

    is_current: Optional[bool] = None

    reasoning: Optional[str] = None

    resolved_at: Optional[str] = None

    source_nodegroup_ids: Optional[List[str]] = None

    stability_confidence: Optional[float] = None

    temporal_precision: Optional[str] = None

    temporal_validity: Optional[object] = None

    truth_confidence: Optional[float] = None

    use_confidence: Optional[float] = None


class NebulaResultsMemoryRecallResultsSourceEvidenceRef(BaseModel):
    """Tagged reference to a source of evidence."""

    ref_type: Literal["chunk", "table_artifact"]

    artifact_id: Optional[str] = None

    chunk_id: Optional[str] = None

    collection_id: Optional[str] = None

    column_names: Optional[List[str]] = None

    row_indices: Optional[List[int]] = None

    table_name: Optional[str] = None


class NebulaResultsMemoryRecallResultsSource(BaseModel):
    """A source that grounds facts in episodic memory.

    This is the raw source material that supports the structured knowledge.
    Provides the exact quotes and context for verification.

    ``evidence_ref`` carries typed provenance so the client can distinguish
    chunk-backed sources from table-artifact-backed sources (or future
    modalities) without parsing opaque metadata.
    """

    id: str

    text: str

    activation_score: Optional[float] = None

    display_name: Optional[str] = None

    engram_id: Optional[str] = None

    evidence_ref: Optional[NebulaResultsMemoryRecallResultsSourceEvidenceRef] = None
    """Tagged reference to a source of evidence."""

    metadata: Optional[Dict[str, object]] = None

    owner_id: Optional[str] = None

    page_number: Optional[int] = None

    section_path: Optional[List[str]] = None

    source_role: Optional[str] = None

    speaker: Optional[str] = None

    speaker_id: Optional[str] = None

    structure_label: Optional[str] = None

    supporting_fact_ids: Optional[List[str]] = None

    timestamp: Optional[datetime] = None


class NebulaResultsMemoryRecallResults(BaseModel):
    """Hierarchical memory response - all layers, weighted by activation.

    This is the primary response type for conceptual memory retrieval.
    It contains all layers of the memory hierarchy:

    1. **Entities (gestalt/schema layer)**: EntityProfiles that represent
       the conceptual understanding of activated entities.

    2. **Semantics (semantic layer)**: Structured assertions (facts,
       inferences, tasks) scored by relevance and confidence.

    3. **Episodes (temporal clusters)**: Episodic nodegroups that cluster
       temporally related facts and events.

    4. **Sources (episodic layer)**: The raw source material that
       grounds the structured knowledge in actual moments/quotes.

    The RecallFocus weights determine how much emphasis each layer gets
    in filtering and presentation, but all layers are always available.
    """

    query: str

    entities: Optional[List[NebulaResultsMemoryRecallResultsEntity]] = None

    episodic: Optional[List[NebulaResultsMemoryRecallResultsEpisodic]] = None

    inference_hints: Optional[List[NebulaResultsMemoryRecallResultsInferenceHint]] = None

    procedural: Optional[List[NebulaResultsMemoryRecallResultsProcedural]] = None

    semantic: Optional[List[NebulaResultsMemoryRecallResultsSemantic]] = None

    sources: Optional[List[NebulaResultsMemoryRecallResultsSource]] = None

    total_traversal_time_ms: Optional[float] = None


class NebulaResultsMemoryRecall(BaseModel):
    results: NebulaResultsMemoryRecallResults
    """Hierarchical memory response - all layers, weighted by activation.

    This is the primary response type for conceptual memory retrieval. It contains
    all layers of the memory hierarchy:

    1. **Entities (gestalt/schema layer)**: EntityProfiles that represent the
       conceptual understanding of activated entities.

    2. **Semantics (semantic layer)**: Structured assertions (facts, inferences,
       tasks) scored by relevance and confidence.

    3. **Episodes (temporal clusters)**: Episodic nodegroups that cluster temporally
       related facts and events.

    4. **Sources (episodic layer)**: The raw source material that grounds the
       structured knowledge in actual moments/quotes.

    The RecallFocus weights determine how much emphasis each layer gets in filtering
    and presentation, but all layers are always available.
    """


class NebulaResultsSnapshotSearchResultResultsEntity(BaseModel):
    id: str

    name: str

    score: float

    category: Optional[str] = None

    description: Optional[str] = None


class NebulaResultsSnapshotSearchResultResultsRelationship(BaseModel):
    id: str

    object_id: str

    predicate: str

    subject_id: str

    description: Optional[str] = None

    weight: Optional[float] = None


class NebulaResultsSnapshotSearchResultResults(BaseModel):
    """Stateless snapshot-search response shape."""

    entities: Optional[List[NebulaResultsSnapshotSearchResultResultsEntity]] = None

    relationships: Optional[List[NebulaResultsSnapshotSearchResultResultsRelationship]] = None


class NebulaResultsSnapshotSearchResult(BaseModel):
    results: NebulaResultsSnapshotSearchResultResults
    """Stateless snapshot-search response shape."""


MemorySearchResponse: TypeAlias = Union[
    NebulaResultsCompactMemoryRecallResponse, NebulaResultsMemoryRecall, NebulaResultsSnapshotSearchResult
]
