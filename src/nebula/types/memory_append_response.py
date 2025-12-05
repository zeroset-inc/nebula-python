# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias

from .message import Message
from .._models import BaseModel

__all__ = [
    "MemoryAppendResponse",
    "NebulaResultsMessageResponse",
    "NebulaResultsMessageResponseResults",
    "NebulaResultsIngestionResponse",
    "NebulaResultsIngestionResponseResults",
]


class NebulaResultsMessageResponseResults(BaseModel):
    id: str

    message: Message

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
