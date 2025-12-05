# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CollectionRetrieveByNameParams"]


class CollectionRetrieveByNameParams(TypedDict, total=False):
    owner_id: Optional[str]
    """(Superuser only) Specify the owner_id to retrieve a collection by name"""
