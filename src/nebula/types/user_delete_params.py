# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UserDeleteParams"]


class UserDeleteParams(TypedDict, total=False):
    delete_vector_data: Optional[bool]
    """Whether to delete the user's vector data"""

    password: Optional[str]
    """User's current password"""
