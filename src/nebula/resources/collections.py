# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    collection_list_params,
    collection_create_params,
    collection_update_params,
    collection_retrieve_by_name_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.collection_list_response import CollectionListResponse
from ..types.collection_create_response import CollectionCreateResponse
from ..types.collection_delete_response import CollectionDeleteResponse
from ..types.collection_update_response import CollectionUpdateResponse
from ..types.collection_retrieve_response import CollectionRetrieveResponse
from ..types.collection_retrieve_by_name_response import CollectionRetrieveByNameResponse

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return CollectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        workspace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionCreateResponse:
        """
        Create a new collection and automatically add the creating user to it.

        This endpoint allows authenticated users to create a new collection with a
        specified name and optional description. The user creating the collection is
        automatically added as a member.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/collections",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "workspace_id": workspace_id,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionCreateResponse,
        )

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
    ) -> CollectionRetrieveResponse:
        """
        Get details of a specific collection.

        This endpoint retrieves detailed information about a single collection
        identified by its UUID. The user must have access to the collection to view its
        details.

        Args:
          id: The unique identifier of the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/collections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        access_tier: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        generate_description: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionUpdateResponse:
        """
        Update an existing collection's configuration.

        This endpoint allows updating the name, description, and access settings of an
        existing collection. The user must have appropriate permissions to modify the
        collection.

        Args:
          id: The unique identifier of the collection to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/collections/{id}", id=id),
            body=maybe_transform(
                {
                    "access_tier": access_tier,
                    "description": description,
                    "generate_description": generate_description,
                    "name": name,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionUpdateResponse,
        )

    def list(
        self,
        *,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        name: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        owner_only: bool | Omit = omit,
        workspace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionListResponse:
        """
        Returns a paginated list of collections the authenticated user has access to.

        Results can be filtered by providing specific collection IDs. Regular users will
        only see collections they own or have access to. Superusers can see all
        collections.

        The collections are returned in order of last modification, with most recent
        first.

        Args:
          ids: A list of collection IDs to retrieve. If not provided, all collections will be
              returned.

          limit: Specifies a limit on the number of objects to return, ranging between 1
              and 1000. Defaults to 100.

          name: Filter collections by name (case-insensitive exact match).

          offset: Specifies the number of objects to skip. Defaults to 0.

          owner_only: If true, only returns collections owned by the user, not all accessible
              collections.

          workspace_id: Filter by workspace ID. Pass a UUID to scope to a workspace, or omit for all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "owner_only": owner_only,
                        "workspace_id": workspace_id,
                    },
                    collection_list_params.CollectionListParams,
                ),
            ),
            cast_to=CollectionListResponse,
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
    ) -> CollectionDeleteResponse:
        """
        Delete an existing collection.

        This endpoint allows deletion of a collection identified by its UUID. The user
        must have appropriate permissions to delete the collection. Deleting a
        collection removes all associations but does not delete the engrams within it.

        Args:
          id: The unique identifier of the collection to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/v1/collections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionDeleteResponse,
        )

    def retrieve_by_name(
        self,
        collection_name: str,
        *,
        owner_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionRetrieveByNameResponse:
        """
        Retrieve a collection by its (owner_id, name) combination.

        The authenticated user can only fetch collections they own, or, if superuser,
        from anyone.

        Args:
          collection_name: The name of the collection

          owner_id: (Superuser only) Specify the owner_id to retrieve a collection by name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_name:
            raise ValueError(f"Expected a non-empty value for `collection_name` but received {collection_name!r}")
        return self._get(
            path_template("/v1/collections/name/{collection_name}", collection_name=collection_name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"owner_id": owner_id}, collection_retrieve_by_name_params.CollectionRetrieveByNameParams
                ),
            ),
            cast_to=CollectionRetrieveByNameResponse,
        )


class AsyncCollectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return AsyncCollectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        workspace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionCreateResponse:
        """
        Create a new collection and automatically add the creating user to it.

        This endpoint allows authenticated users to create a new collection with a
        specified name and optional description. The user creating the collection is
        automatically added as a member.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/collections",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "workspace_id": workspace_id,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionCreateResponse,
        )

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
    ) -> CollectionRetrieveResponse:
        """
        Get details of a specific collection.

        This endpoint retrieves detailed information about a single collection
        identified by its UUID. The user must have access to the collection to view its
        details.

        Args:
          id: The unique identifier of the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/collections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        access_tier: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        generate_description: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionUpdateResponse:
        """
        Update an existing collection's configuration.

        This endpoint allows updating the name, description, and access settings of an
        existing collection. The user must have appropriate permissions to modify the
        collection.

        Args:
          id: The unique identifier of the collection to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/collections/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "access_tier": access_tier,
                    "description": description,
                    "generate_description": generate_description,
                    "name": name,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionUpdateResponse,
        )

    async def list(
        self,
        *,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        name: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        owner_only: bool | Omit = omit,
        workspace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionListResponse:
        """
        Returns a paginated list of collections the authenticated user has access to.

        Results can be filtered by providing specific collection IDs. Regular users will
        only see collections they own or have access to. Superusers can see all
        collections.

        The collections are returned in order of last modification, with most recent
        first.

        Args:
          ids: A list of collection IDs to retrieve. If not provided, all collections will be
              returned.

          limit: Specifies a limit on the number of objects to return, ranging between 1
              and 1000. Defaults to 100.

          name: Filter collections by name (case-insensitive exact match).

          offset: Specifies the number of objects to skip. Defaults to 0.

          owner_only: If true, only returns collections owned by the user, not all accessible
              collections.

          workspace_id: Filter by workspace ID. Pass a UUID to scope to a workspace, or omit for all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "owner_only": owner_only,
                        "workspace_id": workspace_id,
                    },
                    collection_list_params.CollectionListParams,
                ),
            ),
            cast_to=CollectionListResponse,
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
    ) -> CollectionDeleteResponse:
        """
        Delete an existing collection.

        This endpoint allows deletion of a collection identified by its UUID. The user
        must have appropriate permissions to delete the collection. Deleting a
        collection removes all associations but does not delete the engrams within it.

        Args:
          id: The unique identifier of the collection to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/v1/collections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionDeleteResponse,
        )

    async def retrieve_by_name(
        self,
        collection_name: str,
        *,
        owner_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionRetrieveByNameResponse:
        """
        Retrieve a collection by its (owner_id, name) combination.

        The authenticated user can only fetch collections they own, or, if superuser,
        from anyone.

        Args:
          collection_name: The name of the collection

          owner_id: (Superuser only) Specify the owner_id to retrieve a collection by name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_name:
            raise ValueError(f"Expected a non-empty value for `collection_name` but received {collection_name!r}")
        return await self._get(
            path_template("/v1/collections/name/{collection_name}", collection_name=collection_name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"owner_id": owner_id}, collection_retrieve_by_name_params.CollectionRetrieveByNameParams
                ),
            ),
            cast_to=CollectionRetrieveByNameResponse,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_raw_response_wrapper(
            collections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            collections.update,
        )
        self.list = to_raw_response_wrapper(
            collections.list,
        )
        self.delete = to_raw_response_wrapper(
            collections.delete,
        )
        self.retrieve_by_name = to_raw_response_wrapper(
            collections.retrieve_by_name,
        )


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_raw_response_wrapper(
            collections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            collections.update,
        )
        self.list = async_to_raw_response_wrapper(
            collections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            collections.delete,
        )
        self.retrieve_by_name = async_to_raw_response_wrapper(
            collections.retrieve_by_name,
        )


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_streamed_response_wrapper(
            collections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            collections.update,
        )
        self.list = to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = to_streamed_response_wrapper(
            collections.delete,
        )
        self.retrieve_by_name = to_streamed_response_wrapper(
            collections.retrieve_by_name,
        )


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_streamed_response_wrapper(
            collections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            collections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            collections.delete,
        )
        self.retrieve_by_name = async_to_streamed_response_wrapper(
            collections.retrieve_by_name,
        )
