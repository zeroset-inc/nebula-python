# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ConnectorSyncResponse", "Results"]


class Results(BaseModel):
    message: str


class ConnectorSyncResponse(BaseModel):
    results: Results
