# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContradictions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cascade_invalidation(self, client: Nebula) -> None:
        contradiction = client.contradictions.cascade_invalidation(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, contradiction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cascade_invalidation_with_all_params(self, client: Nebula) -> None:
        contradiction = client.contradictions.cascade_invalidation(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_depth=1,
            min_confidence_threshold=0,
        )
        assert_matches_type(object, contradiction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cascade_invalidation(self, client: Nebula) -> None:
        response = client.contradictions.with_raw_response.cascade_invalidation(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contradiction = response.parse()
        assert_matches_type(object, contradiction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cascade_invalidation(self, client: Nebula) -> None:
        with client.contradictions.with_streaming_response.cascade_invalidation(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contradiction = response.parse()
            assert_matches_type(object, contradiction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cascade_invalidation(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relationship_id` but received ''"):
            client.contradictions.with_raw_response.cascade_invalidation(
                relationship_id="",
            )


class TestAsyncContradictions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cascade_invalidation(self, async_client: AsyncNebula) -> None:
        contradiction = await async_client.contradictions.cascade_invalidation(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, contradiction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cascade_invalidation_with_all_params(self, async_client: AsyncNebula) -> None:
        contradiction = await async_client.contradictions.cascade_invalidation(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_depth=1,
            min_confidence_threshold=0,
        )
        assert_matches_type(object, contradiction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cascade_invalidation(self, async_client: AsyncNebula) -> None:
        response = await async_client.contradictions.with_raw_response.cascade_invalidation(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contradiction = await response.parse()
        assert_matches_type(object, contradiction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cascade_invalidation(self, async_client: AsyncNebula) -> None:
        async with async_client.contradictions.with_streaming_response.cascade_invalidation(
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contradiction = await response.parse()
            assert_matches_type(object, contradiction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cascade_invalidation(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relationship_id` but received ''"):
            await async_client.contradictions.with_raw_response.cascade_invalidation(
                relationship_id="",
            )
