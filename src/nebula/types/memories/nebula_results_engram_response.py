# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .engram_response import EngramResponse

__all__ = ["NebulaResultsEngramResponse"]


class NebulaResultsEngramResponse(BaseModel):
    results: EngramResponse
    """Base class for engram information handling."""
