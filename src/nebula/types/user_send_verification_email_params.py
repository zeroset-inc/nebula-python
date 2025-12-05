# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserSendVerificationEmailParams"]


class UserSendVerificationEmailParams(TypedDict, total=False):
    body: Required[str]
    """User's email address"""
