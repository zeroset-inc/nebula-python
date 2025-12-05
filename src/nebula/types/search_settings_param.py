# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["SearchSettingsParam"]


class SearchSettingsParam(TypedDict, total=False):
    enable_conceptual_expansion: bool
    """
    Enable conceptual expansion for cross-domain discovery through overlapping SLPA
    concepts
    """

    filters: Dict[str, object]
    """Filters to apply to the search.

    Allowed operators include `eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `like`,
    `ilike`, `in`, and `nin`.

          Commonly seen filters include operations include the following:

            `{"engram_id": {"$eq": "9fbe403b-..."}}`

            `{"engram_id": {"$in": ["9fbe403b-...", "3e157b3a-..."]}}`

            `{"collection_ids": {"$overlap": ["122fdf6a-...", "..."]}}`

            `{"$and": {"$engram_id": ..., "collection_ids": ...}}`

          **Special Filter Keys for Graph Search:**

            `{"source_role": "user"}` - Filter by source role (e.g., 'user', 'assistant', 'CEO')

            `{"timestamp": {"$gte": "2024-01-01", "$lte": "2024-12-31"}}` - Filter by timestamp (date range)

            `{"owner_scope": ["user_id_1", "user_id_2"]}` - Filter by owner IDs
    """

    fulltext_weight: float
    """Weight for fulltext search in hybrid mode. Set to 0 for pure semantic search."""

    include_metadatas: bool
    """Whether to include element metadata in the search results"""

    include_scores: bool
    """Whether to include search score values in the search results"""

    limit: int
    """Maximum number of overall results to return"""

    search_mode: str
    """
    Graph search algorithm: 'fast' (fast BFS) or 'super' (SuperBFS with
    contextualization)
    """

    semantic_weight: float
    """Weight for semantic search in hybrid mode. Set to 0 for pure fulltext search."""
