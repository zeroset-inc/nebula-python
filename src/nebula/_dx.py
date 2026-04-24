from __future__ import annotations

from typing import Any, cast
from collections.abc import Mapping, Sequence
from typing_extensions import override

import anyio
import httpx

from ._types import Body, Query, Headers, Timeout, NotGiven, omit, not_given
from ._client import Nebula as GeneratedNebula, AsyncNebula as GeneratedAsyncNebula
from ._base_client import DEFAULT_MAX_RETRIES


class Nebula(GeneratedNebula):
    """Nebula's handwritten DevEx facade on top of the Stainless client."""

    def __init__(
        self,
        *,
        api_key: str | None = None,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        http_client: httpx.Client | None = None,
        _strict_response_validation: bool = False,
    ) -> None:
        explicit_auth = api_key is not None or access_token is not None
        api_key, access_token = _normalize_auth(api_key, access_token)
        super().__init__(
            api_key=api_key,
            access_token=access_token,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            default_query=default_query,
            http_client=http_client,
            _strict_response_validation=_strict_response_validation,
        )
        if explicit_auth:
            self.api_key = api_key
            self.access_token = access_token

    @override
    def health(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Any:
        return super().health(
            extra_headers=_without_auth_headers(extra_headers),
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    def store_memory(self, memory: Mapping[str, Any] | None = None, **params: Any) -> str:
        body = _memory_params(memory, params)
        result = _unwrap(self.post("/v1/memories", body=body, cast_to=object))
        return _extract_id(result)

    def store_memories(self, memories: Sequence[Mapping[str, Any]], **options: Any) -> list[str]:
        return [self.store_memory(memory, **options) for memory in memories]

    def get_memory(self, memory_id: str, **options: Any) -> Any:
        return _unwrap(self.memories.retrieve(memory_id, **options))

    def update_memory(self, memory_id: str, **params: Any) -> Any:
        return _unwrap(self.memories.update(memory_id, **params))

    def list_memories(self, collection_ids: str | Sequence[str] | None = None, **params: Any) -> Any:
        if collection_ids is not None:
            params["collection_ids"] = _listify(collection_ids)
        return _unwrap(self.memories.list(**params))

    def search(self, query: str, **params: Any) -> Any:
        return _unwrap(self.memories.search(query=query, **params))

    def delete_memory(self, memory_id: str, **options: Any) -> bool:
        self.memories.delete(memory_id, **options)
        return True

    def delete_memories(self, memory_ids: Sequence[str], **options: Any) -> Any:
        return self.memories.delete_many(body=list(memory_ids), **options)

    @override
    def delete(self, path: str | Sequence[str], **kwargs: Any) -> Any:  # pyright: ignore[reportIncompatibleMethodOverride]
        if isinstance(path, str) and (_is_request_path(path) or "cast_to" in kwargs):
            return super().delete(path, **kwargs)
        if isinstance(path, str):
            return self.delete_memory(path, **kwargs)
        return self.delete_memories(path, **kwargs)


class AsyncNebula(GeneratedAsyncNebula):
    """Async variant of Nebula's handwritten DevEx facade."""

    def __init__(
        self,
        *,
        api_key: str | None = None,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        http_client: httpx.AsyncClient | None = None,
        _strict_response_validation: bool = False,
    ) -> None:
        explicit_auth = api_key is not None or access_token is not None
        api_key, access_token = _normalize_auth(api_key, access_token)
        super().__init__(
            api_key=api_key,
            access_token=access_token,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            default_query=default_query,
            http_client=http_client,
            _strict_response_validation=_strict_response_validation,
        )
        if explicit_auth:
            self.api_key = api_key
            self.access_token = access_token

    @override
    async def health(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Any:
        return await super().health(
            extra_headers=_without_auth_headers(extra_headers),
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    async def store_memory(self, memory: Mapping[str, Any] | None = None, **params: Any) -> str:
        body = _memory_params(memory, params)
        result = _unwrap(await self.post("/v1/memories", body=body, cast_to=object))
        return _extract_id(result)

    async def store_memories(
        self,
        memories: Sequence[Mapping[str, Any]],
        *,
        max_concurrency: int = 8,
        **options: Any,
    ) -> list[str]:
        results: list[str | None] = [None] * len(memories)
        semaphore = anyio.Semaphore(max_concurrency)

        async def worker(index: int, memory: Mapping[str, Any]) -> None:
            async with semaphore:
                results[index] = await self.store_memory(memory, **options)

        async with anyio.create_task_group() as task_group:
            for index, memory in enumerate(memories):
                task_group.start_soon(worker, index, memory)

        return _completed_results(results)

    async def get_memory(self, memory_id: str, **options: Any) -> Any:
        return _unwrap(await self.memories.retrieve(memory_id, **options))

    async def update_memory(self, memory_id: str, **params: Any) -> Any:
        return _unwrap(await self.memories.update(memory_id, **params))

    async def list_memories(self, collection_ids: str | Sequence[str] | None = None, **params: Any) -> Any:
        if collection_ids is not None:
            params["collection_ids"] = _listify(collection_ids)
        return _unwrap(await self.memories.list(**params))

    async def search(self, query: str, **params: Any) -> Any:
        return _unwrap(await self.memories.search(query=query, **params))

    async def delete_memory(self, memory_id: str, **options: Any) -> bool:
        await self.memories.delete(memory_id, **options)
        return True

    async def delete_memories(self, memory_ids: Sequence[str], **options: Any) -> Any:
        return await self.memories.delete_many(body=list(memory_ids), **options)

    @override
    async def delete(self, path: str | Sequence[str], **kwargs: Any) -> Any:  # pyright: ignore[reportIncompatibleMethodOverride]
        if isinstance(path, str) and (_is_request_path(path) or "cast_to" in kwargs):
            return await super().delete(path, **kwargs)
        if isinstance(path, str):
            return await self.delete_memory(path, **kwargs)
        return await self.delete_memories(path, **kwargs)


def _normalize_auth(api_key: str | None, access_token: str | None) -> tuple[str | None, str | None]:
    if api_key and access_token is None and not _looks_like_nebula_api_key(api_key):
        return None, api_key
    return api_key, access_token


def _completed_results(results: Sequence[str | None]) -> list[str]:
    completed: list[str] = []
    for index, result in enumerate(results):
        if result is None:
            raise RuntimeError(f"Nebula memory batch result missing at index {index}")
        completed.append(result)
    return completed


def _without_auth_headers(extra_headers: Headers | None) -> Headers:
    if isinstance(extra_headers, Mapping):
        return {"X-API-Key": omit, "Authorization": omit, **extra_headers}
    return {"X-API-Key": omit, "Authorization": omit}


def _looks_like_nebula_api_key(token: str) -> bool:
    parts = token.split(".", 1)
    if len(parts) != 2:
        return False
    public_part, raw_part = parts
    return bool(raw_part) and (public_part.startswith("key_") or public_part.startswith("neb_"))


def _memory_params(memory: Mapping[str, Any] | None, params: Mapping[str, Any]) -> dict[str, Any]:
    body = dict(memory or {})
    body.update(params)
    if "collectionId" in body and "collection_id" not in body:
        body["collection_id"] = body.pop("collectionId")
    else:
        body.pop("collectionId", None)
    content = body.pop("content", None)
    body.pop("memory_id", None)
    if content is not None:
        if isinstance(content, str):
            body.setdefault("raw_text", content)
        else:
            body.setdefault("content_parts", content)
    if body.get("messages") and not body.get("engram_type"):
        body["engram_type"] = "conversation"
    return body


def _unwrap(response: Any) -> Any:
    mapping = cast("Mapping[str, Any] | None", response if isinstance(response, Mapping) else None)
    if mapping is not None and "results" in mapping:
        return mapping["results"]
    response_obj = cast(Any, response)
    if hasattr(response_obj, "results"):
        return response_obj.results
    return response_obj


def _extract_id(value: Any) -> str:
    value_object = cast(object, value)
    mapping = cast(Mapping[str, Any], value) if isinstance(value, Mapping) else None
    for key in ("id", "memory_id", "ephemeral_collection_id"):
        found = getattr(value_object, key, None)
        if isinstance(found, str):
            return found
        if mapping is not None:
            found = mapping.get(key)
            if isinstance(found, str):
                return found
    raise RuntimeError("Nebula memory create response did not include an id")


def _listify(value: str | Sequence[str]) -> list[str]:
    return [value] if isinstance(value, str) else list(value)


def _is_request_path(value: str) -> bool:
    return value.startswith("/") or value.startswith("http://") or value.startswith("https://")


Client = Nebula
AsyncClient = AsyncNebula
