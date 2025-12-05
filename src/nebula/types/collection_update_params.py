# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CollectionUpdateParams"]


class CollectionUpdateParams(TypedDict, total=False):
    access_tier: Optional[str]
    """Access tier for the collection: 'private', 'public_preview', or 'marketplace'"""

    description: Optional[str]
    """An optional description of the collection"""

    generate_description: Optional[bool]
    """Whether to generate a new synthetic description for the collection"""

    name: Optional[str]
    """The name of the collection"""
