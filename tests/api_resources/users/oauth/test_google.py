# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types.collections import NebulaResultsGenericMessageResponse
from nebula.types.users.oauth import LoginResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGoogle:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_authorize(self, client: Nebula) -> None:
        google = client.users.oauth.google.authorize()
        assert_matches_type(NebulaResultsGenericMessageResponse, google, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_authorize(self, client: Nebula) -> None:
        response = client.users.oauth.google.with_raw_response.authorize()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        google = response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, google, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_authorize(self, client: Nebula) -> None:
        with client.users.oauth.google.with_streaming_response.authorize() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            google = response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, google, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_callback(self, client: Nebula) -> None:
        google = client.users.oauth.google.callback(
            code="code",
            state="state",
        )
        assert_matches_type(LoginResponse, google, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_callback(self, client: Nebula) -> None:
        response = client.users.oauth.google.with_raw_response.callback(
            code="code",
            state="state",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        google = response.parse()
        assert_matches_type(LoginResponse, google, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_callback(self, client: Nebula) -> None:
        with client.users.oauth.google.with_streaming_response.callback(
            code="code",
            state="state",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            google = response.parse()
            assert_matches_type(LoginResponse, google, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGoogle:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_authorize(self, async_client: AsyncNebula) -> None:
        google = await async_client.users.oauth.google.authorize()
        assert_matches_type(NebulaResultsGenericMessageResponse, google, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_authorize(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.oauth.google.with_raw_response.authorize()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        google = await response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, google, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_authorize(self, async_client: AsyncNebula) -> None:
        async with async_client.users.oauth.google.with_streaming_response.authorize() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            google = await response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, google, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_callback(self, async_client: AsyncNebula) -> None:
        google = await async_client.users.oauth.google.callback(
            code="code",
            state="state",
        )
        assert_matches_type(LoginResponse, google, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_callback(self, async_client: AsyncNebula) -> None:
        response = await async_client.users.oauth.google.with_raw_response.callback(
            code="code",
            state="state",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        google = await response.parse()
        assert_matches_type(LoginResponse, google, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_callback(self, async_client: AsyncNebula) -> None:
        async with async_client.users.oauth.google.with_streaming_response.callback(
            code="code",
            state="state",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            google = await response.parse()
            assert_matches_type(LoginResponse, google, path=["response"])

        assert cast(Any, response.is_closed) is True
