# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SecretRotateParams"]


class SecretRotateParams(TypedDict, total=False):
    notify_external: bool

    reason: str

    secret_key: str
