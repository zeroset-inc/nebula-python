# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import source_list_params, source_delete_params, source_search_params, source_update_params
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
from ..types.source_list_response import SourceListResponse
from ..types.source_delete_response import SourceDeleteResponse
from ..types.source_search_response import SourceSearchResponse
from ..types.source_update_response import SourceUpdateResponse

__all__ = ["SourcesResource", "AsyncSourcesResource"]


class SourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return SourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return SourcesResourceWithStreamingResponse(self)

    def update(
        self,
        id: str,
        *,
        content: str,
        collection_id: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceUpdateResponse:
        """
        Update an existing source's content and/or metadata.

        The source's vectors will be automatically recomputed based on the new content.
        Users can only update sources they own unless they are superusers.

        Args:
          collection_id: Collection context for copy-on-write. If provided and the parent engram is
              shared across multiple collections, a collection-specific copy will be created
              before applying the update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/sources/{id}", id=id),
            body=maybe_transform(
                {
                    "content": content,
                    "metadata": metadata,
                },
                source_update_params.SourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"collection_id": collection_id}, source_update_params.SourceUpdateParams),
            ),
            cast_to=SourceUpdateResponse,
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
    ) -> SourceListResponse:
        """
        List sources with pagination support.

        Returns a paginated list of sources that the user has access to. Results can be
        filtered and sorted based on various parameters. Vector embeddings are only
        included if specifically requested.

        Regular users can only list sources they own or have access to through
        collections. Superusers can list all sources in the system.

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
            "/v1/sources",
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
                    source_list_params.SourceListParams,
                ),
            ),
            cast_to=SourceListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        collection_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceDeleteResponse:
        """
        Delete a specific source by ID.

        This permanently removes the source and its associated vector embeddings. The
        parent engram remains unchanged. Users can only delete sources they own unless
        they are superusers.

        Args:
          collection_id: Collection context for copy-on-write. If provided and the parent engram is
              shared across multiple collections, a collection-specific copy will be created
              before applying the delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/v1/sources/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"collection_id": collection_id}, source_delete_params.SourceDeleteParams),
            ),
            cast_to=SourceDeleteResponse,
        )

    def search(
        self,
        *,
        query: str,
        search_settings: source_search_params.SearchSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceSearchResponse:
        """
        Perform a semantic search query over all stored sources.

        This endpoint allows for complex filtering of search results using
        PostgreSQL-based queries. Filters can be applied to various fields such as
        engram_id, and internal metadata values.

        Allowed operators include `eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `like`,
        `ilike`, `in`, and `nin`.

        Args:
          search_settings: Advanced search settings for fine-tuning search behavior.

              Note: Core parameters (query, collection_ids, filters) are now top-level API
              parameters. This class contains advanced tuning options plus internal fields
              used by the retrieval service.

              Memory search uses `effort` (auto/low/medium/high) to control compute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/sources/search",
            body=maybe_transform(
                {
                    "query": query,
                    "search_settings": search_settings,
                },
                source_search_params.SourceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceSearchResponse,
        )


class AsyncSourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return AsyncSourcesResourceWithStreamingResponse(self)

    async def update(
        self,
        id: str,
        *,
        content: str,
        collection_id: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceUpdateResponse:
        """
        Update an existing source's content and/or metadata.

        The source's vectors will be automatically recomputed based on the new content.
        Users can only update sources they own unless they are superusers.

        Args:
          collection_id: Collection context for copy-on-write. If provided and the parent engram is
              shared across multiple collections, a collection-specific copy will be created
              before applying the update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/sources/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "content": content,
                    "metadata": metadata,
                },
                source_update_params.SourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"collection_id": collection_id}, source_update_params.SourceUpdateParams
                ),
            ),
            cast_to=SourceUpdateResponse,
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
    ) -> SourceListResponse:
        """
        List sources with pagination support.

        Returns a paginated list of sources that the user has access to. Results can be
        filtered and sorted based on various parameters. Vector embeddings are only
        included if specifically requested.

        Regular users can only list sources they own or have access to through
        collections. Superusers can list all sources in the system.

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
            "/v1/sources",
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
                    source_list_params.SourceListParams,
                ),
            ),
            cast_to=SourceListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        collection_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceDeleteResponse:
        """
        Delete a specific source by ID.

        This permanently removes the source and its associated vector embeddings. The
        parent engram remains unchanged. Users can only delete sources they own unless
        they are superusers.

        Args:
          collection_id: Collection context for copy-on-write. If provided and the parent engram is
              shared across multiple collections, a collection-specific copy will be created
              before applying the delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/v1/sources/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"collection_id": collection_id}, source_delete_params.SourceDeleteParams
                ),
            ),
            cast_to=SourceDeleteResponse,
        )

    async def search(
        self,
        *,
        query: str,
        search_settings: source_search_params.SearchSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceSearchResponse:
        """
        Perform a semantic search query over all stored sources.

        This endpoint allows for complex filtering of search results using
        PostgreSQL-based queries. Filters can be applied to various fields such as
        engram_id, and internal metadata values.

        Allowed operators include `eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `like`,
        `ilike`, `in`, and `nin`.

        Args:
          search_settings: Advanced search settings for fine-tuning search behavior.

              Note: Core parameters (query, collection_ids, filters) are now top-level API
              parameters. This class contains advanced tuning options plus internal fields
              used by the retrieval service.

              Memory search uses `effort` (auto/low/medium/high) to control compute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/sources/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "search_settings": search_settings,
                },
                source_search_params.SourceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceSearchResponse,
        )


class SourcesResourceWithRawResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.update = to_raw_response_wrapper(
            sources.update,
        )
        self.list = to_raw_response_wrapper(
            sources.list,
        )
        self.delete = to_raw_response_wrapper(
            sources.delete,
        )
        self.search = to_raw_response_wrapper(
            sources.search,
        )


class AsyncSourcesResourceWithRawResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.update = async_to_raw_response_wrapper(
            sources.update,
        )
        self.list = async_to_raw_response_wrapper(
            sources.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sources.delete,
        )
        self.search = async_to_raw_response_wrapper(
            sources.search,
        )


class SourcesResourceWithStreamingResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.update = to_streamed_response_wrapper(
            sources.update,
        )
        self.list = to_streamed_response_wrapper(
            sources.list,
        )
        self.delete = to_streamed_response_wrapper(
            sources.delete,
        )
        self.search = to_streamed_response_wrapper(
            sources.search,
        )


class AsyncSourcesResourceWithStreamingResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.update = async_to_streamed_response_wrapper(
            sources.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sources.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sources.delete,
        )
        self.search = async_to_streamed_response_wrapper(
            sources.search,
        )
