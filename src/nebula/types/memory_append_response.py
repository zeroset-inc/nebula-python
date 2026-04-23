# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "MemoryAppendResponse",
    "NebulaResultsMessageResponse",
    "NebulaResultsMessageResponseResults",
    "NebulaResultsMessageResponseResultsMessage",
    "NebulaResultsIngestionResponse",
    "NebulaResultsIngestionResponseResults",
]


class NebulaResultsMessageResponseResultsMessage(BaseModel):
    role: Union[Literal["system", "user", "assistant", "function", "tool"], str]

    content: Optional[object] = None

    function_call: Optional[Dict[str, object]] = None

    image_data: Optional[Dict[str, str]] = None

    image_url: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    name: Optional[str] = None

    structured_content: Optional[List[Dict[str, object]]] = None

    tool_call_id: Optional[str] = None

    tool_calls: Optional[List[Dict[str, object]]] = None


class NebulaResultsMessageResponseResults(BaseModel):
    id: str

    message: NebulaResultsMessageResponseResultsMessage

    metadata: Optional[Dict[str, object]] = None


class NebulaResultsMessageResponse(BaseModel):
    results: NebulaResultsMessageResponseResults


class NebulaResultsIngestionResponseResults(BaseModel):
    engram_id: str
    """The ID of the engram that was ingested."""

    message: str
    """A message describing the result of the ingestion request."""

    task_id: Optional[str] = None
    """The task ID of the ingestion request."""


class NebulaResultsIngestionResponse(BaseModel):
    results: NebulaResultsIngestionResponseResults


MemoryAppendResponse: TypeAlias = Union[NebulaResultsMessageResponse, NebulaResultsIngestionResponse]
