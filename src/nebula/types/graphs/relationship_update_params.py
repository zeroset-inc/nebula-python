# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import builtins
from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["RelationshipUpdateParams"]


class RelationshipUpdateParams(TypedDict, total=False):
    collection_id: Required[str]
    """The collection ID corresponding to the graph containing the relationship."""

    object: Required[Optional[str]]
    """The updated object of the relationship."""

    object_id: Required[Optional[str]]
    """The updated object ID of the relationship."""

    predicate: Required[Optional[str]]
    """The updated predicate of the relationship."""

    subject: Required[Optional[str]]
    """The updated subject of the relationship."""

    subject_id: Required[Optional[str]]
    """The updated subject ID of the relationship."""

    description: Optional[str]
    """The updated description of the relationship."""

    metadata: Optional[Dict[str, builtins.object]]
    """The updated metadata of the relationship."""

    weight: Optional[float]
    """The updated weight of the relationship."""
