# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .standard_user import StandardUser

__all__ = ["NebulaResultsUser"]


class NebulaResultsUser(BaseModel):
    results: StandardUser
