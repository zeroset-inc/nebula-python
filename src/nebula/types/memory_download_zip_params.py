# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MemoryDownloadZipParams"]


class MemoryDownloadZipParams(TypedDict, total=False):
    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter engrams created before this date."""

    engram_ids: Optional[SequenceNotStr[str]]
    """List of engram IDs to include in the export.

    If not provided, all accessible engrams will be included.
    """

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter engrams created on or after this date."""
