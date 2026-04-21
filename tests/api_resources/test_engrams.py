# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEngrams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_duplicate_stats(self, client: Nebula) -> None:
        engram = client.engrams.retrieve_duplicate_stats(
            engram_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, engram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_duplicate_stats_with_all_params(self, client: Nebula) -> None:
        engram = client.engrams.retrieve_duplicate_stats(
            engram_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            public=True,
        )
        assert_matches_type(object, engram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_duplicate_stats(self, client: Nebula) -> None:
        response = client.engrams.with_raw_response.retrieve_duplicate_stats(
            engram_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engram = response.parse()
        assert_matches_type(object, engram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_duplicate_stats(self, client: Nebula) -> None:
        with client.engrams.with_streaming_response.retrieve_duplicate_stats(
            engram_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engram = response.parse()
            assert_matches_type(object, engram, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_duplicate_stats(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engram_id` but received ''"):
            client.engrams.with_raw_response.retrieve_duplicate_stats(
                engram_id="",
            )


class TestAsyncEngrams:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_duplicate_stats(self, async_client: AsyncNebula) -> None:
        engram = await async_client.engrams.retrieve_duplicate_stats(
            engram_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, engram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_duplicate_stats_with_all_params(self, async_client: AsyncNebula) -> None:
        engram = await async_client.engrams.retrieve_duplicate_stats(
            engram_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            public=True,
        )
        assert_matches_type(object, engram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_duplicate_stats(self, async_client: AsyncNebula) -> None:
        response = await async_client.engrams.with_raw_response.retrieve_duplicate_stats(
            engram_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engram = await response.parse()
        assert_matches_type(object, engram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_duplicate_stats(self, async_client: AsyncNebula) -> None:
        async with async_client.engrams.with_streaming_response.retrieve_duplicate_stats(
            engram_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engram = await response.parse()
            assert_matches_type(object, engram, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_duplicate_stats(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engram_id` but received ''"):
            await async_client.engrams.with_raw_response.retrieve_duplicate_stats(
                engram_id="",
            )
