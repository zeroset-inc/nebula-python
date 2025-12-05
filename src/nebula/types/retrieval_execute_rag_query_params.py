# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .search_mode import SearchMode
from .search_settings_param import SearchSettingsParam
from .generation_config_param import GenerationConfigParam

__all__ = ["RetrievalExecuteRagQueryParams"]


class RetrievalExecuteRagQueryParams(TypedDict, total=False):
    query: Required[str]

    include_title_if_available: bool
    """Include engram titles in responses when available"""

    include_web_search: bool
    """Include web search results provided to the LLM."""

    rag_generation_config: GenerationConfigParam
    """Configuration for RAG generation"""

    search_mode: SearchMode
    """Graph search algorithm selection:

    `fast`: Fast BFS graph traversal (max_depth=3, simple scoring) `super`: SuperBFS
    with set transformers (max_depth=3, contextualized scoring, default)

    All modes now use depth=3 for optimal speed + relevance balance. All search
    settings can be controlled via `search_settings` regardless of mode.
    """

    search_settings: Optional[SearchSettingsParam]
    """
    Simplified search settings with automatic hybrid search and type-specific
    limits.
    """

    task_prompt: Optional[str]
    """Optional custom prompt to override default"""
