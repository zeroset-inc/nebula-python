# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ConnectorListFoldersResponse", "Result"]


class Result(BaseModel):
    id: str

    has_children: bool

    name: str

    is_selected: Optional[bool] = None


class ConnectorListFoldersResponse(BaseModel):
    results: List[Result]
