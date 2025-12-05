# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["EntityUpdateParams"]


class EntityUpdateParams(TypedDict, total=False):
    collection_id: Required[str]
    """The collection ID corresponding to the graph containing the entity."""

    name: Required[Optional[str]]
    """The updated name of the entity."""

    category: Optional[str]
    """The updated category of the entity."""

    description: Optional[str]
    """The updated description of the entity."""

    metadata: Optional[Dict[str, object]]
    """The updated metadata of the entity."""
