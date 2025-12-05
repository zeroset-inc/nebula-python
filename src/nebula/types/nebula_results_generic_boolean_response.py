# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["NebulaResultsGenericBooleanResponse", "Results"]


class Results(BaseModel):
    success: bool


class NebulaResultsGenericBooleanResponse(BaseModel):
    results: Results
