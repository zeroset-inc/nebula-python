# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["APIKeyCreateResponse", "Results"]


class Results(BaseModel):
    api_key: str

    key_id: str

    public_key: str

    name: Optional[str] = None


class APIKeyCreateResponse(BaseModel):
    results: Results
