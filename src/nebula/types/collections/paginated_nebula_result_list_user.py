# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..standard_user import StandardUser

__all__ = ["PaginatedNebulaResultListUser"]


class PaginatedNebulaResultListUser(BaseModel):
    results: List[StandardUser]

    total_entries: int
