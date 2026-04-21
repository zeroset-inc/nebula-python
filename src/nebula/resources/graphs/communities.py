# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.graphs import (
    community_list_params,
    community_build_params,
    community_create_params,
    community_export_params,
    community_update_params,
)
from ...types.graphs.community_list_response import CommunityListResponse
from ...types.graphs.nebula_results_community import NebulaResultsCommunity
from ...types.nebula_results_generic_boolean_response import NebulaResultsGenericBooleanResponse
from ...types.collections.nebula_results_generic_message_response import NebulaResultsGenericMessageResponse

__all__ = ["CommunitiesResource", "AsyncCommunitiesResource"]


class CommunitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommunitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return CommunitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommunitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return CommunitiesResourceWithStreamingResponse(self)

    def create(
        self,
        collection_id: str,
        *,
        name: str,
        summary: str,
        findings: Optional[SequenceNotStr[str]] | Omit = omit,
        rating: Optional[float] | Omit = omit,
        rating_explanation: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsCommunity:
        """
        Creates a new community in the graph.

        While communities are typically built automatically via the
        /graphs/{id}/communities/build endpoint, this endpoint allows you to manually
        create your own communities.

        This can be useful when you want to:

        - Define custom groupings of entities based on domain knowledge
        - Add communities that weren't detected by the automatic process
        - Create hierarchical organization structures
        - Tag groups of entities with specific metadata

        The created communities will be integrated with any existing automatically
        detected communities in the graph's community structure.

        Args:
          collection_id: The collection ID corresponding to the graph to create the community in.

          name: The name of the community

          summary: A summary of the community

          findings: Findings about the community

          rating: Rating between 1 and 10

          rating_explanation: Explanation for the rating

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._post(
            path_template("/v1/graphs/{collection_id}/communities", collection_id=collection_id),
            body=maybe_transform(
                {
                    "name": name,
                    "summary": summary,
                    "findings": findings,
                    "rating": rating,
                    "rating_explanation": rating_explanation,
                },
                community_create_params.CommunityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsCommunity,
        )

    def retrieve(
        self,
        community_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsCommunity:
        """
        Retrieves a specific community by its ID.

        Args:
          collection_id: The ID of the collection to get communities for.

          community_id: The ID of the community to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        return self._get(
            path_template(
                "/v1/graphs/{collection_id}/communities/{community_id}",
                collection_id=collection_id,
                community_id=community_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsCommunity,
        )

    def update(
        self,
        community_id: str,
        *,
        collection_id: str,
        findings: Optional[SequenceNotStr[str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        rating: Optional[float] | Omit = omit,
        rating_explanation: Optional[str] | Omit = omit,
        summary: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsCommunity:
        """
        Updates an existing community in the graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        return self._post(
            path_template(
                "/v1/graphs/{collection_id}/communities/{community_id}",
                collection_id=collection_id,
                community_id=community_id,
            ),
            body=maybe_transform(
                {
                    "findings": findings,
                    "name": name,
                    "rating": rating,
                    "rating_explanation": rating_explanation,
                    "summary": summary,
                },
                community_update_params.CommunityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsCommunity,
        )

    def list(
        self,
        collection_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityListResponse:
        """
        Lists all communities in the graph with pagination support.

        Args:
          collection_id: The collection ID corresponding to the graph to get communities for.

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._get(
            path_template("/v1/graphs/{collection_id}/communities", collection_id=collection_id),
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
                    community_list_params.CommunityListParams,
                ),
            ),
            cast_to=CommunityListResponse,
        )

    def delete(
        self,
        community_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericBooleanResponse:
        """
        Delete a community

        Args:
          collection_id: The collection ID corresponding to the graph to delete the community from.

          community_id: The ID of the community to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        return self._delete(
            path_template(
                "/v1/graphs/{collection_id}/communities/{community_id}",
                collection_id=collection_id,
                community_id=community_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
        )

    def build(
        self,
        collection_id: str,
        *,
        body: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Creates communities in the graph by analyzing entity relationships and
        similarities.

        Communities are created through the following process:

        1. Analyzes entity relationships and metadata to build a similarity graph
        2. Applies advanced community detection algorithms (e.g. Leiden) to identify
           densely connected groups
        3. Creates hierarchical community structure with multiple granularity levels
        4. Generates natural language summaries and statistical insights for each
           community

        The resulting communities can be used to:

        - Understand high-level graph structure and organization
        - Identify key entity groupings and their relationships
        - Navigate and explore the graph at different levels of detail
        - Generate insights about entity clusters and their characteristics

        The community detection process is configurable through settings like: -
        Community detection algorithm parameters - Summary generation prompt

        Args:
          collection_id: The unique identifier of the collection

          body: Settings for the graph enrichment process.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._post(
            path_template("/v1/graphs/{collection_id}/communities/build", collection_id=collection_id),
            body=maybe_transform(body, community_build_params.CommunityBuildParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    def export(
        self,
        collection_id: str,
        *,
        columns: Optional[SequenceNotStr[str]] | Omit = omit,
        filters: Optional[Dict[str, object]] | Omit = omit,
        include_header: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Export engrams as a downloadable CSV file.

        Args:
          collection_id: The ID of the engram to export entities from.

          columns: Specific columns to export

          filters: Filters to apply to the export

          include_header: Whether to include column headers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._post(
            path_template("/v1/graphs/{collection_id}/communities/export", collection_id=collection_id),
            body=maybe_transform(
                {
                    "columns": columns,
                    "filters": filters,
                    "include_header": include_header,
                },
                community_export_params.CommunityExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncCommunitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommunitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return AsyncCommunitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommunitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return AsyncCommunitiesResourceWithStreamingResponse(self)

    async def create(
        self,
        collection_id: str,
        *,
        name: str,
        summary: str,
        findings: Optional[SequenceNotStr[str]] | Omit = omit,
        rating: Optional[float] | Omit = omit,
        rating_explanation: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsCommunity:
        """
        Creates a new community in the graph.

        While communities are typically built automatically via the
        /graphs/{id}/communities/build endpoint, this endpoint allows you to manually
        create your own communities.

        This can be useful when you want to:

        - Define custom groupings of entities based on domain knowledge
        - Add communities that weren't detected by the automatic process
        - Create hierarchical organization structures
        - Tag groups of entities with specific metadata

        The created communities will be integrated with any existing automatically
        detected communities in the graph's community structure.

        Args:
          collection_id: The collection ID corresponding to the graph to create the community in.

          name: The name of the community

          summary: A summary of the community

          findings: Findings about the community

          rating: Rating between 1 and 10

          rating_explanation: Explanation for the rating

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._post(
            path_template("/v1/graphs/{collection_id}/communities", collection_id=collection_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "summary": summary,
                    "findings": findings,
                    "rating": rating,
                    "rating_explanation": rating_explanation,
                },
                community_create_params.CommunityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsCommunity,
        )

    async def retrieve(
        self,
        community_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsCommunity:
        """
        Retrieves a specific community by its ID.

        Args:
          collection_id: The ID of the collection to get communities for.

          community_id: The ID of the community to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        return await self._get(
            path_template(
                "/v1/graphs/{collection_id}/communities/{community_id}",
                collection_id=collection_id,
                community_id=community_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsCommunity,
        )

    async def update(
        self,
        community_id: str,
        *,
        collection_id: str,
        findings: Optional[SequenceNotStr[str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        rating: Optional[float] | Omit = omit,
        rating_explanation: Optional[str] | Omit = omit,
        summary: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsCommunity:
        """
        Updates an existing community in the graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        return await self._post(
            path_template(
                "/v1/graphs/{collection_id}/communities/{community_id}",
                collection_id=collection_id,
                community_id=community_id,
            ),
            body=await async_maybe_transform(
                {
                    "findings": findings,
                    "name": name,
                    "rating": rating,
                    "rating_explanation": rating_explanation,
                    "summary": summary,
                },
                community_update_params.CommunityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsCommunity,
        )

    async def list(
        self,
        collection_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityListResponse:
        """
        Lists all communities in the graph with pagination support.

        Args:
          collection_id: The collection ID corresponding to the graph to get communities for.

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._get(
            path_template("/v1/graphs/{collection_id}/communities", collection_id=collection_id),
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
                    community_list_params.CommunityListParams,
                ),
            ),
            cast_to=CommunityListResponse,
        )

    async def delete(
        self,
        community_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericBooleanResponse:
        """
        Delete a community

        Args:
          collection_id: The collection ID corresponding to the graph to delete the community from.

          community_id: The ID of the community to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not community_id:
            raise ValueError(f"Expected a non-empty value for `community_id` but received {community_id!r}")
        return await self._delete(
            path_template(
                "/v1/graphs/{collection_id}/communities/{community_id}",
                collection_id=collection_id,
                community_id=community_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
        )

    async def build(
        self,
        collection_id: str,
        *,
        body: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Creates communities in the graph by analyzing entity relationships and
        similarities.

        Communities are created through the following process:

        1. Analyzes entity relationships and metadata to build a similarity graph
        2. Applies advanced community detection algorithms (e.g. Leiden) to identify
           densely connected groups
        3. Creates hierarchical community structure with multiple granularity levels
        4. Generates natural language summaries and statistical insights for each
           community

        The resulting communities can be used to:

        - Understand high-level graph structure and organization
        - Identify key entity groupings and their relationships
        - Navigate and explore the graph at different levels of detail
        - Generate insights about entity clusters and their characteristics

        The community detection process is configurable through settings like: -
        Community detection algorithm parameters - Summary generation prompt

        Args:
          collection_id: The unique identifier of the collection

          body: Settings for the graph enrichment process.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._post(
            path_template("/v1/graphs/{collection_id}/communities/build", collection_id=collection_id),
            body=await async_maybe_transform(body, community_build_params.CommunityBuildParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    async def export(
        self,
        collection_id: str,
        *,
        columns: Optional[SequenceNotStr[str]] | Omit = omit,
        filters: Optional[Dict[str, object]] | Omit = omit,
        include_header: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Export engrams as a downloadable CSV file.

        Args:
          collection_id: The ID of the engram to export entities from.

          columns: Specific columns to export

          filters: Filters to apply to the export

          include_header: Whether to include column headers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._post(
            path_template("/v1/graphs/{collection_id}/communities/export", collection_id=collection_id),
            body=await async_maybe_transform(
                {
                    "columns": columns,
                    "filters": filters,
                    "include_header": include_header,
                },
                community_export_params.CommunityExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class CommunitiesResourceWithRawResponse:
    def __init__(self, communities: CommunitiesResource) -> None:
        self._communities = communities

        self.create = to_raw_response_wrapper(
            communities.create,
        )
        self.retrieve = to_raw_response_wrapper(
            communities.retrieve,
        )
        self.update = to_raw_response_wrapper(
            communities.update,
        )
        self.list = to_raw_response_wrapper(
            communities.list,
        )
        self.delete = to_raw_response_wrapper(
            communities.delete,
        )
        self.build = to_raw_response_wrapper(
            communities.build,
        )
        self.export = to_raw_response_wrapper(
            communities.export,
        )


class AsyncCommunitiesResourceWithRawResponse:
    def __init__(self, communities: AsyncCommunitiesResource) -> None:
        self._communities = communities

        self.create = async_to_raw_response_wrapper(
            communities.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            communities.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            communities.update,
        )
        self.list = async_to_raw_response_wrapper(
            communities.list,
        )
        self.delete = async_to_raw_response_wrapper(
            communities.delete,
        )
        self.build = async_to_raw_response_wrapper(
            communities.build,
        )
        self.export = async_to_raw_response_wrapper(
            communities.export,
        )


class CommunitiesResourceWithStreamingResponse:
    def __init__(self, communities: CommunitiesResource) -> None:
        self._communities = communities

        self.create = to_streamed_response_wrapper(
            communities.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            communities.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            communities.update,
        )
        self.list = to_streamed_response_wrapper(
            communities.list,
        )
        self.delete = to_streamed_response_wrapper(
            communities.delete,
        )
        self.build = to_streamed_response_wrapper(
            communities.build,
        )
        self.export = to_streamed_response_wrapper(
            communities.export,
        )


class AsyncCommunitiesResourceWithStreamingResponse:
    def __init__(self, communities: AsyncCommunitiesResource) -> None:
        self._communities = communities

        self.create = async_to_streamed_response_wrapper(
            communities.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            communities.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            communities.update,
        )
        self.list = async_to_streamed_response_wrapper(
            communities.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            communities.delete,
        )
        self.build = async_to_streamed_response_wrapper(
            communities.build,
        )
        self.export = async_to_streamed_response_wrapper(
            communities.export,
        )
