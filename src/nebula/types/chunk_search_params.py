# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .search_settings_param import SearchSettingsParam

__all__ = ["ChunkSearchParams"]


class ChunkSearchParams(TypedDict, total=False):
    query: Required[str]

    search_settings: SearchSettingsParam
    """
    Simplified search settings with automatic hybrid search and type-specific
    limits.
    """
