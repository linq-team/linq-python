# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .webhook_event_type import WebhookEventType

__all__ = ["MessageFailedWebhookEvent", "Data"]


class Data(BaseModel):
    """
    Error details for message.failed webhook events.
    See [WebhookErrorCode](#/components/schemas/WebhookErrorCode) for the full error code reference.

    In rare cases the message can still be delivered after this event fires — a `message.delivered` webhook for the same message ID may follow.
    """

    code: int
    """Error codes in webhook failure events (3007, 4001, 4005)."""

    failed_at: datetime
    """When the failure was detected"""

    chat_id: Optional[str] = None
    """Chat identifier (UUID)"""

    message_id: Optional[str] = None
    """Message identifier (UUID)"""

    reason: Optional[str] = None
    """Human-readable description of the failure"""


class MessageFailedWebhookEvent(BaseModel):
    """Complete webhook payload for message.failed events"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """
    Error details for message.failed webhook events. See
    [WebhookErrorCode](#/components/schemas/WebhookErrorCode) for the full error
    code reference.

    In rare cases the message can still be delivered after this event fires — a
    `message.delivered` webhook for the same message ID may follow.
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
