# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    ids: SequenceNotStr[str]
    """List of user IDs to filter by"""

    limit: int
    """Specifies a limit on the number of objects to return, ranging between 1 and 100.

    Defaults to 100.
    """

    offset: int
    """Specifies the number of objects to skip. Defaults to 0."""
