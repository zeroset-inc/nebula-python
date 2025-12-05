# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..graphs.relationship import Relationship

__all__ = ["PaginatedNebulaResultRelationship"]


class PaginatedNebulaResultRelationship(BaseModel):
    results: List[Relationship]

    total_entries: int
