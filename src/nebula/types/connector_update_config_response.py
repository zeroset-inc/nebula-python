# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectorUpdateConfigResponse", "Results"]


class Results(BaseModel):
    message: str

    status: Literal["active"]


class ConnectorUpdateConfigResponse(BaseModel):
    results: Results
