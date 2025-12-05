# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel
from .usage_limit import UsageLimit
from .system_defaults import SystemDefaults
from .storage_type_limit import StorageTypeLimit

__all__ = ["UserFetchLimitsResponse", "Results", "ResultsStorageLimits", "ResultsUsage", "ResultsUsageRoutes"]


class ResultsStorageLimits(BaseModel):
    chunks: StorageTypeLimit

    collections: StorageTypeLimit

    engrams: StorageTypeLimit


class ResultsUsageRoutes(BaseModel):
    monthly_limit: UsageLimit

    route_per_min: UsageLimit


class ResultsUsage(BaseModel):
    global_per_min: UsageLimit

    monthly_limit: UsageLimit

    routes: Dict[str, ResultsUsageRoutes]


class Results(BaseModel):
    effective_limits: SystemDefaults

    storage_limits: ResultsStorageLimits

    system_defaults: SystemDefaults

    usage: ResultsUsage

    user_overrides: Dict[str, object]


class UserFetchLimitsResponse(BaseModel):
    results: Results
