# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import engram_retrieve_duplicate_stats_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["EngramsResource", "AsyncEngramsResource"]


class EngramsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EngramsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return EngramsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EngramsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return EngramsResourceWithStreamingResponse(self)

    def retrieve_duplicate_stats(
        self,
        engram_id: str,
        *,
        public: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get duplicate detection statistics for an engram.

        Args:
          engram_id: Engram ID to get duplicate statistics for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not engram_id:
            raise ValueError(f"Expected a non-empty value for `engram_id` but received {engram_id!r}")
        return self._get(
            path_template("/v1/engrams/{engram_id}/duplicate-stats", engram_id=engram_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"public": public}, engram_retrieve_duplicate_stats_params.EngramRetrieveDuplicateStatsParams
                ),
            ),
            cast_to=object,
        )


class AsyncEngramsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEngramsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEngramsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEngramsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return AsyncEngramsResourceWithStreamingResponse(self)

    async def retrieve_duplicate_stats(
        self,
        engram_id: str,
        *,
        public: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get duplicate detection statistics for an engram.

        Args:
          engram_id: Engram ID to get duplicate statistics for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not engram_id:
            raise ValueError(f"Expected a non-empty value for `engram_id` but received {engram_id!r}")
        return await self._get(
            path_template("/v1/engrams/{engram_id}/duplicate-stats", engram_id=engram_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"public": public}, engram_retrieve_duplicate_stats_params.EngramRetrieveDuplicateStatsParams
                ),
            ),
            cast_to=object,
        )


class EngramsResourceWithRawResponse:
    def __init__(self, engrams: EngramsResource) -> None:
        self._engrams = engrams

        self.retrieve_duplicate_stats = to_raw_response_wrapper(
            engrams.retrieve_duplicate_stats,
        )


class AsyncEngramsResourceWithRawResponse:
    def __init__(self, engrams: AsyncEngramsResource) -> None:
        self._engrams = engrams

        self.retrieve_duplicate_stats = async_to_raw_response_wrapper(
            engrams.retrieve_duplicate_stats,
        )


class EngramsResourceWithStreamingResponse:
    def __init__(self, engrams: EngramsResource) -> None:
        self._engrams = engrams

        self.retrieve_duplicate_stats = to_streamed_response_wrapper(
            engrams.retrieve_duplicate_stats,
        )


class AsyncEngramsResourceWithStreamingResponse:
    def __init__(self, engrams: AsyncEngramsResource) -> None:
        self._engrams = engrams

        self.retrieve_duplicate_stats = async_to_streamed_response_wrapper(
            engrams.retrieve_duplicate_stats,
        )
