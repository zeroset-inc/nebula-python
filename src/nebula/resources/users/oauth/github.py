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
from ....types.users.oauth import github_callback_params
from ....types.users.oauth.login_response import LoginResponse
from ....types.collections.nebula_results_generic_message_response import NebulaResultsGenericMessageResponse

__all__ = ["GitHubResource", "AsyncGitHubResource"]


class GitHubResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GitHubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return GitHubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitHubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return GitHubResourceWithStreamingResponse(self)

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
        """Redirect user to GitHub's OAuth consent screen."""
        return self._get(
            "/v1/users/oauth/github/authorize",
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
        GitHub callback route to exchange code for an access_token, then fetch user info
        from GitHub's API, then do the same 'oauth-based' login or registration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/users/oauth/github/callback",
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
                    github_callback_params.GitHubCallbackParams,
                ),
            ),
            cast_to=LoginResponse,
        )


class AsyncGitHubResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGitHubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGitHubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitHubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return AsyncGitHubResourceWithStreamingResponse(self)

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
        """Redirect user to GitHub's OAuth consent screen."""
        return await self._get(
            "/v1/users/oauth/github/authorize",
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
        GitHub callback route to exchange code for an access_token, then fetch user info
        from GitHub's API, then do the same 'oauth-based' login or registration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/users/oauth/github/callback",
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
                    github_callback_params.GitHubCallbackParams,
                ),
            ),
            cast_to=LoginResponse,
        )


class GitHubResourceWithRawResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

        self.authorize = to_raw_response_wrapper(
            github.authorize,
        )
        self.callback = to_raw_response_wrapper(
            github.callback,
        )


class AsyncGitHubResourceWithRawResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

        self.authorize = async_to_raw_response_wrapper(
            github.authorize,
        )
        self.callback = async_to_raw_response_wrapper(
            github.callback,
        )


class GitHubResourceWithStreamingResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

        self.authorize = to_streamed_response_wrapper(
            github.authorize,
        )
        self.callback = to_streamed_response_wrapper(
            github.callback,
        )


class AsyncGitHubResourceWithStreamingResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

        self.authorize = async_to_streamed_response_wrapper(
            github.authorize,
        )
        self.callback = async_to_streamed_response_wrapper(
            github.callback,
        )
