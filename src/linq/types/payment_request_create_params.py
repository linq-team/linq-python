# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentRequestCreateParams"]


class PaymentRequestCreateParams(TypedDict, total=False):
    amount: int
    """Amount to charge, in the currency's minor units (e.g.

    cents). Must be at least the payment provider's minimum (50 for `usd`). Required
    in `payment` mode; must be omitted in `subscription` mode (the amount comes from
    the price).
    """

    currency: str
    """Three-letter ISO 4217 currency code.

    Only `usd` is currently supported. Required in `payment` mode; must be omitted
    in `subscription` mode (the currency comes from the price).
    """

    customer_id: str
    """
    Optional id of an **existing Customer** on your connected Stripe account
    (`cus_...`) to attach this request to, instead of a new Customer being created.
    In `payment` mode the charge lands on that customer's payment history; in
    `subscription` mode the subscription is created on them. The customer must exist
    (and not be deleted) on your connected account.
    """

    description: str
    """Optional description shown to the recipient at checkout."""

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Required for `rail: natural`.

    The line the request is sent from, in E.164 format. Must be a phone number your
    organization owns.
    """

    metadata: Dict[str, str]
    """
    Optional key/value metadata (up to 49 keys) echoed back on retrieval and on
    `payment.*` webhooks, and stamped on the Stripe objects we create on your
    connected account (the PaymentIntent, and in subscription mode the Subscription
    and any Customer created for you — a customer you pass via `customer_id` is
    never modified) — use it to correlate a request with your own records (e.g. a
    chat id). Keys starting with `linq_` are reserved.
    """

    mode: Literal["payment", "subscription"]
    """`payment` (default) collects a one-time charge for `amount` + `currency`.

    `subscription` starts an auto-renewing subscription from a recurring `price_id`
    on your connected Stripe account: the recipient pays the first invoice at
    checkout and Stripe renews it automatically from then on.
    """

    payer_handle: str
    """Required for `rail: natural`. The payer to bill, in E.164 format."""

    price_id: str
    """
    Subscription mode only (required there): id of an **active recurring Price** on
    your connected Stripe account (`price_...`). If you sell through Stripe Payment
    Links today, pass the same price the link was built from to get the native
    iMessage checkout for it.
    """

    quantity: int
    """Subscription mode only — units of the price to subscribe to."""

    rail: Literal["stripe", "natural"]
    """Payment rail.

    `stripe` (default) is the direct-charge flow that settles to your connected
    Stripe account. `natural` collects through the Natural custodial wallet; it
    requires `from` + `payer_handle` and that your organization has completed
    Natural merchant onboarding.
    """

    trial_end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Subscription mode only — end the free trial at a fixed timestamp (must be in the
    future) instead of a day count. Mutually exclusive with `trial_period_days`.
    """

    trial_period_days: int
    """
    Subscription mode only — start with a free trial of this many days. The
    recipient's card is still collected at checkout (Apple Pay or card), saved to
    the subscription, and first charged when the trial ends. Mutually exclusive with
    `trial_end`.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
