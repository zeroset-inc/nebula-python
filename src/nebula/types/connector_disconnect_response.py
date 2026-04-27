# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ConnectorDisconnectResponse", "Results", "ResultsWarning"]


class ResultsWarning(BaseModel):
    code: str

    message: str


class Results(BaseModel):
    message: str

    warnings: Optional[List[ResultsWarning]] = None


class ConnectorDisconnectResponse(BaseModel):
    results: Results
