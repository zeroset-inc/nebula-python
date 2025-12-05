# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types import NebulaResultsGenericBooleanResponse
from nebula.types.graphs import (
    NebulaResultsRelationship,
)
from nebula.types.memories import PaginatedNebulaResultRelationship

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRelationships:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Nebula) -> None:
        relationship = client.graphs.relationships.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Nebula) -> None:
        relationship = client.graphs.relationships.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "bar"},
            weight=0,
        )
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Nebula) -> None:
        response = client.graphs.relationships.with_raw_response.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = response.parse()
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Nebula) -> None:
        with client.graphs.relationships.with_streaming_response.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = response.parse()
            assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.graphs.relationships.with_raw_response.create(
                collection_id="",
                description="description",
                object="object",
                object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                predicate="predicate",
                subject="subject",
                subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Nebula) -> None:
        relationship = client.graphs.relationships.retrieve(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Nebula) -> None:
        response = client.graphs.relationships.with_raw_response.retrieve(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = response.parse()
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Nebula) -> None:
        with client.graphs.relationships.with_streaming_response.retrieve(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = response.parse()
            assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.graphs.relationships.with_raw_response.retrieve(
                relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relationship_id` but received ''"):
            client.graphs.relationships.with_raw_response.retrieve(
                relationship_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Nebula) -> None:
        relationship = client.graphs.relationships.update(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Nebula) -> None:
        relationship = client.graphs.relationships.update(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            metadata={"foo": "bar"},
            weight=0,
        )
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Nebula) -> None:
        response = client.graphs.relationships.with_raw_response.update(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = response.parse()
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Nebula) -> None:
        with client.graphs.relationships.with_streaming_response.update(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = response.parse()
            assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.graphs.relationships.with_raw_response.update(
                relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
                object="object",
                object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                predicate="predicate",
                subject="subject",
                subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relationship_id` but received ''"):
            client.graphs.relationships.with_raw_response.update(
                relationship_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                object="object",
                object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                predicate="predicate",
                subject="subject",
                subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Nebula) -> None:
        relationship = client.graphs.relationships.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaginatedNebulaResultRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Nebula) -> None:
        relationship = client.graphs.relationships.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            offset=0,
        )
        assert_matches_type(PaginatedNebulaResultRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Nebula) -> None:
        response = client.graphs.relationships.with_raw_response.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = response.parse()
        assert_matches_type(PaginatedNebulaResultRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Nebula) -> None:
        with client.graphs.relationships.with_streaming_response.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = response.parse()
            assert_matches_type(PaginatedNebulaResultRelationship, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.graphs.relationships.with_raw_response.list(
                collection_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Nebula) -> None:
        relationship = client.graphs.relationships.delete(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Nebula) -> None:
        response = client.graphs.relationships.with_raw_response.delete(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Nebula) -> None:
        with client.graphs.relationships.with_streaming_response.delete(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.graphs.relationships.with_raw_response.delete(
                relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relationship_id` but received ''"):
            client.graphs.relationships.with_raw_response.delete(
                relationship_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export(self, client: Nebula) -> None:
        relationship = client.graphs.relationships.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export_with_all_params(self, client: Nebula) -> None:
        relationship = client.graphs.relationships.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            columns=["string"],
            filters={"foo": "bar"},
            include_header=True,
        )
        assert_matches_type(object, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_export(self, client: Nebula) -> None:
        response = client.graphs.relationships.with_raw_response.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = response.parse()
        assert_matches_type(object, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_export(self, client: Nebula) -> None:
        with client.graphs.relationships.with_streaming_response.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = response.parse()
            assert_matches_type(object, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_export(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.graphs.relationships.with_raw_response.export(
                collection_id="",
            )


class TestAsyncRelationships:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncNebula) -> None:
        relationship = await async_client.graphs.relationships.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNebula) -> None:
        relationship = await async_client.graphs.relationships.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "bar"},
            weight=0,
        )
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNebula) -> None:
        response = await async_client.graphs.relationships.with_raw_response.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = await response.parse()
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNebula) -> None:
        async with async_client.graphs.relationships.with_streaming_response.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = await response.parse()
            assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.graphs.relationships.with_raw_response.create(
                collection_id="",
                description="description",
                object="object",
                object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                predicate="predicate",
                subject="subject",
                subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNebula) -> None:
        relationship = await async_client.graphs.relationships.retrieve(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNebula) -> None:
        response = await async_client.graphs.relationships.with_raw_response.retrieve(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = await response.parse()
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNebula) -> None:
        async with async_client.graphs.relationships.with_streaming_response.retrieve(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = await response.parse()
            assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.graphs.relationships.with_raw_response.retrieve(
                relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relationship_id` but received ''"):
            await async_client.graphs.relationships.with_raw_response.retrieve(
                relationship_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncNebula) -> None:
        relationship = await async_client.graphs.relationships.update(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncNebula) -> None:
        relationship = await async_client.graphs.relationships.update(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            metadata={"foo": "bar"},
            weight=0,
        )
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNebula) -> None:
        response = await async_client.graphs.relationships.with_raw_response.update(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = await response.parse()
        assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNebula) -> None:
        async with async_client.graphs.relationships.with_streaming_response.update(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object="object",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            predicate="predicate",
            subject="subject",
            subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = await response.parse()
            assert_matches_type(NebulaResultsRelationship, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.graphs.relationships.with_raw_response.update(
                relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
                object="object",
                object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                predicate="predicate",
                subject="subject",
                subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relationship_id` but received ''"):
            await async_client.graphs.relationships.with_raw_response.update(
                relationship_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                object="object",
                object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                predicate="predicate",
                subject="subject",
                subject_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNebula) -> None:
        relationship = await async_client.graphs.relationships.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaginatedNebulaResultRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNebula) -> None:
        relationship = await async_client.graphs.relationships.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            offset=0,
        )
        assert_matches_type(PaginatedNebulaResultRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNebula) -> None:
        response = await async_client.graphs.relationships.with_raw_response.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = await response.parse()
        assert_matches_type(PaginatedNebulaResultRelationship, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNebula) -> None:
        async with async_client.graphs.relationships.with_streaming_response.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = await response.parse()
            assert_matches_type(PaginatedNebulaResultRelationship, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.graphs.relationships.with_raw_response.list(
                collection_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncNebula) -> None:
        relationship = await async_client.graphs.relationships.delete(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNebula) -> None:
        response = await async_client.graphs.relationships.with_raw_response.delete(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = await response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNebula) -> None:
        async with async_client.graphs.relationships.with_streaming_response.delete(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = await response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.graphs.relationships.with_raw_response.delete(
                relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relationship_id` but received ''"):
            await async_client.graphs.relationships.with_raw_response.delete(
                relationship_id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export(self, async_client: AsyncNebula) -> None:
        relationship = await async_client.graphs.relationships.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncNebula) -> None:
        relationship = await async_client.graphs.relationships.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            columns=["string"],
            filters={"foo": "bar"},
            include_header=True,
        )
        assert_matches_type(object, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncNebula) -> None:
        response = await async_client.graphs.relationships.with_raw_response.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = await response.parse()
        assert_matches_type(object, relationship, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncNebula) -> None:
        async with async_client.graphs.relationships.with_streaming_response.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = await response.parse()
            assert_matches_type(object, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_export(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.graphs.relationships.with_raw_response.export(
                collection_id="",
            )
