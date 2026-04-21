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
from ...types.graphs import entity_list_params, entity_create_params, entity_export_params, entity_update_params
from ...types.graphs.nebula_results_entity import NebulaResultsEntity
from ...types.memories.paginated_nebula_result_entity import PaginatedNebulaResultEntity
from ...types.nebula_results_generic_boolean_response import NebulaResultsGenericBooleanResponse

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]


class EntitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return EntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return EntitiesResourceWithStreamingResponse(self)

    def create(
        self,
        collection_id: str,
        *,
        description: str,
        name: str,
        category: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsEntity:
        """
        Creates a new entity in the graph.

        Args:
          collection_id: The collection ID corresponding to the graph to add the entity to.

          description: The description of the entity to create.

          name: The name of the entity to create.

          category: The category of the entity to create.

          metadata: The metadata of the entity to create.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._post(
            path_template("/v1/graphs/{collection_id}/entities", collection_id=collection_id),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "category": category,
                    "metadata": metadata,
                },
                entity_create_params.EntityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsEntity,
        )

    def retrieve(
        self,
        entity_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsEntity:
        """
        Retrieves a specific entity by its ID.

        Args:
          collection_id: The collection ID corresponding to the graph containing the entity.

          entity_id: The ID of the entity to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            path_template(
                "/v1/graphs/{collection_id}/entities/{entity_id}", collection_id=collection_id, entity_id=entity_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsEntity,
        )

    def update(
        self,
        entity_id: str,
        *,
        collection_id: str,
        name: Optional[str],
        category: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsEntity:
        """
        Updates an existing entity in the graph.

        Args:
          collection_id: The collection ID corresponding to the graph containing the entity.

          entity_id: The ID of the entity to update.

          name: The updated name of the entity.

          category: The updated category of the entity.

          description: The updated description of the entity.

          metadata: The updated metadata of the entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._post(
            path_template(
                "/v1/graphs/{collection_id}/entities/{entity_id}", collection_id=collection_id, entity_id=entity_id
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "category": category,
                    "description": description,
                    "metadata": metadata,
                },
                entity_update_params.EntityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsEntity,
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
    ) -> PaginatedNebulaResultEntity:
        """
        Lists all entities in the graph with pagination support.

        Args:
          collection_id: The collection ID corresponding to the graph to list entities from.

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
            path_template("/v1/graphs/{collection_id}/entities", collection_id=collection_id),
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
                    entity_list_params.EntityListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultEntity,
        )

    def delete(
        self,
        entity_id: str,
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
        Removes an entity from the graph.

        Args:
          collection_id: The collection ID corresponding to the graph to remove the entity from.

          entity_id: The ID of the entity to remove from the graph.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._delete(
            path_template(
                "/v1/graphs/{collection_id}/entities/{entity_id}", collection_id=collection_id, entity_id=entity_id
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
          collection_id: The ID of the collection to export entities from.

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
            path_template("/v1/graphs/{collection_id}/entities/export", collection_id=collection_id),
            body=maybe_transform(
                {
                    "columns": columns,
                    "filters": filters,
                    "include_header": include_header,
                },
                entity_export_params.EntityExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncEntitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return AsyncEntitiesResourceWithStreamingResponse(self)

    async def create(
        self,
        collection_id: str,
        *,
        description: str,
        name: str,
        category: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsEntity:
        """
        Creates a new entity in the graph.

        Args:
          collection_id: The collection ID corresponding to the graph to add the entity to.

          description: The description of the entity to create.

          name: The name of the entity to create.

          category: The category of the entity to create.

          metadata: The metadata of the entity to create.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._post(
            path_template("/v1/graphs/{collection_id}/entities", collection_id=collection_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "category": category,
                    "metadata": metadata,
                },
                entity_create_params.EntityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsEntity,
        )

    async def retrieve(
        self,
        entity_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsEntity:
        """
        Retrieves a specific entity by its ID.

        Args:
          collection_id: The collection ID corresponding to the graph containing the entity.

          entity_id: The ID of the entity to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            path_template(
                "/v1/graphs/{collection_id}/entities/{entity_id}", collection_id=collection_id, entity_id=entity_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsEntity,
        )

    async def update(
        self,
        entity_id: str,
        *,
        collection_id: str,
        name: Optional[str],
        category: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsEntity:
        """
        Updates an existing entity in the graph.

        Args:
          collection_id: The collection ID corresponding to the graph containing the entity.

          entity_id: The ID of the entity to update.

          name: The updated name of the entity.

          category: The updated category of the entity.

          description: The updated description of the entity.

          metadata: The updated metadata of the entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._post(
            path_template(
                "/v1/graphs/{collection_id}/entities/{entity_id}", collection_id=collection_id, entity_id=entity_id
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "category": category,
                    "description": description,
                    "metadata": metadata,
                },
                entity_update_params.EntityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsEntity,
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
    ) -> PaginatedNebulaResultEntity:
        """
        Lists all entities in the graph with pagination support.

        Args:
          collection_id: The collection ID corresponding to the graph to list entities from.

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
            path_template("/v1/graphs/{collection_id}/entities", collection_id=collection_id),
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
                    entity_list_params.EntityListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultEntity,
        )

    async def delete(
        self,
        entity_id: str,
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
        Removes an entity from the graph.

        Args:
          collection_id: The collection ID corresponding to the graph to remove the entity from.

          entity_id: The ID of the entity to remove from the graph.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._delete(
            path_template(
                "/v1/graphs/{collection_id}/entities/{entity_id}", collection_id=collection_id, entity_id=entity_id
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
          collection_id: The ID of the collection to export entities from.

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
            path_template("/v1/graphs/{collection_id}/entities/export", collection_id=collection_id),
            body=await async_maybe_transform(
                {
                    "columns": columns,
                    "filters": filters,
                    "include_header": include_header,
                },
                entity_export_params.EntityExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class EntitiesResourceWithRawResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.create = to_raw_response_wrapper(
            entities.create,
        )
        self.retrieve = to_raw_response_wrapper(
            entities.retrieve,
        )
        self.update = to_raw_response_wrapper(
            entities.update,
        )
        self.list = to_raw_response_wrapper(
            entities.list,
        )
        self.delete = to_raw_response_wrapper(
            entities.delete,
        )
        self.export = to_raw_response_wrapper(
            entities.export,
        )


class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.create = async_to_raw_response_wrapper(
            entities.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            entities.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            entities.update,
        )
        self.list = async_to_raw_response_wrapper(
            entities.list,
        )
        self.delete = async_to_raw_response_wrapper(
            entities.delete,
        )
        self.export = async_to_raw_response_wrapper(
            entities.export,
        )


class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.create = to_streamed_response_wrapper(
            entities.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            entities.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            entities.update,
        )
        self.list = to_streamed_response_wrapper(
            entities.list,
        )
        self.delete = to_streamed_response_wrapper(
            entities.delete,
        )
        self.export = to_streamed_response_wrapper(
            entities.export,
        )


class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.create = async_to_streamed_response_wrapper(
            entities.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            entities.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            entities.update,
        )
        self.list = async_to_streamed_response_wrapper(
            entities.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            entities.delete,
        )
        self.export = async_to_streamed_response_wrapper(
            entities.export,
        )
