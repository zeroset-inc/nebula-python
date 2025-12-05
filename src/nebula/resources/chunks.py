# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import chunk_list_params, chunk_search_params, chunk_update_params
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
from ..types.chunk_search_response import ChunkSearchResponse
from ..types.search_settings_param import SearchSettingsParam
from ..types.nebula_results_chunk_response import NebulaResultsChunkResponse
from ..types.nebula_results_generic_boolean_response import NebulaResultsGenericBooleanResponse
from ..types.paginated_nebula_result_list_chunk_response import PaginatedNebulaResultListChunkResponse

__all__ = ["ChunksResource", "AsyncChunksResource"]


class ChunksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChunksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return ChunksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChunksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return ChunksResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsChunkResponse:
        """
        Get a specific chunk by its ID.

        Returns the chunk's content, metadata, and associated engram/collection
        information. Users can only retrieve chunks they own or have access to through
        collections.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/chunks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsChunkResponse,
        )

    def update(
        self,
        path_id: str,
        *,
        body_id: str,
        text: str,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsChunkResponse:
        """
        Update an existing chunk's content and/or metadata.

        The chunk's vectors will be automatically recomputed based on the new content.
        Users can only update chunks they own unless they are superusers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._post(
            f"/v1/chunks/{path_id}",
            body=maybe_transform(
                {
                    "body_id": body_id,
                    "text": text,
                    "metadata": metadata,
                },
                chunk_update_params.ChunkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsChunkResponse,
        )

    def list(
        self,
        *,
        include_vectors: bool | Omit = omit,
        limit: int | Omit = omit,
        metadata_filter: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultListChunkResponse:
        """
        List chunks with pagination support.

        Returns a paginated list of chunks that the user has access to. Results can be
        filtered and sorted based on various parameters. Vector embeddings are only
        included if specifically requested.

        Regular users can only list chunks they own or have access to through
        collections. Superusers can list all chunks in the system.

        Args:
          include_vectors: Include vector data in response

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          metadata_filter: Filter by metadata

          offset: Specifies the number of objects to skip. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/chunks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_vectors": include_vectors,
                        "limit": limit,
                        "metadata_filter": metadata_filter,
                        "offset": offset,
                    },
                    chunk_list_params.ChunkListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultListChunkResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericBooleanResponse:
        """
        Delete a specific chunk by ID.

        This permanently removes the chunk and its associated vector embeddings. The
        parent engram remains unchanged. Users can only delete chunks they own unless
        they are superusers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/v1/chunks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
        )

    def search(
        self,
        *,
        query: str,
        search_settings: SearchSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChunkSearchResponse:
        """
        Perform a semantic search query over all stored chunks.

        This endpoint allows for complex filtering of search results using
        PostgreSQL-based queries. Filters can be applied to various fields such as
        engram_id, and internal metadata values.

        Allowed operators include `eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `like`,
        `ilike`, `in`, and `nin`.

        Args:
          search_settings: Simplified search settings with automatic hybrid search and type-specific
              limits.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/chunks/search",
            body=maybe_transform(
                {
                    "query": query,
                    "search_settings": search_settings,
                },
                chunk_search_params.ChunkSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChunkSearchResponse,
        )


class AsyncChunksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChunksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChunksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChunksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return AsyncChunksResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsChunkResponse:
        """
        Get a specific chunk by its ID.

        Returns the chunk's content, metadata, and associated engram/collection
        information. Users can only retrieve chunks they own or have access to through
        collections.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/chunks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsChunkResponse,
        )

    async def update(
        self,
        path_id: str,
        *,
        body_id: str,
        text: str,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsChunkResponse:
        """
        Update an existing chunk's content and/or metadata.

        The chunk's vectors will be automatically recomputed based on the new content.
        Users can only update chunks they own unless they are superusers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._post(
            f"/v1/chunks/{path_id}",
            body=await async_maybe_transform(
                {
                    "body_id": body_id,
                    "text": text,
                    "metadata": metadata,
                },
                chunk_update_params.ChunkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsChunkResponse,
        )

    async def list(
        self,
        *,
        include_vectors: bool | Omit = omit,
        limit: int | Omit = omit,
        metadata_filter: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultListChunkResponse:
        """
        List chunks with pagination support.

        Returns a paginated list of chunks that the user has access to. Results can be
        filtered and sorted based on various parameters. Vector embeddings are only
        included if specifically requested.

        Regular users can only list chunks they own or have access to through
        collections. Superusers can list all chunks in the system.

        Args:
          include_vectors: Include vector data in response

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          metadata_filter: Filter by metadata

          offset: Specifies the number of objects to skip. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/chunks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_vectors": include_vectors,
                        "limit": limit,
                        "metadata_filter": metadata_filter,
                        "offset": offset,
                    },
                    chunk_list_params.ChunkListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultListChunkResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericBooleanResponse:
        """
        Delete a specific chunk by ID.

        This permanently removes the chunk and its associated vector embeddings. The
        parent engram remains unchanged. Users can only delete chunks they own unless
        they are superusers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/v1/chunks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
        )

    async def search(
        self,
        *,
        query: str,
        search_settings: SearchSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChunkSearchResponse:
        """
        Perform a semantic search query over all stored chunks.

        This endpoint allows for complex filtering of search results using
        PostgreSQL-based queries. Filters can be applied to various fields such as
        engram_id, and internal metadata values.

        Allowed operators include `eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `like`,
        `ilike`, `in`, and `nin`.

        Args:
          search_settings: Simplified search settings with automatic hybrid search and type-specific
              limits.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/chunks/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "search_settings": search_settings,
                },
                chunk_search_params.ChunkSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChunkSearchResponse,
        )


class ChunksResourceWithRawResponse:
    def __init__(self, chunks: ChunksResource) -> None:
        self._chunks = chunks

        self.retrieve = to_raw_response_wrapper(
            chunks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            chunks.update,
        )
        self.list = to_raw_response_wrapper(
            chunks.list,
        )
        self.delete = to_raw_response_wrapper(
            chunks.delete,
        )
        self.search = to_raw_response_wrapper(
            chunks.search,
        )


class AsyncChunksResourceWithRawResponse:
    def __init__(self, chunks: AsyncChunksResource) -> None:
        self._chunks = chunks

        self.retrieve = async_to_raw_response_wrapper(
            chunks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            chunks.update,
        )
        self.list = async_to_raw_response_wrapper(
            chunks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            chunks.delete,
        )
        self.search = async_to_raw_response_wrapper(
            chunks.search,
        )


class ChunksResourceWithStreamingResponse:
    def __init__(self, chunks: ChunksResource) -> None:
        self._chunks = chunks

        self.retrieve = to_streamed_response_wrapper(
            chunks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            chunks.update,
        )
        self.list = to_streamed_response_wrapper(
            chunks.list,
        )
        self.delete = to_streamed_response_wrapper(
            chunks.delete,
        )
        self.search = to_streamed_response_wrapper(
            chunks.search,
        )


class AsyncChunksResourceWithStreamingResponse:
    def __init__(self, chunks: AsyncChunksResource) -> None:
        self._chunks = chunks

        self.retrieve = async_to_streamed_response_wrapper(
            chunks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            chunks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            chunks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            chunks.delete,
        )
        self.search = async_to_streamed_response_wrapper(
            chunks.search,
        )
