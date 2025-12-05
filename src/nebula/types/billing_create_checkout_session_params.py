# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["BillingCreateCheckoutSessionParams"]


class BillingCreateCheckoutSessionParams(TypedDict, total=False):
    plan_id: Required[str]

    billing_interval: str

    cancel_url: Optional[str]

    success_url: Optional[str]
