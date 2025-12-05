# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .token import Token
from .._models import BaseModel

__all__ = ["TokenResponse", "Results"]


class Results(BaseModel):
    access_token: Token

    refresh_token: Token


class TokenResponse(BaseModel):
    results: Results
