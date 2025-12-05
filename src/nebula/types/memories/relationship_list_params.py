# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["RelationshipListParams"]


class RelationshipListParams(TypedDict, total=False):
    entity_names: Optional[SequenceNotStr[str]]
    """Filter relationships by specific entity names."""

    limit: int
    """Specifies a limit on the number of objects to return, ranging between 1 and 100.

    Defaults to 100.
    """

    offset: int
    """Specifies the number of objects to skip. Defaults to 0."""

    relationship_types: Optional[SequenceNotStr[str]]
    """Filter relationships by specific relationship types."""
