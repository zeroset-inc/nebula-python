# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.analytics.collections import centrality_compute_params
from ....types.analytics.collections.centrality_status_response import CentralityStatusResponse
from ....types.analytics.collections.centrality_compute_response import CentralityComputeResponse

__all__ = ["CentralityResource", "AsyncCentralityResource"]


class CentralityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CentralityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return CentralityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CentralityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return CentralityResourceWithStreamingResponse(self)

    def compute(
        self,
        collection_id: str,
        *,
        body: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CentralityComputeResponse:
        """
        Compute and store centrality for a collection

        Args:
          collection_id: Collection ID

          body: If true, returns immediately and runs computation in background (not yet
              implemented)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._post(
            f"/v1/analytics/collections/{collection_id}/centrality/compute",
            body=maybe_transform(body, centrality_compute_params.CentralityComputeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CentralityComputeResponse,
        )

    def status(
        self,
        collection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CentralityStatusResponse:
        """
        Get centrality computation status for a collection

        Args:
          collection_id: Collection ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._get(
            f"/v1/analytics/collections/{collection_id}/centrality/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CentralityStatusResponse,
        )


class AsyncCentralityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCentralityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCentralityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCentralityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return AsyncCentralityResourceWithStreamingResponse(self)

    async def compute(
        self,
        collection_id: str,
        *,
        body: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CentralityComputeResponse:
        """
        Compute and store centrality for a collection

        Args:
          collection_id: Collection ID

          body: If true, returns immediately and runs computation in background (not yet
              implemented)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._post(
            f"/v1/analytics/collections/{collection_id}/centrality/compute",
            body=await async_maybe_transform(body, centrality_compute_params.CentralityComputeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CentralityComputeResponse,
        )

    async def status(
        self,
        collection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CentralityStatusResponse:
        """
        Get centrality computation status for a collection

        Args:
          collection_id: Collection ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._get(
            f"/v1/analytics/collections/{collection_id}/centrality/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CentralityStatusResponse,
        )


class CentralityResourceWithRawResponse:
    def __init__(self, centrality: CentralityResource) -> None:
        self._centrality = centrality

        self.compute = to_raw_response_wrapper(
            centrality.compute,
        )
        self.status = to_raw_response_wrapper(
            centrality.status,
        )


class AsyncCentralityResourceWithRawResponse:
    def __init__(self, centrality: AsyncCentralityResource) -> None:
        self._centrality = centrality

        self.compute = async_to_raw_response_wrapper(
            centrality.compute,
        )
        self.status = async_to_raw_response_wrapper(
            centrality.status,
        )


class CentralityResourceWithStreamingResponse:
    def __init__(self, centrality: CentralityResource) -> None:
        self._centrality = centrality

        self.compute = to_streamed_response_wrapper(
            centrality.compute,
        )
        self.status = to_streamed_response_wrapper(
            centrality.status,
        )


class AsyncCentralityResourceWithStreamingResponse:
    def __init__(self, centrality: AsyncCentralityResource) -> None:
        self._centrality = centrality

        self.compute = async_to_streamed_response_wrapper(
            centrality.compute,
        )
        self.status = async_to_streamed_response_wrapper(
            centrality.status,
        )
