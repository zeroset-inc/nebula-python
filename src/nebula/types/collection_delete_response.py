# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CollectionDeleteResponse", "Results"]


class Results(BaseModel):
    success: bool


class CollectionDeleteResponse(BaseModel):
    results: Results
