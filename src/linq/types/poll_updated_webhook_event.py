# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.chat_handle import ChatHandle
from .webhook_event_type import WebhookEventType

__all__ = ["PollUpdatedWebhookEvent", "Data", "DataAddedOption", "DataAddedOptionVoter", "DataChat"]


class DataAddedOptionVoter(BaseModel):
    handle: str

    voted_at: datetime


class DataAddedOption(BaseModel):
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

    voters: List[DataAddedOptionVoter]


class DataChat(BaseModel):
    """Chat info for poll webhook events."""

    id: str

    is_group: Optional[bool] = None

    owner_handle: Optional[ChatHandle] = None


class Data(BaseModel):
    """Payload for poll.updated (option(s) added — add-only)."""

    added_options: List[DataAddedOption]
    """Only the options this update added — never the ones the poll already had.

    Fetch the poll to read its full option set.
    """

    chat: DataChat
    """Chat info for poll webhook events."""

    direction: Literal["inbound", "outbound"]

    message_id: str

    sender_handle: ChatHandle
    """Your line — the one that received or sent this update.

    Always present. On an inbound update this is NOT who added the option: use
    `added_options[].creator_handle` for that, which will be the remote participant.
    """

    service: str

    zero_retention: Optional[bool] = None
    """True when zero-day-retention applies to this update.

    Behavior differs by `direction`: on an inbound update, `added_options[].text` is
    the real text a participant just added; on an outbound update, it is empty — you
    already saw the real text once, synchronously, in the API response when you made
    the add, and this webhook is built from a database read, which never stored it.
    """


class PollUpdatedWebhookEvent(BaseModel):
    """Complete webhook payload for poll.updated events"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """Payload for poll.updated (option(s) added — add-only)."""

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
