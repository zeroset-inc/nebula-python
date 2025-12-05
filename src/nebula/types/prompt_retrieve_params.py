# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["PromptRetrieveParams"]


class PromptRetrieveParams(TypedDict, total=False):
    prompt_override: Optional[str]
    """Prompt override"""

    body: Optional[Dict[str, str]]
    """Prompt inputs"""
