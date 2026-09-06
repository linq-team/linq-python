# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.chat_handle import ChatHandle
from .webhook_event_type import WebhookEventType

__all__ = [
    "PollFailedWebhookEvent",
    "Data",
    "DataChat",
    "DataError",
    "DataPoll",
    "DataPollOption",
    "DataPollOptionVoter",
]


class DataChat(BaseModel):
    """Chat info for poll webhook events."""

    id: str

    is_group: Optional[bool] = None

    owner_handle: Optional[ChatHandle] = None


class DataError(BaseModel):
    code: int
    """Error codes in webhook failure events.

    The possible set varies by event: message.failed and poll.failed can carry 3007,
    4001, 4002, 4005, 4006, 4007, or 4008; the group update failure events
    (chat.group_name_update_failed, chat.group_icon_update_failed) carry 3007 or
    4001; chat.background_update_failed carries 1005, 2011, 4001, or 5002.
    """

    message: str


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
    """Payload for poll.failed — an outbound poll (or poll action) that failed to send.

    Carries the
    poll snapshot at failure time plus the error and when it failed.
    """

    chat: DataChat
    """Chat info for poll webhook events."""

    direction: Literal["inbound", "outbound"]

    error: DataError

    failed_at: datetime

    message_id: str

    poll: DataPoll

    service: str

    sender_handle: Optional[ChatHandle] = None
    """Null on failure (the send never landed)."""

    zero_retention: Optional[bool] = None
    """True when this poll was sent on a zero-day-retention line.

    `poll` is built from the same database read as poll.sent/delivered/read, so
    every option's `text` is empty.
    """


class PollFailedWebhookEvent(BaseModel):
    """Complete webhook payload for poll.failed events"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """Payload for poll.failed — an outbound poll (or poll action) that failed to send.

    Carries the poll snapshot at failure time plus the error and when it failed.
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
