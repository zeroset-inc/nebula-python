# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import entity_resolve_duplicate_params, entity_retrieve_duplicates_params
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

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]


class EntitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return EntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return EntitiesResourceWithStreamingResponse(self)

    def resolve_duplicate(
        self,
        entity_id: str,
        *,
        action: str,
        public: bool | Omit = omit,
        target_entity_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Manually resolve duplicate relationships.

        Args:
          entity_id: Entity ID to resolve duplicates for

          action: Action to take: 'merge', 'unlink', 'change_canonical'

          target_entity_id: Target entity ID for the action

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._post(
            f"/v1/entities/{entity_id}/resolve-duplicate",
            body=maybe_transform(
                {
                    "action": action,
                    "target_entity_id": target_entity_id,
                },
                entity_resolve_duplicate_params.EntityResolveDuplicateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"public": public}, entity_resolve_duplicate_params.EntityResolveDuplicateParams),
            ),
            cast_to=object,
        )

    def retrieve_duplicates(
        self,
        entity_id: str,
        *,
        public: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get duplicate information for a specific entity.

        Args:
          entity_id: Entity ID to get duplicate information for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            f"/v1/entities/{entity_id}/duplicates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"public": public}, entity_retrieve_duplicates_params.EntityRetrieveDuplicatesParams
                ),
            ),
            cast_to=object,
        )


class AsyncEntitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return AsyncEntitiesResourceWithStreamingResponse(self)

    async def resolve_duplicate(
        self,
        entity_id: str,
        *,
        action: str,
        public: bool | Omit = omit,
        target_entity_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Manually resolve duplicate relationships.

        Args:
          entity_id: Entity ID to resolve duplicates for

          action: Action to take: 'merge', 'unlink', 'change_canonical'

          target_entity_id: Target entity ID for the action

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._post(
            f"/v1/entities/{entity_id}/resolve-duplicate",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "target_entity_id": target_entity_id,
                },
                entity_resolve_duplicate_params.EntityResolveDuplicateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"public": public}, entity_resolve_duplicate_params.EntityResolveDuplicateParams
                ),
            ),
            cast_to=object,
        )

    async def retrieve_duplicates(
        self,
        entity_id: str,
        *,
        public: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get duplicate information for a specific entity.

        Args:
          entity_id: Entity ID to get duplicate information for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            f"/v1/entities/{entity_id}/duplicates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"public": public}, entity_retrieve_duplicates_params.EntityRetrieveDuplicatesParams
                ),
            ),
            cast_to=object,
        )


class EntitiesResourceWithRawResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.resolve_duplicate = to_raw_response_wrapper(
            entities.resolve_duplicate,
        )
        self.retrieve_duplicates = to_raw_response_wrapper(
            entities.retrieve_duplicates,
        )


class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.resolve_duplicate = async_to_raw_response_wrapper(
            entities.resolve_duplicate,
        )
        self.retrieve_duplicates = async_to_raw_response_wrapper(
            entities.retrieve_duplicates,
        )


class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.resolve_duplicate = to_streamed_response_wrapper(
            entities.resolve_duplicate,
        )
        self.retrieve_duplicates = to_streamed_response_wrapper(
            entities.retrieve_duplicates,
        )


class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.resolve_duplicate = async_to_streamed_response_wrapper(
            entities.resolve_duplicate,
        )
        self.retrieve_duplicates = async_to_streamed_response_wrapper(
            entities.retrieve_duplicates,
        )
