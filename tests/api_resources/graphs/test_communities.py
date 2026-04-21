# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types import NebulaResultsGenericBooleanResponse
from nebula.types.graphs import (
    CommunityListResponse,
    NebulaResultsCommunity,
)
from nebula.types.collections import NebulaResultsGenericMessageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommunities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Nebula) -> None:
        community = client.graphs.communities.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            summary="summary",
        )
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Nebula) -> None:
        community = client.graphs.communities.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            summary="summary",
            findings=["string"],
            rating=1,
            rating_explanation="rating_explanation",
        )
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Nebula) -> None:
        response = client.graphs.communities.with_raw_response.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            summary="summary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Nebula) -> None:
        with client.graphs.communities.with_streaming_response.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            summary="summary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(NebulaResultsCommunity, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.graphs.communities.with_raw_response.create(
                collection_id="",
                name="name",
                summary="summary",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Nebula) -> None:
        community = client.graphs.communities.retrieve(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Nebula) -> None:
        response = client.graphs.communities.with_raw_response.retrieve(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Nebula) -> None:
        with client.graphs.communities.with_streaming_response.retrieve(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(NebulaResultsCommunity, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.graphs.communities.with_raw_response.retrieve(
                community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `community_id` but received ''"):
            client.graphs.communities.with_raw_response.retrieve(
                community_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Nebula) -> None:
        community = client.graphs.communities.update(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Nebula) -> None:
        community = client.graphs.communities.update(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            findings=["string"],
            name="name",
            rating=1,
            rating_explanation="rating_explanation",
            summary="summary",
        )
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Nebula) -> None:
        response = client.graphs.communities.with_raw_response.update(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Nebula) -> None:
        with client.graphs.communities.with_streaming_response.update(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(NebulaResultsCommunity, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.graphs.communities.with_raw_response.update(
                community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `community_id` but received ''"):
            client.graphs.communities.with_raw_response.update(
                community_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Nebula) -> None:
        community = client.graphs.communities.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommunityListResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Nebula) -> None:
        community = client.graphs.communities.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            offset=0,
        )
        assert_matches_type(CommunityListResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Nebula) -> None:
        response = client.graphs.communities.with_raw_response.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(CommunityListResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Nebula) -> None:
        with client.graphs.communities.with_streaming_response.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(CommunityListResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.graphs.communities.with_raw_response.list(
                collection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Nebula) -> None:
        community = client.graphs.communities.delete(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Nebula) -> None:
        response = client.graphs.communities.with_raw_response.delete(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Nebula) -> None:
        with client.graphs.communities.with_streaming_response.delete(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.graphs.communities.with_raw_response.delete(
                community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `community_id` but received ''"):
            client.graphs.communities.with_raw_response.delete(
                community_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_build(self, client: Nebula) -> None:
        community = client.graphs.communities.build(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_build_with_all_params(self, client: Nebula) -> None:
        community = client.graphs.communities.build(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body={"foo": "bar"},
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_build(self, client: Nebula) -> None:
        response = client.graphs.communities.with_raw_response.build(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_build(self, client: Nebula) -> None:
        with client.graphs.communities.with_streaming_response.build(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_build(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.graphs.communities.with_raw_response.build(
                collection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export(self, client: Nebula) -> None:
        community = client.graphs.communities.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export_with_all_params(self, client: Nebula) -> None:
        community = client.graphs.communities.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            columns=["string"],
            filters={"foo": "bar"},
            include_header=True,
        )
        assert_matches_type(object, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_export(self, client: Nebula) -> None:
        response = client.graphs.communities.with_raw_response.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(object, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_export(self, client: Nebula) -> None:
        with client.graphs.communities.with_streaming_response.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(object, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_export(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.graphs.communities.with_raw_response.export(
                collection_id="",
            )


class TestAsyncCommunities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncNebula) -> None:
        community = await async_client.graphs.communities.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            summary="summary",
        )
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNebula) -> None:
        community = await async_client.graphs.communities.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            summary="summary",
            findings=["string"],
            rating=1,
            rating_explanation="rating_explanation",
        )
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNebula) -> None:
        response = await async_client.graphs.communities.with_raw_response.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            summary="summary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNebula) -> None:
        async with async_client.graphs.communities.with_streaming_response.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            summary="summary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(NebulaResultsCommunity, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.graphs.communities.with_raw_response.create(
                collection_id="",
                name="name",
                summary="summary",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNebula) -> None:
        community = await async_client.graphs.communities.retrieve(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNebula) -> None:
        response = await async_client.graphs.communities.with_raw_response.retrieve(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNebula) -> None:
        async with async_client.graphs.communities.with_streaming_response.retrieve(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(NebulaResultsCommunity, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.graphs.communities.with_raw_response.retrieve(
                community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `community_id` but received ''"):
            await async_client.graphs.communities.with_raw_response.retrieve(
                community_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncNebula) -> None:
        community = await async_client.graphs.communities.update(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncNebula) -> None:
        community = await async_client.graphs.communities.update(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            findings=["string"],
            name="name",
            rating=1,
            rating_explanation="rating_explanation",
            summary="summary",
        )
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNebula) -> None:
        response = await async_client.graphs.communities.with_raw_response.update(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(NebulaResultsCommunity, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNebula) -> None:
        async with async_client.graphs.communities.with_streaming_response.update(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(NebulaResultsCommunity, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.graphs.communities.with_raw_response.update(
                community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `community_id` but received ''"):
            await async_client.graphs.communities.with_raw_response.update(
                community_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNebula) -> None:
        community = await async_client.graphs.communities.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommunityListResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNebula) -> None:
        community = await async_client.graphs.communities.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            offset=0,
        )
        assert_matches_type(CommunityListResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNebula) -> None:
        response = await async_client.graphs.communities.with_raw_response.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(CommunityListResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNebula) -> None:
        async with async_client.graphs.communities.with_streaming_response.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(CommunityListResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.graphs.communities.with_raw_response.list(
                collection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncNebula) -> None:
        community = await async_client.graphs.communities.delete(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNebula) -> None:
        response = await async_client.graphs.communities.with_raw_response.delete(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNebula) -> None:
        async with async_client.graphs.communities.with_streaming_response.delete(
            community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.graphs.communities.with_raw_response.delete(
                community_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `community_id` but received ''"):
            await async_client.graphs.communities.with_raw_response.delete(
                community_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_build(self, async_client: AsyncNebula) -> None:
        community = await async_client.graphs.communities.build(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_build_with_all_params(self, async_client: AsyncNebula) -> None:
        community = await async_client.graphs.communities.build(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body={"foo": "bar"},
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_build(self, async_client: AsyncNebula) -> None:
        response = await async_client.graphs.communities.with_raw_response.build(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_build(self, async_client: AsyncNebula) -> None:
        async with async_client.graphs.communities.with_streaming_response.build(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_build(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.graphs.communities.with_raw_response.build(
                collection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export(self, async_client: AsyncNebula) -> None:
        community = await async_client.graphs.communities.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncNebula) -> None:
        community = await async_client.graphs.communities.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            columns=["string"],
            filters={"foo": "bar"},
            include_header=True,
        )
        assert_matches_type(object, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncNebula) -> None:
        response = await async_client.graphs.communities.with_raw_response.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(object, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncNebula) -> None:
        async with async_client.graphs.communities.with_streaming_response.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(object, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_export(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.graphs.communities.with_raw_response.export(
                collection_id="",
            )
