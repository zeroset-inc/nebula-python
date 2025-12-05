# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["StorageTypeLimit"]


class StorageTypeLimit(BaseModel):
    limit: int

    remaining: int

    used: int
