# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types import (
    ChunkSearchResponse,
    NebulaResultsChunkResponse,
    NebulaResultsGenericBooleanResponse,
    PaginatedNebulaResultListChunkResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChunks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Nebula) -> None:
        chunk = client.chunks.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Nebula) -> None:
        response = client.chunks.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chunk = response.parse()
        assert_matches_type(NebulaResultsChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Nebula) -> None:
        with client.chunks.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chunk = response.parse()
            assert_matches_type(NebulaResultsChunkResponse, chunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.chunks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Nebula) -> None:
        chunk = client.chunks.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )
        assert_matches_type(NebulaResultsChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Nebula) -> None:
        chunk = client.chunks.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            metadata={"foo": "bar"},
        )
        assert_matches_type(NebulaResultsChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Nebula) -> None:
        response = client.chunks.with_raw_response.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chunk = response.parse()
        assert_matches_type(NebulaResultsChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Nebula) -> None:
        with client.chunks.with_streaming_response.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chunk = response.parse()
            assert_matches_type(NebulaResultsChunkResponse, chunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.chunks.with_raw_response.update(
                path_id="",
                body_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                text="text",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Nebula) -> None:
        chunk = client.chunks.list()
        assert_matches_type(PaginatedNebulaResultListChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Nebula) -> None:
        chunk = client.chunks.list(
            include_vectors=True,
            limit=1,
            metadata_filter="metadata_filter",
            offset=0,
        )
        assert_matches_type(PaginatedNebulaResultListChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Nebula) -> None:
        response = client.chunks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chunk = response.parse()
        assert_matches_type(PaginatedNebulaResultListChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Nebula) -> None:
        with client.chunks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chunk = response.parse()
            assert_matches_type(PaginatedNebulaResultListChunkResponse, chunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Nebula) -> None:
        chunk = client.chunks.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Nebula) -> None:
        response = client.chunks.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chunk = response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Nebula) -> None:
        with client.chunks.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chunk = response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, chunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.chunks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Nebula) -> None:
        chunk = client.chunks.search(
            query="query",
        )
        assert_matches_type(ChunkSearchResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Nebula) -> None:
        chunk = client.chunks.search(
            query="query",
            search_settings={
                "enable_conceptual_expansion": True,
                "filters": {"category": "bar"},
                "fulltext_weight": 1,
                "include_metadatas": True,
                "include_scores": True,
                "limit": 20,
                "search_mode": "search_mode",
                "semantic_weight": 5,
            },
        )
        assert_matches_type(ChunkSearchResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Nebula) -> None:
        response = client.chunks.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chunk = response.parse()
        assert_matches_type(ChunkSearchResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Nebula) -> None:
        with client.chunks.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chunk = response.parse()
            assert_matches_type(ChunkSearchResponse, chunk, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChunks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNebula) -> None:
        chunk = await async_client.chunks.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNebula) -> None:
        response = await async_client.chunks.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chunk = await response.parse()
        assert_matches_type(NebulaResultsChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNebula) -> None:
        async with async_client.chunks.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chunk = await response.parse()
            assert_matches_type(NebulaResultsChunkResponse, chunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.chunks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncNebula) -> None:
        chunk = await async_client.chunks.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )
        assert_matches_type(NebulaResultsChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncNebula) -> None:
        chunk = await async_client.chunks.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            metadata={"foo": "bar"},
        )
        assert_matches_type(NebulaResultsChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNebula) -> None:
        response = await async_client.chunks.with_raw_response.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chunk = await response.parse()
        assert_matches_type(NebulaResultsChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNebula) -> None:
        async with async_client.chunks.with_streaming_response.update(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chunk = await response.parse()
            assert_matches_type(NebulaResultsChunkResponse, chunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.chunks.with_raw_response.update(
                path_id="",
                body_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                text="text",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNebula) -> None:
        chunk = await async_client.chunks.list()
        assert_matches_type(PaginatedNebulaResultListChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNebula) -> None:
        chunk = await async_client.chunks.list(
            include_vectors=True,
            limit=1,
            metadata_filter="metadata_filter",
            offset=0,
        )
        assert_matches_type(PaginatedNebulaResultListChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNebula) -> None:
        response = await async_client.chunks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chunk = await response.parse()
        assert_matches_type(PaginatedNebulaResultListChunkResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNebula) -> None:
        async with async_client.chunks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chunk = await response.parse()
            assert_matches_type(PaginatedNebulaResultListChunkResponse, chunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncNebula) -> None:
        chunk = await async_client.chunks.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNebula) -> None:
        response = await async_client.chunks.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chunk = await response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNebula) -> None:
        async with async_client.chunks.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chunk = await response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, chunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.chunks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncNebula) -> None:
        chunk = await async_client.chunks.search(
            query="query",
        )
        assert_matches_type(ChunkSearchResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncNebula) -> None:
        chunk = await async_client.chunks.search(
            query="query",
            search_settings={
                "enable_conceptual_expansion": True,
                "filters": {"category": "bar"},
                "fulltext_weight": 1,
                "include_metadatas": True,
                "include_scores": True,
                "limit": 20,
                "search_mode": "search_mode",
                "semantic_weight": 5,
            },
        )
        assert_matches_type(ChunkSearchResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncNebula) -> None:
        response = await async_client.chunks.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chunk = await response.parse()
        assert_matches_type(ChunkSearchResponse, chunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncNebula) -> None:
        async with async_client.chunks.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chunk = await response.parse()
            assert_matches_type(ChunkSearchResponse, chunk, path=["response"])

        assert cast(Any, response.is_closed) is True
