# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["HealthResponse", "Results"]


class Results(BaseModel):
    message: str

    id: Optional[str] = None

    memory_id: Optional[str] = None


class HealthResponse(BaseModel):
    results: Results
