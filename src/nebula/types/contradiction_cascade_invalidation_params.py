# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ContradictionCascadeInvalidationParams"]


class ContradictionCascadeInvalidationParams(TypedDict, total=False):
    max_depth: int

    min_confidence_threshold: float
