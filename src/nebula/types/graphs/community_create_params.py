# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CommunityCreateParams"]


class CommunityCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the community"""

    summary: Required[str]
    """A summary of the community"""

    findings: Optional[SequenceNotStr[str]]
    """Findings about the community"""

    rating: Optional[float]
    """Rating between 1 and 10"""

    rating_explanation: Optional[str]
    """Explanation for the rating"""
