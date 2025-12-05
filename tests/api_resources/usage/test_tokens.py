# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_current_month(self, client: Nebula) -> None:
        token = client.usage.tokens.retrieve_current_month()
        assert_matches_type(object, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_current_month(self, client: Nebula) -> None:
        response = client.usage.tokens.with_raw_response.retrieve_current_month()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(object, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_current_month(self, client: Nebula) -> None:
        with client.usage.tokens.with_streaming_response.retrieve_current_month() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(object, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_history(self, client: Nebula) -> None:
        token = client.usage.tokens.retrieve_history()
        assert_matches_type(object, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_history_with_all_params(self, client: Nebula) -> None:
        token = client.usage.tokens.retrieve_history(
            months=0,
        )
        assert_matches_type(object, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_history(self, client: Nebula) -> None:
        response = client.usage.tokens.with_raw_response.retrieve_history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(object, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_history(self, client: Nebula) -> None:
        with client.usage.tokens.with_streaming_response.retrieve_history() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(object, token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_current_month(self, async_client: AsyncNebula) -> None:
        token = await async_client.usage.tokens.retrieve_current_month()
        assert_matches_type(object, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_current_month(self, async_client: AsyncNebula) -> None:
        response = await async_client.usage.tokens.with_raw_response.retrieve_current_month()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(object, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_current_month(self, async_client: AsyncNebula) -> None:
        async with async_client.usage.tokens.with_streaming_response.retrieve_current_month() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(object, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_history(self, async_client: AsyncNebula) -> None:
        token = await async_client.usage.tokens.retrieve_history()
        assert_matches_type(object, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_history_with_all_params(self, async_client: AsyncNebula) -> None:
        token = await async_client.usage.tokens.retrieve_history(
            months=0,
        )
        assert_matches_type(object, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_history(self, async_client: AsyncNebula) -> None:
        response = await async_client.usage.tokens.with_raw_response.retrieve_history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(object, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_history(self, async_client: AsyncNebula) -> None:
        async with async_client.usage.tokens.with_streaming_response.retrieve_history() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(object, token, path=["response"])

        assert cast(Any, response.is_closed) is True
