# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["RelationshipExportParams"]


class RelationshipExportParams(TypedDict, total=False):
    columns: Optional[SequenceNotStr[str]]
    """Specific columns to export"""

    filters: Optional[Dict[str, object]]
    """Filters to apply to the export"""

    include_header: Optional[bool]
    """Whether to include column headers"""
