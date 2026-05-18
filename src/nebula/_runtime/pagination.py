from __future__ import annotations

from typing import Any, AsyncIterator, Awaitable, Callable, Generic, Sequence, TypeVar
from typing import TypedDict


T = TypeVar("T")


class OffsetPageEnvelope(TypedDict, Generic[T]):
    results: Sequence[T]
    total_entries: int


async def paginate_offset(
    fetcher: Callable[..., Awaitable[OffsetPageEnvelope[Any]]],
    *,
    page_size: int = 100,
    **kwargs: Any,
) -> AsyncIterator[Any]:
    offset = int(kwargs.pop("offset", 0))
    while True:
        page = await fetcher(offset=offset, limit=page_size, **kwargs)
        results = page["results"]
        for item in results:
            yield item
        if len(results) < page_size:
            return
        if offset + len(results) >= page["total_entries"]:
            return
        offset += len(results)
