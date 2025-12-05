# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["GraphListParams"]


class GraphListParams(TypedDict, total=False):
    collection_ids: SequenceNotStr[str]
    """A list of graph IDs to retrieve. If not provided, all graphs will be returned."""

    limit: int
    """Specifies a limit on the number of objects to return, ranging between 1 and 100.

    Defaults to 100.
    """

    offset: int
    """Specifies the number of objects to skip. Defaults to 0."""
