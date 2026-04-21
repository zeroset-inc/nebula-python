# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types import NebulaResultsGenericBooleanResponse, PaginatedNebulaResultListCollectionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Nebula) -> None:
        collection = client.users.collections.add(
            collection_id="750e8400-e29b-41d4-a716-446655440000",
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Nebula) -> None:
        response = client.users.collections.with_raw_response.add(
            collection_id="750e8400-e29b-41d4-a716-446655440000",
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Nebula) -> None:
        with client.users.collections.with_streaming_response.add(
            collection_id="750e8400-e29b-41d4-a716-446655440000",
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.collections.with_raw_response.add(
                collection_id="750e8400-e29b-41d4-a716-446655440000",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.users.collections.with_raw_response.add(
                collection_id="",
                id="550e8400-e29b-41d4-a716-446655440000",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_all(self, client: Nebula) -> None:
        collection = client.users.collections.get_all(
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_all_with_all_params(self, client: Nebula) -> None:
        collection = client.users.collections.get_all(
            id="550e8400-e29b-41d4-a716-446655440000",
            limit=1,
            offset=0,
        )
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_all(self, client: Nebula) -> None:
        response = client.users.collections.with_raw_response.get_all(
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_all(self, client: Nebula) -> None:
        with client.users.collections.with_streaming_response.get_all(
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_all(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.collections.with_raw_response.get_all(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Nebula) -> None:
        collection = client.users.collections.remove(
            collection_id="750e8400-e29b-41d4-a716-446655440000",
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Nebula) -> None:
        response = client.users.collections.with_raw_response.remove(
            collection_id="750e8400-e29b-41d4-a716-446655440000",
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Nebula) -> None:
        with client.users.collections.with_streaming_response.remove(
            collection_id="750e8400-e29b-41d4-a716-446655440000",
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.collections.with_raw_response.remove(
                collection_id="750e8400-e29b-41d4-a716-446655440000",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.users.collections.with_raw_response.remove(
                collection_id="",
                id="550e8400-e29b-41d4-a716-446655440000",
            )


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncNebula) -> None:
        collection = await async_client.users.collections.add(
            collection_id="750e8400-e29b-41d4-a716-446655440000",
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.collections.with_raw_response.add(
            collection_id="750e8400-e29b-41d4-a716-446655440000",
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncNebula) -> None:
        async with async_client.users.collections.with_streaming_response.add(
            collection_id="750e8400-e29b-41d4-a716-446655440000",
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.collections.with_raw_response.add(
                collection_id="750e8400-e29b-41d4-a716-446655440000",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.users.collections.with_raw_response.add(
                collection_id="",
                id="550e8400-e29b-41d4-a716-446655440000",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_all(self, async_client: AsyncNebula) -> None:
        collection = await async_client.users.collections.get_all(
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_all_with_all_params(self, async_client: AsyncNebula) -> None:
        collection = await async_client.users.collections.get_all(
            id="550e8400-e29b-41d4-a716-446655440000",
            limit=1,
            offset=0,
        )
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_all(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.collections.with_raw_response.get_all(
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_all(self, async_client: AsyncNebula) -> None:
        async with async_client.users.collections.with_streaming_response.get_all(
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_all(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.collections.with_raw_response.get_all(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncNebula) -> None:
        collection = await async_client.users.collections.remove(
            collection_id="750e8400-e29b-41d4-a716-446655440000",
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.collections.with_raw_response.remove(
            collection_id="750e8400-e29b-41d4-a716-446655440000",
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncNebula) -> None:
        async with async_client.users.collections.with_streaming_response.remove(
            collection_id="750e8400-e29b-41d4-a716-446655440000",
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.collections.with_raw_response.remove(
                collection_id="750e8400-e29b-41d4-a716-446655440000",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.users.collections.with_raw_response.remove(
                collection_id="",
                id="550e8400-e29b-41d4-a716-446655440000",
            )
