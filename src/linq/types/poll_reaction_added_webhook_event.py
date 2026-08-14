# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel
from .webhook_event_type import WebhookEventType
from .reaction_event_base import ReactionEventBase

__all__ = ["PollReactionAddedWebhookEvent"]


class PollReactionAddedWebhookEvent(BaseModel):
    """Complete webhook payload for poll.reaction.added events"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: ReactionEventBase
    """Payload for poll.reaction.added — a reaction on a poll message.

    Same shape as reaction.added; `message_id` is the poll-definition message's ID.
    Poll reactions are stickers, which iMessage cannot remove, so there is no
    removal counterpart.
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
