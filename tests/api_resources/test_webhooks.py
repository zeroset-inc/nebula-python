# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types import (
    WebhookGetStatsResponse,
    WebhookListEventsResponse,
    WebhookTriggerCleanupResponse,
    WebhookScheduleCleanupResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_stats(self, client: Nebula) -> None:
        webhook = client.webhooks.get_stats()
        assert_matches_type(WebhookGetStatsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_stats(self, client: Nebula) -> None:
        response = client.webhooks.with_raw_response.get_stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookGetStatsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_stats(self, client: Nebula) -> None:
        with client.webhooks.with_streaming_response.get_stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookGetStatsResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_events(self, client: Nebula) -> None:
        webhook = client.webhooks.list_events()
        assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_events_with_all_params(self, client: Nebula) -> None:
        webhook = client.webhooks.list_events(
            limit=0,
            processing_status="processing_status",
            webhook_type="webhook_type",
        )
        assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_events(self, client: Nebula) -> None:
        response = client.webhooks.with_raw_response.list_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_events(self, client: Nebula) -> None:
        with client.webhooks.with_streaming_response.list_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_schedule_cleanup(self, client: Nebula) -> None:
        webhook = client.webhooks.schedule_cleanup()
        assert_matches_type(WebhookScheduleCleanupResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_schedule_cleanup_with_all_params(self, client: Nebula) -> None:
        webhook = client.webhooks.schedule_cleanup(
            cron_expression="cron_expression",
            retention_days=0,
        )
        assert_matches_type(WebhookScheduleCleanupResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_schedule_cleanup(self, client: Nebula) -> None:
        response = client.webhooks.with_raw_response.schedule_cleanup()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookScheduleCleanupResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_schedule_cleanup(self, client: Nebula) -> None:
        with client.webhooks.with_streaming_response.schedule_cleanup() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookScheduleCleanupResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_trigger_cleanup(self, client: Nebula) -> None:
        webhook = client.webhooks.trigger_cleanup()
        assert_matches_type(WebhookTriggerCleanupResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_trigger_cleanup_with_all_params(self, client: Nebula) -> None:
        webhook = client.webhooks.trigger_cleanup(
            days=0,
        )
        assert_matches_type(WebhookTriggerCleanupResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_trigger_cleanup(self, client: Nebula) -> None:
        response = client.webhooks.with_raw_response.trigger_cleanup()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookTriggerCleanupResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_trigger_cleanup(self, client: Nebula) -> None:
        with client.webhooks.with_streaming_response.trigger_cleanup() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookTriggerCleanupResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_stats(self, async_client: AsyncNebula) -> None:
        webhook = await async_client.webhooks.get_stats()
        assert_matches_type(WebhookGetStatsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_stats(self, async_client: AsyncNebula) -> None:
        response = await async_client.webhooks.with_raw_response.get_stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookGetStatsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_stats(self, async_client: AsyncNebula) -> None:
        async with async_client.webhooks.with_streaming_response.get_stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookGetStatsResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_events(self, async_client: AsyncNebula) -> None:
        webhook = await async_client.webhooks.list_events()
        assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_events_with_all_params(self, async_client: AsyncNebula) -> None:
        webhook = await async_client.webhooks.list_events(
            limit=0,
            processing_status="processing_status",
            webhook_type="webhook_type",
        )
        assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_events(self, async_client: AsyncNebula) -> None:
        response = await async_client.webhooks.with_raw_response.list_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_events(self, async_client: AsyncNebula) -> None:
        async with async_client.webhooks.with_streaming_response.list_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_schedule_cleanup(self, async_client: AsyncNebula) -> None:
        webhook = await async_client.webhooks.schedule_cleanup()
        assert_matches_type(WebhookScheduleCleanupResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_schedule_cleanup_with_all_params(self, async_client: AsyncNebula) -> None:
        webhook = await async_client.webhooks.schedule_cleanup(
            cron_expression="cron_expression",
            retention_days=0,
        )
        assert_matches_type(WebhookScheduleCleanupResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_schedule_cleanup(self, async_client: AsyncNebula) -> None:
        response = await async_client.webhooks.with_raw_response.schedule_cleanup()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookScheduleCleanupResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_schedule_cleanup(self, async_client: AsyncNebula) -> None:
        async with async_client.webhooks.with_streaming_response.schedule_cleanup() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookScheduleCleanupResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_trigger_cleanup(self, async_client: AsyncNebula) -> None:
        webhook = await async_client.webhooks.trigger_cleanup()
        assert_matches_type(WebhookTriggerCleanupResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_trigger_cleanup_with_all_params(self, async_client: AsyncNebula) -> None:
        webhook = await async_client.webhooks.trigger_cleanup(
            days=0,
        )
        assert_matches_type(WebhookTriggerCleanupResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_trigger_cleanup(self, async_client: AsyncNebula) -> None:
        response = await async_client.webhooks.with_raw_response.trigger_cleanup()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookTriggerCleanupResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_trigger_cleanup(self, async_client: AsyncNebula) -> None:
        async with async_client.webhooks.with_streaming_response.trigger_cleanup() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookTriggerCleanupResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True
