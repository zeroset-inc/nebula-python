# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ChunkUpdateParams"]


class ChunkUpdateParams(TypedDict, total=False):
    body_id: Required[Annotated[str, PropertyInfo(alias="id")]]

    text: Required[str]

    metadata: Optional[Dict[str, object]]
