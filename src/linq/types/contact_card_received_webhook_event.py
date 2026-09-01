# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .webhook_event_type import WebhookEventType

__all__ = ["ContactCardReceivedWebhookEvent", "Data"]


class Data(BaseModel):
    """Payload for contact_card.received webhook events.

    A contact belongs to a line, not to an individual chat. You receive one event per person who
    shares their contact, regardless of how many chats they have in common with your line.

    The event fires again whenever the shared contact's name or media changes.
    """

    first_name: str
    """First name from the shared contact card"""

    last_name: str
    """Last name from the shared contact card (may be empty)"""

    owner_handle: str
    """Which of your lines they shared it with."""

    sender_handle: str
    """The person who shared their card — a phone number or email address."""

    media_url: Optional[str] = None
    """URL of the contact's media, served from `cdn.linqapp.com`.

    `null` when the contact shared no media, and also when media was shared but
    could not be retrieved — this field does not distinguish the two.

    Download the media and store it yourself. The URL may be signed and expire, in
    as little as 45 minutes, and altering its query string invalidates it
    immediately.
    """


class ContactCardReceivedWebhookEvent(BaseModel):
    """Complete webhook payload for contact_card.received events"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """Payload for contact_card.received webhook events.

    A contact belongs to a line, not to an individual chat. You receive one event
    per person who shares their contact, regardless of how many chats they have in
    common with your line.

    The event fires again whenever the shared contact's name or media changes.
    """

    event_id: str
    """Unique identifier for this event (for deduplication)"""

    event_type: WebhookEventType
    """Valid webhook event types that can be subscribed to.

    **Note:** `message.edited` is only delivered to subscriptions using
    `webhook_version: "2026-02-03"`. Subscribing to this event on a v2025
    subscription will not produce any deliveries.
    """

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
