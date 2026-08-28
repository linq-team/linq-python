# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentRequest", "Discount", "Natural", "Stripe"]


class Discount(BaseModel):
    """Subscription mode — the discount applied, as Stripe applied it."""

    coupon: Optional[str] = None
    """The ID of the coupon applied."""

    label: Optional[str] = None
    """The customer-facing discount description shown at checkout."""

    promotion_code: Optional[str] = None
    """The ID of the promotion code applied, if you passed one."""


class Natural(BaseModel):
    """Natural-rail join keys, present when `rail: natural`."""

    payment_request_id: Optional[str] = None
    """The Natural payment request (`prq_...`)."""

    transaction_id: Optional[str] = None
    """The settled transaction (`txn_...`)."""


class Stripe(BaseModel):
    """
    Ids of the Stripe objects created **on your connected account** —
    your join keys into your own Stripe Dashboard, webhooks, and API.
    After a subscription's first payment succeeds, its ongoing lifecycle
    (renewals, plan changes, cancellation) is managed in your Stripe
    account using `subscription_id`.
    """

    customer_id: Optional[str] = None
    """The Customer this request is attached to (`cus_...`).

    Always set in subscription mode (created for you unless you passed
    `customer_id`); set in payment mode only when you passed one.
    """

    payment_intent_id: Optional[str] = None
    """The PaymentIntent collected at checkout (`pi_...`)."""

    subscription_id: Optional[str] = None
    """Subscription mode — the Subscription (`sub_...`)."""


class PaymentRequest(BaseModel):
    id: str
    """Unique identifier of the payment request."""

    amount: int
    """What the recipient is charged at checkout, in the currency's minor units.

    In `subscription` mode this is the first invoice's amount due — all items after
    any discounts are applied — so a discount that covers the whole invoice returns
    `0` and checkout shows $0.00.
    """

    checkout_url: str
    """
    URL the recipient opens to pay:
    `https://zero.linqapp.com/pay/{slug}?session=...`, where `{slug}` is your
    partner checkout slug.
    """

    created_at: datetime

    currency: str

    mode: Literal["payment", "subscription"]
    """Whether this request collects a one-time charge or starts a subscription."""

    object: str

    status: Literal["requested", "succeeded", "canceled", "expired"]
    """Lifecycle status of the payment request."""

    description: Optional[str] = None

    discount: Optional[Discount] = None
    """Subscription mode — the discount applied, as Stripe applied it."""

    expires_at: Optional[datetime] = None
    """When an unpaid request auto-expires."""

    interval: Optional[Literal["day", "week", "month", "year"]] = None
    """Subscription mode — how often the subscription renews."""

    interval_count: Optional[int] = None
    """Subscription mode — intervals per renewal (e.g. `3` + `month` = quarterly)."""

    metadata: Optional[Dict[str, str]] = None

    natural: Optional[Natural] = None
    """Natural-rail join keys, present when `rail: natural`."""

    paid_at: Optional[datetime] = None
    """When the request was paid. Absent until it succeeds."""

    price_id: Optional[str] = None
    """Subscription mode — the recurring price this request subscribes to."""

    quantity: Optional[int] = None
    """Subscription mode — units of the price subscribed to."""

    rail: Optional[Literal["stripe", "natural"]] = None
    """The rail this request settled on."""

    stripe: Optional[Stripe] = None
    """
    Ids of the Stripe objects created **on your connected account** — your join keys
    into your own Stripe Dashboard, webhooks, and API. After a subscription's first
    payment succeeds, its ongoing lifecycle (renewals, plan changes, cancellation)
    is managed in your Stripe account using `subscription_id`.
    """

    trial_end: Optional[datetime] = None
    """Subscription mode — when the free trial ends and the first charge happens.

    Present only on trial requests; `paid_at`/`succeeded` mean the payment method
    was collected (no funds move until this time).
    """

    updated_at: Optional[datetime] = None
