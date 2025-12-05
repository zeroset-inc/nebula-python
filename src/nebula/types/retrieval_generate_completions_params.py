# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .message_param import MessageParam
from .generation_config_param import GenerationConfigParam

__all__ = ["RetrievalGenerateCompletionsParams"]


class RetrievalGenerateCompletionsParams(TypedDict, total=False):
    messages: Required[Iterable[MessageParam]]
    """List of messages to generate completion for"""

    response_model: object

    generation_config: GenerationConfigParam
    """Configuration for text generation"""
