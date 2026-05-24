from __future__ import annotations

from typing import Any

import httpx
import pytest

from nebula import Nebula, NebulaClient, ClientOptions
from nebula._dx import _looks_like_nebula_api_key


def _make_dx(transport: httpx.MockTransport, **overrides: Any) -> Nebula:
    options = ClientOptions(
        base_url=overrides.pop("base_url", "https://api.example.com"),
        api_key=overrides.pop("api_key", None),
        bearer_token=overrides.pop("bearer_token", None),
        transport=transport,
        **overrides,
    )
    return Nebula(options)


@pytest.mark.asyncio
async def test_nebula_extends_nebula_client() -> None:
    transport = httpx.MockTransport(lambda _r: httpx.Response(204))
    client = _make_dx(transport)
    assert isinstance(client, NebulaClient)
    assert client.memories is not None
    assert client.collections is not None


@pytest.mark.asyncio
async def test_store_memory_create_dispatches_to_create() -> None:
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"results": {"id": "mem_new"}})

    async with _make_dx(httpx.MockTransport(handler)) as client:
        new_id = await client.store_memory(collection_id="c1", raw_text="hi")
    assert new_id == "mem_new"
    assert captured[0].method == "POST"
    assert str(captured[0].url) == "https://api.example.com/v1/memories"
    import json
    body = json.loads(captured[0].content)
    assert body["collection_id"] == "c1"
    assert body["raw_text"] == "hi"


@pytest.mark.asyncio
async def test_store_memory_append_dispatches_when_memory_id_set() -> None:
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"results": {"id": "appended"}})

    async with _make_dx(httpx.MockTransport(handler)) as client:
        result = await client.store_memory(
            {"memory_id": "mem_existing", "collection_id": "c1", "raw_text": "more"}
        )
    assert result == "mem_existing"
    assert str(captured[0].url) == "https://api.example.com/v1/memories/mem_existing/append"


@pytest.mark.asyncio
async def test_store_memory_content_string_maps_to_raw_text() -> None:
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"results": {"id": "x"}})

    async with _make_dx(httpx.MockTransport(handler)) as client:
        await client.store_memory(collection_id="c1", content="shorthand")
    import json
    body = json.loads(captured[0].content)
    assert body["raw_text"] == "shorthand"
    assert "content" not in body


@pytest.mark.asyncio
async def test_store_memory_messages_sets_kind_conversation() -> None:
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"results": {"id": "mem_conv"}})

    async with _make_dx(httpx.MockTransport(handler)) as client:
        await client.store_memory(
            collection_id="c1",
            messages=[{"role": "user", "content": "hi"}],
        )
    import json
    body = json.loads(captured[0].content)
    assert body["kind"] == "conversation"
    assert "engram_type" not in body


@pytest.mark.asyncio
async def test_search_unwraps_results() -> None:
    def handler(_req: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"results": {"hits": [{"id": "1"}]}})

    async with _make_dx(httpx.MockTransport(handler)) as client:
        result = await client.search("find me")
    assert result == {"hits": [{"id": "1"}]}


@pytest.mark.asyncio
async def test_delete_string_calls_memories_delete() -> None:
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(204)

    async with _make_dx(httpx.MockTransport(handler)) as client:
        ok = await client.delete("mem_to_delete")
    assert ok is True
    assert captured[0].method == "DELETE"
    assert str(captured[0].url) == "https://api.example.com/v1/memories/mem_to_delete"


@pytest.mark.asyncio
async def test_delete_list_calls_delete_many() -> None:
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"results": {"succeeded": 2}})

    async with _make_dx(httpx.MockTransport(handler)) as client:
        await client.delete(["a", "b"])
    assert captured[0].method == "POST"
    assert str(captured[0].url) == "https://api.example.com/v1/memories/delete"
    import json
    body = json.loads(captured[0].content)
    assert body == ["a", "b"]


def test_looks_like_nebula_api_key_prefix_detection() -> None:
    assert _looks_like_nebula_api_key("key_abc.def") is True
    assert _looks_like_nebula_api_key("neb_xyz.123") is True
    assert _looks_like_nebula_api_key("eyJhbGciOiJIUzI1NiJ9") is False
    assert _looks_like_nebula_api_key("key_abc") is False


@pytest.mark.asyncio
async def test_compat_api_key_alias_via_init_kwargs() -> None:
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"results": {}})

    transport = httpx.MockTransport(handler)
    client = Nebula(
        ClientOptions(base_url="https://api.example.com", transport=transport),
        api_key="key_real.token",
    )
    try:
        await client.get_memory("m1")
    finally:
        await client.aclose()

    assert captured[0].headers.get("x-api-key") == "key_real.token"
    assert "authorization" not in captured[0].headers


@pytest.mark.asyncio
async def test_auth_normalization_non_keyshape_routes_to_bearer() -> None:
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"results": {}})

    transport = httpx.MockTransport(handler)
    client = Nebula(
        ClientOptions(
            base_url="https://api.example.com",
            api_key="eyJhbGciOiJIUzI1NiJ9.opaquebearer",
            transport=transport,
        ),
    )
    try:
        await client.get_memory("m1")
    finally:
        await client.aclose()

    assert captured[0].headers.get("authorization") == "Bearer eyJhbGciOiJIUzI1NiJ9.opaquebearer"
    assert "x-api-key" not in captured[0].headers


@pytest.mark.asyncio
async def test_delete_collection_coerces_to_bool() -> None:
    def handler(_req: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"results": {"success": True}})

    async with _make_dx(httpx.MockTransport(handler)) as client:
        ok = await client.delete_collection("c1")
    assert ok is True


@pytest.mark.asyncio
async def test_list_memories_string_becomes_collection_ids() -> None:
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"results": [], "total_entries": 0})

    async with _make_dx(httpx.MockTransport(handler)) as client:
        await client.list_memories("collection-abc")
    assert "collection_ids=collection-abc" in str(captured[0].url)


@pytest.mark.asyncio
async def test_legacy_cluster_aliases_delegate_to_collection() -> None:
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"results": {"id": "c1", "name": "X"}})

    async with _make_dx(httpx.MockTransport(handler)) as client:
        await client.get_cluster("c1")
    assert str(captured[0].url) == "https://api.example.com/v1/collections/c1"


@pytest.mark.asyncio
async def test_get_cluster_by_name_forwards_collection_name() -> None:
    """Regression: get_cluster_by_name(name) used to pass `name` positionally
    into the kwargs-only generated method, raising TypeError."""
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"results": {"id": "c1", "name": "alpha"}})

    async with _make_dx(httpx.MockTransport(handler)) as client:
        await client.get_cluster_by_name("alpha")
    assert str(captured[0].url) == "https://api.example.com/v1/collections/name/alpha"


@pytest.mark.asyncio
async def test_update_cluster_forwards_id_and_body() -> None:
    """Regression: update_cluster(collection_id, **params) used to pass
    `collection_id` positionally into the kwargs-only generated method,
    raising TypeError."""
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(
            200, json={"results": {"id": "c1", "name": "renamed"}}
        )

    async with _make_dx(httpx.MockTransport(handler)) as client:
        await client.update_cluster("c1", body={"name": "renamed"})
    assert str(captured[0].url) == "https://api.example.com/v1/collections/c1"
    assert captured[0].method == "POST"
    import json
    body = json.loads(captured[0].content)
    assert body == {"name": "renamed"}
