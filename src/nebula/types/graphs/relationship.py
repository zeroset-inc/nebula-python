# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Union, Optional

from ..._models import BaseModel

__all__ = ["Relationship"]


class Relationship(BaseModel):
    """A relationship between two entities.

    This is a generic relationship, and can be used to represent any type of
    relationship between any two entities.
    """

    object: str

    predicate: str

    subject: str

    id: Optional[str] = None

    attributes: Optional[Dict[str, builtins.object]] = None

    category: Optional[str] = None

    chunk_ids: Optional[List[str]] = None

    collection_id: Optional[str] = None

    description: Optional[str] = None

    description_embedding: Optional[List[float]] = None

    engram_id: Optional[str] = None

    inference_metadata: Optional[Dict[str, builtins.object]] = None

    is_derived: Optional[bool] = None

    metadata: Optional[Dict[str, builtins.object]] = None

    object_id: Optional[str] = None

    occurrence_index: Optional[int] = None

    parent_relationship_id: Optional[int] = None

    recurrence_rule: Union[Dict[str, builtins.object], str, None] = None

    relationship_type: Optional[str] = None

    subject_id: Optional[str] = None

    temporal_precision: Optional[str] = None

    valid_span: Optional[builtins.object] = None

    weight: Optional[float] = None
