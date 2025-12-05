# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EntityResolveDuplicateParams"]


class EntityResolveDuplicateParams(TypedDict, total=False):
    action: Required[str]
    """Action to take: 'merge', 'unlink', 'change_canonical'"""

    public: bool

    target_entity_id: Optional[str]
    """Target entity ID for the action"""
