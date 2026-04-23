# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CollectionRetrieveByNameResponse", "Results"]


class Results(BaseModel):
    id: str

    created_at: datetime

    description: Optional[str] = None

    engram_count: int

    graph_collection_status: str

    graph_sync_status: str

    name: str

    owner_id: Optional[str] = None

    updated_at: datetime

    user_count: int

    access_tier: Optional[str] = None

    cache_policy: Optional[str] = None

    chain_type: Optional[str] = None

    contract_address: Optional[str] = None

    creator_royalty_bps: Optional[int] = None

    has_preview_access: Optional[bool] = None

    is_forked: Optional[bool] = None

    marketplace_metadata: Optional[Dict[str, object]] = None

    memory_count: Optional[int] = None

    nft_collection_address: Optional[str] = None

    owner_email: Optional[str] = None

    owner_name: Optional[str] = None

    preview_query_limit: Optional[int] = None

    purchase_price_usd: Optional[str] = None

    rental_price_monthly_usd: Optional[str] = None

    workspace_id: Optional[str] = None


class CollectionRetrieveByNameResponse(BaseModel):
    results: Results
