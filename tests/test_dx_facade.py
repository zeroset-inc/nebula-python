from __future__ import annotations

from unittest.mock import Mock, AsyncMock

import pytest

import nebula
from nebula import Nebula, AsyncNebula


def test_store_memory_returns_snapshot_result() -> None:
    client = Nebula(api_key="key_public.secret", access_token="token")
    snapshot = {"collection_id": "collection-123", "root_hash": "root-123"}
    client.memories.create = Mock(return_value={"results": {"snapshot": snapshot}})  # type: ignore[method-assign]

    assert client.store_memory({"snapshot": snapshot, "content": "remember this"}) == snapshot


def test_store_memory_appends_when_memory_id_is_provided() -> None:
    client = Nebula(api_key="key_public.secret", access_token="token")
    client.memories.append = Mock(return_value={"results": {"success": True}})  # type: ignore[method-assign]

    assert (
        client.store_memory(
            {
                "collection_id": "collection-123",
                "memory_id": "memory-123",
                "content": "additional context",
            }
        )
        == "memory-123"
    )
    client.memories.append.assert_called_once_with(  # type: ignore[attr-defined]
        "memory-123",
        collection_id="collection-123",
        raw_text="additional context",
    )


def test_store_memory_extracts_legacy_id_fields() -> None:
    client = Nebula(api_key="key_public.secret", access_token="token")
    client.memories.create = Mock(return_value={"results": {"engram_id": "engram-123"}})  # type: ignore[method-assign]

    assert client.store_memory({"collection_id": "collection-123", "content": "remember this"}) == "engram-123"


def test_top_level_type_exports_are_available() -> None:
    assert nebula.MemoryCreateResponse is nebula.types.MemoryCreateResponse


@pytest.mark.asyncio
async def test_async_store_memory_appends_when_memory_id_is_provided() -> None:
    client = AsyncNebula(api_key="key_public.secret", access_token="token")
    client.memories.append = AsyncMock(return_value={"results": {"success": True}})  # type: ignore[method-assign]

    assert (
        await client.store_memory(
            {
                "collection_id": "collection-123",
                "memory_id": "memory-123",
                "content": "additional context",
            }
        )
        == "memory-123"
    )
    client.memories.append.assert_awaited_once_with(  # type: ignore[attr-defined]
        "memory-123",
        collection_id="collection-123",
        raw_text="additional context",
    )
