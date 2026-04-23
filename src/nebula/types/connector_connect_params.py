# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ConnectorConnectParams"]


class ConnectorConnectParams(TypedDict, total=False):
    collection_id: Required[str]

    config: Optional[Dict[str, object]]
