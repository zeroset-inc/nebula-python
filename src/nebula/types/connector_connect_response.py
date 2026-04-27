# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ConnectorConnectResponse", "Results"]


class Results(BaseModel):
    auth_url: str

    state: str


class ConnectorConnectResponse(BaseModel):
    results: Results
