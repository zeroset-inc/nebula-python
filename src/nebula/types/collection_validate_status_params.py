# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CollectionValidateStatusParams"]


class CollectionValidateStatusParams(TypedDict, total=False):
    force_update: bool
    """Force update to computed status even if already in sync"""
