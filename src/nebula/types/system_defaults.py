# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SystemDefaults"]


class SystemDefaults(BaseModel):
    global_per_min: int

    monthly_limit: int

    route_per_min: Optional[int] = None
