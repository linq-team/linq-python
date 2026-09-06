# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.chat_handle import ChatHandle
from .webhook_event_type import WebhookEventType

__all__ = ["PollDeliveredWebhookEvent", "Data", "DataChat", "DataPoll", "DataPollOption", "DataPollOptionVoter"]


class DataChat(BaseModel):
    """Chat info for poll webhook events."""

    id: str

    is_group: Optional[bool] = None

    owner_handle: Optional[ChatHandle] = None


class DataPollOptionVoter(BaseModel):
    handle: str

    voted_at: datetime


class DataPollOption(BaseModel):
    can_be_edited: bool

    creator_handle: ChatHandle
    """
    The participant who added this option (poll creator for the initial options;
    whoever added later ones). On a poll.updated this differs from the event's
    `sender_handle` whenever a remote participant added the option. Null when
    unknown.
    """

    option_id: str

    text: str

    voters: List[DataPollOptionVoter]


class DataPoll(BaseModel):
    options: List[DataPollOption]

    total_voters: int
    """Distinct participants across the whole poll."""


class Data(BaseModel):
    """Payload for poll.sent, poll.delivered, and poll.read webhook events.

    Timestamps indicate
    state (null = not yet happened): sent → sent_at; delivered → +delivered_at; read → +read_at.
    """

    chat: DataChat
    """Chat info for poll webhook events."""

    created_at: datetime

    direction: Literal["inbound", "outbound"]

    message_id: str

    poll: DataPoll

    service: str

    updated_at: datetime

    delivered_at: Optional[datetime] = None

    read_at: Optional[datetime] = None

    sender_handle: Optional[ChatHandle] = None
    """The handle that sent the poll."""

    sent_at: Optional[datetime] = None

    zero_retention: Optional[bool] = None
    """True when this poll was sent on a zero-day-retention line.

    Every option's `text` is empty in that case — Linq never persists poll option
    text, so there is nothing to include here. The real text was only ever shown
    once, synchronously, in the API response when the poll was created or added to.
    """


class PollDeliveredWebhookEvent(BaseModel):
    """Complete webhook payload for poll.delivered events"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """Payload for poll.sent, poll.delivered, and poll.read webhook events.

    Timestamps indicate state (null = not yet happened): sent → sent_at; delivered →
    +delivered_at; read → +read_at.
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
