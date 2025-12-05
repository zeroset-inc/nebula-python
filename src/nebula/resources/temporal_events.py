# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import temporal_event_list_params
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

__all__ = ["TemporalEventsResource", "AsyncTemporalEventsResource"]


class TemporalEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TemporalEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return TemporalEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemporalEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return TemporalEventsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieve a single temporal-event by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            f"/v1/temporal-events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        event_type: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        since: Union[str, datetime, None] | Omit = omit,
        target_relationship_id: Optional[str] | Omit = omit,
        until: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Return temporal-event rows with basic filtering/pagination.

        Args:
          event_type: Filter by event_type

          since: Filter events created after this timestamp (inclusive)

          target_relationship_id: Filter by relationship UUID

          until: Filter events created before this timestamp (inclusive)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/temporal-events/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event_type": event_type,
                        "limit": limit,
                        "offset": offset,
                        "since": since,
                        "target_relationship_id": target_relationship_id,
                        "until": until,
                    },
                    temporal_event_list_params.TemporalEventListParams,
                ),
            ),
            cast_to=object,
        )


class AsyncTemporalEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTemporalEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTemporalEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemporalEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return AsyncTemporalEventsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieve a single temporal-event by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            f"/v1/temporal-events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def list(
        self,
        *,
        event_type: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        since: Union[str, datetime, None] | Omit = omit,
        target_relationship_id: Optional[str] | Omit = omit,
        until: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Return temporal-event rows with basic filtering/pagination.

        Args:
          event_type: Filter by event_type

          since: Filter events created after this timestamp (inclusive)

          target_relationship_id: Filter by relationship UUID

          until: Filter events created before this timestamp (inclusive)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/temporal-events/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "event_type": event_type,
                        "limit": limit,
                        "offset": offset,
                        "since": since,
                        "target_relationship_id": target_relationship_id,
                        "until": until,
                    },
                    temporal_event_list_params.TemporalEventListParams,
                ),
            ),
            cast_to=object,
        )


class TemporalEventsResourceWithRawResponse:
    def __init__(self, temporal_events: TemporalEventsResource) -> None:
        self._temporal_events = temporal_events

        self.retrieve = to_raw_response_wrapper(
            temporal_events.retrieve,
        )
        self.list = to_raw_response_wrapper(
            temporal_events.list,
        )


class AsyncTemporalEventsResourceWithRawResponse:
    def __init__(self, temporal_events: AsyncTemporalEventsResource) -> None:
        self._temporal_events = temporal_events

        self.retrieve = async_to_raw_response_wrapper(
            temporal_events.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            temporal_events.list,
        )


class TemporalEventsResourceWithStreamingResponse:
    def __init__(self, temporal_events: TemporalEventsResource) -> None:
        self._temporal_events = temporal_events

        self.retrieve = to_streamed_response_wrapper(
            temporal_events.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            temporal_events.list,
        )


class AsyncTemporalEventsResourceWithStreamingResponse:
    def __init__(self, temporal_events: AsyncTemporalEventsResource) -> None:
        self._temporal_events = temporal_events

        self.retrieve = async_to_streamed_response_wrapper(
            temporal_events.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            temporal_events.list,
        )
