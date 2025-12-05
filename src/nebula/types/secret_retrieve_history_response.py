# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["SecretRetrieveHistoryResponse"]


class SecretRetrieveHistoryResponse(BaseModel):
    history: List[Dict[str, object]]

    total_rotations: int
