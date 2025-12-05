# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import webhook_list_events_params, webhook_trigger_cleanup_params, webhook_schedule_cleanup_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.webhook_get_stats_response import WebhookGetStatsResponse
from ..types.webhook_list_events_response import WebhookListEventsResponse
from ..types.webhook_trigger_cleanup_response import WebhookTriggerCleanupResponse
from ..types.webhook_schedule_cleanup_response import WebhookScheduleCleanupResponse

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)

    def get_stats(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookGetStatsResponse:
        """Get statistics about webhook events for monitoring dashboard."""
        return self._get(
            "/v1/webhooks/stats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookGetStatsResponse,
        )

    def list_events(
        self,
        *,
        limit: int | Omit = omit,
        processing_status: Optional[str] | Omit = omit,
        webhook_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListEventsResponse:
        """
        Get recent webhook events for monitoring.

        Args: webhook_type: Filter by webhook type (e.g., 'subscription_sync')
        processing_status: Filter by status ('processed', 'failed', 'retry') limit:
        Maximum number of events to return (default 100)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/webhooks/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "processing_status": processing_status,
                        "webhook_type": webhook_type,
                    },
                    webhook_list_events_params.WebhookListEventsParams,
                ),
            ),
            cast_to=WebhookListEventsResponse,
        )

    def schedule_cleanup(
        self,
        *,
        cron_expression: str | Omit = omit,
        retention_days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookScheduleCleanupResponse:
        """
        Schedule periodic cleanup of webhook events using cron expression.

        Args: cron_expression: Cron expression for scheduling (default: daily at
        midnight) retention_days: Delete events older than this many days (default 90)

        Common cron expressions: - "0 0 \\** \\** _" - Daily at midnight - "0 _/6 \\** \\** _" -
        Every 6 hours - "0 0 _ _ 0" - Weekly on Sunday at midnight - "0 0 1 _ \\**" -
        Monthly on the 1st at midnight

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/webhooks/schedule-cleanup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cron_expression": cron_expression,
                        "retention_days": retention_days,
                    },
                    webhook_schedule_cleanup_params.WebhookScheduleCleanupParams,
                ),
            ),
            cast_to=WebhookScheduleCleanupResponse,
        )

    def trigger_cleanup(
        self,
        *,
        days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookTriggerCleanupResponse:
        """
        Trigger Hatchet workflow to clean up old webhook events.

        Args: days: Delete events older than this many days (default 90)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/webhooks/cleanup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"days": days}, webhook_trigger_cleanup_params.WebhookTriggerCleanupParams),
            ),
            cast_to=WebhookTriggerCleanupResponse,
        )


class AsyncWebhooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)

    async def get_stats(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookGetStatsResponse:
        """Get statistics about webhook events for monitoring dashboard."""
        return await self._get(
            "/v1/webhooks/stats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookGetStatsResponse,
        )

    async def list_events(
        self,
        *,
        limit: int | Omit = omit,
        processing_status: Optional[str] | Omit = omit,
        webhook_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListEventsResponse:
        """
        Get recent webhook events for monitoring.

        Args: webhook_type: Filter by webhook type (e.g., 'subscription_sync')
        processing_status: Filter by status ('processed', 'failed', 'retry') limit:
        Maximum number of events to return (default 100)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/webhooks/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "processing_status": processing_status,
                        "webhook_type": webhook_type,
                    },
                    webhook_list_events_params.WebhookListEventsParams,
                ),
            ),
            cast_to=WebhookListEventsResponse,
        )

    async def schedule_cleanup(
        self,
        *,
        cron_expression: str | Omit = omit,
        retention_days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookScheduleCleanupResponse:
        """
        Schedule periodic cleanup of webhook events using cron expression.

        Args: cron_expression: Cron expression for scheduling (default: daily at
        midnight) retention_days: Delete events older than this many days (default 90)

        Common cron expressions: - "0 0 \\** \\** _" - Daily at midnight - "0 _/6 \\** \\** _" -
        Every 6 hours - "0 0 _ _ 0" - Weekly on Sunday at midnight - "0 0 1 _ \\**" -
        Monthly on the 1st at midnight

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/webhooks/schedule-cleanup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cron_expression": cron_expression,
                        "retention_days": retention_days,
                    },
                    webhook_schedule_cleanup_params.WebhookScheduleCleanupParams,
                ),
            ),
            cast_to=WebhookScheduleCleanupResponse,
        )

    async def trigger_cleanup(
        self,
        *,
        days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookTriggerCleanupResponse:
        """
        Trigger Hatchet workflow to clean up old webhook events.

        Args: days: Delete events older than this many days (default 90)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/webhooks/cleanup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"days": days}, webhook_trigger_cleanup_params.WebhookTriggerCleanupParams
                ),
            ),
            cast_to=WebhookTriggerCleanupResponse,
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.get_stats = to_raw_response_wrapper(
            webhooks.get_stats,
        )
        self.list_events = to_raw_response_wrapper(
            webhooks.list_events,
        )
        self.schedule_cleanup = to_raw_response_wrapper(
            webhooks.schedule_cleanup,
        )
        self.trigger_cleanup = to_raw_response_wrapper(
            webhooks.trigger_cleanup,
        )


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.get_stats = async_to_raw_response_wrapper(
            webhooks.get_stats,
        )
        self.list_events = async_to_raw_response_wrapper(
            webhooks.list_events,
        )
        self.schedule_cleanup = async_to_raw_response_wrapper(
            webhooks.schedule_cleanup,
        )
        self.trigger_cleanup = async_to_raw_response_wrapper(
            webhooks.trigger_cleanup,
        )


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.get_stats = to_streamed_response_wrapper(
            webhooks.get_stats,
        )
        self.list_events = to_streamed_response_wrapper(
            webhooks.list_events,
        )
        self.schedule_cleanup = to_streamed_response_wrapper(
            webhooks.schedule_cleanup,
        )
        self.trigger_cleanup = to_streamed_response_wrapper(
            webhooks.trigger_cleanup,
        )


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.get_stats = async_to_streamed_response_wrapper(
            webhooks.get_stats,
        )
        self.list_events = async_to_streamed_response_wrapper(
            webhooks.list_events,
        )
        self.schedule_cleanup = async_to_streamed_response_wrapper(
            webhooks.schedule_cleanup,
        )
        self.trigger_cleanup = async_to_streamed_response_wrapper(
            webhooks.trigger_cleanup,
        )
