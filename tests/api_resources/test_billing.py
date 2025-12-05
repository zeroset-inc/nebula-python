# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBilling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_billing_portal_session(self, client: Nebula) -> None:
        billing = client.billing.create_billing_portal_session()
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_billing_portal_session_with_all_params(self, client: Nebula) -> None:
        billing = client.billing.create_billing_portal_session(
            return_url="return_url",
        )
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_billing_portal_session(self, client: Nebula) -> None:
        response = client.billing.with_raw_response.create_billing_portal_session()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_billing_portal_session(self, client: Nebula) -> None:
        with client.billing.with_streaming_response.create_billing_portal_session() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(object, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_checkout_session(self, client: Nebula) -> None:
        billing = client.billing.create_checkout_session(
            plan_id="plan_id",
        )
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_checkout_session_with_all_params(self, client: Nebula) -> None:
        billing = client.billing.create_checkout_session(
            plan_id="plan_id",
            billing_interval="billing_interval",
            cancel_url="cancel_url",
            success_url="success_url",
        )
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_checkout_session(self, client: Nebula) -> None:
        response = client.billing.with_raw_response.create_checkout_session(
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_checkout_session(self, client: Nebula) -> None:
        with client.billing.with_streaming_response.create_checkout_session(
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(object, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_handle_webhook(self, client: Nebula) -> None:
        billing = client.billing.handle_webhook()
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_handle_webhook(self, client: Nebula) -> None:
        response = client.billing.with_raw_response.handle_webhook()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_handle_webhook(self, client: Nebula) -> None:
        with client.billing.with_streaming_response.handle_webhook() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(object, billing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBilling:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_billing_portal_session(self, async_client: AsyncNebula) -> None:
        billing = await async_client.billing.create_billing_portal_session()
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_billing_portal_session_with_all_params(self, async_client: AsyncNebula) -> None:
        billing = await async_client.billing.create_billing_portal_session(
            return_url="return_url",
        )
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_billing_portal_session(self, async_client: AsyncNebula) -> None:
        response = await async_client.billing.with_raw_response.create_billing_portal_session()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_billing_portal_session(self, async_client: AsyncNebula) -> None:
        async with async_client.billing.with_streaming_response.create_billing_portal_session() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(object, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_checkout_session(self, async_client: AsyncNebula) -> None:
        billing = await async_client.billing.create_checkout_session(
            plan_id="plan_id",
        )
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_checkout_session_with_all_params(self, async_client: AsyncNebula) -> None:
        billing = await async_client.billing.create_checkout_session(
            plan_id="plan_id",
            billing_interval="billing_interval",
            cancel_url="cancel_url",
            success_url="success_url",
        )
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_checkout_session(self, async_client: AsyncNebula) -> None:
        response = await async_client.billing.with_raw_response.create_checkout_session(
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_checkout_session(self, async_client: AsyncNebula) -> None:
        async with async_client.billing.with_streaming_response.create_checkout_session(
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(object, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_handle_webhook(self, async_client: AsyncNebula) -> None:
        billing = await async_client.billing.handle_webhook()
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_handle_webhook(self, async_client: AsyncNebula) -> None:
        response = await async_client.billing.with_raw_response.handle_webhook()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(object, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_handle_webhook(self, async_client: AsyncNebula) -> None:
        async with async_client.billing.with_streaming_response.handle_webhook() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(object, billing, path=["response"])

        assert cast(Any, response.is_closed) is True
