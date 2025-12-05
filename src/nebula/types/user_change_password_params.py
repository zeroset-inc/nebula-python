# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserChangePasswordParams"]


class UserChangePasswordParams(TypedDict, total=False):
    current_password: Required[str]
    """Current password"""

    new_password: Required[str]
    """New password"""
