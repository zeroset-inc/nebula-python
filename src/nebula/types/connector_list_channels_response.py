# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ConnectorListChannelsResponse", "Result"]


class Result(BaseModel):
    id: str

    name: str

    is_private: Optional[bool] = None

    is_selected: Optional[bool] = None

    num_members: Optional[int] = None


class ConnectorListChannelsResponse(BaseModel):
    results: List[Result]
