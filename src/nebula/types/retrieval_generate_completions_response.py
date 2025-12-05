# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "RetrievalGenerateCompletionsResponse",
    "Results",
    "ResultsChoice",
    "ResultsChoiceMessage",
    "ResultsChoiceMessageFunctionCall",
    "ResultsChoiceMessageToolCall",
    "ResultsChoiceMessageToolCallFunction",
]


class ResultsChoiceMessageFunctionCall(BaseModel):
    arguments: str

    name: str


class ResultsChoiceMessageToolCallFunction(BaseModel):
    arguments: str

    name: str


class ResultsChoiceMessageToolCall(BaseModel):
    id: str

    function: ResultsChoiceMessageToolCallFunction

    type: Literal["function"]


class ResultsChoiceMessage(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None

    function_call: Optional[ResultsChoiceMessageFunctionCall] = None

    refusal: Optional[str] = None

    structured_content: Optional[List[Dict[str, object]]] = None

    tool_calls: Optional[List[ResultsChoiceMessageToolCall]] = None


class ResultsChoice(BaseModel):
    index: int

    message: ResultsChoiceMessage

    finish_reason: Optional[
        Literal["stop", "length", "tool_calls", "content_filter", "function_call", "max_tokens"]
    ] = None


class Results(BaseModel):
    id: str

    model: str

    object: Literal["chat.completion", "response"]

    choices: Optional[List[ResultsChoice]] = None

    created: Optional[int] = None

    created_at: Optional[int] = None

    metadata: Optional[Dict[str, builtins.object]] = None

    output: Optional[List[builtins.object]] = None

    reasoning: Optional[Dict[str, builtins.object]] = None

    service_tier: Optional[Literal["auto", "default", "scale", "flex", "priority"]] = None

    status: Optional[str] = None

    system_fingerprint: Optional[str] = None

    usage: Optional[builtins.object] = None


class RetrievalGenerateCompletionsResponse(BaseModel):
    results: Results
