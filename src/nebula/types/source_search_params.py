# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SourceSearchParams", "SearchSettings"]


class SourceSearchParams(TypedDict, total=False):
    query: Required[str]

    search_settings: SearchSettings
    """Advanced search settings for fine-tuning search behavior.

    Note: Core parameters (query, collection_ids, filters) are now top-level API
    parameters. This class contains advanced tuning options plus internal fields
    used by the retrieval service.

    Memory search uses `effort` (auto/low/medium/high) to control compute.
    """


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
