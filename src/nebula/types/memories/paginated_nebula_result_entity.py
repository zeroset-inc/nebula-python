# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..graphs.entity import Entity

__all__ = ["PaginatedNebulaResultEntity"]


class PaginatedNebulaResultEntity(BaseModel):
    results: List[Entity]

    total_entries: int
