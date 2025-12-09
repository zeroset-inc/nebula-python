# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SecretRotateResponse"]


class SecretRotateResponse(BaseModel):
    """Response model for secret rotation"""

    message: str

    success: bool

    next_rotation_at: Optional[datetime] = None

    version: Optional[int] = None
