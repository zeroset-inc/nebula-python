# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .community import Community

__all__ = ["CommunityListResponse"]


class CommunityListResponse(BaseModel):
    results: List[Community]

    total_entries: int
