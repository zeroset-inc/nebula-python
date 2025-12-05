# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["UserRegisterParams"]


class UserRegisterParams(TypedDict, total=False):
    email: Required[str]
    """User's email address"""

    password: Required[str]
    """User's password"""

    bio: Optional[str]
    """The bio for the new user"""

    is_verified: bool
    """Whether to verify the user immediately"""

    name: Optional[str]
    """The name for the new user"""

    profile_picture: Optional[str]
    """Updated user profile picture"""
