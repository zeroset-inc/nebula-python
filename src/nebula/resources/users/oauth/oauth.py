# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .github import (
    GitHubResource,
    AsyncGitHubResource,
    GitHubResourceWithRawResponse,
    AsyncGitHubResourceWithRawResponse,
    GitHubResourceWithStreamingResponse,
    AsyncGitHubResourceWithStreamingResponse,
)
from .google import (
    GoogleResource,
    AsyncGoogleResource,
    GoogleResourceWithRawResponse,
    AsyncGoogleResourceWithRawResponse,
    GoogleResourceWithStreamingResponse,
    AsyncGoogleResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["OAuthResource", "AsyncOAuthResource"]


class OAuthResource(SyncAPIResource):
    @cached_property
    def google(self) -> GoogleResource:
        return GoogleResource(self._client)

    @cached_property
    def github(self) -> GitHubResource:
        return GitHubResource(self._client)

    @cached_property
    def with_raw_response(self) -> OAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return OAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return OAuthResourceWithStreamingResponse(self)


class AsyncOAuthResource(AsyncAPIResource):
    @cached_property
    def google(self) -> AsyncGoogleResource:
        return AsyncGoogleResource(self._client)

    @cached_property
    def github(self) -> AsyncGitHubResource:
        return AsyncGitHubResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return AsyncOAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return AsyncOAuthResourceWithStreamingResponse(self)


class OAuthResourceWithRawResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

    @cached_property
    def google(self) -> GoogleResourceWithRawResponse:
        return GoogleResourceWithRawResponse(self._oauth.google)

    @cached_property
    def github(self) -> GitHubResourceWithRawResponse:
        return GitHubResourceWithRawResponse(self._oauth.github)


class AsyncOAuthResourceWithRawResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

    @cached_property
    def google(self) -> AsyncGoogleResourceWithRawResponse:
        return AsyncGoogleResourceWithRawResponse(self._oauth.google)

    @cached_property
    def github(self) -> AsyncGitHubResourceWithRawResponse:
        return AsyncGitHubResourceWithRawResponse(self._oauth.github)


class OAuthResourceWithStreamingResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

    @cached_property
    def google(self) -> GoogleResourceWithStreamingResponse:
        return GoogleResourceWithStreamingResponse(self._oauth.google)

    @cached_property
    def github(self) -> GitHubResourceWithStreamingResponse:
        return GitHubResourceWithStreamingResponse(self._oauth.github)


class AsyncOAuthResourceWithStreamingResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

    @cached_property
    def google(self) -> AsyncGoogleResourceWithStreamingResponse:
        return AsyncGoogleResourceWithStreamingResponse(self._oauth.google)

    @cached_property
    def github(self) -> AsyncGitHubResourceWithStreamingResponse:
        return AsyncGitHubResourceWithStreamingResponse(self._oauth.github)
