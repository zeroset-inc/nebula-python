# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .centrality import (
    CentralityResource,
    AsyncCentralityResource,
    CentralityResourceWithRawResponse,
    AsyncCentralityResourceWithRawResponse,
    CentralityResourceWithStreamingResponse,
    AsyncCentralityResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    @cached_property
    def centrality(self) -> CentralityResource:
        return CentralityResource(self._client)

    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return CollectionsResourceWithStreamingResponse(self)


class AsyncCollectionsResource(AsyncAPIResource):
    @cached_property
    def centrality(self) -> AsyncCentralityResource:
        return AsyncCentralityResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nebula-python#with_streaming_response
        """
        return AsyncCollectionsResourceWithStreamingResponse(self)


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

    @cached_property
    def centrality(self) -> CentralityResourceWithRawResponse:
        return CentralityResourceWithRawResponse(self._collections.centrality)


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

    @cached_property
    def centrality(self) -> AsyncCentralityResourceWithRawResponse:
        return AsyncCentralityResourceWithRawResponse(self._collections.centrality)


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

    @cached_property
    def centrality(self) -> CentralityResourceWithStreamingResponse:
        return CentralityResourceWithStreamingResponse(self._collections.centrality)


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

    @cached_property
    def centrality(self) -> AsyncCentralityResourceWithStreamingResponse:
        return AsyncCentralityResourceWithStreamingResponse(self._collections.centrality)
