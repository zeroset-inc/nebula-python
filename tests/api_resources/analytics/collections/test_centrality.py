# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types.analytics.collections import (
    CentralityStatusResponse,
    CentralityComputeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCentrality:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_compute(self, client: Nebula) -> None:
        centrality = client.analytics.collections.centrality.compute(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CentralityComputeResponse, centrality, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_compute_with_all_params(self, client: Nebula) -> None:
        centrality = client.analytics.collections.centrality.compute(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=True,
        )
        assert_matches_type(CentralityComputeResponse, centrality, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_compute(self, client: Nebula) -> None:
        response = client.analytics.collections.centrality.with_raw_response.compute(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        centrality = response.parse()
        assert_matches_type(CentralityComputeResponse, centrality, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_compute(self, client: Nebula) -> None:
        with client.analytics.collections.centrality.with_streaming_response.compute(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            centrality = response.parse()
            assert_matches_type(CentralityComputeResponse, centrality, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_compute(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.analytics.collections.centrality.with_raw_response.compute(
                collection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_status(self, client: Nebula) -> None:
        centrality = client.analytics.collections.centrality.status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CentralityStatusResponse, centrality, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_status(self, client: Nebula) -> None:
        response = client.analytics.collections.centrality.with_raw_response.status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        centrality = response.parse()
        assert_matches_type(CentralityStatusResponse, centrality, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_status(self, client: Nebula) -> None:
        with client.analytics.collections.centrality.with_streaming_response.status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            centrality = response.parse()
            assert_matches_type(CentralityStatusResponse, centrality, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_status(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.analytics.collections.centrality.with_raw_response.status(
                "",
            )


class TestAsyncCentrality:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_compute(self, async_client: AsyncNebula) -> None:
        centrality = await async_client.analytics.collections.centrality.compute(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CentralityComputeResponse, centrality, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_compute_with_all_params(self, async_client: AsyncNebula) -> None:
        centrality = await async_client.analytics.collections.centrality.compute(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=True,
        )
        assert_matches_type(CentralityComputeResponse, centrality, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_compute(self, async_client: AsyncNebula) -> None:
        response = await async_client.analytics.collections.centrality.with_raw_response.compute(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        centrality = await response.parse()
        assert_matches_type(CentralityComputeResponse, centrality, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_compute(self, async_client: AsyncNebula) -> None:
        async with async_client.analytics.collections.centrality.with_streaming_response.compute(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            centrality = await response.parse()
            assert_matches_type(CentralityComputeResponse, centrality, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_compute(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.analytics.collections.centrality.with_raw_response.compute(
                collection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_status(self, async_client: AsyncNebula) -> None:
        centrality = await async_client.analytics.collections.centrality.status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CentralityStatusResponse, centrality, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncNebula) -> None:
        response = await async_client.analytics.collections.centrality.with_raw_response.status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        centrality = await response.parse()
        assert_matches_type(CentralityStatusResponse, centrality, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncNebula) -> None:
        async with async_client.analytics.collections.centrality.with_streaming_response.status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            centrality = await response.parse()
            assert_matches_type(CentralityStatusResponse, centrality, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_status(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.analytics.collections.centrality.with_raw_response.status(
                "",
            )
