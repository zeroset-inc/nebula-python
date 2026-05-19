# Handwritten Nebula DX layer.
#
# Carries only the methods that need real dispatch logic (storeMemory's
# create-vs-append branch, polymorphic delete, auth normalization). The
# simple unwrap/passthrough methods (get_memory, list_collections,
# export_snapshot, ...) are generated from
# `nebula-sdks/config/dx-extensions.yaml` into `_dx_generated.py`, which
# this class extends via NebulaDX.
#
# Source of truth: nebula-sdks/custom/python/_dx.py
# The generator copies this file into sdks/python/src/nebula/_dx.py on every
# `bun run generate`. Edit the source, not the copy.

from __future__ import annotations

import asyncio
import json
from collections.abc import Mapping, Sequence
from typing import Any, Optional, cast

from ._client import NebulaClient as GeneratedNebula
from ._dx_generated import NebulaDX
from ._runtime import ClientOptions


class Nebula(NebulaDX):
    """Nebula's handwritten DevEx facade on top of the generated async client."""

    def __init__(self, options: Optional[ClientOptions] = None, **compat: Any) -> None:
        """
        Accepts either a ClientOptions instance, or keyword aliases like:
          api_key, apiKey
          access_token, accessToken, bearer_token, bearerToken
          base_url, baseUrl
        """
        if options is None:
            options = ClientOptions()

        api_key = _first_defined(compat.get("api_key"), compat.get("apiKey"), options.api_key)
        bearer_token = _first_defined(
            compat.get("access_token"),
            compat.get("accessToken"),
            compat.get("bearer_token"),
            compat.get("bearerToken"),
            options.bearer_token,
        )
        base_url = _first_defined(compat.get("base_url"), compat.get("baseUrl"), options.base_url)

        api_key, bearer_token = _normalize_auth(api_key, bearer_token)

        normalized = ClientOptions(
            base_url=base_url if base_url is not None else options.base_url,
            api_key=api_key,
            bearer_token=bearer_token,
            default_headers=options.default_headers,
            timeout_seconds=options.timeout_seconds,
            retry=options.retry,
            user_agent=options.user_agent,
            transport=options.transport,
        )
        super().__init__(normalized)

    # ---- memories ----

    async def store_memory(
        self,
        memory: Optional[Mapping[str, Any]] = None,
        **params: Any,
    ) -> Any:
        """
        Polymorphic memory creator: dispatches to memories.create or memories.append
        based on whether `memory_id` is set on the input. Returns the new memory id
        (string), or the updated snapshot envelope when `snapshot` is set.
        """
        body = _memory_params(memory, params)
        memory_id = _memory_id(body)

        if body.get("snapshot") is not None:
            response = await self.memories.create(body=cast(Any, _snapshot_create_params(body)))
            result = _unwrap(response)
            return _snapshot_result(result)

        if memory_id:
            await self.memories.append(
                id=str(memory_id),
                body=cast(Any, _memory_append_params(body)),
            )
            return str(memory_id)

        response = await self.memories.create(body=cast(Any, _memory_create_params(body)))
        result = _unwrap(response)
        return _extract_id(result)

    async def store_memories(
        self,
        memories: Sequence[Mapping[str, Any]],
        *,
        max_concurrency: int = 8,
        **options: Any,
    ) -> list[Any]:
        semaphore = asyncio.Semaphore(max_concurrency)

        async def worker(memory: Mapping[str, Any]) -> Any:
            async with semaphore:
                return await self.store_memory(memory, **options)

        return await asyncio.gather(*(worker(memory) for memory in memories))

    # ---- memories ----

    async def list_memories(
        self,
        collection_ids: Optional[str | Sequence[str]] = None,
        **params: Any,
    ) -> Any:
        """Override of generated list_memories to add the
        collection_ids-as-str-or-list shortcut + metadata_filters JSON
        encoding. The simple generated form is replaced by this richer one.
        """
        if collection_ids is not None:
            params["collection_ids"] = _listify(collection_ids)
        if isinstance(params.get("metadata_filters"), Mapping):
            params["metadata_filters"] = json.dumps(params["metadata_filters"])
        return _unwrap(await self.memories.list(**params))

    async def search(self, query: Optional[str] = None, **params: Any) -> Any:
        """Memory search shortcut: takes an optional query string plus
        arbitrary search params. Kept handwritten so callers can do
        `client.search("hello")` without constructing a body dict."""
        body: dict[str, Any] = {}
        if query is not None:
            body["query"] = query
        body.update(params)
        return _unwrap(await self.memories.search(body=cast(Any, body)))

    # ---- collections ----

    async def delete_collection(self, collection_id: str) -> bool:
        """Override of generated delete_collection to coerce the response
        {success: bool} envelope into a Python bool return."""
        result = _unwrap(await self.collections.delete(id=collection_id))
        return bool(_extract_value(result, "success"))

    # Legacy aliases — "cluster" was the old name for "collection".
    async def create_cluster(self, **params: Any) -> Any:
        return await self.create_collection(**params)

    async def get_cluster(self, collection_id: str) -> Any:
        return await self.get_collection(collection_id)

    async def get_cluster_by_name(self, name: str) -> Any:
        return await self.get_collection_by_name(name)

    async def list_clusters(self, **params: Any) -> Any:
        return await self.list_collections(**params)

    async def update_cluster(self, collection_id: str, **params: Any) -> Any:
        return await self.update_collection(collection_id, **params)

    async def delete_cluster(self, collection_id: str) -> bool:
        return await self.delete_collection(collection_id)

    # ---- connectors ----

    async def connect_provider(
        self,
        provider: str,
        collection_id: str,
        config: Optional[Mapping[str, Any]] = None,
    ) -> Any:
        """Custom signature: positional provider + collection_id + optional
        config dict, packed into the wire body shape."""
        body: dict[str, Any] = {"collection_id": collection_id}
        if config is not None:
            body["config"] = dict(config)
        return _unwrap(await self.connectors.connect(provider=provider, body=cast(Any, body)))

    async def disconnect(
        self,
        connection_id: str,
        delete_memories: bool = False,
    ) -> Any:
        """Disconnect a connector by id. Positional shortcut; unwraps results."""
        return _unwrap(
            await self.connectors.disconnect(
                connection_id=connection_id, delete_memories=delete_memories
            )
        )

    # ---- delete dispatch ----

    async def delete_memory(self, memory_id: str) -> bool:
        await self.memories.delete(id=memory_id)
        return True

    async def delete_memories(self, memory_ids: Sequence[str]) -> Any:
        return await self.memories.delete_many(body=cast(Any, list(memory_ids)))

    async def delete(self, path_or_ids: str | Sequence[str]) -> Any:
        """
        Polymorphic delete:
          - delete("memory-id")          -> delete_memory
          - delete(["id1", "id2"])       -> delete_memories
          - delete("/some/path")         -> NotImplemented (escape hatch)
        """
        if isinstance(path_or_ids, str) and _is_request_path(path_or_ids):
            raise NotImplementedError(
                f'delete("{path_or_ids}") raw-path escape hatch is not implemented in this SDK yet'
            )
        if isinstance(path_or_ids, str):
            return await self.delete_memory(path_or_ids)
        return await self.delete_memories(path_or_ids)


# ---------- helpers ----------


def _normalize_auth(
    api_key: Optional[str], bearer_token: Optional[str]
) -> tuple[Optional[str], Optional[str]]:
    if api_key and bearer_token is None and not _looks_like_nebula_api_key(api_key):
        return None, api_key
    return api_key, bearer_token


def _first_defined(*values: Optional[Any]) -> Optional[Any]:
    for value in values:
        if value is not None:
            return value
    return None


def _looks_like_nebula_api_key(token: str) -> bool:
    parts = token.split(".", 1)
    if len(parts) != 2:
        return False
    public_part, raw_part = parts
    return bool(raw_part) and (
        public_part.startswith("key_") or public_part.startswith("neb_")
    )


def _memory_params(
    memory: Optional[Mapping[str, Any]], params: Mapping[str, Any]
) -> dict[str, Any]:
    body: dict[str, Any] = dict(memory or {})
    body.update(params)
    if "collectionId" in body and "collection_id" not in body:
        body["collection_id"] = body.pop("collectionId")
    else:
        body.pop("collectionId", None)
    if "memoryId" in body and "memory_id" not in body:
        body["memory_id"] = body.pop("memoryId")
    else:
        body.pop("memoryId", None)
    content = body.pop("content", None)
    if content is not None:
        if isinstance(content, str):
            body.setdefault("raw_text", content)
        else:
            body.setdefault("content_parts", content)
    if body.get("messages") and not body.get("engram_type"):
        body["engram_type"] = "conversation"
    return body


def _memory_id(memory: Mapping[str, Any]) -> Any:
    return memory.get("memory_id") or memory.get("memoryId")


def _memory_create_params(body: Mapping[str, Any]) -> dict[str, Any]:
    params = dict(body)
    params.pop("memory_id", None)
    return params


def _snapshot_create_params(body: Mapping[str, Any]) -> dict[str, Any]:
    params: dict[str, Any] = {"snapshot": body["snapshot"]}
    if isinstance(body.get("raw_text"), str):
        params["raw_text"] = body["raw_text"]
    if isinstance(body.get("contents"), list):
        params["contents"] = body["contents"]
    return params


def _memory_append_params(body: Mapping[str, Any]) -> dict[str, Any]:
    collection_id = body.get("collection_id")
    if not collection_id:
        raise ValueError(
            "collection_id is required when appending to an existing memory"
        )
    params: dict[str, Any] = {"collection_id": collection_id}
    for key in (
        "metadata",
        "ingestion_config",
        "ingestion_mode",
        "raw_text",
        "chunks",
        "messages",
    ):
        if body.get(key) is not None:
            params[key] = body[key]
    return params


def _unwrap(response: Any) -> Any:
    if isinstance(response, Mapping) and "results" in response:
        return response["results"]
    if hasattr(response, "results"):
        return response.results
    return response


def _extract_value(obj: Any, name: str, default: Any = None) -> Any:
    if isinstance(obj, Mapping):
        return obj.get(name, default)
    return getattr(obj, name, default)


def _snapshot_result(value: Any) -> Any:
    return _extract_value(value, "snapshot", value)


def _extract_id(value: Any) -> str:
    mapping = value if isinstance(value, Mapping) else None
    for key in ("id", "memory_id", "engram_id", "ephemeral_collection_id"):
        attr = getattr(value, key, None)
        if isinstance(attr, str):
            return attr
        if mapping is not None:
            mapped = mapping.get(key)
            if isinstance(mapped, str):
                return mapped
    raise RuntimeError("Nebula memory create response did not include an id")


def _listify(value: str | Sequence[str]) -> list[str]:
    return [value] if isinstance(value, str) else list(value)


def _is_request_path(value: str) -> bool:
    return (
        value.startswith("/")
        or value.startswith("http://")
        or value.startswith("https://")
    )


# Convenience alias (Stainless ships `Client = Nebula`).
Client = Nebula
