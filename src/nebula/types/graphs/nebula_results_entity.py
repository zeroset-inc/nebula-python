# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .entity import Entity
from ..._models import BaseModel

__all__ = ["NebulaResultsEntity"]


class NebulaResultsEntity(BaseModel):
    results: Entity
    """An entity extracted from a engram."""
