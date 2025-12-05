# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CentralityComputeParams"]


class CentralityComputeParams(TypedDict, total=False):
    body: Optional[bool]
    """
    If true, returns immediately and runs computation in background (not yet
    implemented)
    """
