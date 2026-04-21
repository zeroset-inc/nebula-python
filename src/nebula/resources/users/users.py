# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ...types import (
    user_list_params,
    user_login_params,
    user_delete_params,
    user_export_params,
    user_update_params,
    user_register_params,
    user_verify_email_params,
    user_refresh_token_params,
    user_reset_password_params,
    user_change_password_params,
    user_retrieve_metrics_params,
    user_request_password_reset_params,
    user_send_verification_email_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .api_keys import (
    APIKeysResource,
    AsyncAPIKeysResource,
    APIKeysResourceWithRawResponse,
    AsyncAPIKeysResourceWithRawResponse,
    APIKeysResourceWithStreamingResponse,
    AsyncAPIKeysResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .collections import (
    CollectionsResource,
    AsyncCollectionsResource,
    CollectionsResourceWithRawResponse,
    AsyncCollectionsResourceWithRawResponse,
    CollectionsResourceWithStreamingResponse,
    AsyncCollectionsResourceWithStreamingResponse,
)
from .oauth.oauth import (
    OAuthResource,
    AsyncOAuthResource,
    OAuthResourceWithRawResponse,
    AsyncOAuthResourceWithRawResponse,
    OAuthResourceWithStreamingResponse,
    AsyncOAuthResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.token_response import TokenResponse
from ...types.nebula_results_user import NebulaResultsUser
from ...types.user_fetch_limits_response import UserFetchLimitsResponse
from ...types.nebula_results_generic_boolean_response import NebulaResultsGenericBooleanResponse
from ...types.collections.paginated_nebula_result_list_user import PaginatedNebulaResultListUser
from ...types.collections.nebula_results_generic_message_response import NebulaResultsGenericMessageResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def collections(self) -> CollectionsResource:
        return CollectionsResource(self._client)

    @cached_property
    def api_keys(self) -> APIKeysResource:
        return APIKeysResource(self._client)

    @cached_property
    def oauth(self) -> OAuthResource:
        return OAuthResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

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
    ) -> NebulaResultsUser:
        """
        Get detailed information about a specific user.

        Users can only access their own information unless they are superusers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/users/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsUser,
        )

    def update(
        self,
        id: str,
        *,
        bio: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        is_superuser: Optional[bool] | Omit = omit,
        limits_overrides: Dict[str, object] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        profile_picture: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsUser:
        """
        Update user information.

        Users can only update their own information unless they are superusers.
        Superuser status can only be modified by existing superusers.

        Args:
          id: ID of the user to update

          bio: Updated user bio

          email: Updated email address

          is_superuser: Updated superuser status

          limits_overrides: Updated limits overrides

          name: Updated user name

          profile_picture: Updated profile picture URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/users/{id}", id=id),
            body=maybe_transform(
                {
                    "bio": bio,
                    "email": email,
                    "is_superuser": is_superuser,
                    "limits_overrides": limits_overrides,
                    "metadata": metadata,
                    "name": name,
                    "profile_picture": profile_picture,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsUser,
        )

    def list(
        self,
        *,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultListUser:
        """
        List all users with pagination and filtering options.

        Only accessible by superusers.

        Args:
          ids: List of user IDs to filter by

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "offset": offset,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultListUser,
        )

    def delete(
        self,
        id: str,
        *,
        delete_vector_data: Optional[bool] | Omit = omit,
        password: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericBooleanResponse:
        """
        Delete a specific user.

        Users can only delete their own account unless they are superusers.

        Args:
          delete_vector_data: Whether to delete the user's vector data

          password: User's current password

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/v1/users/{id}", id=id),
            body=maybe_transform(
                {
                    "delete_vector_data": delete_vector_data,
                    "password": password,
                },
                user_delete_params.UserDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
        )

    def change_password(
        self,
        *,
        current_password: str,
        new_password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Change the authenticated user's password.

        Args:
          current_password: Current password

          new_password: New password

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/change-password",
            body=maybe_transform(
                {
                    "current_password": current_password,
                    "new_password": new_password,
                },
                user_change_password_params.UserChangePasswordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    def export(
        self,
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
        Export users as a CSV file.

        Args:
          columns: Specific columns to export

          filters: Filters to apply to the export

          include_header: Whether to include column headers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/export",
            body=maybe_transform(
                {
                    "columns": columns,
                    "filters": filters,
                    "include_header": include_header,
                },
                user_export_params.UserExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def fetch_limits(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserFetchLimitsResponse:
        """
        Return the system default limits, user-level overrides, and final "effective"
        limit settings for the specified user.

        Only superusers or the user themself may fetch these values.

        Args:
          id: ID of the user to fetch limits for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/users/{id}/limits", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserFetchLimitsResponse,
        )

    def get_current_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsUser:
        """Get detailed information about the currently authenticated user."""
        return self._get(
            "/v1/users/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsUser,
        )

    def login(
        self,
        *,
        password: str,
        username: str,
        client_id: Optional[str] | Omit = omit,
        client_secret: Optional[str] | Omit = omit,
        grant_type: Optional[str] | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponse:
        """
        Authenticate a user and provide access tokens.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/login",
            body=maybe_transform(
                {
                    "password": password,
                    "username": username,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "grant_type": grant_type,
                    "scope": scope,
                },
                user_login_params.UserLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )

    def logout(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """Log out the current user."""
        return self._post(
            "/v1/users/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    def refresh_token(
        self,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponse:
        """
        Refresh the access token using a refresh token.

        Args:
          body: Refresh token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/refresh-token",
            body=maybe_transform(body, user_refresh_token_params.UserRefreshTokenParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )

    def register(
        self,
        *,
        email: str,
        password: str,
        bio: Optional[str] | Omit = omit,
        is_verified: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        profile_picture: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsUser:
        """
        Register a new user with the given email and password.

        Args:
          email: User's email address

          password: User's password

          bio: The bio for the new user

          is_verified: Whether to verify the user immediately

          name: The name for the new user

          profile_picture: Updated user profile picture

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "bio": bio,
                    "is_verified": is_verified,
                    "name": name,
                    "profile_picture": profile_picture,
                },
                user_register_params.UserRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsUser,
        )

    def request_password_reset(
        self,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Request a password reset for a user.

        Args:
          body: User's email address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/request-password-reset",
            body=maybe_transform(body, user_request_password_reset_params.UserRequestPasswordResetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    def reset_password(
        self,
        *,
        new_password: str,
        reset_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Reset a user's password using a reset token.

        Args:
          new_password: New password

          reset_token: Password reset token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/reset-password",
            body=maybe_transform(
                {
                    "new_password": new_password,
                    "reset_token": reset_token,
                },
                user_reset_password_params.UserResetPasswordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    def retrieve_metrics(
        self,
        *,
        days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get aggregated metrics across all user collections

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/user/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"days": days}, user_retrieve_metrics_params.UserRetrieveMetricsParams),
            ),
            cast_to=object,
        )

    def send_verification_email(
        self,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Send a user's email a verification code.

        Args:
          body: User's email address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/send-verification-email",
            body=maybe_transform(body, user_send_verification_email_params.UserSendVerificationEmailParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    def verify_email(
        self,
        *,
        email: str,
        verification_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Verify a user's email address.

        Args:
          email: User's email address

          verification_code: Email verification code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/verify-email",
            body=maybe_transform(
                {
                    "email": email,
                    "verification_code": verification_code,
                },
                user_verify_email_params.UserVerifyEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def collections(self) -> AsyncCollectionsResource:
        return AsyncCollectionsResource(self._client)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        return AsyncAPIKeysResource(self._client)

    @cached_property
    def oauth(self) -> AsyncOAuthResource:
        return AsyncOAuthResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

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
    ) -> NebulaResultsUser:
        """
        Get detailed information about a specific user.

        Users can only access their own information unless they are superusers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/users/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsUser,
        )

    async def update(
        self,
        id: str,
        *,
        bio: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        is_superuser: Optional[bool] | Omit = omit,
        limits_overrides: Dict[str, object] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        profile_picture: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsUser:
        """
        Update user information.

        Users can only update their own information unless they are superusers.
        Superuser status can only be modified by existing superusers.

        Args:
          id: ID of the user to update

          bio: Updated user bio

          email: Updated email address

          is_superuser: Updated superuser status

          limits_overrides: Updated limits overrides

          name: Updated user name

          profile_picture: Updated profile picture URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/users/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "bio": bio,
                    "email": email,
                    "is_superuser": is_superuser,
                    "limits_overrides": limits_overrides,
                    "metadata": metadata,
                    "name": name,
                    "profile_picture": profile_picture,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsUser,
        )

    async def list(
        self,
        *,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultListUser:
        """
        List all users with pagination and filtering options.

        Only accessible by superusers.

        Args:
          ids: List of user IDs to filter by

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "offset": offset,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultListUser,
        )

    async def delete(
        self,
        id: str,
        *,
        delete_vector_data: Optional[bool] | Omit = omit,
        password: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericBooleanResponse:
        """
        Delete a specific user.

        Users can only delete their own account unless they are superusers.

        Args:
          delete_vector_data: Whether to delete the user's vector data

          password: User's current password

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/v1/users/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "delete_vector_data": delete_vector_data,
                    "password": password,
                },
                user_delete_params.UserDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
        )

    async def change_password(
        self,
        *,
        current_password: str,
        new_password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Change the authenticated user's password.

        Args:
          current_password: Current password

          new_password: New password

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/change-password",
            body=await async_maybe_transform(
                {
                    "current_password": current_password,
                    "new_password": new_password,
                },
                user_change_password_params.UserChangePasswordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    async def export(
        self,
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
        Export users as a CSV file.

        Args:
          columns: Specific columns to export

          filters: Filters to apply to the export

          include_header: Whether to include column headers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/export",
            body=await async_maybe_transform(
                {
                    "columns": columns,
                    "filters": filters,
                    "include_header": include_header,
                },
                user_export_params.UserExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def fetch_limits(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserFetchLimitsResponse:
        """
        Return the system default limits, user-level overrides, and final "effective"
        limit settings for the specified user.

        Only superusers or the user themself may fetch these values.

        Args:
          id: ID of the user to fetch limits for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/users/{id}/limits", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserFetchLimitsResponse,
        )

    async def get_current_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsUser:
        """Get detailed information about the currently authenticated user."""
        return await self._get(
            "/v1/users/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsUser,
        )

    async def login(
        self,
        *,
        password: str,
        username: str,
        client_id: Optional[str] | Omit = omit,
        client_secret: Optional[str] | Omit = omit,
        grant_type: Optional[str] | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponse:
        """
        Authenticate a user and provide access tokens.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/login",
            body=await async_maybe_transform(
                {
                    "password": password,
                    "username": username,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "grant_type": grant_type,
                    "scope": scope,
                },
                user_login_params.UserLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )

    async def logout(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """Log out the current user."""
        return await self._post(
            "/v1/users/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    async def refresh_token(
        self,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponse:
        """
        Refresh the access token using a refresh token.

        Args:
          body: Refresh token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/refresh-token",
            body=await async_maybe_transform(body, user_refresh_token_params.UserRefreshTokenParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )

    async def register(
        self,
        *,
        email: str,
        password: str,
        bio: Optional[str] | Omit = omit,
        is_verified: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        profile_picture: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsUser:
        """
        Register a new user with the given email and password.

        Args:
          email: User's email address

          password: User's password

          bio: The bio for the new user

          is_verified: Whether to verify the user immediately

          name: The name for the new user

          profile_picture: Updated user profile picture

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "bio": bio,
                    "is_verified": is_verified,
                    "name": name,
                    "profile_picture": profile_picture,
                },
                user_register_params.UserRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsUser,
        )

    async def request_password_reset(
        self,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Request a password reset for a user.

        Args:
          body: User's email address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/request-password-reset",
            body=await async_maybe_transform(body, user_request_password_reset_params.UserRequestPasswordResetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    async def reset_password(
        self,
        *,
        new_password: str,
        reset_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Reset a user's password using a reset token.

        Args:
          new_password: New password

          reset_token: Password reset token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/reset-password",
            body=await async_maybe_transform(
                {
                    "new_password": new_password,
                    "reset_token": reset_token,
                },
                user_reset_password_params.UserResetPasswordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    async def retrieve_metrics(
        self,
        *,
        days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get aggregated metrics across all user collections

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/user/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"days": days}, user_retrieve_metrics_params.UserRetrieveMetricsParams
                ),
            ),
            cast_to=object,
        )

    async def send_verification_email(
        self,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Send a user's email a verification code.

        Args:
          body: User's email address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/send-verification-email",
            body=await async_maybe_transform(body, user_send_verification_email_params.UserSendVerificationEmailParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    async def verify_email(
        self,
        *,
        email: str,
        verification_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Verify a user's email address.

        Args:
          email: User's email address

          verification_code: Email verification code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/verify-email",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "verification_code": verification_code,
                },
                user_verify_email_params.UserVerifyEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )
        self.change_password = to_raw_response_wrapper(
            users.change_password,
        )
        self.export = to_raw_response_wrapper(
            users.export,
        )
        self.fetch_limits = to_raw_response_wrapper(
            users.fetch_limits,
        )
        self.get_current_user = to_raw_response_wrapper(
            users.get_current_user,
        )
        self.login = to_raw_response_wrapper(
            users.login,
        )
        self.logout = to_raw_response_wrapper(
            users.logout,
        )
        self.refresh_token = to_raw_response_wrapper(
            users.refresh_token,
        )
        self.register = to_raw_response_wrapper(
            users.register,
        )
        self.request_password_reset = to_raw_response_wrapper(
            users.request_password_reset,
        )
        self.reset_password = to_raw_response_wrapper(
            users.reset_password,
        )
        self.retrieve_metrics = to_raw_response_wrapper(
            users.retrieve_metrics,
        )
        self.send_verification_email = to_raw_response_wrapper(
            users.send_verification_email,
        )
        self.verify_email = to_raw_response_wrapper(
            users.verify_email,
        )

    @cached_property
    def collections(self) -> CollectionsResourceWithRawResponse:
        return CollectionsResourceWithRawResponse(self._users.collections)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithRawResponse:
        return APIKeysResourceWithRawResponse(self._users.api_keys)

    @cached_property
    def oauth(self) -> OAuthResourceWithRawResponse:
        return OAuthResourceWithRawResponse(self._users.oauth)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )
        self.change_password = async_to_raw_response_wrapper(
            users.change_password,
        )
        self.export = async_to_raw_response_wrapper(
            users.export,
        )
        self.fetch_limits = async_to_raw_response_wrapper(
            users.fetch_limits,
        )
        self.get_current_user = async_to_raw_response_wrapper(
            users.get_current_user,
        )
        self.login = async_to_raw_response_wrapper(
            users.login,
        )
        self.logout = async_to_raw_response_wrapper(
            users.logout,
        )
        self.refresh_token = async_to_raw_response_wrapper(
            users.refresh_token,
        )
        self.register = async_to_raw_response_wrapper(
            users.register,
        )
        self.request_password_reset = async_to_raw_response_wrapper(
            users.request_password_reset,
        )
        self.reset_password = async_to_raw_response_wrapper(
            users.reset_password,
        )
        self.retrieve_metrics = async_to_raw_response_wrapper(
            users.retrieve_metrics,
        )
        self.send_verification_email = async_to_raw_response_wrapper(
            users.send_verification_email,
        )
        self.verify_email = async_to_raw_response_wrapper(
            users.verify_email,
        )

    @cached_property
    def collections(self) -> AsyncCollectionsResourceWithRawResponse:
        return AsyncCollectionsResourceWithRawResponse(self._users.collections)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithRawResponse:
        return AsyncAPIKeysResourceWithRawResponse(self._users.api_keys)

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithRawResponse:
        return AsyncOAuthResourceWithRawResponse(self._users.oauth)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )
        self.change_password = to_streamed_response_wrapper(
            users.change_password,
        )
        self.export = to_streamed_response_wrapper(
            users.export,
        )
        self.fetch_limits = to_streamed_response_wrapper(
            users.fetch_limits,
        )
        self.get_current_user = to_streamed_response_wrapper(
            users.get_current_user,
        )
        self.login = to_streamed_response_wrapper(
            users.login,
        )
        self.logout = to_streamed_response_wrapper(
            users.logout,
        )
        self.refresh_token = to_streamed_response_wrapper(
            users.refresh_token,
        )
        self.register = to_streamed_response_wrapper(
            users.register,
        )
        self.request_password_reset = to_streamed_response_wrapper(
            users.request_password_reset,
        )
        self.reset_password = to_streamed_response_wrapper(
            users.reset_password,
        )
        self.retrieve_metrics = to_streamed_response_wrapper(
            users.retrieve_metrics,
        )
        self.send_verification_email = to_streamed_response_wrapper(
            users.send_verification_email,
        )
        self.verify_email = to_streamed_response_wrapper(
            users.verify_email,
        )

    @cached_property
    def collections(self) -> CollectionsResourceWithStreamingResponse:
        return CollectionsResourceWithStreamingResponse(self._users.collections)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithStreamingResponse:
        return APIKeysResourceWithStreamingResponse(self._users.api_keys)

    @cached_property
    def oauth(self) -> OAuthResourceWithStreamingResponse:
        return OAuthResourceWithStreamingResponse(self._users.oauth)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
        self.change_password = async_to_streamed_response_wrapper(
            users.change_password,
        )
        self.export = async_to_streamed_response_wrapper(
            users.export,
        )
        self.fetch_limits = async_to_streamed_response_wrapper(
            users.fetch_limits,
        )
        self.get_current_user = async_to_streamed_response_wrapper(
            users.get_current_user,
        )
        self.login = async_to_streamed_response_wrapper(
            users.login,
        )
        self.logout = async_to_streamed_response_wrapper(
            users.logout,
        )
        self.refresh_token = async_to_streamed_response_wrapper(
            users.refresh_token,
        )
        self.register = async_to_streamed_response_wrapper(
            users.register,
        )
        self.request_password_reset = async_to_streamed_response_wrapper(
            users.request_password_reset,
        )
        self.reset_password = async_to_streamed_response_wrapper(
            users.reset_password,
        )
        self.retrieve_metrics = async_to_streamed_response_wrapper(
            users.retrieve_metrics,
        )
        self.send_verification_email = async_to_streamed_response_wrapper(
            users.send_verification_email,
        )
        self.verify_email = async_to_streamed_response_wrapper(
            users.verify_email,
        )

    @cached_property
    def collections(self) -> AsyncCollectionsResourceWithStreamingResponse:
        return AsyncCollectionsResourceWithStreamingResponse(self._users.collections)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        return AsyncAPIKeysResourceWithStreamingResponse(self._users.api_keys)

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithStreamingResponse:
        return AsyncOAuthResourceWithStreamingResponse(self._users.oauth)
