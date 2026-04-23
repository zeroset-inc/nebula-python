# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MemoryDeleteResponse", "Results"]


class Results(BaseModel):
    success: bool


class MemoryDeleteResponse(BaseModel):
    results: Results
