# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.collections import engram_list_params
from ...types.nebula_results_generic_boolean_response import NebulaResultsGenericBooleanResponse
from ...types.collections.nebula_results_generic_message_response import NebulaResultsGenericMessageResponse
from ...types.collections.paginated_nebula_result_list_engram_response import PaginatedNebulaResultListEngramResponse

__all__ = ["EngramsResource", "AsyncEngramsResource"]


class EngramsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EngramsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return EngramsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EngramsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return EngramsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultListEngramResponse:
        """
        Get all engrams in a collection with pagination and sorting options.

        This endpoint retrieves a paginated list of engrams associated with a specific
        collection. It supports sorting options to customize the order of returned
        engrams.

        Args:
          id: The unique identifier of the collection

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/collections/{id}/engrams", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    engram_list_params.EngramListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultListEngramResponse,
        )

    def add(
        self,
        engram_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Add an engram to a collection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not engram_id:
            raise ValueError(f"Expected a non-empty value for `engram_id` but received {engram_id!r}")
        return self._post(
            path_template("/v1/collections/{id}/engrams/{engram_id}", id=id, engram_id=engram_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    def remove(
        self,
        engram_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericBooleanResponse:
        """
        Remove an engram from a collection.

        This endpoint removes the association between an engram and a collection. It
        does not delete the engram itself. The user must have permissions to modify the
        collection.

        Args:
          id: The unique identifier of the collection

          engram_id: The unique identifier of the engram to remove

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not engram_id:
            raise ValueError(f"Expected a non-empty value for `engram_id` but received {engram_id!r}")
        return self._delete(
            path_template("/v1/collections/{id}/engrams/{engram_id}", id=id, engram_id=engram_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
        )


class AsyncEngramsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEngramsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return AsyncEngramsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEngramsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return AsyncEngramsResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultListEngramResponse:
        """
        Get all engrams in a collection with pagination and sorting options.

        This endpoint retrieves a paginated list of engrams associated with a specific
        collection. It supports sorting options to customize the order of returned
        engrams.

        Args:
          id: The unique identifier of the collection

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/collections/{id}/engrams", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    engram_list_params.EngramListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultListEngramResponse,
        )

    async def add(
        self,
        engram_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Add an engram to a collection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not engram_id:
            raise ValueError(f"Expected a non-empty value for `engram_id` but received {engram_id!r}")
        return await self._post(
            path_template("/v1/collections/{id}/engrams/{engram_id}", id=id, engram_id=engram_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    async def remove(
        self,
        engram_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericBooleanResponse:
        """
        Remove an engram from a collection.

        This endpoint removes the association between an engram and a collection. It
        does not delete the engram itself. The user must have permissions to modify the
        collection.

        Args:
          id: The unique identifier of the collection

          engram_id: The unique identifier of the engram to remove

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not engram_id:
            raise ValueError(f"Expected a non-empty value for `engram_id` but received {engram_id!r}")
        return await self._delete(
            path_template("/v1/collections/{id}/engrams/{engram_id}", id=id, engram_id=engram_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
        )


class EngramsResourceWithRawResponse:
    def __init__(self, engrams: EngramsResource) -> None:
        self._engrams = engrams

        self.list = to_raw_response_wrapper(
            engrams.list,
        )
        self.add = to_raw_response_wrapper(
            engrams.add,
        )
        self.remove = to_raw_response_wrapper(
            engrams.remove,
        )


class AsyncEngramsResourceWithRawResponse:
    def __init__(self, engrams: AsyncEngramsResource) -> None:
        self._engrams = engrams

        self.list = async_to_raw_response_wrapper(
            engrams.list,
        )
        self.add = async_to_raw_response_wrapper(
            engrams.add,
        )
        self.remove = async_to_raw_response_wrapper(
            engrams.remove,
        )


class EngramsResourceWithStreamingResponse:
    def __init__(self, engrams: EngramsResource) -> None:
        self._engrams = engrams

        self.list = to_streamed_response_wrapper(
            engrams.list,
        )
        self.add = to_streamed_response_wrapper(
            engrams.add,
        )
        self.remove = to_streamed_response_wrapper(
            engrams.remove,
        )


class AsyncEngramsResourceWithStreamingResponse:
    def __init__(self, engrams: AsyncEngramsResource) -> None:
        self._engrams = engrams

        self.list = async_to_streamed_response_wrapper(
            engrams.list,
        )
        self.add = async_to_streamed_response_wrapper(
            engrams.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            engrams.remove,
        )
