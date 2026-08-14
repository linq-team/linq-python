# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.chat_handle import ChatHandle
from .webhook_event_type import WebhookEventType

__all__ = ["PollVoteAddedWebhookEvent", "Data", "DataChat"]


class DataChat(BaseModel):
    """Chat info for poll webhook events."""

    id: str

    is_group: Optional[bool] = None

    owner_handle: Optional[ChatHandle] = None


class Data(BaseModel):
    """Payload for poll.vote.added and poll.vote.removed (one option toggled)."""

    chat: DataChat
    """Chat info for poll webhook events."""

    direction: Literal["inbound", "outbound"]

    message_id: str

    option_id: str

    sender_handle: ChatHandle
    """The voter — always present."""

    service: str


class PollVoteAddedWebhookEvent(BaseModel):
    """Complete webhook payload for poll.vote.added events"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """Payload for poll.vote.added and poll.vote.removed (one option toggled)."""

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
