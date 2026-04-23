# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConnectorUpdateConfigParams"]


class ConnectorUpdateConfigParams(TypedDict, total=False):
    config: Required[Dict[str, object]]

    apply: Literal["full_resync"]
