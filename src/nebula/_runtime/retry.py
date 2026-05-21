from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class RetryPolicy:
    max_retries: int = 2
    base_seconds: float = 0.25
    max_seconds: float = 8.0


DEFAULT_RETRY = RetryPolicy()

_RETRYABLE_STATUSES: frozenset[int] = frozenset({408, 429, 502, 503, 504})


def is_retryable_status(status: int) -> bool:
    return status in _RETRYABLE_STATUSES


def backoff_seconds(
    attempt: int, policy: RetryPolicy, retry_after: Optional[float] = None
) -> float:
    if retry_after is not None:
        return min(retry_after, policy.max_seconds)
    cap = min(policy.base_seconds * (2 ** attempt), policy.max_seconds)
    return random.uniform(0, cap)
