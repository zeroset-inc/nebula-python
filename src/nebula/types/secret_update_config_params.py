# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SecretUpdateConfigParams"]


class SecretUpdateConfigParams(TypedDict, total=False):
    auto_rotation_enabled: Optional[bool]

    rotation_interval_days: Optional[int]

    secret_key: str
