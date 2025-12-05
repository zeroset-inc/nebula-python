# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CommunityUpdateParams"]


class CommunityUpdateParams(TypedDict, total=False):
    collection_id: Required[str]

    findings: Optional[SequenceNotStr[str]]

    name: Optional[str]

    rating: Optional[float]

    rating_explanation: Optional[str]

    summary: Optional[str]
