# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import (
    secret_rotate_params,
    secret_initialize_params,
    secret_update_config_params,
    secret_retrieve_status_params,
    secret_retrieve_history_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .scheduler import (
    SchedulerResource,
    AsyncSchedulerResource,
    SchedulerResourceWithRawResponse,
    AsyncSchedulerResourceWithRawResponse,
    SchedulerResourceWithStreamingResponse,
    AsyncSchedulerResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.secret_rotate_response import SecretRotateResponse
from ...types.secret_initialize_response import SecretInitializeResponse
from ...types.secret_update_config_response import SecretUpdateConfigResponse
from ...types.secret_retrieve_status_response import SecretRetrieveStatusResponse
from ...types.secret_retrieve_history_response import SecretRetrieveHistoryResponse

__all__ = ["SecretsResource", "AsyncSecretsResource"]


class SecretsResource(SyncAPIResource):
    @cached_property
    def scheduler(self) -> SchedulerResource:
        return SchedulerResource(self._client)

    @cached_property
    def with_raw_response(self) -> SecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return SecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return SecretsResourceWithStreamingResponse(self)

    def initialize(
        self,
        *,
        secret_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretInitializeResponse:
        """
        Initialize a new webhook secret if none exists

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/secrets/initialize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"secret_key": secret_key}, secret_initialize_params.SecretInitializeParams),
            ),
            cast_to=SecretInitializeResponse,
        )

    def retrieve_history(
        self,
        *,
        limit: int | Omit = omit,
        secret_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretRetrieveHistoryResponse:
        """
        Get rotation history for audit purposes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/secrets/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "secret_key": secret_key,
                    },
                    secret_retrieve_history_params.SecretRetrieveHistoryParams,
                ),
            ),
            cast_to=SecretRetrieveHistoryResponse,
        )

    def retrieve_status(
        self,
        *,
        secret_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretRetrieveStatusResponse:
        """
        Get current rotation status and configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/secrets/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"secret_key": secret_key}, secret_retrieve_status_params.SecretRetrieveStatusParams
                ),
            ),
            cast_to=SecretRetrieveStatusResponse,
        )

    def rotate(
        self,
        *,
        notify_external: bool | Omit = omit,
        reason: str | Omit = omit,
        secret_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretRotateResponse:
        """Manually trigger secret rotation.

        Requires admin privileges.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/secrets/rotate",
            body=maybe_transform(
                {
                    "notify_external": notify_external,
                    "reason": reason,
                    "secret_key": secret_key,
                },
                secret_rotate_params.SecretRotateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretRotateResponse,
        )

    def update_config(
        self,
        *,
        auto_rotation_enabled: Optional[bool] | Omit = omit,
        rotation_interval_days: Optional[int] | Omit = omit,
        secret_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretUpdateConfigResponse:
        """
        Update rotation configuration for a secret

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/secrets/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "auto_rotation_enabled": auto_rotation_enabled,
                        "rotation_interval_days": rotation_interval_days,
                        "secret_key": secret_key,
                    },
                    secret_update_config_params.SecretUpdateConfigParams,
                ),
            ),
            cast_to=SecretUpdateConfigResponse,
        )


class AsyncSecretsResource(AsyncAPIResource):
    @cached_property
    def scheduler(self) -> AsyncSchedulerResource:
        return AsyncSchedulerResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return AsyncSecretsResourceWithStreamingResponse(self)

    async def initialize(
        self,
        *,
        secret_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretInitializeResponse:
        """
        Initialize a new webhook secret if none exists

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/secrets/initialize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"secret_key": secret_key}, secret_initialize_params.SecretInitializeParams
                ),
            ),
            cast_to=SecretInitializeResponse,
        )

    async def retrieve_history(
        self,
        *,
        limit: int | Omit = omit,
        secret_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretRetrieveHistoryResponse:
        """
        Get rotation history for audit purposes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/secrets/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "secret_key": secret_key,
                    },
                    secret_retrieve_history_params.SecretRetrieveHistoryParams,
                ),
            ),
            cast_to=SecretRetrieveHistoryResponse,
        )

    async def retrieve_status(
        self,
        *,
        secret_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretRetrieveStatusResponse:
        """
        Get current rotation status and configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/secrets/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"secret_key": secret_key}, secret_retrieve_status_params.SecretRetrieveStatusParams
                ),
            ),
            cast_to=SecretRetrieveStatusResponse,
        )

    async def rotate(
        self,
        *,
        notify_external: bool | Omit = omit,
        reason: str | Omit = omit,
        secret_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretRotateResponse:
        """Manually trigger secret rotation.

        Requires admin privileges.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/secrets/rotate",
            body=await async_maybe_transform(
                {
                    "notify_external": notify_external,
                    "reason": reason,
                    "secret_key": secret_key,
                },
                secret_rotate_params.SecretRotateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretRotateResponse,
        )

    async def update_config(
        self,
        *,
        auto_rotation_enabled: Optional[bool] | Omit = omit,
        rotation_interval_days: Optional[int] | Omit = omit,
        secret_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretUpdateConfigResponse:
        """
        Update rotation configuration for a secret

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/secrets/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "auto_rotation_enabled": auto_rotation_enabled,
                        "rotation_interval_days": rotation_interval_days,
                        "secret_key": secret_key,
                    },
                    secret_update_config_params.SecretUpdateConfigParams,
                ),
            ),
            cast_to=SecretUpdateConfigResponse,
        )


class SecretsResourceWithRawResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.initialize = to_raw_response_wrapper(
            secrets.initialize,
        )
        self.retrieve_history = to_raw_response_wrapper(
            secrets.retrieve_history,
        )
        self.retrieve_status = to_raw_response_wrapper(
            secrets.retrieve_status,
        )
        self.rotate = to_raw_response_wrapper(
            secrets.rotate,
        )
        self.update_config = to_raw_response_wrapper(
            secrets.update_config,
        )

    @cached_property
    def scheduler(self) -> SchedulerResourceWithRawResponse:
        return SchedulerResourceWithRawResponse(self._secrets.scheduler)


class AsyncSecretsResourceWithRawResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.initialize = async_to_raw_response_wrapper(
            secrets.initialize,
        )
        self.retrieve_history = async_to_raw_response_wrapper(
            secrets.retrieve_history,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            secrets.retrieve_status,
        )
        self.rotate = async_to_raw_response_wrapper(
            secrets.rotate,
        )
        self.update_config = async_to_raw_response_wrapper(
            secrets.update_config,
        )

    @cached_property
    def scheduler(self) -> AsyncSchedulerResourceWithRawResponse:
        return AsyncSchedulerResourceWithRawResponse(self._secrets.scheduler)


class SecretsResourceWithStreamingResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.initialize = to_streamed_response_wrapper(
            secrets.initialize,
        )
        self.retrieve_history = to_streamed_response_wrapper(
            secrets.retrieve_history,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            secrets.retrieve_status,
        )
        self.rotate = to_streamed_response_wrapper(
            secrets.rotate,
        )
        self.update_config = to_streamed_response_wrapper(
            secrets.update_config,
        )

    @cached_property
    def scheduler(self) -> SchedulerResourceWithStreamingResponse:
        return SchedulerResourceWithStreamingResponse(self._secrets.scheduler)


class AsyncSecretsResourceWithStreamingResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.initialize = async_to_streamed_response_wrapper(
            secrets.initialize,
        )
        self.retrieve_history = async_to_streamed_response_wrapper(
            secrets.retrieve_history,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            secrets.retrieve_status,
        )
        self.rotate = async_to_streamed_response_wrapper(
            secrets.rotate,
        )
        self.update_config = async_to_streamed_response_wrapper(
            secrets.update_config,
        )

    @cached_property
    def scheduler(self) -> AsyncSchedulerResourceWithStreamingResponse:
        return AsyncSchedulerResourceWithStreamingResponse(self._secrets.scheduler)
