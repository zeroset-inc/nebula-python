# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
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
from ._compat import cached_property
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)

if TYPE_CHECKING:
    from .resources import (
        plans,
        usage,
        users,
        chunks,
        graphs,
        health,
        system,
        billing,
        engrams,
        prompts,
        secrets,
        version,
        entities,
        memories,
        webhooks,
        analytics,
        retrieval,
        management,
        collections,
        marketplace,
        contradictions,
        temporal_events,
    )
    from .resources.plans import PlansResource, AsyncPlansResource
    from .resources.chunks import ChunksResource, AsyncChunksResource
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.system import SystemResource, AsyncSystemResource
    from .resources.billing import BillingResource, AsyncBillingResource
    from .resources.engrams import EngramsResource, AsyncEngramsResource
    from .resources.prompts import PromptsResource, AsyncPromptsResource
    from .resources.version import VersionResource, AsyncVersionResource
    from .resources.entities import EntitiesResource, AsyncEntitiesResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.retrieval import RetrievalResource, AsyncRetrievalResource
    from .resources.management import ManagementResource, AsyncManagementResource
    from .resources.usage.usage import UsageResource, AsyncUsageResource
    from .resources.users.users import UsersResource, AsyncUsersResource
    from .resources.graphs.graphs import GraphsResource, AsyncGraphsResource
    from .resources.contradictions import ContradictionsResource, AsyncContradictionsResource
    from .resources.secrets.secrets import SecretsResource, AsyncSecretsResource
    from .resources.temporal_events import TemporalEventsResource, AsyncTemporalEventsResource
    from .resources.memories.memories import MemoriesResource, AsyncMemoriesResource
    from .resources.analytics.analytics import AnalyticsResource, AsyncAnalyticsResource
    from .resources.collections.collections import CollectionsResource, AsyncCollectionsResource
    from .resources.marketplace.marketplace import MarketplaceResource, AsyncMarketplaceResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Nebula", "AsyncNebula", "Client", "AsyncClient"]


class Nebula(SyncAPIClient):
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

    @cached_property
    def chunks(self) -> ChunksResource:
        from .resources.chunks import ChunksResource

        return ChunksResource(self)

    @cached_property
    def collections(self) -> CollectionsResource:
        from .resources.collections import CollectionsResource

        return CollectionsResource(self)

    @cached_property
    def memories(self) -> MemoriesResource:
        from .resources.memories import MemoriesResource

        return MemoriesResource(self)

    @cached_property
    def graphs(self) -> GraphsResource:
        from .resources.graphs import GraphsResource

        return GraphsResource(self)

    @cached_property
    def entities(self) -> EntitiesResource:
        from .resources.entities import EntitiesResource

        return EntitiesResource(self)

    @cached_property
    def engrams(self) -> EngramsResource:
        from .resources.engrams import EngramsResource

        return EngramsResource(self)

    @cached_property
    def prompts(self) -> PromptsResource:
        from .resources.prompts import PromptsResource

        return PromptsResource(self)

    @cached_property
    def retrieval(self) -> RetrievalResource:
        from .resources.retrieval import RetrievalResource

        return RetrievalResource(self)

    @cached_property
    def marketplace(self) -> MarketplaceResource:
        from .resources.marketplace import MarketplaceResource

        return MarketplaceResource(self)

    @cached_property
    def analytics(self) -> AnalyticsResource:
        from .resources.analytics import AnalyticsResource

        return AnalyticsResource(self)

    @cached_property
    def health(self) -> HealthResource:
        from .resources.health import HealthResource

        return HealthResource(self)

    @cached_property
    def version(self) -> VersionResource:
        from .resources.version import VersionResource

        return VersionResource(self)

    @cached_property
    def management(self) -> ManagementResource:
        from .resources.management import ManagementResource

        return ManagementResource(self)

    @cached_property
    def plans(self) -> PlansResource:
        from .resources.plans import PlansResource

        return PlansResource(self)

    @cached_property
    def usage(self) -> UsageResource:
        from .resources.usage import UsageResource

        return UsageResource(self)

    @cached_property
    def system(self) -> SystemResource:
        from .resources.system import SystemResource

        return SystemResource(self)

    @cached_property
    def secrets(self) -> SecretsResource:
        from .resources.secrets import SecretsResource

        return SecretsResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def billing(self) -> BillingResource:
        from .resources.billing import BillingResource

        return BillingResource(self)

    @cached_property
    def contradictions(self) -> ContradictionsResource:
        from .resources.contradictions import ContradictionsResource

        return ContradictionsResource(self)

    @cached_property
    def temporal_events(self) -> TemporalEventsResource:
        from .resources.temporal_events import TemporalEventsResource

        return TemporalEventsResource(self)

    @cached_property
    def users(self) -> UsersResource:
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def with_raw_response(self) -> NebulaWithRawResponse:
        return NebulaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NebulaWithStreamedResponse:
        return NebulaWithStreamedResponse(self)

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
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        if headers.get("X-API-Key") or isinstance(custom_headers.get("X-API-Key"), Omit):
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

    @cached_property
    def chunks(self) -> AsyncChunksResource:
        from .resources.chunks import AsyncChunksResource

        return AsyncChunksResource(self)

    @cached_property
    def collections(self) -> AsyncCollectionsResource:
        from .resources.collections import AsyncCollectionsResource

        return AsyncCollectionsResource(self)

    @cached_property
    def memories(self) -> AsyncMemoriesResource:
        from .resources.memories import AsyncMemoriesResource

        return AsyncMemoriesResource(self)

    @cached_property
    def graphs(self) -> AsyncGraphsResource:
        from .resources.graphs import AsyncGraphsResource

        return AsyncGraphsResource(self)

    @cached_property
    def entities(self) -> AsyncEntitiesResource:
        from .resources.entities import AsyncEntitiesResource

        return AsyncEntitiesResource(self)

    @cached_property
    def engrams(self) -> AsyncEngramsResource:
        from .resources.engrams import AsyncEngramsResource

        return AsyncEngramsResource(self)

    @cached_property
    def prompts(self) -> AsyncPromptsResource:
        from .resources.prompts import AsyncPromptsResource

        return AsyncPromptsResource(self)

    @cached_property
    def retrieval(self) -> AsyncRetrievalResource:
        from .resources.retrieval import AsyncRetrievalResource

        return AsyncRetrievalResource(self)

    @cached_property
    def marketplace(self) -> AsyncMarketplaceResource:
        from .resources.marketplace import AsyncMarketplaceResource

        return AsyncMarketplaceResource(self)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        from .resources.analytics import AsyncAnalyticsResource

        return AsyncAnalyticsResource(self)

    @cached_property
    def health(self) -> AsyncHealthResource:
        from .resources.health import AsyncHealthResource

        return AsyncHealthResource(self)

    @cached_property
    def version(self) -> AsyncVersionResource:
        from .resources.version import AsyncVersionResource

        return AsyncVersionResource(self)

    @cached_property
    def management(self) -> AsyncManagementResource:
        from .resources.management import AsyncManagementResource

        return AsyncManagementResource(self)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        from .resources.plans import AsyncPlansResource

        return AsyncPlansResource(self)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        from .resources.usage import AsyncUsageResource

        return AsyncUsageResource(self)

    @cached_property
    def system(self) -> AsyncSystemResource:
        from .resources.system import AsyncSystemResource

        return AsyncSystemResource(self)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        from .resources.secrets import AsyncSecretsResource

        return AsyncSecretsResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def billing(self) -> AsyncBillingResource:
        from .resources.billing import AsyncBillingResource

        return AsyncBillingResource(self)

    @cached_property
    def contradictions(self) -> AsyncContradictionsResource:
        from .resources.contradictions import AsyncContradictionsResource

        return AsyncContradictionsResource(self)

    @cached_property
    def temporal_events(self) -> AsyncTemporalEventsResource:
        from .resources.temporal_events import AsyncTemporalEventsResource

        return AsyncTemporalEventsResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncNebulaWithRawResponse:
        return AsyncNebulaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNebulaWithStreamedResponse:
        return AsyncNebulaWithStreamedResponse(self)

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
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        if headers.get("X-API-Key") or isinstance(custom_headers.get("X-API-Key"), Omit):
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
    _client: Nebula

    def __init__(self, client: Nebula) -> None:
        self._client = client

        self.get_status = to_raw_response_wrapper(
            client.get_status,
        )

    @cached_property
    def chunks(self) -> chunks.ChunksResourceWithRawResponse:
        from .resources.chunks import ChunksResourceWithRawResponse

        return ChunksResourceWithRawResponse(self._client.chunks)

    @cached_property
    def collections(self) -> collections.CollectionsResourceWithRawResponse:
        from .resources.collections import CollectionsResourceWithRawResponse

        return CollectionsResourceWithRawResponse(self._client.collections)

    @cached_property
    def memories(self) -> memories.MemoriesResourceWithRawResponse:
        from .resources.memories import MemoriesResourceWithRawResponse

        return MemoriesResourceWithRawResponse(self._client.memories)

    @cached_property
    def graphs(self) -> graphs.GraphsResourceWithRawResponse:
        from .resources.graphs import GraphsResourceWithRawResponse

        return GraphsResourceWithRawResponse(self._client.graphs)

    @cached_property
    def entities(self) -> entities.EntitiesResourceWithRawResponse:
        from .resources.entities import EntitiesResourceWithRawResponse

        return EntitiesResourceWithRawResponse(self._client.entities)

    @cached_property
    def engrams(self) -> engrams.EngramsResourceWithRawResponse:
        from .resources.engrams import EngramsResourceWithRawResponse

        return EngramsResourceWithRawResponse(self._client.engrams)

    @cached_property
    def prompts(self) -> prompts.PromptsResourceWithRawResponse:
        from .resources.prompts import PromptsResourceWithRawResponse

        return PromptsResourceWithRawResponse(self._client.prompts)

    @cached_property
    def retrieval(self) -> retrieval.RetrievalResourceWithRawResponse:
        from .resources.retrieval import RetrievalResourceWithRawResponse

        return RetrievalResourceWithRawResponse(self._client.retrieval)

    @cached_property
    def marketplace(self) -> marketplace.MarketplaceResourceWithRawResponse:
        from .resources.marketplace import MarketplaceResourceWithRawResponse

        return MarketplaceResourceWithRawResponse(self._client.marketplace)

    @cached_property
    def analytics(self) -> analytics.AnalyticsResourceWithRawResponse:
        from .resources.analytics import AnalyticsResourceWithRawResponse

        return AnalyticsResourceWithRawResponse(self._client.analytics)

    @cached_property
    def health(self) -> health.HealthResourceWithRawResponse:
        from .resources.health import HealthResourceWithRawResponse

        return HealthResourceWithRawResponse(self._client.health)

    @cached_property
    def version(self) -> version.VersionResourceWithRawResponse:
        from .resources.version import VersionResourceWithRawResponse

        return VersionResourceWithRawResponse(self._client.version)

    @cached_property
    def management(self) -> management.ManagementResourceWithRawResponse:
        from .resources.management import ManagementResourceWithRawResponse

        return ManagementResourceWithRawResponse(self._client.management)

    @cached_property
    def plans(self) -> plans.PlansResourceWithRawResponse:
        from .resources.plans import PlansResourceWithRawResponse

        return PlansResourceWithRawResponse(self._client.plans)

    @cached_property
    def usage(self) -> usage.UsageResourceWithRawResponse:
        from .resources.usage import UsageResourceWithRawResponse

        return UsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def system(self) -> system.SystemResourceWithRawResponse:
        from .resources.system import SystemResourceWithRawResponse

        return SystemResourceWithRawResponse(self._client.system)

    @cached_property
    def secrets(self) -> secrets.SecretsResourceWithRawResponse:
        from .resources.secrets import SecretsResourceWithRawResponse

        return SecretsResourceWithRawResponse(self._client.secrets)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def billing(self) -> billing.BillingResourceWithRawResponse:
        from .resources.billing import BillingResourceWithRawResponse

        return BillingResourceWithRawResponse(self._client.billing)

    @cached_property
    def contradictions(self) -> contradictions.ContradictionsResourceWithRawResponse:
        from .resources.contradictions import ContradictionsResourceWithRawResponse

        return ContradictionsResourceWithRawResponse(self._client.contradictions)

    @cached_property
    def temporal_events(self) -> temporal_events.TemporalEventsResourceWithRawResponse:
        from .resources.temporal_events import TemporalEventsResourceWithRawResponse

        return TemporalEventsResourceWithRawResponse(self._client.temporal_events)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)


class AsyncNebulaWithRawResponse:
    _client: AsyncNebula

    def __init__(self, client: AsyncNebula) -> None:
        self._client = client

        self.get_status = async_to_raw_response_wrapper(
            client.get_status,
        )

    @cached_property
    def chunks(self) -> chunks.AsyncChunksResourceWithRawResponse:
        from .resources.chunks import AsyncChunksResourceWithRawResponse

        return AsyncChunksResourceWithRawResponse(self._client.chunks)

    @cached_property
    def collections(self) -> collections.AsyncCollectionsResourceWithRawResponse:
        from .resources.collections import AsyncCollectionsResourceWithRawResponse

        return AsyncCollectionsResourceWithRawResponse(self._client.collections)

    @cached_property
    def memories(self) -> memories.AsyncMemoriesResourceWithRawResponse:
        from .resources.memories import AsyncMemoriesResourceWithRawResponse

        return AsyncMemoriesResourceWithRawResponse(self._client.memories)

    @cached_property
    def graphs(self) -> graphs.AsyncGraphsResourceWithRawResponse:
        from .resources.graphs import AsyncGraphsResourceWithRawResponse

        return AsyncGraphsResourceWithRawResponse(self._client.graphs)

    @cached_property
    def entities(self) -> entities.AsyncEntitiesResourceWithRawResponse:
        from .resources.entities import AsyncEntitiesResourceWithRawResponse

        return AsyncEntitiesResourceWithRawResponse(self._client.entities)

    @cached_property
    def engrams(self) -> engrams.AsyncEngramsResourceWithRawResponse:
        from .resources.engrams import AsyncEngramsResourceWithRawResponse

        return AsyncEngramsResourceWithRawResponse(self._client.engrams)

    @cached_property
    def prompts(self) -> prompts.AsyncPromptsResourceWithRawResponse:
        from .resources.prompts import AsyncPromptsResourceWithRawResponse

        return AsyncPromptsResourceWithRawResponse(self._client.prompts)

    @cached_property
    def retrieval(self) -> retrieval.AsyncRetrievalResourceWithRawResponse:
        from .resources.retrieval import AsyncRetrievalResourceWithRawResponse

        return AsyncRetrievalResourceWithRawResponse(self._client.retrieval)

    @cached_property
    def marketplace(self) -> marketplace.AsyncMarketplaceResourceWithRawResponse:
        from .resources.marketplace import AsyncMarketplaceResourceWithRawResponse

        return AsyncMarketplaceResourceWithRawResponse(self._client.marketplace)

    @cached_property
    def analytics(self) -> analytics.AsyncAnalyticsResourceWithRawResponse:
        from .resources.analytics import AsyncAnalyticsResourceWithRawResponse

        return AsyncAnalyticsResourceWithRawResponse(self._client.analytics)

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithRawResponse:
        from .resources.health import AsyncHealthResourceWithRawResponse

        return AsyncHealthResourceWithRawResponse(self._client.health)

    @cached_property
    def version(self) -> version.AsyncVersionResourceWithRawResponse:
        from .resources.version import AsyncVersionResourceWithRawResponse

        return AsyncVersionResourceWithRawResponse(self._client.version)

    @cached_property
    def management(self) -> management.AsyncManagementResourceWithRawResponse:
        from .resources.management import AsyncManagementResourceWithRawResponse

        return AsyncManagementResourceWithRawResponse(self._client.management)

    @cached_property
    def plans(self) -> plans.AsyncPlansResourceWithRawResponse:
        from .resources.plans import AsyncPlansResourceWithRawResponse

        return AsyncPlansResourceWithRawResponse(self._client.plans)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithRawResponse:
        from .resources.usage import AsyncUsageResourceWithRawResponse

        return AsyncUsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def system(self) -> system.AsyncSystemResourceWithRawResponse:
        from .resources.system import AsyncSystemResourceWithRawResponse

        return AsyncSystemResourceWithRawResponse(self._client.system)

    @cached_property
    def secrets(self) -> secrets.AsyncSecretsResourceWithRawResponse:
        from .resources.secrets import AsyncSecretsResourceWithRawResponse

        return AsyncSecretsResourceWithRawResponse(self._client.secrets)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def billing(self) -> billing.AsyncBillingResourceWithRawResponse:
        from .resources.billing import AsyncBillingResourceWithRawResponse

        return AsyncBillingResourceWithRawResponse(self._client.billing)

    @cached_property
    def contradictions(self) -> contradictions.AsyncContradictionsResourceWithRawResponse:
        from .resources.contradictions import AsyncContradictionsResourceWithRawResponse

        return AsyncContradictionsResourceWithRawResponse(self._client.contradictions)

    @cached_property
    def temporal_events(self) -> temporal_events.AsyncTemporalEventsResourceWithRawResponse:
        from .resources.temporal_events import AsyncTemporalEventsResourceWithRawResponse

        return AsyncTemporalEventsResourceWithRawResponse(self._client.temporal_events)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)


class NebulaWithStreamedResponse:
    _client: Nebula

    def __init__(self, client: Nebula) -> None:
        self._client = client

        self.get_status = to_streamed_response_wrapper(
            client.get_status,
        )

    @cached_property
    def chunks(self) -> chunks.ChunksResourceWithStreamingResponse:
        from .resources.chunks import ChunksResourceWithStreamingResponse

        return ChunksResourceWithStreamingResponse(self._client.chunks)

    @cached_property
    def collections(self) -> collections.CollectionsResourceWithStreamingResponse:
        from .resources.collections import CollectionsResourceWithStreamingResponse

        return CollectionsResourceWithStreamingResponse(self._client.collections)

    @cached_property
    def memories(self) -> memories.MemoriesResourceWithStreamingResponse:
        from .resources.memories import MemoriesResourceWithStreamingResponse

        return MemoriesResourceWithStreamingResponse(self._client.memories)

    @cached_property
    def graphs(self) -> graphs.GraphsResourceWithStreamingResponse:
        from .resources.graphs import GraphsResourceWithStreamingResponse

        return GraphsResourceWithStreamingResponse(self._client.graphs)

    @cached_property
    def entities(self) -> entities.EntitiesResourceWithStreamingResponse:
        from .resources.entities import EntitiesResourceWithStreamingResponse

        return EntitiesResourceWithStreamingResponse(self._client.entities)

    @cached_property
    def engrams(self) -> engrams.EngramsResourceWithStreamingResponse:
        from .resources.engrams import EngramsResourceWithStreamingResponse

        return EngramsResourceWithStreamingResponse(self._client.engrams)

    @cached_property
    def prompts(self) -> prompts.PromptsResourceWithStreamingResponse:
        from .resources.prompts import PromptsResourceWithStreamingResponse

        return PromptsResourceWithStreamingResponse(self._client.prompts)

    @cached_property
    def retrieval(self) -> retrieval.RetrievalResourceWithStreamingResponse:
        from .resources.retrieval import RetrievalResourceWithStreamingResponse

        return RetrievalResourceWithStreamingResponse(self._client.retrieval)

    @cached_property
    def marketplace(self) -> marketplace.MarketplaceResourceWithStreamingResponse:
        from .resources.marketplace import MarketplaceResourceWithStreamingResponse

        return MarketplaceResourceWithStreamingResponse(self._client.marketplace)

    @cached_property
    def analytics(self) -> analytics.AnalyticsResourceWithStreamingResponse:
        from .resources.analytics import AnalyticsResourceWithStreamingResponse

        return AnalyticsResourceWithStreamingResponse(self._client.analytics)

    @cached_property
    def health(self) -> health.HealthResourceWithStreamingResponse:
        from .resources.health import HealthResourceWithStreamingResponse

        return HealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def version(self) -> version.VersionResourceWithStreamingResponse:
        from .resources.version import VersionResourceWithStreamingResponse

        return VersionResourceWithStreamingResponse(self._client.version)

    @cached_property
    def management(self) -> management.ManagementResourceWithStreamingResponse:
        from .resources.management import ManagementResourceWithStreamingResponse

        return ManagementResourceWithStreamingResponse(self._client.management)

    @cached_property
    def plans(self) -> plans.PlansResourceWithStreamingResponse:
        from .resources.plans import PlansResourceWithStreamingResponse

        return PlansResourceWithStreamingResponse(self._client.plans)

    @cached_property
    def usage(self) -> usage.UsageResourceWithStreamingResponse:
        from .resources.usage import UsageResourceWithStreamingResponse

        return UsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def system(self) -> system.SystemResourceWithStreamingResponse:
        from .resources.system import SystemResourceWithStreamingResponse

        return SystemResourceWithStreamingResponse(self._client.system)

    @cached_property
    def secrets(self) -> secrets.SecretsResourceWithStreamingResponse:
        from .resources.secrets import SecretsResourceWithStreamingResponse

        return SecretsResourceWithStreamingResponse(self._client.secrets)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def billing(self) -> billing.BillingResourceWithStreamingResponse:
        from .resources.billing import BillingResourceWithStreamingResponse

        return BillingResourceWithStreamingResponse(self._client.billing)

    @cached_property
    def contradictions(self) -> contradictions.ContradictionsResourceWithStreamingResponse:
        from .resources.contradictions import ContradictionsResourceWithStreamingResponse

        return ContradictionsResourceWithStreamingResponse(self._client.contradictions)

    @cached_property
    def temporal_events(self) -> temporal_events.TemporalEventsResourceWithStreamingResponse:
        from .resources.temporal_events import TemporalEventsResourceWithStreamingResponse

        return TemporalEventsResourceWithStreamingResponse(self._client.temporal_events)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)


class AsyncNebulaWithStreamedResponse:
    _client: AsyncNebula

    def __init__(self, client: AsyncNebula) -> None:
        self._client = client

        self.get_status = async_to_streamed_response_wrapper(
            client.get_status,
        )

    @cached_property
    def chunks(self) -> chunks.AsyncChunksResourceWithStreamingResponse:
        from .resources.chunks import AsyncChunksResourceWithStreamingResponse

        return AsyncChunksResourceWithStreamingResponse(self._client.chunks)

    @cached_property
    def collections(self) -> collections.AsyncCollectionsResourceWithStreamingResponse:
        from .resources.collections import AsyncCollectionsResourceWithStreamingResponse

        return AsyncCollectionsResourceWithStreamingResponse(self._client.collections)

    @cached_property
    def memories(self) -> memories.AsyncMemoriesResourceWithStreamingResponse:
        from .resources.memories import AsyncMemoriesResourceWithStreamingResponse

        return AsyncMemoriesResourceWithStreamingResponse(self._client.memories)

    @cached_property
    def graphs(self) -> graphs.AsyncGraphsResourceWithStreamingResponse:
        from .resources.graphs import AsyncGraphsResourceWithStreamingResponse

        return AsyncGraphsResourceWithStreamingResponse(self._client.graphs)

    @cached_property
    def entities(self) -> entities.AsyncEntitiesResourceWithStreamingResponse:
        from .resources.entities import AsyncEntitiesResourceWithStreamingResponse

        return AsyncEntitiesResourceWithStreamingResponse(self._client.entities)

    @cached_property
    def engrams(self) -> engrams.AsyncEngramsResourceWithStreamingResponse:
        from .resources.engrams import AsyncEngramsResourceWithStreamingResponse

        return AsyncEngramsResourceWithStreamingResponse(self._client.engrams)

    @cached_property
    def prompts(self) -> prompts.AsyncPromptsResourceWithStreamingResponse:
        from .resources.prompts import AsyncPromptsResourceWithStreamingResponse

        return AsyncPromptsResourceWithStreamingResponse(self._client.prompts)

    @cached_property
    def retrieval(self) -> retrieval.AsyncRetrievalResourceWithStreamingResponse:
        from .resources.retrieval import AsyncRetrievalResourceWithStreamingResponse

        return AsyncRetrievalResourceWithStreamingResponse(self._client.retrieval)

    @cached_property
    def marketplace(self) -> marketplace.AsyncMarketplaceResourceWithStreamingResponse:
        from .resources.marketplace import AsyncMarketplaceResourceWithStreamingResponse

        return AsyncMarketplaceResourceWithStreamingResponse(self._client.marketplace)

    @cached_property
    def analytics(self) -> analytics.AsyncAnalyticsResourceWithStreamingResponse:
        from .resources.analytics import AsyncAnalyticsResourceWithStreamingResponse

        return AsyncAnalyticsResourceWithStreamingResponse(self._client.analytics)

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithStreamingResponse:
        from .resources.health import AsyncHealthResourceWithStreamingResponse

        return AsyncHealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def version(self) -> version.AsyncVersionResourceWithStreamingResponse:
        from .resources.version import AsyncVersionResourceWithStreamingResponse

        return AsyncVersionResourceWithStreamingResponse(self._client.version)

    @cached_property
    def management(self) -> management.AsyncManagementResourceWithStreamingResponse:
        from .resources.management import AsyncManagementResourceWithStreamingResponse

        return AsyncManagementResourceWithStreamingResponse(self._client.management)

    @cached_property
    def plans(self) -> plans.AsyncPlansResourceWithStreamingResponse:
        from .resources.plans import AsyncPlansResourceWithStreamingResponse

        return AsyncPlansResourceWithStreamingResponse(self._client.plans)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithStreamingResponse:
        from .resources.usage import AsyncUsageResourceWithStreamingResponse

        return AsyncUsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def system(self) -> system.AsyncSystemResourceWithStreamingResponse:
        from .resources.system import AsyncSystemResourceWithStreamingResponse

        return AsyncSystemResourceWithStreamingResponse(self._client.system)

    @cached_property
    def secrets(self) -> secrets.AsyncSecretsResourceWithStreamingResponse:
        from .resources.secrets import AsyncSecretsResourceWithStreamingResponse

        return AsyncSecretsResourceWithStreamingResponse(self._client.secrets)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def billing(self) -> billing.AsyncBillingResourceWithStreamingResponse:
        from .resources.billing import AsyncBillingResourceWithStreamingResponse

        return AsyncBillingResourceWithStreamingResponse(self._client.billing)

    @cached_property
    def contradictions(self) -> contradictions.AsyncContradictionsResourceWithStreamingResponse:
        from .resources.contradictions import AsyncContradictionsResourceWithStreamingResponse

        return AsyncContradictionsResourceWithStreamingResponse(self._client.contradictions)

    @cached_property
    def temporal_events(self) -> temporal_events.AsyncTemporalEventsResourceWithStreamingResponse:
        from .resources.temporal_events import AsyncTemporalEventsResourceWithStreamingResponse

        return AsyncTemporalEventsResourceWithStreamingResponse(self._client.temporal_events)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)


Client = Nebula

AsyncClient = AsyncNebula
