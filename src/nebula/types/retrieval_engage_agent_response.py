# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .message import Message
from .._models import BaseModel

__all__ = ["RetrievalEngageAgentResponse", "Results"]


class Results(BaseModel):
    conversation_id: str
    """The conversation ID for the RAG agent response"""

    messages: List[Message]
    """Agent response messages"""


class RetrievalEngageAgentResponse(BaseModel):
    results: Results
