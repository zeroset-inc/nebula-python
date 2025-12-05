# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["EntityCreateParams"]


class EntityCreateParams(TypedDict, total=False):
    description: Required[str]
    """The description of the entity to create."""

    name: Required[str]
    """The name of the entity to create."""

    category: Optional[str]
    """The category of the entity to create."""

    metadata: Optional[Dict[str, object]]
    """The metadata of the entity to create."""
