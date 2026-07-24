# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import payment_request_list_params, payment_request_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.payment_request import PaymentRequest
from ..types.payment_request_list_response import PaymentRequestListResponse

__all__ = ["PaymentRequestsResource", "AsyncPaymentRequestsResource"]


class PaymentRequestsResource(SyncAPIResource):
    """Request a payment from a recipient over iMessage.

    You create a payment
    request, send its `checkout_url` to the recipient, and they pay with Apple
    Pay or card. Funds settle **directly to your own Stripe account** — Linq
    never holds the money.

    ## How it works

    1. **Create** a payment request with an amount and currency. You get back a
       `checkout_url` and a `status` of `requested`.
    2. **Send** the `checkout_url` to the recipient as a `link` message part so
       it arrives as a tappable card (see *Sending the link* below).
    3. The recipient **pays** on the hosted checkout (Apple Pay App Clip on a
       supported iPhone, web checkout everywhere else).
    4. You receive a **`payment.succeeded`** webhook and the request's `status`
       becomes `succeeded`. Requests you don't collect eventually `expire`.

    ## Connected accounts (Stripe Standard, direct charges)

    Agent Pay runs on **Stripe Connect Standard accounts** using **direct
    charges**: the charge is created on *your* connected account and **you are
    the merchant of record**. That means the money, the payout schedule, the
    customer relationship, and the compliance surface are all yours — Linq
    orchestrates the request and the checkout but is never in the funds flow.

    **Refunds, disputes, and chargebacks are handled by you, in your own Stripe
    Dashboard.** Because charges settle directly to your account, Linq has no
    custody of the funds and cannot issue refunds or contest disputes on your
    behalf — and there is no refund/dispute endpoint in this API by design. Use
    the Stripe Dashboard (or the Stripe API on your own account) for the money
    lifecycle after a payment succeeds.

    ## Getting set up

    Open **Agent Pay** in your Linq dashboard
    (`https://zero.linqapp.com/organization/payments`), click **Connect Stripe**,
    and complete Stripe's onboarding (business details + a bank account). When
    your account reaches `charges_enabled`, request creation unlocks; until you
    connect Stripe, `POST /v3/payment_requests` returns `403`. You can keep
    collecting even while Stripe finishes background verification.

    ## Subscriptions

    Set `mode: subscription` on `POST /v3/payment_requests` to start an
    **auto-renewing subscription** instead of a one-time charge. Instead of an
    amount, you pass a `price_id` — an active **recurring Price** on your
    connected Stripe account (create one in your Stripe Dashboard under
    Product catalog; if you sell through Stripe Payment Links today, reuse the
    price your link is built from). The recipient pays the first invoice at
    the same checkout, and their payment method is saved to the subscription
    for automatic renewals.

    The division of labor is deliberate: **Linq handles the first payment,
    your Stripe account handles the rest.** The request reaches `succeeded`
    when the first invoice is paid; from then on the subscription lives
    entirely on your connected account. The response's `stripe` object gives
    you the join keys — `customer_id` and `subscription_id` — so renewals,
    plan changes, dunning, and cancellation are managed with your own Stripe
    Dashboard/API and your own Stripe webhooks. Your `metadata` is stamped on
    the Customer and Subscription, so correlating in either direction is
    trivial. There are no renewal webhooks from Linq by design.

    ### Free trials

    Add `trial_period_days` (or a fixed `trial_end` timestamp) to start the
    subscription with a free trial. The checkout still collects the
    recipient's payment method — the pay sheet shows "$0 due today" with the
    first charge date — and saves it to the subscription; Stripe bills it
    automatically when the trial ends. The request reaches `succeeded` when
    the card is collected, and the response carries `trial_end`. If the trial
    would end without a payment method on file, the subscription cancels
    rather than generating unpayable invoices. Trial lifecycle after checkout
    (extending, ending early) is managed in your own Stripe account via
    `stripe.subscription_id`.

    A subscription request you cancel (or that expires unpaid) cancels the
    incomplete Stripe subscription — nothing lingers on your account.

    ## Pre-created customers

    By default each request stands alone: payment mode attaches no Customer,
    and subscription mode creates a fresh one. If you already manage
    Customers on your connected account, pass their id as `customer_id`
    (`cus_...`) on create — in payment mode the charge lands on that
    customer's payment history, and in subscription mode the subscription is
    created on them instead of on a new Customer. The id must reference an
    existing, non-deleted customer on your connected account or the request
    fails with `400`. We never modify a customer you pass — no metadata is
    stamped on it.

    ## Sending the link

    Deliver the `checkout_url` as a **`link` message part** via
    `POST /v3/chats/{chatId}/messages` — it renders as a rich card with your
    branding (title, amount, image) instead of a bare URL, which converts far
    better. A `link` part must be the only part in the message. See
    [Rich Link Previews](/guides/messaging/sending-messages).

    On a supported iPhone the link opens an **Apple Pay App Clip** — a native,
    no-install checkout sheet. Everywhere else (Android, desktop, iPhones
    without the App Clip yet) the same URL opens the web checkout, so the link
    always works. The App Clip experience for your payment links is registered
    automatically by Linq and refreshed whenever you update your Agent Pay
    branding; a newly registered experience can take up to ~24 hours to
    activate on Apple's side, during which links open the web checkout.

    ## Webhooks

    Subscribe to payment lifecycle events to reconcile server-side rather than
    polling: `payment.succeeded`, `payment.canceled`, and `payment.expired`.
    Each event carries the payment request id, amount, currency, and your
    `metadata`. See [Webhooks](/guides/webhooks).
    """

    @cached_property
    def with_raw_response(self) -> PaymentRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return PaymentRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return PaymentRequestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int | Omit = omit,
        currency: str | Omit = omit,
        customer_id: str | Omit = omit,
        description: str | Omit = omit,
        from_: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        mode: Literal["payment", "subscription"] | Omit = omit,
        payer_handle: str | Omit = omit,
        price_id: str | Omit = omit,
        quantity: int | Omit = omit,
        rail: Literal["stripe", "natural"] | Omit = omit,
        trial_end: Union[str, datetime] | Omit = omit,
        trial_period_days: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentRequest:
        """
        Creates a payment request and returns a `checkout_url` the recipient opens to
        pay with Apple Pay or card. Funds settle directly to your connected Stripe
        account. A payment request is independent of any chat; to associate one with a
        chat for your records, store the chat id in `metadata`. Requires your connected
        account to be `charges_enabled` (returns `403` otherwise).

        Set `mode: subscription` with a recurring `price_id` from your connected Stripe
        account to start an **auto-renewing subscription** instead of a one-time charge
        — the recipient pays the first invoice at checkout and the response's `stripe`
        object carries the customer and subscription ids for the ongoing lifecycle in
        your own Stripe account. See the _Subscriptions_ section of the tag overview.

        In either mode, pass `customer_id` to attach the request to an **existing
        Customer** on your connected account instead of creating a new one — see
        _Pre-created customers_ in the tag overview.

        Args:
          amount: Amount to charge, in the currency's minor units (e.g. cents). Must be at least
              the payment provider's minimum (50 for `usd`). Required in `payment` mode; must
              be omitted in `subscription` mode (the amount comes from the price).

          currency: Three-letter ISO 4217 currency code. Only `usd` is currently supported. Required
              in `payment` mode; must be omitted in `subscription` mode (the currency comes
              from the price).

          customer_id: Optional id of an **existing Customer** on your connected Stripe account
              (`cus_...`) to attach this request to, instead of a new Customer being created.
              In `payment` mode the charge lands on that customer's payment history; in
              `subscription` mode the subscription is created on them. The customer must exist
              (and not be deleted) on your connected account.

          description: Optional description shown to the recipient at checkout.

          from_: Required for `rail: natural`. The line the request is sent from, in E.164
              format. Must be a phone number your organization owns.

          metadata: Optional key/value metadata (up to 49 keys) echoed back on retrieval and on
              `payment.*` webhooks, and stamped on the Stripe objects we create on your
              connected account (the PaymentIntent, and in subscription mode the Subscription
              and any Customer created for you — a customer you pass via `customer_id` is
              never modified) — use it to correlate a request with your own records (e.g. a
              chat id). Keys starting with `linq_` are reserved.

          mode: `payment` (default) collects a one-time charge for `amount` + `currency`.
              `subscription` starts an auto-renewing subscription from a recurring `price_id`
              on your connected Stripe account: the recipient pays the first invoice at
              checkout and Stripe renews it automatically from then on.

          payer_handle: Required for `rail: natural`. The payer to bill, in E.164 format.

          price_id: Subscription mode only (required there): id of an **active recurring Price** on
              your connected Stripe account (`price_...`). If you sell through Stripe Payment
              Links today, pass the same price the link was built from to get the native
              iMessage checkout for it.

          quantity: Subscription mode only — units of the price to subscribe to.

          rail: Payment rail. `stripe` (default) is the direct-charge flow that settles to your
              connected Stripe account. `natural` collects through the Natural custodial
              wallet; it requires `from` + `payer_handle` and that your organization has
              completed Natural merchant onboarding.

          trial_end: Subscription mode only — end the free trial at a fixed timestamp (must be in the
              future) instead of a day count. Mutually exclusive with `trial_period_days`.

          trial_period_days: Subscription mode only — start with a free trial of this many days. The
              recipient's card is still collected at checkout (Apple Pay or card), saved to
              the subscription, and first charged when the trial ends. Mutually exclusive with
              `trial_end`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/v3/payment_requests",
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "customer_id": customer_id,
                    "description": description,
                    "from_": from_,
                    "metadata": metadata,
                    "mode": mode,
                    "payer_handle": payer_handle,
                    "price_id": price_id,
                    "quantity": quantity,
                    "rail": rail,
                    "trial_end": trial_end,
                    "trial_period_days": trial_period_days,
                },
                payment_request_create_params.PaymentRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRequest,
        )

    def retrieve(
        self,
        payment_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentRequest:
        """
        Returns a payment request's status and details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_request_id:
            raise ValueError(f"Expected a non-empty value for `payment_request_id` but received {payment_request_id!r}")
        return self._get(
            path_template("/v3/payment_requests/{payment_request_id}", payment_request_id=payment_request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRequest,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["requested", "succeeded", "canceled", "expired"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentRequestListResponse:
        """Lists your payment requests, newest first, for reconciliation.

        Paginate with
        `limit` + `offset`; `has_more` indicates whether another page exists.

        Args:
          limit: Max results to return (default 20, max 100).

          offset: Number of results to skip.

          status: Filter by lifecycle status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/payment_requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    payment_request_list_params.PaymentRequestListParams,
                ),
            ),
            cast_to=PaymentRequestListResponse,
        )

    def cancel(
        self,
        payment_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentRequest:
        """
        Cancels an unpaid payment request: the underlying payment intent is canceled and
        the request moves to `canceled`. A request that is already paid, canceled, or
        expired returns 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_request_id:
            raise ValueError(f"Expected a non-empty value for `payment_request_id` but received {payment_request_id!r}")
        return self._post(
            path_template("/v3/payment_requests/{payment_request_id}/cancel", payment_request_id=payment_request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRequest,
        )


class AsyncPaymentRequestsResource(AsyncAPIResource):
    """Request a payment from a recipient over iMessage.

    You create a payment
    request, send its `checkout_url` to the recipient, and they pay with Apple
    Pay or card. Funds settle **directly to your own Stripe account** — Linq
    never holds the money.

    ## How it works

    1. **Create** a payment request with an amount and currency. You get back a
       `checkout_url` and a `status` of `requested`.
    2. **Send** the `checkout_url` to the recipient as a `link` message part so
       it arrives as a tappable card (see *Sending the link* below).
    3. The recipient **pays** on the hosted checkout (Apple Pay App Clip on a
       supported iPhone, web checkout everywhere else).
    4. You receive a **`payment.succeeded`** webhook and the request's `status`
       becomes `succeeded`. Requests you don't collect eventually `expire`.

    ## Connected accounts (Stripe Standard, direct charges)

    Agent Pay runs on **Stripe Connect Standard accounts** using **direct
    charges**: the charge is created on *your* connected account and **you are
    the merchant of record**. That means the money, the payout schedule, the
    customer relationship, and the compliance surface are all yours — Linq
    orchestrates the request and the checkout but is never in the funds flow.

    **Refunds, disputes, and chargebacks are handled by you, in your own Stripe
    Dashboard.** Because charges settle directly to your account, Linq has no
    custody of the funds and cannot issue refunds or contest disputes on your
    behalf — and there is no refund/dispute endpoint in this API by design. Use
    the Stripe Dashboard (or the Stripe API on your own account) for the money
    lifecycle after a payment succeeds.

    ## Getting set up

    Open **Agent Pay** in your Linq dashboard
    (`https://zero.linqapp.com/organization/payments`), click **Connect Stripe**,
    and complete Stripe's onboarding (business details + a bank account). When
    your account reaches `charges_enabled`, request creation unlocks; until you
    connect Stripe, `POST /v3/payment_requests` returns `403`. You can keep
    collecting even while Stripe finishes background verification.

    ## Subscriptions

    Set `mode: subscription` on `POST /v3/payment_requests` to start an
    **auto-renewing subscription** instead of a one-time charge. Instead of an
    amount, you pass a `price_id` — an active **recurring Price** on your
    connected Stripe account (create one in your Stripe Dashboard under
    Product catalog; if you sell through Stripe Payment Links today, reuse the
    price your link is built from). The recipient pays the first invoice at
    the same checkout, and their payment method is saved to the subscription
    for automatic renewals.

    The division of labor is deliberate: **Linq handles the first payment,
    your Stripe account handles the rest.** The request reaches `succeeded`
    when the first invoice is paid; from then on the subscription lives
    entirely on your connected account. The response's `stripe` object gives
    you the join keys — `customer_id` and `subscription_id` — so renewals,
    plan changes, dunning, and cancellation are managed with your own Stripe
    Dashboard/API and your own Stripe webhooks. Your `metadata` is stamped on
    the Customer and Subscription, so correlating in either direction is
    trivial. There are no renewal webhooks from Linq by design.

    ### Free trials

    Add `trial_period_days` (or a fixed `trial_end` timestamp) to start the
    subscription with a free trial. The checkout still collects the
    recipient's payment method — the pay sheet shows "$0 due today" with the
    first charge date — and saves it to the subscription; Stripe bills it
    automatically when the trial ends. The request reaches `succeeded` when
    the card is collected, and the response carries `trial_end`. If the trial
    would end without a payment method on file, the subscription cancels
    rather than generating unpayable invoices. Trial lifecycle after checkout
    (extending, ending early) is managed in your own Stripe account via
    `stripe.subscription_id`.

    A subscription request you cancel (or that expires unpaid) cancels the
    incomplete Stripe subscription — nothing lingers on your account.

    ## Pre-created customers

    By default each request stands alone: payment mode attaches no Customer,
    and subscription mode creates a fresh one. If you already manage
    Customers on your connected account, pass their id as `customer_id`
    (`cus_...`) on create — in payment mode the charge lands on that
    customer's payment history, and in subscription mode the subscription is
    created on them instead of on a new Customer. The id must reference an
    existing, non-deleted customer on your connected account or the request
    fails with `400`. We never modify a customer you pass — no metadata is
    stamped on it.

    ## Sending the link

    Deliver the `checkout_url` as a **`link` message part** via
    `POST /v3/chats/{chatId}/messages` — it renders as a rich card with your
    branding (title, amount, image) instead of a bare URL, which converts far
    better. A `link` part must be the only part in the message. See
    [Rich Link Previews](/guides/messaging/sending-messages).

    On a supported iPhone the link opens an **Apple Pay App Clip** — a native,
    no-install checkout sheet. Everywhere else (Android, desktop, iPhones
    without the App Clip yet) the same URL opens the web checkout, so the link
    always works. The App Clip experience for your payment links is registered
    automatically by Linq and refreshed whenever you update your Agent Pay
    branding; a newly registered experience can take up to ~24 hours to
    activate on Apple's side, during which links open the web checkout.

    ## Webhooks

    Subscribe to payment lifecycle events to reconcile server-side rather than
    polling: `payment.succeeded`, `payment.canceled`, and `payment.expired`.
    Each event carries the payment request id, amount, currency, and your
    `metadata`. See [Webhooks](/guides/webhooks).
    """

    @cached_property
    def with_raw_response(self) -> AsyncPaymentRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncPaymentRequestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int | Omit = omit,
        currency: str | Omit = omit,
        customer_id: str | Omit = omit,
        description: str | Omit = omit,
        from_: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        mode: Literal["payment", "subscription"] | Omit = omit,
        payer_handle: str | Omit = omit,
        price_id: str | Omit = omit,
        quantity: int | Omit = omit,
        rail: Literal["stripe", "natural"] | Omit = omit,
        trial_end: Union[str, datetime] | Omit = omit,
        trial_period_days: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentRequest:
        """
        Creates a payment request and returns a `checkout_url` the recipient opens to
        pay with Apple Pay or card. Funds settle directly to your connected Stripe
        account. A payment request is independent of any chat; to associate one with a
        chat for your records, store the chat id in `metadata`. Requires your connected
        account to be `charges_enabled` (returns `403` otherwise).

        Set `mode: subscription` with a recurring `price_id` from your connected Stripe
        account to start an **auto-renewing subscription** instead of a one-time charge
        — the recipient pays the first invoice at checkout and the response's `stripe`
        object carries the customer and subscription ids for the ongoing lifecycle in
        your own Stripe account. See the _Subscriptions_ section of the tag overview.

        In either mode, pass `customer_id` to attach the request to an **existing
        Customer** on your connected account instead of creating a new one — see
        _Pre-created customers_ in the tag overview.

        Args:
          amount: Amount to charge, in the currency's minor units (e.g. cents). Must be at least
              the payment provider's minimum (50 for `usd`). Required in `payment` mode; must
              be omitted in `subscription` mode (the amount comes from the price).

          currency: Three-letter ISO 4217 currency code. Only `usd` is currently supported. Required
              in `payment` mode; must be omitted in `subscription` mode (the currency comes
              from the price).

          customer_id: Optional id of an **existing Customer** on your connected Stripe account
              (`cus_...`) to attach this request to, instead of a new Customer being created.
              In `payment` mode the charge lands on that customer's payment history; in
              `subscription` mode the subscription is created on them. The customer must exist
              (and not be deleted) on your connected account.

          description: Optional description shown to the recipient at checkout.

          from_: Required for `rail: natural`. The line the request is sent from, in E.164
              format. Must be a phone number your organization owns.

          metadata: Optional key/value metadata (up to 49 keys) echoed back on retrieval and on
              `payment.*` webhooks, and stamped on the Stripe objects we create on your
              connected account (the PaymentIntent, and in subscription mode the Subscription
              and any Customer created for you — a customer you pass via `customer_id` is
              never modified) — use it to correlate a request with your own records (e.g. a
              chat id). Keys starting with `linq_` are reserved.

          mode: `payment` (default) collects a one-time charge for `amount` + `currency`.
              `subscription` starts an auto-renewing subscription from a recurring `price_id`
              on your connected Stripe account: the recipient pays the first invoice at
              checkout and Stripe renews it automatically from then on.

          payer_handle: Required for `rail: natural`. The payer to bill, in E.164 format.

          price_id: Subscription mode only (required there): id of an **active recurring Price** on
              your connected Stripe account (`price_...`). If you sell through Stripe Payment
              Links today, pass the same price the link was built from to get the native
              iMessage checkout for it.

          quantity: Subscription mode only — units of the price to subscribe to.

          rail: Payment rail. `stripe` (default) is the direct-charge flow that settles to your
              connected Stripe account. `natural` collects through the Natural custodial
              wallet; it requires `from` + `payer_handle` and that your organization has
              completed Natural merchant onboarding.

          trial_end: Subscription mode only — end the free trial at a fixed timestamp (must be in the
              future) instead of a day count. Mutually exclusive with `trial_period_days`.

          trial_period_days: Subscription mode only — start with a free trial of this many days. The
              recipient's card is still collected at checkout (Apple Pay or card), saved to
              the subscription, and first charged when the trial ends. Mutually exclusive with
              `trial_end`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/v3/payment_requests",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "customer_id": customer_id,
                    "description": description,
                    "from_": from_,
                    "metadata": metadata,
                    "mode": mode,
                    "payer_handle": payer_handle,
                    "price_id": price_id,
                    "quantity": quantity,
                    "rail": rail,
                    "trial_end": trial_end,
                    "trial_period_days": trial_period_days,
                },
                payment_request_create_params.PaymentRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRequest,
        )

    async def retrieve(
        self,
        payment_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentRequest:
        """
        Returns a payment request's status and details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_request_id:
            raise ValueError(f"Expected a non-empty value for `payment_request_id` but received {payment_request_id!r}")
        return await self._get(
            path_template("/v3/payment_requests/{payment_request_id}", payment_request_id=payment_request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRequest,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["requested", "succeeded", "canceled", "expired"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentRequestListResponse:
        """Lists your payment requests, newest first, for reconciliation.

        Paginate with
        `limit` + `offset`; `has_more` indicates whether another page exists.

        Args:
          limit: Max results to return (default 20, max 100).

          offset: Number of results to skip.

          status: Filter by lifecycle status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/payment_requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    payment_request_list_params.PaymentRequestListParams,
                ),
            ),
            cast_to=PaymentRequestListResponse,
        )

    async def cancel(
        self,
        payment_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentRequest:
        """
        Cancels an unpaid payment request: the underlying payment intent is canceled and
        the request moves to `canceled`. A request that is already paid, canceled, or
        expired returns 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_request_id:
            raise ValueError(f"Expected a non-empty value for `payment_request_id` but received {payment_request_id!r}")
        return await self._post(
            path_template("/v3/payment_requests/{payment_request_id}/cancel", payment_request_id=payment_request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRequest,
        )


class PaymentRequestsResourceWithRawResponse:
    def __init__(self, payment_requests: PaymentRequestsResource) -> None:
        self._payment_requests = payment_requests

        self.create = to_raw_response_wrapper(
            payment_requests.create,
        )
        self.retrieve = to_raw_response_wrapper(
            payment_requests.retrieve,
        )
        self.list = to_raw_response_wrapper(
            payment_requests.list,
        )
        self.cancel = to_raw_response_wrapper(
            payment_requests.cancel,
        )


class AsyncPaymentRequestsResourceWithRawResponse:
    def __init__(self, payment_requests: AsyncPaymentRequestsResource) -> None:
        self._payment_requests = payment_requests

        self.create = async_to_raw_response_wrapper(
            payment_requests.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            payment_requests.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            payment_requests.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            payment_requests.cancel,
        )


class PaymentRequestsResourceWithStreamingResponse:
    def __init__(self, payment_requests: PaymentRequestsResource) -> None:
        self._payment_requests = payment_requests

        self.create = to_streamed_response_wrapper(
            payment_requests.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            payment_requests.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            payment_requests.list,
        )
        self.cancel = to_streamed_response_wrapper(
            payment_requests.cancel,
        )


class AsyncPaymentRequestsResourceWithStreamingResponse:
    def __init__(self, payment_requests: AsyncPaymentRequestsResource) -> None:
        self._payment_requests = payment_requests

        self.create = async_to_streamed_response_wrapper(
            payment_requests.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payment_requests.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            payment_requests.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            payment_requests.cancel,
        )
