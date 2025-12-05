# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import TypeAlias

from .._models import BaseModel
from .nebula_results_generic_boolean_response import NebulaResultsGenericBooleanResponse

__all__ = ["MemoryDeleteMultipleResponse", "BatchDeleteResponse", "BatchDeleteResponseResults"]


class BatchDeleteResponseResults(BaseModel):
    failed: List[Dict[str, object]]

    successful: List[str]

    summary: Dict[str, object]


class BatchDeleteResponse(BaseModel):
    message: str

    results: BatchDeleteResponseResults


MemoryDeleteMultipleResponse: TypeAlias = Union[NebulaResultsGenericBooleanResponse, BatchDeleteResponse]
