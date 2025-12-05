# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resolve_duplicate(self, client: Nebula) -> None:
        entity = client.entities.resolve_duplicate(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="action",
        )
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resolve_duplicate_with_all_params(self, client: Nebula) -> None:
        entity = client.entities.resolve_duplicate(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="action",
            public=True,
            target_entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_resolve_duplicate(self, client: Nebula) -> None:
        response = client.entities.with_raw_response.resolve_duplicate(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_resolve_duplicate(self, client: Nebula) -> None:
        with client.entities.with_streaming_response.resolve_duplicate(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(object, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_resolve_duplicate(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.with_raw_response.resolve_duplicate(
                entity_id="",
                action="action",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_duplicates(self, client: Nebula) -> None:
        entity = client.entities.retrieve_duplicates(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_duplicates_with_all_params(self, client: Nebula) -> None:
        entity = client.entities.retrieve_duplicates(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            public=True,
        )
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_duplicates(self, client: Nebula) -> None:
        response = client.entities.with_raw_response.retrieve_duplicates(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_duplicates(self, client: Nebula) -> None:
        with client.entities.with_streaming_response.retrieve_duplicates(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(object, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_duplicates(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.with_raw_response.retrieve_duplicates(
                entity_id="",
            )


class TestAsyncEntities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resolve_duplicate(self, async_client: AsyncNebula) -> None:
        entity = await async_client.entities.resolve_duplicate(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="action",
        )
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resolve_duplicate_with_all_params(self, async_client: AsyncNebula) -> None:
        entity = await async_client.entities.resolve_duplicate(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="action",
            public=True,
            target_entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_resolve_duplicate(self, async_client: AsyncNebula) -> None:
        response = await async_client.entities.with_raw_response.resolve_duplicate(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_resolve_duplicate(self, async_client: AsyncNebula) -> None:
        async with async_client.entities.with_streaming_response.resolve_duplicate(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(object, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_resolve_duplicate(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.with_raw_response.resolve_duplicate(
                entity_id="",
                action="action",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_duplicates(self, async_client: AsyncNebula) -> None:
        entity = await async_client.entities.retrieve_duplicates(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_duplicates_with_all_params(self, async_client: AsyncNebula) -> None:
        entity = await async_client.entities.retrieve_duplicates(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            public=True,
        )
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_duplicates(self, async_client: AsyncNebula) -> None:
        response = await async_client.entities.with_raw_response.retrieve_duplicates(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_duplicates(self, async_client: AsyncNebula) -> None:
        async with async_client.entities.with_streaming_response.retrieve_duplicates(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(object, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_duplicates(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.with_raw_response.retrieve_duplicates(
                entity_id="",
            )
