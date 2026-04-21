# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.users.oauth import google_callback_params
from ....types.users.oauth.login_response import LoginResponse
from ....types.collections.nebula_results_generic_message_response import NebulaResultsGenericMessageResponse

__all__ = ["GoogleResource", "AsyncGoogleResource"]


class GoogleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GoogleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return GoogleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GoogleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return GoogleResourceWithStreamingResponse(self)

    def authorize(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """Redirect user to Google's OAuth 2.0 consent screen."""
        return self._get(
            "/v1/users/oauth/google/authorize",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    def callback(
        self,
        *,
        code: str,
        state: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginResponse:
        """
        Google's callback that will receive the `code` and `state`.

        We then exchange code for tokens, verify, and log the user in.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/users/oauth/google/callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code": code,
                        "state": state,
                    },
                    google_callback_params.GoogleCallbackParams,
                ),
            ),
            cast_to=LoginResponse,
        )


class AsyncGoogleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGoogleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return AsyncGoogleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGoogleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return AsyncGoogleResourceWithStreamingResponse(self)

    async def authorize(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """Redirect user to Google's OAuth 2.0 consent screen."""
        return await self._get(
            "/v1/users/oauth/google/authorize",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    async def callback(
        self,
        *,
        code: str,
        state: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginResponse:
        """
        Google's callback that will receive the `code` and `state`.

        We then exchange code for tokens, verify, and log the user in.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/users/oauth/google/callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "code": code,
                        "state": state,
                    },
                    google_callback_params.GoogleCallbackParams,
                ),
            ),
            cast_to=LoginResponse,
        )


class GoogleResourceWithRawResponse:
    def __init__(self, google: GoogleResource) -> None:
        self._google = google

        self.authorize = to_raw_response_wrapper(
            google.authorize,
        )
        self.callback = to_raw_response_wrapper(
            google.callback,
        )


class AsyncGoogleResourceWithRawResponse:
    def __init__(self, google: AsyncGoogleResource) -> None:
        self._google = google

        self.authorize = async_to_raw_response_wrapper(
            google.authorize,
        )
        self.callback = async_to_raw_response_wrapper(
            google.callback,
        )


class GoogleResourceWithStreamingResponse:
    def __init__(self, google: GoogleResource) -> None:
        self._google = google

        self.authorize = to_streamed_response_wrapper(
            google.authorize,
        )
        self.callback = to_streamed_response_wrapper(
            google.callback,
        )


class AsyncGoogleResourceWithStreamingResponse:
    def __init__(self, google: AsyncGoogleResource) -> None:
        self._google = google

        self.authorize = async_to_streamed_response_wrapper(
            google.authorize,
        )
        self.callback = async_to_streamed_response_wrapper(
            google.callback,
        )
