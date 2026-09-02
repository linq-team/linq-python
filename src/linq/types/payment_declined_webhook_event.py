# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentDeclinedWebhookEvent", "Data", "DataDiscount", "DataNatural", "DataStripe"]


class DataDiscount(BaseModel):
    """Subscription mode — the discount Stripe applied, read back
    from the coupon.

    Absent when none was applied.
    """

    coupon: Optional[str] = None

    label: Optional[str] = None
    """Name of the coupon/promo code displayed to customers."""

    promotion_code: Optional[str] = None


class DataNatural(BaseModel):
    """Natural-rail join keys, present when `rail: natural`."""

    payment_request_id: Optional[str] = None
    """The Natural payment request (`prq_...`)."""

    transaction_id: Optional[str] = None
    """The settled transaction (`txn_...`)."""


class DataStripe(BaseModel):
    """
    Ids of the Stripe objects on your connected account — join
    keys into your own Stripe Dashboard/API. Manage a
    subscription's post-checkout lifecycle with `subscription_id`.
    """

    customer_id: Optional[str] = None
    """
    The Customer the request is attached to (`cus_...`). Always set in subscription
    mode; set in payment mode only when the request was created with a
    `customer_id`.
    """

    payment_intent_id: Optional[str] = None
    """The PaymentIntent collected at checkout (`pi_...`)."""

    subscription_id: Optional[str] = None
    """Subscription mode — the Subscription (`sub_...`)."""


class Data(BaseModel):
    """
    The payment request, as returned by
    `GET /v3/payment_requests/{paymentRequestId}`.
    """

    id: str
    """The payment request id."""

    amount: int
    """What was charged at checkout, in the currency's minor units.

    In `subscription` mode this is the first invoice's total — all items after any
    discounts are applied.
    """

    checkout_url: str
    """
    URL the recipient opens to pay
    (`https://zero.linqapp.com/pay/{slug}?session=...`).
    """

    created_at: datetime

    currency: str

    object: str

    status: Literal["succeeded", "failed", "canceled", "expired"]

    description: Optional[str] = None

    discount: Optional[DataDiscount] = None
    """Subscription mode — the discount Stripe applied, read back from the coupon.

    Absent when none was applied.
    """

    interval: Optional[Literal["day", "week", "month", "year"]] = None
    """Subscription mode — how often the subscription renews."""

    interval_count: Optional[int] = None
    """Subscription mode — intervals per renewal."""

    metadata: Optional[Dict[str, str]] = None

    mode: Optional[Literal["payment", "subscription"]] = None
    """Whether the request collected a one-time charge or started a subscription."""

    natural: Optional[DataNatural] = None
    """Natural-rail join keys, present when `rail: natural`."""

    price_id: Optional[str] = None
    """Subscription mode — the recurring price subscribed to."""

    quantity: Optional[int] = None
    """Subscription mode — units of the price subscribed to."""

    rail: Optional[Literal["stripe", "natural"]] = None
    """The rail this request settled on."""

    stripe: Optional[DataStripe] = None
    """
    Ids of the Stripe objects on your connected account — join keys into your own
    Stripe Dashboard/API. Manage a subscription's post-checkout lifecycle with
    `subscription_id`.
    """

    trial_end: Optional[datetime] = None
    """Subscription mode — when the free trial ends and the first charge happens.

    On a trial request, `payment.succeeded` means the payment method was collected
    ($0 moved).
    """

    updated_at: Optional[datetime] = None


class PaymentDeclinedWebhookEvent(BaseModel):
    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """
    The payment request, as returned by
    `GET /v3/payment_requests/{paymentRequestId}`.
    """

    event_id: str
    """Unique identifier for this event (for deduplication)"""

    event_type: Literal[
        "payment.succeeded",
        "payment.canceled",
        "payment.expired",
        "message.sent",
        "message.received",
        "message.read",
        "message.delivered",
        "message.failed",
        "message.edited",
        "reaction.added",
        "reaction.removed",
        "poll.received",
        "poll.failed",
        "poll.sent",
        "poll.delivered",
        "poll.read",
        "poll.updated",
        "poll.vote.added",
        "poll.vote.removed",
        "poll.reaction.added",
        "participant.added",
        "participant.removed",
        "chat.created",
        "chat.group_name_updated",
        "chat.group_icon_updated",
        "chat.group_name_update_failed",
        "chat.group_icon_update_failed",
        "chat.background_updated",
        "chat.background_update_failed",
        "chat.typing_indicator.started",
        "chat.typing_indicator.stopped",
        "phone_number.status_updated",
        "contact_card.received",
        "call.initiated",
        "call.ringing",
        "call.answered",
        "call.ended",
        "call.failed",
        "call.declined",
        "call.no_answer",
        "location.sharing.started",
        "location.sharing.stopped",
        "payment.declined",
        "payment.authorized",
        "connection.created",
        "connection.revoked",
    ]

    partner_id: str
    """Partner identifier. Present on all webhooks for cross-referencing."""

    trace_id: str
    """Trace ID for debugging and correlation across systems."""

    webhook_version: str
    """
    Date-based webhook payload version. Determined by the `?version=` query
    parameter in your webhook subscription URL. If no version parameter is
    specified, defaults based on subscription creation date.
    """
