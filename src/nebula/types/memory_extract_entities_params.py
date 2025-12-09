# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .generation_config_param import GenerationConfigParam

__all__ = ["MemoryExtractEntitiesParams", "EntityDeduplication"]


class MemoryExtractEntitiesParams(TypedDict, total=False):
    automatic_clustering: bool
    """Whether to automatically trigger graph clustering after entity deduplication."""

    automatic_deduplication: bool
    """Whether to automatically deduplicate entities."""

    chunk_merge_count: int
    """The number of extractions to merge into a single graph extraction."""

    conversation_context_enabled: bool
    """
    Whether to include multi-message context windows when extracting from
    conversations. Enables temporal continuity across messages.
    """

    conversation_context_window_size: int
    """
    Number of recent messages to include verbatim in engram_summary for conversation
    context. Messages beyond this window are summarized.
    """

    conversation_summary_update_frequency: int
    """
    How often (in number of messages) to re-summarize older conversation context.
    Lower values give fresher summaries but cost more. Set to 0 to disable summary
    caching and always summarize on-the-fly.
    """

    entity_deduplication: Optional[EntityDeduplication]
    """Enhanced settings for entity deduplication."""

    entity_types: SequenceNotStr[str]
    """The types of entities to extract."""

    generation_config: Optional[GenerationConfigParam]
    """Configuration for text generation during graph enrichment."""

    graph_entity_description_prompt: str
    """The prompt to use for entity description generation."""

    graph_extraction_prompt: str
    """The prompt to use for knowledge graph extraction."""

    idle_check_interval_minutes: int
    """Interval in minutes to check for idle system state for full re-clustering."""

    idle_full_clustering: bool
    """
    Whether to trigger full re-clustering during idle periods when no other
    workflows are active.
    """

    incremental_clustering: bool
    """Enable incremental (streaming) clustering updates after each ingestion."""

    incremental_jaccard_filter: float
    """
    Lightweight Jaccard filter when in 'leiden' mode; used only to prune obviously
    unrelated communities.
    """

    incremental_jaccard_reuse_threshold: float
    """
    Minimum Jaccard overlap to reuse an existing community during incremental
    updates.
    """

    incremental_min_cluster_size: int
    """Minimum size of a new incremental cluster before considering promotion."""

    incremental_neighbor_hops: int
    """Number of hops around changed entities to include in incremental subgraph."""

    incremental_structural_affinity_threshold: float
    """
    Minimum structural affinity (local modularity proxy) to reuse an existing
    community in incremental updates.
    """

    max_concurrent_entities_per_extraction: int
    """Maximum number of entities to create concurrently per extraction.

    Set to 1 for sequential processing.
    """

    max_concurrent_relationships_per_extraction: int
    """Maximum number of relationships to process concurrently per extraction.

    Set to 1 for sequential processing.
    """

    max_description_input_length: int
    """The maximum length of the description for a node in the graph."""

    max_knowledge_relationships: int
    """The maximum number of knowledge relationships to extract from each chunk."""

    relation_types: SequenceNotStr[str]
    """The types of relations to extract."""


class EntityDeduplication(TypedDict, total=False):
    """Enhanced settings for entity deduplication."""

    auto_merge_threshold: float
    """Confidence threshold for automatic entity merging."""

    candidate_pool_limit: int
    """
    Maximum number of candidates to load for in-memory vectorized retrieval
    fallback.
    """

    collection_scope: bool
    """Whether to limit deduplication to within collections."""

    create_audit_relationships: bool
    """Whether to create IS_DUPLICATE_OF relationships for audit trail."""

    cross_engram_deduplication: bool
    """Whether to deduplicate entities across engrams."""

    dedup_candidate_search_limit: int
    """Maximum concurrent candidate searches during deduplication."""

    dedup_llm_per_chunk_limit: int
    """
    Per-entity concurrency factor (multiplied with dedup_max_concurrent_chunks for
    effective concurrency).
    """

    dedup_max_concurrent_chunks: int
    """
    Base concurrency factor for deduplication (multiplied with
    dedup_llm_per_chunk_limit for effective concurrency).
    """

    dedup_timeout_seconds: int
    """Overall timeout for enhanced deduplication per engram (seconds)."""

    embedding_cache_enabled: bool
    """Whether to enable embedding caching."""

    enabled: bool
    """Whether to enable entity deduplication."""

    link_threshold: float
    """Confidence threshold for creating IS_DUPLICATE_OF relationships."""

    max_candidate_entities: int
    """Maximum number of candidate entities to consider for each entity."""

    max_concurrent_llm_calls: int
    """Global ceiling for concurrent LLM calls across all deduplication operations."""

    max_recursive_iterations: int
    """Maximum number of recursive deduplication iterations."""

    merge_prompt_template: str
    """Prompt template for entity merging."""

    preserve_entities: bool
    """Whether to preserve original entities with IS_DUPLICATE_OF links."""

    query_time_resolution: bool
    """Whether to resolve duplicates during search queries."""

    recursive_deduplication: bool
    """Whether to recursively resolve transitive duplicates."""

    retrieval_top_k: int
    """
    Number of top candidates to retrieve per entity using vectorized cosine
    similarity before reranking.
    """

    semantic_similarity_threshold: float
    """Minimum similarity threshold for semantic matching."""

    show_duplicate_relationships: bool
    """Whether to include IS_DUPLICATE_OF relationships in queries."""

    strategy: str
    """Deduplication strategy: 'exact', 'semantic', or 'hybrid'."""

    use_engram_context: bool
    """Whether to use engram context in deduplication decisions."""

    use_llm_for_merging: bool
    """Whether to use LLM for intelligent entity merging."""

    vector_doc_chunk_size: int
    """Number of document embeddings to process at once during vectorized retrieval."""

    vector_query_chunk_size: int
    """Number of query embeddings to process at once during vectorized retrieval."""
