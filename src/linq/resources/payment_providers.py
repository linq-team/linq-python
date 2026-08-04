# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import payment_provider_connect_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.payment_provider import PaymentProvider
from ..types.payment_provider_connect_response import PaymentProviderConnectResponse

__all__ = ["PaymentProvidersResource", "AsyncPaymentProvidersResource"]


class PaymentProvidersResource(SyncAPIResource):
    """
    Let an agent pay on a customer's behalf with a single-use virtual card.
    Connect a customer once, then create a payment — a virtual card is minted
    scoped to that purchase and the card details are handed back for checkout.
    """

    @cached_property
    def with_raw_response(self) -> PaymentProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return PaymentProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return PaymentProvidersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        provider: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentProvider:
        """
        Returns your organization's onboarding status for a payment provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return self._get(
            path_template("/v3/payments/providers/{provider}", provider=provider),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentProvider,
        )

    def connect(
        self,
        provider: str,
        *,
        return_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentProviderConnectResponse:
        """Begins connecting your organization to a payment provider (e.g.

        `agentcard`).
        Returns a hosted URL where an admin authorizes the connection; on completion the
        provider redirects back and Linq stores your connected credentials.

        Args:
          return_url: Where to send the admin after they authorize the connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return self._post(
            path_template("/v3/payments/providers/{provider}/connect", provider=provider),
            body=maybe_transform(
                {"return_url": return_url}, payment_provider_connect_params.PaymentProviderConnectParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentProviderConnectResponse,
        )


class AsyncPaymentProvidersResource(AsyncAPIResource):
    """
    Let an agent pay on a customer's behalf with a single-use virtual card.
    Connect a customer once, then create a payment — a virtual card is minted
    scoped to that purchase and the card details are handed back for checkout.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPaymentProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncPaymentProvidersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        provider: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentProvider:
        """
        Returns your organization's onboarding status for a payment provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return await self._get(
            path_template("/v3/payments/providers/{provider}", provider=provider),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentProvider,
        )

    async def connect(
        self,
        provider: str,
        *,
        return_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentProviderConnectResponse:
        """Begins connecting your organization to a payment provider (e.g.

        `agentcard`).
        Returns a hosted URL where an admin authorizes the connection; on completion the
        provider redirects back and Linq stores your connected credentials.

        Args:
          return_url: Where to send the admin after they authorize the connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return await self._post(
            path_template("/v3/payments/providers/{provider}/connect", provider=provider),
            body=await async_maybe_transform(
                {"return_url": return_url}, payment_provider_connect_params.PaymentProviderConnectParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentProviderConnectResponse,
        )


class PaymentProvidersResourceWithRawResponse:
    def __init__(self, payment_providers: PaymentProvidersResource) -> None:
        self._payment_providers = payment_providers

        self.retrieve = to_raw_response_wrapper(
            payment_providers.retrieve,
        )
        self.connect = to_raw_response_wrapper(
            payment_providers.connect,
        )


class AsyncPaymentProvidersResourceWithRawResponse:
    def __init__(self, payment_providers: AsyncPaymentProvidersResource) -> None:
        self._payment_providers = payment_providers

        self.retrieve = async_to_raw_response_wrapper(
            payment_providers.retrieve,
        )
        self.connect = async_to_raw_response_wrapper(
            payment_providers.connect,
        )


class PaymentProvidersResourceWithStreamingResponse:
    def __init__(self, payment_providers: PaymentProvidersResource) -> None:
        self._payment_providers = payment_providers

        self.retrieve = to_streamed_response_wrapper(
            payment_providers.retrieve,
        )
        self.connect = to_streamed_response_wrapper(
            payment_providers.connect,
        )


class AsyncPaymentProvidersResourceWithStreamingResponse:
    def __init__(self, payment_providers: AsyncPaymentProvidersResource) -> None:
        self._payment_providers = payment_providers

        self.retrieve = async_to_streamed_response_wrapper(
            payment_providers.retrieve,
        )
        self.connect = async_to_streamed_response_wrapper(
            payment_providers.connect,
        )
