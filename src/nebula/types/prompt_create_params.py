# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["PromptCreateParams"]


class PromptCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the prompt"""

    template: Required[str]
    """The template string for the prompt"""

    input_types: Dict[str, str]
    """A dictionary mapping input names to their types"""
