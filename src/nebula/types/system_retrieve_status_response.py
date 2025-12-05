# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["SystemRetrieveStatusResponse", "Results"]


class Results(BaseModel):
    cpu_usage: float

    memory_usage: float

    start_time: datetime

    uptime_seconds: float


class SystemRetrieveStatusResponse(BaseModel):
    results: Results
