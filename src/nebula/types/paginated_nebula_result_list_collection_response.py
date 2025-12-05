# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .collection_response import CollectionResponse

__all__ = ["PaginatedNebulaResultListCollectionResponse"]


class PaginatedNebulaResultListCollectionResponse(BaseModel):
    results: List[CollectionResponse]

    total_entries: int
