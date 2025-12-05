# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .community import Community

__all__ = ["NebulaResultsCommunity"]


class NebulaResultsCommunity(BaseModel):
    results: Community
