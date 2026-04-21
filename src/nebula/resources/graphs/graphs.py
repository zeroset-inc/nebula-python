# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import graph_list_params, graph_update_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .entities import (
    EntitiesResource,
    AsyncEntitiesResource,
    EntitiesResourceWithRawResponse,
    AsyncEntitiesResourceWithRawResponse,
    EntitiesResourceWithStreamingResponse,
    AsyncEntitiesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .communities import (
    CommunitiesResource,
    AsyncCommunitiesResource,
    CommunitiesResourceWithRawResponse,
    AsyncCommunitiesResourceWithRawResponse,
    CommunitiesResourceWithStreamingResponse,
    AsyncCommunitiesResourceWithStreamingResponse,
)
from .relationships import (
    RelationshipsResource,
    AsyncRelationshipsResource,
    RelationshipsResourceWithRawResponse,
    AsyncRelationshipsResourceWithRawResponse,
    RelationshipsResourceWithStreamingResponse,
    AsyncRelationshipsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.graph_list_response import GraphListResponse
from ...types.nebula_results_graph_response import NebulaResultsGraphResponse
from ...types.nebula_results_generic_boolean_response import NebulaResultsGenericBooleanResponse

__all__ = ["GraphsResource", "AsyncGraphsResource"]


class GraphsResource(SyncAPIResource):
    @cached_property
    def communities(self) -> CommunitiesResource:
        return CommunitiesResource(self._client)

    @cached_property
    def entities(self) -> EntitiesResource:
        return EntitiesResource(self._client)

    @cached_property
    def relationships(self) -> RelationshipsResource:
        return RelationshipsResource(self._client)

    @cached_property
    def with_raw_response(self) -> GraphsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return GraphsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GraphsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return GraphsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        collection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGraphResponse:
        """
        Retrieves detailed information about a specific graph by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._get(
            path_template("/v1/graphs/{collection_id}", collection_id=collection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGraphResponse,
        )

    def update(
        self,
        collection_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGraphResponse:
        """
        Update an existing graphs's configuration.

        This endpoint allows updating the name and description of an existing
        collection. The user must have appropriate permissions to modify the collection.

        Args:
          collection_id: The collection ID corresponding to the graph to update

          description: An optional description of the graph

          name: The name of the graph

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._post(
            path_template("/v1/graphs/{collection_id}", collection_id=collection_id),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                graph_update_params.GraphUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGraphResponse,
        )

    def list(
        self,
        *,
        collection_ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphListResponse:
        """
        Returns a paginated list of graphs the authenticated user has access to.

        Results can be filtered by providing specific graph IDs. Regular users will only
        see graphs they own or have access to. Superusers can see all graphs.

        The graphs are returned in order of last modification, with most recent first.

        Args:
          collection_ids: A list of graph IDs to retrieve. If not provided, all graphs will be returned.

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/graphs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection_ids": collection_ids,
                        "limit": limit,
                        "offset": offset,
                    },
                    graph_list_params.GraphListParams,
                ),
            ),
            cast_to=GraphListResponse,
        )

    def reset(
        self,
        collection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericBooleanResponse:
        """
        Deletes a graph and all its associated data.

        This endpoint permanently removes the specified graph along with all entities
        and relationships that belong to only this graph. The original source entities
        and relationships extracted from underlying engrams are not deleted and are
        managed through the engram lifecycle.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._post(
            path_template("/v1/graphs/{collection_id}/reset", collection_id=collection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
        )


class AsyncGraphsResource(AsyncAPIResource):
    @cached_property
    def communities(self) -> AsyncCommunitiesResource:
        return AsyncCommunitiesResource(self._client)

    @cached_property
    def entities(self) -> AsyncEntitiesResource:
        return AsyncEntitiesResource(self._client)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResource:
        return AsyncRelationshipsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGraphsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return AsyncGraphsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGraphsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return AsyncGraphsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        collection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGraphResponse:
        """
        Retrieves detailed information about a specific graph by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._get(
            path_template("/v1/graphs/{collection_id}", collection_id=collection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGraphResponse,
        )

    async def update(
        self,
        collection_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGraphResponse:
        """
        Update an existing graphs's configuration.

        This endpoint allows updating the name and description of an existing
        collection. The user must have appropriate permissions to modify the collection.

        Args:
          collection_id: The collection ID corresponding to the graph to update

          description: An optional description of the graph

          name: The name of the graph

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._post(
            path_template("/v1/graphs/{collection_id}", collection_id=collection_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                graph_update_params.GraphUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGraphResponse,
        )

    async def list(
        self,
        *,
        collection_ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphListResponse:
        """
        Returns a paginated list of graphs the authenticated user has access to.

        Results can be filtered by providing specific graph IDs. Regular users will only
        see graphs they own or have access to. Superusers can see all graphs.

        The graphs are returned in order of last modification, with most recent first.

        Args:
          collection_ids: A list of graph IDs to retrieve. If not provided, all graphs will be returned.

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/graphs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "collection_ids": collection_ids,
                        "limit": limit,
                        "offset": offset,
                    },
                    graph_list_params.GraphListParams,
                ),
            ),
            cast_to=GraphListResponse,
        )

    async def reset(
        self,
        collection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericBooleanResponse:
        """
        Deletes a graph and all its associated data.

        This endpoint permanently removes the specified graph along with all entities
        and relationships that belong to only this graph. The original source entities
        and relationships extracted from underlying engrams are not deleted and are
        managed through the engram lifecycle.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._post(
            path_template("/v1/graphs/{collection_id}/reset", collection_id=collection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
        )


class GraphsResourceWithRawResponse:
    def __init__(self, graphs: GraphsResource) -> None:
        self._graphs = graphs

        self.retrieve = to_raw_response_wrapper(
            graphs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            graphs.update,
        )
        self.list = to_raw_response_wrapper(
            graphs.list,
        )
        self.reset = to_raw_response_wrapper(
            graphs.reset,
        )

    @cached_property
    def communities(self) -> CommunitiesResourceWithRawResponse:
        return CommunitiesResourceWithRawResponse(self._graphs.communities)

    @cached_property
    def entities(self) -> EntitiesResourceWithRawResponse:
        return EntitiesResourceWithRawResponse(self._graphs.entities)

    @cached_property
    def relationships(self) -> RelationshipsResourceWithRawResponse:
        return RelationshipsResourceWithRawResponse(self._graphs.relationships)


class AsyncGraphsResourceWithRawResponse:
    def __init__(self, graphs: AsyncGraphsResource) -> None:
        self._graphs = graphs

        self.retrieve = async_to_raw_response_wrapper(
            graphs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            graphs.update,
        )
        self.list = async_to_raw_response_wrapper(
            graphs.list,
        )
        self.reset = async_to_raw_response_wrapper(
            graphs.reset,
        )

    @cached_property
    def communities(self) -> AsyncCommunitiesResourceWithRawResponse:
        return AsyncCommunitiesResourceWithRawResponse(self._graphs.communities)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithRawResponse:
        return AsyncEntitiesResourceWithRawResponse(self._graphs.entities)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResourceWithRawResponse:
        return AsyncRelationshipsResourceWithRawResponse(self._graphs.relationships)


class GraphsResourceWithStreamingResponse:
    def __init__(self, graphs: GraphsResource) -> None:
        self._graphs = graphs

        self.retrieve = to_streamed_response_wrapper(
            graphs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            graphs.update,
        )
        self.list = to_streamed_response_wrapper(
            graphs.list,
        )
        self.reset = to_streamed_response_wrapper(
            graphs.reset,
        )

    @cached_property
    def communities(self) -> CommunitiesResourceWithStreamingResponse:
        return CommunitiesResourceWithStreamingResponse(self._graphs.communities)

    @cached_property
    def entities(self) -> EntitiesResourceWithStreamingResponse:
        return EntitiesResourceWithStreamingResponse(self._graphs.entities)

    @cached_property
    def relationships(self) -> RelationshipsResourceWithStreamingResponse:
        return RelationshipsResourceWithStreamingResponse(self._graphs.relationships)


class AsyncGraphsResourceWithStreamingResponse:
    def __init__(self, graphs: AsyncGraphsResource) -> None:
        self._graphs = graphs

        self.retrieve = async_to_streamed_response_wrapper(
            graphs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            graphs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            graphs.list,
        )
        self.reset = async_to_streamed_response_wrapper(
            graphs.reset,
        )

    @cached_property
    def communities(self) -> AsyncCommunitiesResourceWithStreamingResponse:
        return AsyncCommunitiesResourceWithStreamingResponse(self._graphs.communities)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithStreamingResponse:
        return AsyncEntitiesResourceWithStreamingResponse(self._graphs.entities)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResourceWithStreamingResponse:
        return AsyncRelationshipsResourceWithStreamingResponse(self._graphs.relationships)
