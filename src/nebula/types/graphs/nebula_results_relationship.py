# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .relationship import Relationship

__all__ = ["NebulaResultsRelationship"]


class NebulaResultsRelationship(BaseModel):
    results: Relationship
    """A relationship between two entities.

    This is a generic relationship, and can be used to represent any type of
    relationship between any two entities.
    """
