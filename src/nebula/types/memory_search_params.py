# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .search_mode import SearchMode
from .search_settings_param import SearchSettingsParam

__all__ = ["MemorySearchParams"]


class MemorySearchParams(TypedDict, total=False):
    query: Required[str]
    """The search query to perform."""

    search_mode: SearchMode
    """Graph search algorithm selection:

    `fast`: Fast BFS graph traversal (max_depth=3, simple scoring) `super`: SuperBFS
    with set transformers (max_depth=3, contextualized scoring, default)

    All modes now use depth=3 for optimal speed + relevance balance. All search
    settings can be controlled via `search_settings` regardless of mode.
    """

    search_settings: SearchSettingsParam
    """Settings for engram search"""
