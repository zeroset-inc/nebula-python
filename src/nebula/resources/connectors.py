# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    connector_list_params,
    connector_connect_params,
    connector_disconnect_params,
    connector_list_folders_params,
    connector_list_contents_params,
    connector_update_config_params,
)
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
from ..types.connector_list_response import ConnectorListResponse
from ..types.connector_sync_response import ConnectorSyncResponse
from ..types.connector_connect_response import ConnectorConnectResponse
from ..types.connector_retrieve_response import ConnectorRetrieveResponse
from ..types.connector_disconnect_response import ConnectorDisconnectResponse
from ..types.connector_list_folders_response import ConnectorListFoldersResponse
from ..types.connector_list_channels_response import ConnectorListChannelsResponse
from ..types.connector_list_contents_response import ConnectorListContentsResponse
from ..types.connector_update_config_response import ConnectorUpdateConfigResponse
from ..types.connector_list_providers_response import ConnectorListProvidersResponse

__all__ = ["ConnectorsResource", "AsyncConnectorsResource"]


class ConnectorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return ConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return ConnectorsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorRetrieveResponse:
        """
        Get a single connection by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            path_template("/v1/connectors/{connection_id}", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorRetrieveResponse,
        )

    def list(
        self,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListResponse:
        """
        List active connections for a collection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/connectors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"collection_id": collection_id}, connector_list_params.ConnectorListParams),
            ),
            cast_to=ConnectorListResponse,
        )

    def connect(
        self,
        provider: str,
        *,
        collection_id: str,
        config: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorConnectResponse:
        """
        Start OAuth connection flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return self._post(
            path_template("/v1/connectors/{provider}/connect", provider=provider),
            body=maybe_transform(
                {
                    "collection_id": collection_id,
                    "config": config,
                },
                connector_connect_params.ConnectorConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorConnectResponse,
        )

    def disconnect(
        self,
        connection_id: str,
        *,
        delete_memories: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorDisconnectResponse:
        """
        Disconnect an external data source

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._delete(
            path_template("/v1/connectors/{connection_id}", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"delete_memories": delete_memories}, connector_disconnect_params.ConnectorDisconnectParams
                ),
            ),
            cast_to=ConnectorDisconnectResponse,
        )

    def list_channels(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListChannelsResponse:
        """
        List Slack channels for a connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            path_template("/v1/connectors/{connection_id}/channels", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorListChannelsResponse,
        )

    def list_contents(
        self,
        connection_id: str,
        *,
        parent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListContentsResponse:
        """
        Browse Google Drive folders and files for a connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            path_template("/v1/connectors/{connection_id}/contents", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"parent_id": parent_id}, connector_list_contents_params.ConnectorListContentsParams
                ),
            ),
            cast_to=ConnectorListContentsResponse,
        )

    def list_folders(
        self,
        connection_id: str,
        *,
        parent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListFoldersResponse:
        """
        Browse Google Drive folders for a connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            path_template("/v1/connectors/{connection_id}/folders", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"parent_id": parent_id}, connector_list_folders_params.ConnectorListFoldersParams
                ),
            ),
            cast_to=ConnectorListFoldersResponse,
        )

    def list_providers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListProvidersResponse:
        """List available connector providers"""
        return self._get(
            "/v1/connectors/providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorListProvidersResponse,
        )

    def sync(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorSyncResponse:
        """
        Manually trigger a sync

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            path_template("/v1/connectors/{connection_id}/sync", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorSyncResponse,
        )

    def update_config(
        self,
        connection_id: str,
        *,
        config: Dict[str, object],
        apply: Literal["full_resync"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorUpdateConfigResponse:
        """Update connection config (e.g.

        folder selection)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._patch(
            path_template("/v1/connectors/{connection_id}/config", connection_id=connection_id),
            body=maybe_transform(
                {
                    "config": config,
                    "apply": apply,
                },
                connector_update_config_params.ConnectorUpdateConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorUpdateConfigResponse,
        )


class AsyncConnectorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return AsyncConnectorsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorRetrieveResponse:
        """
        Get a single connection by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            path_template("/v1/connectors/{connection_id}", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorRetrieveResponse,
        )

    async def list(
        self,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListResponse:
        """
        List active connections for a collection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/connectors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"collection_id": collection_id}, connector_list_params.ConnectorListParams
                ),
            ),
            cast_to=ConnectorListResponse,
        )

    async def connect(
        self,
        provider: str,
        *,
        collection_id: str,
        config: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorConnectResponse:
        """
        Start OAuth connection flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return await self._post(
            path_template("/v1/connectors/{provider}/connect", provider=provider),
            body=await async_maybe_transform(
                {
                    "collection_id": collection_id,
                    "config": config,
                },
                connector_connect_params.ConnectorConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorConnectResponse,
        )

    async def disconnect(
        self,
        connection_id: str,
        *,
        delete_memories: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorDisconnectResponse:
        """
        Disconnect an external data source

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._delete(
            path_template("/v1/connectors/{connection_id}", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"delete_memories": delete_memories}, connector_disconnect_params.ConnectorDisconnectParams
                ),
            ),
            cast_to=ConnectorDisconnectResponse,
        )

    async def list_channels(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListChannelsResponse:
        """
        List Slack channels for a connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            path_template("/v1/connectors/{connection_id}/channels", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorListChannelsResponse,
        )

    async def list_contents(
        self,
        connection_id: str,
        *,
        parent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListContentsResponse:
        """
        Browse Google Drive folders and files for a connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            path_template("/v1/connectors/{connection_id}/contents", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"parent_id": parent_id}, connector_list_contents_params.ConnectorListContentsParams
                ),
            ),
            cast_to=ConnectorListContentsResponse,
        )

    async def list_folders(
        self,
        connection_id: str,
        *,
        parent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListFoldersResponse:
        """
        Browse Google Drive folders for a connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            path_template("/v1/connectors/{connection_id}/folders", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"parent_id": parent_id}, connector_list_folders_params.ConnectorListFoldersParams
                ),
            ),
            cast_to=ConnectorListFoldersResponse,
        )

    async def list_providers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListProvidersResponse:
        """List available connector providers"""
        return await self._get(
            "/v1/connectors/providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorListProvidersResponse,
        )

    async def sync(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorSyncResponse:
        """
        Manually trigger a sync

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            path_template("/v1/connectors/{connection_id}/sync", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorSyncResponse,
        )

    async def update_config(
        self,
        connection_id: str,
        *,
        config: Dict[str, object],
        apply: Literal["full_resync"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorUpdateConfigResponse:
        """Update connection config (e.g.

        folder selection)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._patch(
            path_template("/v1/connectors/{connection_id}/config", connection_id=connection_id),
            body=await async_maybe_transform(
                {
                    "config": config,
                    "apply": apply,
                },
                connector_update_config_params.ConnectorUpdateConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorUpdateConfigResponse,
        )


class ConnectorsResourceWithRawResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.retrieve = to_raw_response_wrapper(
            connectors.retrieve,
        )
        self.list = to_raw_response_wrapper(
            connectors.list,
        )
        self.connect = to_raw_response_wrapper(
            connectors.connect,
        )
        self.disconnect = to_raw_response_wrapper(
            connectors.disconnect,
        )
        self.list_channels = to_raw_response_wrapper(
            connectors.list_channels,
        )
        self.list_contents = to_raw_response_wrapper(
            connectors.list_contents,
        )
        self.list_folders = to_raw_response_wrapper(
            connectors.list_folders,
        )
        self.list_providers = to_raw_response_wrapper(
            connectors.list_providers,
        )
        self.sync = to_raw_response_wrapper(
            connectors.sync,
        )
        self.update_config = to_raw_response_wrapper(
            connectors.update_config,
        )


class AsyncConnectorsResourceWithRawResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.retrieve = async_to_raw_response_wrapper(
            connectors.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            connectors.list,
        )
        self.connect = async_to_raw_response_wrapper(
            connectors.connect,
        )
        self.disconnect = async_to_raw_response_wrapper(
            connectors.disconnect,
        )
        self.list_channels = async_to_raw_response_wrapper(
            connectors.list_channels,
        )
        self.list_contents = async_to_raw_response_wrapper(
            connectors.list_contents,
        )
        self.list_folders = async_to_raw_response_wrapper(
            connectors.list_folders,
        )
        self.list_providers = async_to_raw_response_wrapper(
            connectors.list_providers,
        )
        self.sync = async_to_raw_response_wrapper(
            connectors.sync,
        )
        self.update_config = async_to_raw_response_wrapper(
            connectors.update_config,
        )


class ConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.retrieve = to_streamed_response_wrapper(
            connectors.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            connectors.list,
        )
        self.connect = to_streamed_response_wrapper(
            connectors.connect,
        )
        self.disconnect = to_streamed_response_wrapper(
            connectors.disconnect,
        )
        self.list_channels = to_streamed_response_wrapper(
            connectors.list_channels,
        )
        self.list_contents = to_streamed_response_wrapper(
            connectors.list_contents,
        )
        self.list_folders = to_streamed_response_wrapper(
            connectors.list_folders,
        )
        self.list_providers = to_streamed_response_wrapper(
            connectors.list_providers,
        )
        self.sync = to_streamed_response_wrapper(
            connectors.sync,
        )
        self.update_config = to_streamed_response_wrapper(
            connectors.update_config,
        )


class AsyncConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.retrieve = async_to_streamed_response_wrapper(
            connectors.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            connectors.list,
        )
        self.connect = async_to_streamed_response_wrapper(
            connectors.connect,
        )
        self.disconnect = async_to_streamed_response_wrapper(
            connectors.disconnect,
        )
        self.list_channels = async_to_streamed_response_wrapper(
            connectors.list_channels,
        )
        self.list_contents = async_to_streamed_response_wrapper(
            connectors.list_contents,
        )
        self.list_folders = async_to_streamed_response_wrapper(
            connectors.list_folders,
        )
        self.list_providers = async_to_streamed_response_wrapper(
            connectors.list_providers,
        )
        self.sync = async_to_streamed_response_wrapper(
            connectors.sync,
        )
        self.update_config = async_to_streamed_response_wrapper(
            connectors.update_config,
        )
