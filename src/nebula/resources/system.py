# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.system_retrieve_status_response import SystemRetrieveStatusResponse
from ..types.system_retrieve_settings_response import SystemRetrieveSettingsResponse

__all__ = ["SystemResource", "AsyncSystemResource"]


class SystemResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SystemResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return SystemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SystemResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return SystemResourceWithStreamingResponse(self)

    def retrieve_settings(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SystemRetrieveSettingsResponse:
        """App Settings"""
        return self._get(
            "/v1/system/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SystemRetrieveSettingsResponse,
        )

    def retrieve_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SystemRetrieveStatusResponse:
        """Server Stats"""
        return self._get(
            "/v1/system/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SystemRetrieveStatusResponse,
        )


class AsyncSystemResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSystemResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSystemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSystemResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return AsyncSystemResourceWithStreamingResponse(self)

    async def retrieve_settings(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SystemRetrieveSettingsResponse:
        """App Settings"""
        return await self._get(
            "/v1/system/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SystemRetrieveSettingsResponse,
        )

    async def retrieve_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SystemRetrieveStatusResponse:
        """Server Stats"""
        return await self._get(
            "/v1/system/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SystemRetrieveStatusResponse,
        )


class SystemResourceWithRawResponse:
    def __init__(self, system: SystemResource) -> None:
        self._system = system

        self.retrieve_settings = to_raw_response_wrapper(
            system.retrieve_settings,
        )
        self.retrieve_status = to_raw_response_wrapper(
            system.retrieve_status,
        )


class AsyncSystemResourceWithRawResponse:
    def __init__(self, system: AsyncSystemResource) -> None:
        self._system = system

        self.retrieve_settings = async_to_raw_response_wrapper(
            system.retrieve_settings,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            system.retrieve_status,
        )


class SystemResourceWithStreamingResponse:
    def __init__(self, system: SystemResource) -> None:
        self._system = system

        self.retrieve_settings = to_streamed_response_wrapper(
            system.retrieve_settings,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            system.retrieve_status,
        )


class AsyncSystemResourceWithStreamingResponse:
    def __init__(self, system: AsyncSystemResource) -> None:
        self._system = system

        self.retrieve_settings = async_to_streamed_response_wrapper(
            system.retrieve_settings,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            system.retrieve_status,
        )
