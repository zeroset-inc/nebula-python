# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime

from .._models import BaseModel

__all__ = ["PromptResponse"]


class PromptResponse(BaseModel):
    id: str

    created_at: datetime

    input_types: Dict[str, str]

    name: str

    template: str

    updated_at: datetime
