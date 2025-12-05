# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .graph_response import GraphResponse

__all__ = ["NebulaResultsGraphResponse"]


class NebulaResultsGraphResponse(BaseModel):
    results: GraphResponse
