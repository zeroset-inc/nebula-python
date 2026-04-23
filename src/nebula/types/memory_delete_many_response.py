# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "MemoryDeleteManyResponse",
    "NebulaResultsGenericBooleanResponse",
    "NebulaResultsGenericBooleanResponseResults",
    "BatchDeleteResponse",
    "BatchDeleteResponseResults",
]


class NebulaResultsGenericBooleanResponseResults(BaseModel):
    success: bool


class NebulaResultsGenericBooleanResponse(BaseModel):
    results: NebulaResultsGenericBooleanResponseResults


class BatchDeleteResponseResults(BaseModel):
    failed: List[Dict[str, object]]

    successful: List[str]

    summary: Dict[str, object]


class BatchDeleteResponse(BaseModel):
    message: str

    results: BatchDeleteResponseResults


MemoryDeleteManyResponse: TypeAlias = Union[NebulaResultsGenericBooleanResponse, BatchDeleteResponse]
