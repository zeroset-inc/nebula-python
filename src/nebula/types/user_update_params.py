# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    bio: Optional[str]
    """Updated user bio"""

    email: Optional[str]
    """Updated email address"""

    is_superuser: Optional[bool]
    """Updated superuser status"""

    limits_overrides: Dict[str, object]
    """Updated limits overrides"""

    metadata: Optional[Dict[str, Optional[str]]]

    name: Optional[str]
    """Updated user name"""

    profile_picture: Optional[str]
    """Updated profile picture URL"""
