# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import billing_create_checkout_session_params, billing_create_billing_portal_session_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return BillingResourceWithStreamingResponse(self)

    def create_billing_portal_session(
        self,
        *,
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Create a Stripe Billing Portal session for the authenticated user.

        This allows users to:

        - View invoices
        - Update payment methods
        - Cancel/modify subscriptions

        Args: return_url: URL to return to after leaving portal

        Returns: { "url": "https://billing.stripe.com/..." }

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/billing/portal",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"return_url": return_url},
                    billing_create_billing_portal_session_params.BillingCreateBillingPortalSessionParams,
                ),
            ),
            cast_to=object,
        )

    def create_checkout_session(
        self,
        *,
        plan_id: str,
        billing_interval: str | Omit = omit,
        cancel_url: Optional[str] | Omit = omit,
        success_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Create a Stripe Checkout session for the authenticated user.

        This endpoint:

        1.

        Gets or creates a Stripe customer for the user
        2. Looks up the plan and its Stripe Price ID
        3. Creates a Checkout session
        4. Returns the session URL for redirect

        Args: plan_id: The plan to subscribe to (e.g., 'pro', 'max') billing_interval:
        'month' or 'year' success_url: URL to redirect after successful payment
        cancel_url: URL to redirect if user cancels

        Returns: { "session*id": "cs*...", "url": "https://checkout.stripe.com/..." }

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/billing/checkout",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "plan_id": plan_id,
                        "billing_interval": billing_interval,
                        "cancel_url": cancel_url,
                        "success_url": success_url,
                    },
                    billing_create_checkout_session_params.BillingCreateCheckoutSessionParams,
                ),
            ),
            cast_to=object,
        )

    def handle_webhook(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Handle Stripe webhook events directly in Nebula API.

        Validates webhook signature and processes events:

        - customer.subscription.created
        - customer.subscription.updated
        - customer.subscription.deleted
        - invoice.payment_succeeded
        - invoice.payment_failed

        This is the single source of truth for subscription updates.
        """
        return self._post(
            "/v1/billing/webhook",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return AsyncBillingResourceWithStreamingResponse(self)

    async def create_billing_portal_session(
        self,
        *,
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Create a Stripe Billing Portal session for the authenticated user.

        This allows users to:

        - View invoices
        - Update payment methods
        - Cancel/modify subscriptions

        Args: return_url: URL to return to after leaving portal

        Returns: { "url": "https://billing.stripe.com/..." }

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/billing/portal",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"return_url": return_url},
                    billing_create_billing_portal_session_params.BillingCreateBillingPortalSessionParams,
                ),
            ),
            cast_to=object,
        )

    async def create_checkout_session(
        self,
        *,
        plan_id: str,
        billing_interval: str | Omit = omit,
        cancel_url: Optional[str] | Omit = omit,
        success_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Create a Stripe Checkout session for the authenticated user.

        This endpoint:

        1.

        Gets or creates a Stripe customer for the user
        2. Looks up the plan and its Stripe Price ID
        3. Creates a Checkout session
        4. Returns the session URL for redirect

        Args: plan_id: The plan to subscribe to (e.g., 'pro', 'max') billing_interval:
        'month' or 'year' success_url: URL to redirect after successful payment
        cancel_url: URL to redirect if user cancels

        Returns: { "session*id": "cs*...", "url": "https://checkout.stripe.com/..." }

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/billing/checkout",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "plan_id": plan_id,
                        "billing_interval": billing_interval,
                        "cancel_url": cancel_url,
                        "success_url": success_url,
                    },
                    billing_create_checkout_session_params.BillingCreateCheckoutSessionParams,
                ),
            ),
            cast_to=object,
        )

    async def handle_webhook(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Handle Stripe webhook events directly in Nebula API.

        Validates webhook signature and processes events:

        - customer.subscription.created
        - customer.subscription.updated
        - customer.subscription.deleted
        - invoice.payment_succeeded
        - invoice.payment_failed

        This is the single source of truth for subscription updates.
        """
        return await self._post(
            "/v1/billing/webhook",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.create_billing_portal_session = to_raw_response_wrapper(
            billing.create_billing_portal_session,
        )
        self.create_checkout_session = to_raw_response_wrapper(
            billing.create_checkout_session,
        )
        self.handle_webhook = to_raw_response_wrapper(
            billing.handle_webhook,
        )


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.create_billing_portal_session = async_to_raw_response_wrapper(
            billing.create_billing_portal_session,
        )
        self.create_checkout_session = async_to_raw_response_wrapper(
            billing.create_checkout_session,
        )
        self.handle_webhook = async_to_raw_response_wrapper(
            billing.handle_webhook,
        )


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.create_billing_portal_session = to_streamed_response_wrapper(
            billing.create_billing_portal_session,
        )
        self.create_checkout_session = to_streamed_response_wrapper(
            billing.create_checkout_session,
        )
        self.handle_webhook = to_streamed_response_wrapper(
            billing.handle_webhook,
        )


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.create_billing_portal_session = async_to_streamed_response_wrapper(
            billing.create_billing_portal_session,
        )
        self.create_checkout_session = async_to_streamed_response_wrapper(
            billing.create_checkout_session,
        )
        self.handle_webhook = async_to_streamed_response_wrapper(
            billing.handle_webhook,
        )
