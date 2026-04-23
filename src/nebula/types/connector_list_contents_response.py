# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectorListContentsResponse", "Result"]


class Result(BaseModel):
    id: str

    has_children: bool

    mime_type: str

    name: str

    type: Literal["folder", "file"]

    is_selected: Optional[bool] = None


class ConnectorListContentsResponse(BaseModel):
    results: List[Result]
