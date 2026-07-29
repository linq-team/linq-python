# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import payment_handle_verify_params
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
from ..types.payment_handle_connection import PaymentHandleConnection

__all__ = ["PaymentHandlesResource", "AsyncPaymentHandlesResource"]


class PaymentHandlesResource(SyncAPIResource):
    """
    Let an agent pay on a customer's behalf with a single-use virtual card.
    Connect a customer once, then create a payment — a virtual card is minted
    scoped to that purchase and the card details are handed back for checkout.
    """

    @cached_property
    def with_raw_response(self) -> PaymentHandlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return PaymentHandlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentHandlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return PaymentHandlesResourceWithStreamingResponse(self)

    def connect(
        self,
        handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentHandleConnection:
        """
        Starts connecting a customer (by phone/email) so an agent can pay on their
        behalf. Linq drives the OTP + consent ceremony through the messaging channel;
        this returns `pending` and a `connection.created` webhook fires once the
        customer completes it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return self._post(
            path_template("/v3/payments/handles/{handle}/connect", handle=handle),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentHandleConnection,
        )

    def connection(
        self,
        handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentHandleConnection:
        """
        Get a handle's connection status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return self._get(
            path_template("/v3/payments/handles/{handle}/connection", handle=handle),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentHandleConnection,
        )

    def revoke(
        self,
        handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentHandleConnection:
        """Revokes this partner's grant for the customer.

        Only your grant is removed; the
        customer's wallet at the provider is untouched.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return self._delete(
            path_template("/v3/payments/handles/{handle}/connection", handle=handle),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentHandleConnection,
        )

    def verify(
        self,
        handle: str,
        *,
        code: str,
        connect_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentHandleConnection:
        """
        Completes the ceremony `connect` started: verifies the code, records the
        customer's consent, and stores the connection. Returns `connected` on success,
        after which payments for this handle no longer need the customer present.

        The code reaches you however your channel works — typically the customer replies
        with it in the thread. Codes are single-use and short-lived; if one has expired,
        call `connect` again for a fresh `connect_id`.

        Args:
          code: The one-time code the customer received.

          connect_id: The id returned by `connect`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return self._post(
            path_template("/v3/payments/handles/{handle}/verify", handle=handle),
            body=maybe_transform(
                {
                    "code": code,
                    "connect_id": connect_id,
                },
                payment_handle_verify_params.PaymentHandleVerifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentHandleConnection,
        )


class AsyncPaymentHandlesResource(AsyncAPIResource):
    """
    Let an agent pay on a customer's behalf with a single-use virtual card.
    Connect a customer once, then create a payment — a virtual card is minted
    scoped to that purchase and the card details are handed back for checkout.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPaymentHandlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentHandlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentHandlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncPaymentHandlesResourceWithStreamingResponse(self)

    async def connect(
        self,
        handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentHandleConnection:
        """
        Starts connecting a customer (by phone/email) so an agent can pay on their
        behalf. Linq drives the OTP + consent ceremony through the messaging channel;
        this returns `pending` and a `connection.created` webhook fires once the
        customer completes it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return await self._post(
            path_template("/v3/payments/handles/{handle}/connect", handle=handle),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentHandleConnection,
        )

    async def connection(
        self,
        handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentHandleConnection:
        """
        Get a handle's connection status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return await self._get(
            path_template("/v3/payments/handles/{handle}/connection", handle=handle),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentHandleConnection,
        )

    async def revoke(
        self,
        handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentHandleConnection:
        """Revokes this partner's grant for the customer.

        Only your grant is removed; the
        customer's wallet at the provider is untouched.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return await self._delete(
            path_template("/v3/payments/handles/{handle}/connection", handle=handle),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentHandleConnection,
        )

    async def verify(
        self,
        handle: str,
        *,
        code: str,
        connect_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentHandleConnection:
        """
        Completes the ceremony `connect` started: verifies the code, records the
        customer's consent, and stores the connection. Returns `connected` on success,
        after which payments for this handle no longer need the customer present.

        The code reaches you however your channel works — typically the customer replies
        with it in the thread. Codes are single-use and short-lived; if one has expired,
        call `connect` again for a fresh `connect_id`.

        Args:
          code: The one-time code the customer received.

          connect_id: The id returned by `connect`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return await self._post(
            path_template("/v3/payments/handles/{handle}/verify", handle=handle),
            body=await async_maybe_transform(
                {
                    "code": code,
                    "connect_id": connect_id,
                },
                payment_handle_verify_params.PaymentHandleVerifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentHandleConnection,
        )


class PaymentHandlesResourceWithRawResponse:
    def __init__(self, payment_handles: PaymentHandlesResource) -> None:
        self._payment_handles = payment_handles

        self.connect = to_raw_response_wrapper(
            payment_handles.connect,
        )
        self.connection = to_raw_response_wrapper(
            payment_handles.connection,
        )
        self.revoke = to_raw_response_wrapper(
            payment_handles.revoke,
        )
        self.verify = to_raw_response_wrapper(
            payment_handles.verify,
        )


class AsyncPaymentHandlesResourceWithRawResponse:
    def __init__(self, payment_handles: AsyncPaymentHandlesResource) -> None:
        self._payment_handles = payment_handles

        self.connect = async_to_raw_response_wrapper(
            payment_handles.connect,
        )
        self.connection = async_to_raw_response_wrapper(
            payment_handles.connection,
        )
        self.revoke = async_to_raw_response_wrapper(
            payment_handles.revoke,
        )
        self.verify = async_to_raw_response_wrapper(
            payment_handles.verify,
        )


class PaymentHandlesResourceWithStreamingResponse:
    def __init__(self, payment_handles: PaymentHandlesResource) -> None:
        self._payment_handles = payment_handles

        self.connect = to_streamed_response_wrapper(
            payment_handles.connect,
        )
        self.connection = to_streamed_response_wrapper(
            payment_handles.connection,
        )
        self.revoke = to_streamed_response_wrapper(
            payment_handles.revoke,
        )
        self.verify = to_streamed_response_wrapper(
            payment_handles.verify,
        )


class AsyncPaymentHandlesResourceWithStreamingResponse:
    def __init__(self, payment_handles: AsyncPaymentHandlesResource) -> None:
        self._payment_handles = payment_handles

        self.connect = async_to_streamed_response_wrapper(
            payment_handles.connect,
        )
        self.connection = async_to_streamed_response_wrapper(
            payment_handles.connection,
        )
        self.revoke = async_to_streamed_response_wrapper(
            payment_handles.revoke,
        )
        self.verify = async_to_streamed_response_wrapper(
            payment_handles.verify,
        )
