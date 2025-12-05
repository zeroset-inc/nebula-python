# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.memories import relationship_list_params, relationship_export_params
from ...types.memories.paginated_nebula_result_relationship import PaginatedNebulaResultRelationship

__all__ = ["RelationshipsResource", "AsyncRelationshipsResource"]


class RelationshipsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelationshipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return RelationshipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelationshipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return RelationshipsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        entity_names: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        relationship_types: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultRelationship:
        """
        Retrieves the relationships between entities that were extracted from an engram.
        These represent connections and interactions between entities found in the text.

        Users can only access relationships from engrams they own or have access to
        through collections. Results can be filtered by entity names and relationship
        types.

        Results are returned in the order they were extracted from the engram.

        Args:
          id: The ID of the engram to retrieve relationships for.

          entity_names: Filter relationships by specific entity names.

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          relationship_types: Filter relationships by specific relationship types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/memories/{id}/relationships",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_names": entity_names,
                        "limit": limit,
                        "offset": offset,
                        "relationship_types": relationship_types,
                    },
                    relationship_list_params.RelationshipListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultRelationship,
        )

    def export(
        self,
        id: str,
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
          id: The ID of the engram to export entities from.

          columns: Specific columns to export

          filters: Filters to apply to the export

          include_header: Whether to include column headers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v1/memories/{id}/relationships/export",
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

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRelationshipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelationshipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return AsyncRelationshipsResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        entity_names: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        relationship_types: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultRelationship:
        """
        Retrieves the relationships between entities that were extracted from an engram.
        These represent connections and interactions between entities found in the text.

        Users can only access relationships from engrams they own or have access to
        through collections. Results can be filtered by entity names and relationship
        types.

        Results are returned in the order they were extracted from the engram.

        Args:
          id: The ID of the engram to retrieve relationships for.

          entity_names: Filter relationships by specific entity names.

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          relationship_types: Filter relationships by specific relationship types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/memories/{id}/relationships",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "entity_names": entity_names,
                        "limit": limit,
                        "offset": offset,
                        "relationship_types": relationship_types,
                    },
                    relationship_list_params.RelationshipListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultRelationship,
        )

    async def export(
        self,
        id: str,
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
          id: The ID of the engram to export entities from.

          columns: Specific columns to export

          filters: Filters to apply to the export

          include_header: Whether to include column headers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v1/memories/{id}/relationships/export",
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

        self.list = to_raw_response_wrapper(
            relationships.list,
        )
        self.export = to_raw_response_wrapper(
            relationships.export,
        )


class AsyncRelationshipsResourceWithRawResponse:
    def __init__(self, relationships: AsyncRelationshipsResource) -> None:
        self._relationships = relationships

        self.list = async_to_raw_response_wrapper(
            relationships.list,
        )
        self.export = async_to_raw_response_wrapper(
            relationships.export,
        )


class RelationshipsResourceWithStreamingResponse:
    def __init__(self, relationships: RelationshipsResource) -> None:
        self._relationships = relationships

        self.list = to_streamed_response_wrapper(
            relationships.list,
        )
        self.export = to_streamed_response_wrapper(
            relationships.export,
        )


class AsyncRelationshipsResourceWithStreamingResponse:
    def __init__(self, relationships: AsyncRelationshipsResource) -> None:
        self._relationships = relationships

        self.list = async_to_streamed_response_wrapper(
            relationships.list,
        )
        self.export = async_to_streamed_response_wrapper(
            relationships.export,
        )
