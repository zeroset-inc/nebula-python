# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types import (
    SourceListResponse,
    SourceDeleteResponse,
    SourceSearchResponse,
    SourceUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Nebula) -> None:
        source = client.sources.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
        )
        assert_matches_type(SourceUpdateResponse, source, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Nebula) -> None:
        source = client.sources.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "bar"},
        )
        assert_matches_type(SourceUpdateResponse, source, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Nebula) -> None:
        response = client.sources.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceUpdateResponse, source, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Nebula) -> None:
        with client.sources.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceUpdateResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sources.with_raw_response.update(
                id="",
                content="content",
            )

    @parametrize
    def test_method_list(self, client: Nebula) -> None:
        source = client.sources.list()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Nebula) -> None:
        source = client.sources.list(
            include_vectors=True,
            limit=1,
            metadata_filter="metadata_filter",
            offset=0,
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Nebula) -> None:
        response = client.sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Nebula) -> None:
        with client.sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Nebula) -> None:
        source = client.sources.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Nebula) -> None:
        source = client.sources.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Nebula) -> None:
        response = client.sources.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Nebula) -> None:
        with client.sources.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceDeleteResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sources.with_raw_response.delete(
                id="",
            )

    @parametrize
    def test_method_search(self, client: Nebula) -> None:
        source = client.sources.search(
            query="query",
        )
        assert_matches_type(SourceSearchResponse, source, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Nebula) -> None:
        source = client.sources.search(
            query="query",
            search_settings={
                "effort": "auto",
                "enable_conceptual_expansion": True,
                "filters": {"foo": "bar"},
                "fulltext_weight": 0.2,
                "graph_settings": {"foo": "bar"},
                "has_pruning_gate": True,
                "include_scores": True,
                "semantic_weight": 0.8,
                "verbose": False,
            },
        )
        assert_matches_type(SourceSearchResponse, source, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Nebula) -> None:
        response = client.sources.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceSearchResponse, source, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Nebula) -> None:
        with client.sources.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceSearchResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncNebula) -> None:
        source = await async_client.sources.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
        )
        assert_matches_type(SourceUpdateResponse, source, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncNebula) -> None:
        source = await async_client.sources.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "bar"},
        )
        assert_matches_type(SourceUpdateResponse, source, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNebula) -> None:
        response = await async_client.sources.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceUpdateResponse, source, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNebula) -> None:
        async with async_client.sources.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceUpdateResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sources.with_raw_response.update(
                id="",
                content="content",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncNebula) -> None:
        source = await async_client.sources.list()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNebula) -> None:
        source = await async_client.sources.list(
            include_vectors=True,
            limit=1,
            metadata_filter="metadata_filter",
            offset=0,
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNebula) -> None:
        response = await async_client.sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNebula) -> None:
        async with async_client.sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncNebula) -> None:
        source = await async_client.sources.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncNebula) -> None:
        source = await async_client.sources.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNebula) -> None:
        response = await async_client.sources.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNebula) -> None:
        async with async_client.sources.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceDeleteResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sources.with_raw_response.delete(
                id="",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncNebula) -> None:
        source = await async_client.sources.search(
            query="query",
        )
        assert_matches_type(SourceSearchResponse, source, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncNebula) -> None:
        source = await async_client.sources.search(
            query="query",
            search_settings={
                "effort": "auto",
                "enable_conceptual_expansion": True,
                "filters": {"foo": "bar"},
                "fulltext_weight": 0.2,
                "graph_settings": {"foo": "bar"},
                "has_pruning_gate": True,
                "include_scores": True,
                "semantic_weight": 0.8,
                "verbose": False,
            },
        )
        assert_matches_type(SourceSearchResponse, source, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncNebula) -> None:
        response = await async_client.sources.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceSearchResponse, source, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncNebula) -> None:
        async with async_client.sources.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceSearchResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True
