# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.memories.nebula_results_engram_response import NebulaResultsEngramResponse

__all__ = ["MetadataResource", "AsyncMetadataResource"]


class MetadataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return MetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return MetadataResourceWithStreamingResponse(self)

    def append(
        self,
        id: str,
        *,
        body: Iterable[Dict[str, object]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsEngramResponse:
        """Appends metadata to an engram.

        This endpoint allows adding new metadata fields
        or updating existing ones.

        Args:
          id: The ID of the engram to append metadata to.

          body: Metadata to append to the engram.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/v1/memories/{id}/metadata",
            body=maybe_transform(body, Iterable[Dict[str, object]]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsEngramResponse,
        )

    def replace(
        self,
        id: str,
        *,
        body: Iterable[Dict[str, object]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsEngramResponse:
        """Replaces metadata in an engram.

        This endpoint allows overwriting existing
        metadata fields.

        Args:
          id: The ID of the engram to append metadata to.

          body: Metadata to append to the engram.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/v1/memories/{id}/metadata",
            body=maybe_transform(body, Iterable[Dict[str, object]]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsEngramResponse,
        )


class AsyncMetadataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return AsyncMetadataResourceWithStreamingResponse(self)

    async def append(
        self,
        id: str,
        *,
        body: Iterable[Dict[str, object]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsEngramResponse:
        """Appends metadata to an engram.

        This endpoint allows adding new metadata fields
        or updating existing ones.

        Args:
          id: The ID of the engram to append metadata to.

          body: Metadata to append to the engram.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/v1/memories/{id}/metadata",
            body=await async_maybe_transform(body, Iterable[Dict[str, object]]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsEngramResponse,
        )

    async def replace(
        self,
        id: str,
        *,
        body: Iterable[Dict[str, object]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsEngramResponse:
        """Replaces metadata in an engram.

        This endpoint allows overwriting existing
        metadata fields.

        Args:
          id: The ID of the engram to append metadata to.

          body: Metadata to append to the engram.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/v1/memories/{id}/metadata",
            body=await async_maybe_transform(body, Iterable[Dict[str, object]]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsEngramResponse,
        )


class MetadataResourceWithRawResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

        self.append = to_raw_response_wrapper(
            metadata.append,
        )
        self.replace = to_raw_response_wrapper(
            metadata.replace,
        )


class AsyncMetadataResourceWithRawResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.append = async_to_raw_response_wrapper(
            metadata.append,
        )
        self.replace = async_to_raw_response_wrapper(
            metadata.replace,
        )


class MetadataResourceWithStreamingResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

        self.append = to_streamed_response_wrapper(
            metadata.append,
        )
        self.replace = to_streamed_response_wrapper(
            metadata.replace,
        )


class AsyncMetadataResourceWithStreamingResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.append = async_to_streamed_response_wrapper(
            metadata.append,
        )
        self.replace = async_to_streamed_response_wrapper(
            metadata.replace,
        )
