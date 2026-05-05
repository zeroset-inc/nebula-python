# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CollectionUpdateParams"]


class CollectionUpdateParams(TypedDict, total=False):
    access_tier: Optional[str]

    description: Optional[str]

    generate_description: bool

    name: Optional[str]

    workflows_enabled: Optional[bool]
