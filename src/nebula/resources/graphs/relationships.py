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
    relationship_list_params,
    relationship_create_params,
    relationship_export_params,
    relationship_update_params,
)
from ...types.graphs.nebula_results_relationship import NebulaResultsRelationship
from ...types.nebula_results_generic_boolean_response import NebulaResultsGenericBooleanResponse
from ...types.memories.paginated_nebula_result_relationship import PaginatedNebulaResultRelationship

__all__ = ["RelationshipsResource", "AsyncRelationshipsResource"]


class RelationshipsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelationshipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return RelationshipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelationshipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return RelationshipsResourceWithStreamingResponse(self)

    def create(
        self,
        collection_id: str,
        *,
        description: str,
        object: str,
        object_id: str,
        predicate: str,
        subject: str,
        subject_id: str,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        weight: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsRelationship:
        """
        Creates a new relationship in the graph.

        Args:
          collection_id: The collection ID corresponding to the graph to add the relationship to.

          description: The description of the relationship to create.

          object: The object of the relationship to create.

          object_id: The ID of the object of the relationship to create.

          predicate: The predicate of the relationship to create.

          subject: The subject of the relationship to create.

          subject_id: The ID of the subject of the relationship to create.

          metadata: The metadata of the relationship to create.

          weight: The weight of the relationship to create.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._post(
            path_template("/v1/graphs/{collection_id}/relationships", collection_id=collection_id),
            body=maybe_transform(
                {
                    "description": description,
                    "object": object,
                    "object_id": object_id,
                    "predicate": predicate,
                    "subject": subject,
                    "subject_id": subject_id,
                    "metadata": metadata,
                    "weight": weight,
                },
                relationship_create_params.RelationshipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsRelationship,
        )

    def retrieve(
        self,
        relationship_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsRelationship:
        """
        Retrieves a specific relationship by its ID.

        Args:
          collection_id: The collection ID corresponding to the graph containing the relationship.

          relationship_id: The ID of the relationship to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not relationship_id:
            raise ValueError(f"Expected a non-empty value for `relationship_id` but received {relationship_id!r}")
        return self._get(
            path_template(
                "/v1/graphs/{collection_id}/relationships/{relationship_id}",
                collection_id=collection_id,
                relationship_id=relationship_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsRelationship,
        )

    def update(
        self,
        relationship_id: str,
        *,
        collection_id: str,
        object: Optional[str],
        object_id: Optional[str],
        predicate: Optional[str],
        subject: Optional[str],
        subject_id: Optional[str],
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        weight: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsRelationship:
        """
        Updates an existing relationship in the graph.

        Args:
          collection_id: The collection ID corresponding to the graph containing the relationship.

          relationship_id: The ID of the relationship to update.

          object: The updated object of the relationship.

          object_id: The updated object ID of the relationship.

          predicate: The updated predicate of the relationship.

          subject: The updated subject of the relationship.

          subject_id: The updated subject ID of the relationship.

          description: The updated description of the relationship.

          metadata: The updated metadata of the relationship.

          weight: The updated weight of the relationship.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not relationship_id:
            raise ValueError(f"Expected a non-empty value for `relationship_id` but received {relationship_id!r}")
        return self._post(
            path_template(
                "/v1/graphs/{collection_id}/relationships/{relationship_id}",
                collection_id=collection_id,
                relationship_id=relationship_id,
            ),
            body=maybe_transform(
                {
                    "object": object,
                    "object_id": object_id,
                    "predicate": predicate,
                    "subject": subject,
                    "subject_id": subject_id,
                    "description": description,
                    "metadata": metadata,
                    "weight": weight,
                },
                relationship_update_params.RelationshipUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsRelationship,
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
    ) -> PaginatedNebulaResultRelationship:
        """
        Lists all relationships in the graph with pagination support.

        Args:
          collection_id: The collection ID corresponding to the graph to list relationships from.

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
            path_template("/v1/graphs/{collection_id}/relationships", collection_id=collection_id),
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
                    relationship_list_params.RelationshipListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultRelationship,
        )

    def delete(
        self,
        relationship_id: str,
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
        Removes a relationship from the graph.

        Args:
          collection_id: The collection ID corresponding to the graph to remove the relationship from.

          relationship_id: The ID of the relationship to remove from the graph.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not relationship_id:
            raise ValueError(f"Expected a non-empty value for `relationship_id` but received {relationship_id!r}")
        return self._delete(
            path_template(
                "/v1/graphs/{collection_id}/relationships/{relationship_id}",
                collection_id=collection_id,
                relationship_id=relationship_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
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
            path_template("/v1/graphs/{collection_id}/relationships/export", collection_id=collection_id),
            body=maybe_transform(
                {
                    "columns": columns,
                    "filters": filters,
                    "include_header": include_header,
                },
                relationship_export_params.RelationshipExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncRelationshipsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelationshipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return AsyncRelationshipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelationshipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return AsyncRelationshipsResourceWithStreamingResponse(self)

    async def create(
        self,
        collection_id: str,
        *,
        description: str,
        object: str,
        object_id: str,
        predicate: str,
        subject: str,
        subject_id: str,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        weight: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsRelationship:
        """
        Creates a new relationship in the graph.

        Args:
          collection_id: The collection ID corresponding to the graph to add the relationship to.

          description: The description of the relationship to create.

          object: The object of the relationship to create.

          object_id: The ID of the object of the relationship to create.

          predicate: The predicate of the relationship to create.

          subject: The subject of the relationship to create.

          subject_id: The ID of the subject of the relationship to create.

          metadata: The metadata of the relationship to create.

          weight: The weight of the relationship to create.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._post(
            path_template("/v1/graphs/{collection_id}/relationships", collection_id=collection_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "object": object,
                    "object_id": object_id,
                    "predicate": predicate,
                    "subject": subject,
                    "subject_id": subject_id,
                    "metadata": metadata,
                    "weight": weight,
                },
                relationship_create_params.RelationshipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsRelationship,
        )

    async def retrieve(
        self,
        relationship_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsRelationship:
        """
        Retrieves a specific relationship by its ID.

        Args:
          collection_id: The collection ID corresponding to the graph containing the relationship.

          relationship_id: The ID of the relationship to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not relationship_id:
            raise ValueError(f"Expected a non-empty value for `relationship_id` but received {relationship_id!r}")
        return await self._get(
            path_template(
                "/v1/graphs/{collection_id}/relationships/{relationship_id}",
                collection_id=collection_id,
                relationship_id=relationship_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsRelationship,
        )

    async def update(
        self,
        relationship_id: str,
        *,
        collection_id: str,
        object: Optional[str],
        object_id: Optional[str],
        predicate: Optional[str],
        subject: Optional[str],
        subject_id: Optional[str],
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        weight: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsRelationship:
        """
        Updates an existing relationship in the graph.

        Args:
          collection_id: The collection ID corresponding to the graph containing the relationship.

          relationship_id: The ID of the relationship to update.

          object: The updated object of the relationship.

          object_id: The updated object ID of the relationship.

          predicate: The updated predicate of the relationship.

          subject: The updated subject of the relationship.

          subject_id: The updated subject ID of the relationship.

          description: The updated description of the relationship.

          metadata: The updated metadata of the relationship.

          weight: The updated weight of the relationship.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not relationship_id:
            raise ValueError(f"Expected a non-empty value for `relationship_id` but received {relationship_id!r}")
        return await self._post(
            path_template(
                "/v1/graphs/{collection_id}/relationships/{relationship_id}",
                collection_id=collection_id,
                relationship_id=relationship_id,
            ),
            body=await async_maybe_transform(
                {
                    "object": object,
                    "object_id": object_id,
                    "predicate": predicate,
                    "subject": subject,
                    "subject_id": subject_id,
                    "description": description,
                    "metadata": metadata,
                    "weight": weight,
                },
                relationship_update_params.RelationshipUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsRelationship,
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
    ) -> PaginatedNebulaResultRelationship:
        """
        Lists all relationships in the graph with pagination support.

        Args:
          collection_id: The collection ID corresponding to the graph to list relationships from.

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
            path_template("/v1/graphs/{collection_id}/relationships", collection_id=collection_id),
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
                    relationship_list_params.RelationshipListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultRelationship,
        )

    async def delete(
        self,
        relationship_id: str,
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
        Removes a relationship from the graph.

        Args:
          collection_id: The collection ID corresponding to the graph to remove the relationship from.

          relationship_id: The ID of the relationship to remove from the graph.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not relationship_id:
            raise ValueError(f"Expected a non-empty value for `relationship_id` but received {relationship_id!r}")
        return await self._delete(
            path_template(
                "/v1/graphs/{collection_id}/relationships/{relationship_id}",
                collection_id=collection_id,
                relationship_id=relationship_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
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
            path_template("/v1/graphs/{collection_id}/relationships/export", collection_id=collection_id),
            body=await async_maybe_transform(
                {
                    "columns": columns,
                    "filters": filters,
                    "include_header": include_header,
                },
                relationship_export_params.RelationshipExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class RelationshipsResourceWithRawResponse:
    def __init__(self, relationships: RelationshipsResource) -> None:
        self._relationships = relationships

        self.create = to_raw_response_wrapper(
            relationships.create,
        )
        self.retrieve = to_raw_response_wrapper(
            relationships.retrieve,
        )
        self.update = to_raw_response_wrapper(
            relationships.update,
        )
        self.list = to_raw_response_wrapper(
            relationships.list,
        )
        self.delete = to_raw_response_wrapper(
            relationships.delete,
        )
        self.export = to_raw_response_wrapper(
            relationships.export,
        )


class AsyncRelationshipsResourceWithRawResponse:
    def __init__(self, relationships: AsyncRelationshipsResource) -> None:
        self._relationships = relationships

        self.create = async_to_raw_response_wrapper(
            relationships.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            relationships.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            relationships.update,
        )
        self.list = async_to_raw_response_wrapper(
            relationships.list,
        )
        self.delete = async_to_raw_response_wrapper(
            relationships.delete,
        )
        self.export = async_to_raw_response_wrapper(
            relationships.export,
        )


class RelationshipsResourceWithStreamingResponse:
    def __init__(self, relationships: RelationshipsResource) -> None:
        self._relationships = relationships

        self.create = to_streamed_response_wrapper(
            relationships.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            relationships.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            relationships.update,
        )
        self.list = to_streamed_response_wrapper(
            relationships.list,
        )
        self.delete = to_streamed_response_wrapper(
            relationships.delete,
        )
        self.export = to_streamed_response_wrapper(
            relationships.export,
        )


class AsyncRelationshipsResourceWithStreamingResponse:
    def __init__(self, relationships: AsyncRelationshipsResource) -> None:
        self._relationships = relationships

        self.create = async_to_streamed_response_wrapper(
            relationships.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            relationships.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            relationships.update,
        )
        self.list = async_to_streamed_response_wrapper(
            relationships.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            relationships.delete,
        )
        self.export = async_to_streamed_response_wrapper(
            relationships.export,
        )
