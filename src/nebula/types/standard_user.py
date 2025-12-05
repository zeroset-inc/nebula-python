# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["StandardUser"]


class StandardUser(BaseModel):
    id: str

    email: str

    account_type: Optional[str] = None

    bio: Optional[str] = None

    collection_ids: Optional[List[str]] = None

    created_at: Optional[datetime] = None

    current_plan_id: Optional[str] = None

    engram_ids: Optional[List[str]] = None

    github_id: Optional[str] = None

    google_id: Optional[str] = None

    graph_ids: Optional[List[str]] = None

    hashed_password: Optional[str] = None

    is_active: Optional[bool] = None

    is_superuser: Optional[bool] = None

    is_verified: Optional[bool] = None

    limits_overrides: Optional[Dict[str, object]] = None

    metadata: Optional[Dict[str, object]] = None

    name: Optional[str] = None

    num_files: Optional[int] = None

    profile_picture: Optional[str] = None

    stripe_customer_id: Optional[str] = None

    subscription_end_date: Optional[datetime] = None

    subscription_start_date: Optional[datetime] = None

    subscription_status: Optional[str] = None

    total_size_in_bytes: Optional[int] = None

    updated_at: Optional[datetime] = None

    verification_code_expiry: Optional[datetime] = None

    wallet_address: Optional[str] = None

    wallet_type: Optional[str] = None
