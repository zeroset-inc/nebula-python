# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["CommunityBuildParams"]


class CommunityBuildParams(TypedDict, total=False):
    body: Optional[Dict[str, object]]
    """Settings for the graph enrichment process."""
