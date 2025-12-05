# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .resources import (
    plans,
    chunks,
    health,
    system,
    billing,
    engrams,
    prompts,
    version,
    entities,
    webhooks,
    retrieval,
    management,
    contradictions,
    temporal_events,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .resources.usage import usage
from .resources.users import users
from .resources.graphs import graphs
from .resources.secrets import secrets
from .resources.memories import memories
from .resources.analytics import analytics
from .resources.collections import collections
from .resources.marketplace import marketplace

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Nebula", "AsyncNebula", "Client", "AsyncClient"]


class Nebula(SyncAPIClient):
    chunks: chunks.ChunksResource
    collections: collections.CollectionsResource
    memories: memories.MemoriesResource
    graphs: graphs.GraphsResource
    entities: entities.EntitiesResource
    engrams: engrams.EngramsResource
    prompts: prompts.PromptsResource
    retrieval: retrieval.RetrievalResource
    marketplace: marketplace.MarketplaceResource
    analytics: analytics.AnalyticsResource
    health: health.HealthResource
    version: version.VersionResource
    management: management.ManagementResource
    plans: plans.PlansResource
    usage: usage.UsageResource
    system: system.SystemResource
    secrets: secrets.SecretsResource
    webhooks: webhooks.WebhooksResource
    billing: billing.BillingResource
    contradictions: contradictions.ContradictionsResource
    temporal_events: temporal_events.TemporalEventsResource
    users: users.UsersResource
    with_raw_response: NebulaWithRawResponse
    with_streaming_response: NebulaWithStreamedResponse

    # client options
    bearer_token: str | None
    api_key: str | None

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Nebula client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_token` from `NEBULA_BEARER_TOKEN`
        - `api_key` from `NEBULA_API_KEY`
        """
        if bearer_token is None:
            bearer_token = os.environ.get("NEBULA_BEARER_TOKEN")
        self.bearer_token = bearer_token

        if api_key is None:
            api_key = os.environ.get("NEBULA_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("NEBULA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.chunks = chunks.ChunksResource(self)
        self.collections = collections.CollectionsResource(self)
        self.memories = memories.MemoriesResource(self)
        self.graphs = graphs.GraphsResource(self)
        self.entities = entities.EntitiesResource(self)
        self.engrams = engrams.EngramsResource(self)
        self.prompts = prompts.PromptsResource(self)
        self.retrieval = retrieval.RetrievalResource(self)
        self.marketplace = marketplace.MarketplaceResource(self)
        self.analytics = analytics.AnalyticsResource(self)
        self.health = health.HealthResource(self)
        self.version = version.VersionResource(self)
        self.management = management.ManagementResource(self)
        self.plans = plans.PlansResource(self)
        self.usage = usage.UsageResource(self)
        self.system = system.SystemResource(self)
        self.secrets = secrets.SecretsResource(self)
        self.webhooks = webhooks.WebhooksResource(self)
        self.billing = billing.BillingResource(self)
        self.contradictions = contradictions.ContradictionsResource(self)
        self.temporal_events = temporal_events.TemporalEventsResource(self)
        self.users = users.UsersResource(self)
        self.with_raw_response = NebulaWithRawResponse(self)
        self.with_streaming_response = NebulaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._http_bearer, **self._api_key_header}

    @property
    def _http_bearer(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _api_key_header(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.bearer_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        if self.api_key and headers.get("X-API-Key"):
            return
        if isinstance(custom_headers.get("X-API-Key"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either bearer_token or api_key to be set. Or for one of the `Authorization` or `X-API-Key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def get_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Root endpoint - API status and welcome message."""
        return self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncNebula(AsyncAPIClient):
    chunks: chunks.AsyncChunksResource
    collections: collections.AsyncCollectionsResource
    memories: memories.AsyncMemoriesResource
    graphs: graphs.AsyncGraphsResource
    entities: entities.AsyncEntitiesResource
    engrams: engrams.AsyncEngramsResource
    prompts: prompts.AsyncPromptsResource
    retrieval: retrieval.AsyncRetrievalResource
    marketplace: marketplace.AsyncMarketplaceResource
    analytics: analytics.AsyncAnalyticsResource
    health: health.AsyncHealthResource
    version: version.AsyncVersionResource
    management: management.AsyncManagementResource
    plans: plans.AsyncPlansResource
    usage: usage.AsyncUsageResource
    system: system.AsyncSystemResource
    secrets: secrets.AsyncSecretsResource
    webhooks: webhooks.AsyncWebhooksResource
    billing: billing.AsyncBillingResource
    contradictions: contradictions.AsyncContradictionsResource
    temporal_events: temporal_events.AsyncTemporalEventsResource
    users: users.AsyncUsersResource
    with_raw_response: AsyncNebulaWithRawResponse
    with_streaming_response: AsyncNebulaWithStreamedResponse

    # client options
    bearer_token: str | None
    api_key: str | None

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncNebula client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_token` from `NEBULA_BEARER_TOKEN`
        - `api_key` from `NEBULA_API_KEY`
        """
        if bearer_token is None:
            bearer_token = os.environ.get("NEBULA_BEARER_TOKEN")
        self.bearer_token = bearer_token

        if api_key is None:
            api_key = os.environ.get("NEBULA_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("NEBULA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.chunks = chunks.AsyncChunksResource(self)
        self.collections = collections.AsyncCollectionsResource(self)
        self.memories = memories.AsyncMemoriesResource(self)
        self.graphs = graphs.AsyncGraphsResource(self)
        self.entities = entities.AsyncEntitiesResource(self)
        self.engrams = engrams.AsyncEngramsResource(self)
        self.prompts = prompts.AsyncPromptsResource(self)
        self.retrieval = retrieval.AsyncRetrievalResource(self)
        self.marketplace = marketplace.AsyncMarketplaceResource(self)
        self.analytics = analytics.AsyncAnalyticsResource(self)
        self.health = health.AsyncHealthResource(self)
        self.version = version.AsyncVersionResource(self)
        self.management = management.AsyncManagementResource(self)
        self.plans = plans.AsyncPlansResource(self)
        self.usage = usage.AsyncUsageResource(self)
        self.system = system.AsyncSystemResource(self)
        self.secrets = secrets.AsyncSecretsResource(self)
        self.webhooks = webhooks.AsyncWebhooksResource(self)
        self.billing = billing.AsyncBillingResource(self)
        self.contradictions = contradictions.AsyncContradictionsResource(self)
        self.temporal_events = temporal_events.AsyncTemporalEventsResource(self)
        self.users = users.AsyncUsersResource(self)
        self.with_raw_response = AsyncNebulaWithRawResponse(self)
        self.with_streaming_response = AsyncNebulaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._http_bearer, **self._api_key_header}

    @property
    def _http_bearer(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _api_key_header(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.bearer_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        if self.api_key and headers.get("X-API-Key"):
            return
        if isinstance(custom_headers.get("X-API-Key"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either bearer_token or api_key to be set. Or for one of the `Authorization` or `X-API-Key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def get_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Root endpoint - API status and welcome message."""
        return await self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class NebulaWithRawResponse:
    def __init__(self, client: Nebula) -> None:
        self.chunks = chunks.ChunksResourceWithRawResponse(client.chunks)
        self.collections = collections.CollectionsResourceWithRawResponse(client.collections)
        self.memories = memories.MemoriesResourceWithRawResponse(client.memories)
        self.graphs = graphs.GraphsResourceWithRawResponse(client.graphs)
        self.entities = entities.EntitiesResourceWithRawResponse(client.entities)
        self.engrams = engrams.EngramsResourceWithRawResponse(client.engrams)
        self.prompts = prompts.PromptsResourceWithRawResponse(client.prompts)
        self.retrieval = retrieval.RetrievalResourceWithRawResponse(client.retrieval)
        self.marketplace = marketplace.MarketplaceResourceWithRawResponse(client.marketplace)
        self.analytics = analytics.AnalyticsResourceWithRawResponse(client.analytics)
        self.health = health.HealthResourceWithRawResponse(client.health)
        self.version = version.VersionResourceWithRawResponse(client.version)
        self.management = management.ManagementResourceWithRawResponse(client.management)
        self.plans = plans.PlansResourceWithRawResponse(client.plans)
        self.usage = usage.UsageResourceWithRawResponse(client.usage)
        self.system = system.SystemResourceWithRawResponse(client.system)
        self.secrets = secrets.SecretsResourceWithRawResponse(client.secrets)
        self.webhooks = webhooks.WebhooksResourceWithRawResponse(client.webhooks)
        self.billing = billing.BillingResourceWithRawResponse(client.billing)
        self.contradictions = contradictions.ContradictionsResourceWithRawResponse(client.contradictions)
        self.temporal_events = temporal_events.TemporalEventsResourceWithRawResponse(client.temporal_events)
        self.users = users.UsersResourceWithRawResponse(client.users)

        self.get_status = to_raw_response_wrapper(
            client.get_status,
        )


class AsyncNebulaWithRawResponse:
    def __init__(self, client: AsyncNebula) -> None:
        self.chunks = chunks.AsyncChunksResourceWithRawResponse(client.chunks)
        self.collections = collections.AsyncCollectionsResourceWithRawResponse(client.collections)
        self.memories = memories.AsyncMemoriesResourceWithRawResponse(client.memories)
        self.graphs = graphs.AsyncGraphsResourceWithRawResponse(client.graphs)
        self.entities = entities.AsyncEntitiesResourceWithRawResponse(client.entities)
        self.engrams = engrams.AsyncEngramsResourceWithRawResponse(client.engrams)
        self.prompts = prompts.AsyncPromptsResourceWithRawResponse(client.prompts)
        self.retrieval = retrieval.AsyncRetrievalResourceWithRawResponse(client.retrieval)
        self.marketplace = marketplace.AsyncMarketplaceResourceWithRawResponse(client.marketplace)
        self.analytics = analytics.AsyncAnalyticsResourceWithRawResponse(client.analytics)
        self.health = health.AsyncHealthResourceWithRawResponse(client.health)
        self.version = version.AsyncVersionResourceWithRawResponse(client.version)
        self.management = management.AsyncManagementResourceWithRawResponse(client.management)
        self.plans = plans.AsyncPlansResourceWithRawResponse(client.plans)
        self.usage = usage.AsyncUsageResourceWithRawResponse(client.usage)
        self.system = system.AsyncSystemResourceWithRawResponse(client.system)
        self.secrets = secrets.AsyncSecretsResourceWithRawResponse(client.secrets)
        self.webhooks = webhooks.AsyncWebhooksResourceWithRawResponse(client.webhooks)
        self.billing = billing.AsyncBillingResourceWithRawResponse(client.billing)
        self.contradictions = contradictions.AsyncContradictionsResourceWithRawResponse(client.contradictions)
        self.temporal_events = temporal_events.AsyncTemporalEventsResourceWithRawResponse(client.temporal_events)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)

        self.get_status = async_to_raw_response_wrapper(
            client.get_status,
        )


class NebulaWithStreamedResponse:
    def __init__(self, client: Nebula) -> None:
        self.chunks = chunks.ChunksResourceWithStreamingResponse(client.chunks)
        self.collections = collections.CollectionsResourceWithStreamingResponse(client.collections)
        self.memories = memories.MemoriesResourceWithStreamingResponse(client.memories)
        self.graphs = graphs.GraphsResourceWithStreamingResponse(client.graphs)
        self.entities = entities.EntitiesResourceWithStreamingResponse(client.entities)
        self.engrams = engrams.EngramsResourceWithStreamingResponse(client.engrams)
        self.prompts = prompts.PromptsResourceWithStreamingResponse(client.prompts)
        self.retrieval = retrieval.RetrievalResourceWithStreamingResponse(client.retrieval)
        self.marketplace = marketplace.MarketplaceResourceWithStreamingResponse(client.marketplace)
        self.analytics = analytics.AnalyticsResourceWithStreamingResponse(client.analytics)
        self.health = health.HealthResourceWithStreamingResponse(client.health)
        self.version = version.VersionResourceWithStreamingResponse(client.version)
        self.management = management.ManagementResourceWithStreamingResponse(client.management)
        self.plans = plans.PlansResourceWithStreamingResponse(client.plans)
        self.usage = usage.UsageResourceWithStreamingResponse(client.usage)
        self.system = system.SystemResourceWithStreamingResponse(client.system)
        self.secrets = secrets.SecretsResourceWithStreamingResponse(client.secrets)
        self.webhooks = webhooks.WebhooksResourceWithStreamingResponse(client.webhooks)
        self.billing = billing.BillingResourceWithStreamingResponse(client.billing)
        self.contradictions = contradictions.ContradictionsResourceWithStreamingResponse(client.contradictions)
        self.temporal_events = temporal_events.TemporalEventsResourceWithStreamingResponse(client.temporal_events)
        self.users = users.UsersResourceWithStreamingResponse(client.users)

        self.get_status = to_streamed_response_wrapper(
            client.get_status,
        )


class AsyncNebulaWithStreamedResponse:
    def __init__(self, client: AsyncNebula) -> None:
        self.chunks = chunks.AsyncChunksResourceWithStreamingResponse(client.chunks)
        self.collections = collections.AsyncCollectionsResourceWithStreamingResponse(client.collections)
        self.memories = memories.AsyncMemoriesResourceWithStreamingResponse(client.memories)
        self.graphs = graphs.AsyncGraphsResourceWithStreamingResponse(client.graphs)
        self.entities = entities.AsyncEntitiesResourceWithStreamingResponse(client.entities)
        self.engrams = engrams.AsyncEngramsResourceWithStreamingResponse(client.engrams)
        self.prompts = prompts.AsyncPromptsResourceWithStreamingResponse(client.prompts)
        self.retrieval = retrieval.AsyncRetrievalResourceWithStreamingResponse(client.retrieval)
        self.marketplace = marketplace.AsyncMarketplaceResourceWithStreamingResponse(client.marketplace)
        self.analytics = analytics.AsyncAnalyticsResourceWithStreamingResponse(client.analytics)
        self.health = health.AsyncHealthResourceWithStreamingResponse(client.health)
        self.version = version.AsyncVersionResourceWithStreamingResponse(client.version)
        self.management = management.AsyncManagementResourceWithStreamingResponse(client.management)
        self.plans = plans.AsyncPlansResourceWithStreamingResponse(client.plans)
        self.usage = usage.AsyncUsageResourceWithStreamingResponse(client.usage)
        self.system = system.AsyncSystemResourceWithStreamingResponse(client.system)
        self.secrets = secrets.AsyncSecretsResourceWithStreamingResponse(client.secrets)
        self.webhooks = webhooks.AsyncWebhooksResourceWithStreamingResponse(client.webhooks)
        self.billing = billing.AsyncBillingResourceWithStreamingResponse(client.billing)
        self.contradictions = contradictions.AsyncContradictionsResourceWithStreamingResponse(client.contradictions)
        self.temporal_events = temporal_events.AsyncTemporalEventsResourceWithStreamingResponse(client.temporal_events)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)

        self.get_status = async_to_streamed_response_wrapper(
            client.get_status,
        )


Client = Nebula

AsyncClient = AsyncNebula
