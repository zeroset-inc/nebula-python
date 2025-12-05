# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import TypedDict

__all__ = ["GenerationConfigParam"]


class GenerationConfigParam(TypedDict, total=False):
    add_generation_kwargs: Optional[Dict[str, object]]

    api_base: Optional[str]

    extended_thinking: bool
    """Flag to enable extended thinking mode (for Anthropic providers)"""

    functions: Optional[Iterable[Dict[str, object]]]

    max_tokens_to_sample: int

    model: Optional[str]

    reasoning_effort: Optional[str]
    """
    Effort level for internal reasoning when extended thinking mode is enabled,
    `low`, `medium`, or `high`.Only applicable to OpenAI providers.
    """

    response_format: Union[Dict[str, object], object, None]

    stream: bool

    temperature: float

    thinking_budget: Optional[int]
    """Token budget for internal reasoning when extended thinking mode is enabled.

    Must be less than max_tokens_to_sample.
    """

    tools: Optional[Iterable[Dict[str, object]]]

    top_p: Optional[float]

    verbosity: Optional[str]
    """Verbosity level for GPT-5 models, controls output token count.

    Options: `low`, `medium`, or `high`. Only applicable to GPT-5 models.
    """
