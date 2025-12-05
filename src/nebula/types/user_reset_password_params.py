# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserResetPasswordParams"]


class UserResetPasswordParams(TypedDict, total=False):
    new_password: Required[str]
    """New password"""

    reset_token: Required[str]
    """Password reset token"""
