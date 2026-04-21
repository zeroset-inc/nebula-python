# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types import (
    SecretRotateResponse,
    SecretInitializeResponse,
    SecretUpdateConfigResponse,
    SecretRetrieveStatusResponse,
    SecretRetrieveHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initialize(self, client: Nebula) -> None:
        secret = client.secrets.initialize()
        assert_matches_type(SecretInitializeResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initialize_with_all_params(self, client: Nebula) -> None:
        secret = client.secrets.initialize(
            secret_key="secret_key",
        )
        assert_matches_type(SecretInitializeResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_initialize(self, client: Nebula) -> None:
        response = client.secrets.with_raw_response.initialize()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretInitializeResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_initialize(self, client: Nebula) -> None:
        with client.secrets.with_streaming_response.initialize() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretInitializeResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_history(self, client: Nebula) -> None:
        secret = client.secrets.retrieve_history()
        assert_matches_type(SecretRetrieveHistoryResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_history_with_all_params(self, client: Nebula) -> None:
        secret = client.secrets.retrieve_history(
            limit=0,
            secret_key="secret_key",
        )
        assert_matches_type(SecretRetrieveHistoryResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_history(self, client: Nebula) -> None:
        response = client.secrets.with_raw_response.retrieve_history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretRetrieveHistoryResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_history(self, client: Nebula) -> None:
        with client.secrets.with_streaming_response.retrieve_history() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretRetrieveHistoryResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: Nebula) -> None:
        secret = client.secrets.retrieve_status()
        assert_matches_type(SecretRetrieveStatusResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status_with_all_params(self, client: Nebula) -> None:
        secret = client.secrets.retrieve_status(
            secret_key="secret_key",
        )
        assert_matches_type(SecretRetrieveStatusResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: Nebula) -> None:
        response = client.secrets.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretRetrieveStatusResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: Nebula) -> None:
        with client.secrets.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretRetrieveStatusResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rotate(self, client: Nebula) -> None:
        secret = client.secrets.rotate()
        assert_matches_type(SecretRotateResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rotate_with_all_params(self, client: Nebula) -> None:
        secret = client.secrets.rotate(
            notify_external=True,
            reason="reason",
            secret_key="secret_key",
        )
        assert_matches_type(SecretRotateResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rotate(self, client: Nebula) -> None:
        response = client.secrets.with_raw_response.rotate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretRotateResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rotate(self, client: Nebula) -> None:
        with client.secrets.with_streaming_response.rotate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretRotateResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_config(self, client: Nebula) -> None:
        secret = client.secrets.update_config()
        assert_matches_type(SecretUpdateConfigResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_config_with_all_params(self, client: Nebula) -> None:
        secret = client.secrets.update_config(
            auto_rotation_enabled=True,
            rotation_interval_days=0,
            secret_key="secret_key",
        )
        assert_matches_type(SecretUpdateConfigResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_config(self, client: Nebula) -> None:
        response = client.secrets.with_raw_response.update_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretUpdateConfigResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_config(self, client: Nebula) -> None:
        with client.secrets.with_streaming_response.update_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretUpdateConfigResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initialize(self, async_client: AsyncNebula) -> None:
        secret = await async_client.secrets.initialize()
        assert_matches_type(SecretInitializeResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initialize_with_all_params(self, async_client: AsyncNebula) -> None:
        secret = await async_client.secrets.initialize(
            secret_key="secret_key",
        )
        assert_matches_type(SecretInitializeResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_initialize(self, async_client: AsyncNebula) -> None:
        response = await async_client.secrets.with_raw_response.initialize()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretInitializeResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_initialize(self, async_client: AsyncNebula) -> None:
        async with async_client.secrets.with_streaming_response.initialize() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretInitializeResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_history(self, async_client: AsyncNebula) -> None:
        secret = await async_client.secrets.retrieve_history()
        assert_matches_type(SecretRetrieveHistoryResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_history_with_all_params(self, async_client: AsyncNebula) -> None:
        secret = await async_client.secrets.retrieve_history(
            limit=0,
            secret_key="secret_key",
        )
        assert_matches_type(SecretRetrieveHistoryResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_history(self, async_client: AsyncNebula) -> None:
        response = await async_client.secrets.with_raw_response.retrieve_history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretRetrieveHistoryResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_history(self, async_client: AsyncNebula) -> None:
        async with async_client.secrets.with_streaming_response.retrieve_history() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretRetrieveHistoryResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncNebula) -> None:
        secret = await async_client.secrets.retrieve_status()
        assert_matches_type(SecretRetrieveStatusResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status_with_all_params(self, async_client: AsyncNebula) -> None:
        secret = await async_client.secrets.retrieve_status(
            secret_key="secret_key",
        )
        assert_matches_type(SecretRetrieveStatusResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncNebula) -> None:
        response = await async_client.secrets.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretRetrieveStatusResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncNebula) -> None:
        async with async_client.secrets.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretRetrieveStatusResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rotate(self, async_client: AsyncNebula) -> None:
        secret = await async_client.secrets.rotate()
        assert_matches_type(SecretRotateResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rotate_with_all_params(self, async_client: AsyncNebula) -> None:
        secret = await async_client.secrets.rotate(
            notify_external=True,
            reason="reason",
            secret_key="secret_key",
        )
        assert_matches_type(SecretRotateResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rotate(self, async_client: AsyncNebula) -> None:
        response = await async_client.secrets.with_raw_response.rotate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretRotateResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rotate(self, async_client: AsyncNebula) -> None:
        async with async_client.secrets.with_streaming_response.rotate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretRotateResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_config(self, async_client: AsyncNebula) -> None:
        secret = await async_client.secrets.update_config()
        assert_matches_type(SecretUpdateConfigResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_config_with_all_params(self, async_client: AsyncNebula) -> None:
        secret = await async_client.secrets.update_config(
            auto_rotation_enabled=True,
            rotation_interval_days=0,
            secret_key="secret_key",
        )
        assert_matches_type(SecretUpdateConfigResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_config(self, async_client: AsyncNebula) -> None:
        response = await async_client.secrets.with_raw_response.update_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretUpdateConfigResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_config(self, async_client: AsyncNebula) -> None:
        async with async_client.secrets.with_streaming_response.update_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretUpdateConfigResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True
