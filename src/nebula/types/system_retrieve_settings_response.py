# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["SystemRetrieveSettingsResponse", "Results"]


class Results(BaseModel):
    config: Dict[str, object]

    nebula_project_name: str

    prompts: Dict[str, object]


class SystemRetrieveSettingsResponse(BaseModel):
    results: Results
