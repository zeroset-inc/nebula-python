# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import contradiction_cascade_invalidation_params
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

__all__ = ["ContradictionsResource", "AsyncContradictionsResource"]


class ContradictionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContradictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return ContradictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContradictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return ContradictionsResourceWithStreamingResponse(self)

    def cascade_invalidation(
        self,
        relationship_id: str,
        *,
        max_depth: int | Omit = omit,
        min_confidence_threshold: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Return IDs invalidated via cascading dependency logic and expire them.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not relationship_id:
            raise ValueError(f"Expected a non-empty value for `relationship_id` but received {relationship_id!r}")
        return self._post(
            path_template("/v1/contradictions/{relationship_id}/cascade", relationship_id=relationship_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "max_depth": max_depth,
                        "min_confidence_threshold": min_confidence_threshold,
                    },
                    contradiction_cascade_invalidation_params.ContradictionCascadeInvalidationParams,
                ),
            ),
            cast_to=object,
        )


class AsyncContradictionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContradictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContradictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContradictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return AsyncContradictionsResourceWithStreamingResponse(self)

    async def cascade_invalidation(
        self,
        relationship_id: str,
        *,
        max_depth: int | Omit = omit,
        min_confidence_threshold: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Return IDs invalidated via cascading dependency logic and expire them.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not relationship_id:
            raise ValueError(f"Expected a non-empty value for `relationship_id` but received {relationship_id!r}")
        return await self._post(
            path_template("/v1/contradictions/{relationship_id}/cascade", relationship_id=relationship_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "max_depth": max_depth,
                        "min_confidence_threshold": min_confidence_threshold,
                    },
                    contradiction_cascade_invalidation_params.ContradictionCascadeInvalidationParams,
                ),
            ),
            cast_to=object,
        )


class ContradictionsResourceWithRawResponse:
    def __init__(self, contradictions: ContradictionsResource) -> None:
        self._contradictions = contradictions

        self.cascade_invalidation = to_raw_response_wrapper(
            contradictions.cascade_invalidation,
        )


class AsyncContradictionsResourceWithRawResponse:
    def __init__(self, contradictions: AsyncContradictionsResource) -> None:
        self._contradictions = contradictions

        self.cascade_invalidation = async_to_raw_response_wrapper(
            contradictions.cascade_invalidation,
        )


class ContradictionsResourceWithStreamingResponse:
    def __init__(self, contradictions: ContradictionsResource) -> None:
        self._contradictions = contradictions

        self.cascade_invalidation = to_streamed_response_wrapper(
            contradictions.cascade_invalidation,
        )


class AsyncContradictionsResourceWithStreamingResponse:
    def __init__(self, contradictions: AsyncContradictionsResource) -> None:
        self._contradictions = contradictions

        self.cascade_invalidation = async_to_streamed_response_wrapper(
            contradictions.cascade_invalidation,
        )
