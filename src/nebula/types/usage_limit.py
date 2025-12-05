# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["UsageLimit"]


class UsageLimit(BaseModel):
    limit: int

    remaining: int

    used: int
