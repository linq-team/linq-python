# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel
from .webhook_event_type import WebhookEventType
from .reaction_event_base import ReactionEventBase

__all__ = ["ReactionRemovedWebhookEvent"]


class ReactionRemovedWebhookEvent(BaseModel):
    """Complete webhook payload for reaction.removed events"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: ReactionEventBase
    """Payload for reaction.removed webhook events"""

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
