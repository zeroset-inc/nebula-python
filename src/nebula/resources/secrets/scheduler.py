# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.secrets.scheduler_stop_response import SchedulerStopResponse
from ...types.secrets.scheduler_start_response import SchedulerStartResponse

__all__ = ["SchedulerResource", "AsyncSchedulerResource"]


class SchedulerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchedulerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return SchedulerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchedulerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return SchedulerResourceWithStreamingResponse(self)

    def start(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchedulerStartResponse:
        """Start the automatic rotation scheduler"""
        return self._post(
            "/v1/secrets/scheduler/start",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchedulerStartResponse,
        )

    def stop(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchedulerStopResponse:
        """Stop the automatic rotation scheduler"""
        return self._post(
            "/v1/secrets/scheduler/stop",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchedulerStopResponse,
        )


class AsyncSchedulerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchedulerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchedulerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchedulerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return AsyncSchedulerResourceWithStreamingResponse(self)

    async def start(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchedulerStartResponse:
        """Start the automatic rotation scheduler"""
        return await self._post(
            "/v1/secrets/scheduler/start",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchedulerStartResponse,
        )

    async def stop(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchedulerStopResponse:
        """Stop the automatic rotation scheduler"""
        return await self._post(
            "/v1/secrets/scheduler/stop",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchedulerStopResponse,
        )


class SchedulerResourceWithRawResponse:
    def __init__(self, scheduler: SchedulerResource) -> None:
        self._scheduler = scheduler

        self.start = to_raw_response_wrapper(
            scheduler.start,
        )
        self.stop = to_raw_response_wrapper(
            scheduler.stop,
        )


class AsyncSchedulerResourceWithRawResponse:
    def __init__(self, scheduler: AsyncSchedulerResource) -> None:
        self._scheduler = scheduler

        self.start = async_to_raw_response_wrapper(
            scheduler.start,
        )
        self.stop = async_to_raw_response_wrapper(
            scheduler.stop,
        )


class SchedulerResourceWithStreamingResponse:
    def __init__(self, scheduler: SchedulerResource) -> None:
        self._scheduler = scheduler

        self.start = to_streamed_response_wrapper(
            scheduler.start,
        )
        self.stop = to_streamed_response_wrapper(
            scheduler.stop,
        )


class AsyncSchedulerResourceWithStreamingResponse:
    def __init__(self, scheduler: AsyncSchedulerResource) -> None:
        self._scheduler = scheduler

        self.start = async_to_streamed_response_wrapper(
            scheduler.start,
        )
        self.stop = async_to_streamed_response_wrapper(
            scheduler.stop,
        )
