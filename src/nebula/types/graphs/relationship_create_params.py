# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import builtins
from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["RelationshipCreateParams"]


class RelationshipCreateParams(TypedDict, total=False):
    description: Required[str]
    """The description of the relationship to create."""

    object: Required[str]
    """The object of the relationship to create."""

    object_id: Required[str]
    """The ID of the object of the relationship to create."""

    predicate: Required[str]
    """The predicate of the relationship to create."""

    subject: Required[str]
    """The subject of the relationship to create."""

    subject_id: Required[str]
    """The ID of the subject of the relationship to create."""

    metadata: Optional[Dict[str, builtins.object]]
    """The metadata of the relationship to create."""

    weight: float
    """The weight of the relationship to create."""
