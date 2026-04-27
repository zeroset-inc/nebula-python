# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types import (
    CollectionListResponse,
    CollectionCreateResponse,
    CollectionDeleteResponse,
    CollectionUpdateResponse,
    CollectionRetrieveResponse,
    CollectionRetrieveByNameResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Nebula) -> None:
        collection = client.collections.create(
            name="name",
        )
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Nebula) -> None:
        collection = client.collections.create(
            name="name",
            description="description",
            workspace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionCreateResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Nebula) -> None:
        collection = client.collections.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.collections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Nebula) -> None:
        collection = client.collections.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Nebula) -> None:
        collection = client.collections.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_tier="access_tier",
            description="description",
            generate_description=True,
            name="name",
        )
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.collections.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Nebula) -> None:
        collection = client.collections.list()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Nebula) -> None:
        collection = client.collections.list(
            ids=["string"],
            limit=1,
            name="name",
            offset=0,
            owner_only=True,
            workspace_id="workspace_id",
        )
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionListResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Nebula) -> None:
        collection = client.collections.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.collections.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_retrieve_by_name(self, client: Nebula) -> None:
        collection = client.collections.retrieve_by_name(
            collection_name="collection_name",
        )
        assert_matches_type(CollectionRetrieveByNameResponse, collection, path=["response"])

    @parametrize
    def test_method_retrieve_by_name_with_all_params(self, client: Nebula) -> None:
        collection = client.collections.retrieve_by_name(
            collection_name="collection_name",
            owner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionRetrieveByNameResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_retrieve_by_name(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.retrieve_by_name(
            collection_name="collection_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionRetrieveByNameResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_by_name(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.retrieve_by_name(
            collection_name="collection_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionRetrieveByNameResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_by_name(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_name` but received ''"):
            client.collections.with_raw_response.retrieve_by_name(
                collection_name="",
            )


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.create(
            name="name",
        )
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.create(
            name="name",
            description="description",
            workspace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionCreateResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.collections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_tier="access_tier",
            description="description",
            generate_description=True,
            name="name",
        )
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.collections.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.list()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.list(
            ids=["string"],
            limit=1,
            name="name",
            offset=0,
            owner_only=True,
            workspace_id="workspace_id",
        )
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionListResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.collections.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_retrieve_by_name(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.retrieve_by_name(
            collection_name="collection_name",
        )
        assert_matches_type(CollectionRetrieveByNameResponse, collection, path=["response"])

    @parametrize
    async def test_method_retrieve_by_name_with_all_params(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.retrieve_by_name(
            collection_name="collection_name",
            owner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionRetrieveByNameResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_by_name(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.retrieve_by_name(
            collection_name="collection_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionRetrieveByNameResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_by_name(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.retrieve_by_name(
            collection_name="collection_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionRetrieveByNameResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_by_name(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_name` but received ''"):
            await async_client.collections.with_raw_response.retrieve_by_name(
                collection_name="",
            )
