# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .graph_response import GraphResponse

__all__ = ["GraphListResponse"]


class GraphListResponse(BaseModel):
    results: List[GraphResponse]

    total_entries: int
