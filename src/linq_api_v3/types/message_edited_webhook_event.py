# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.chat_handle import ChatHandle
from .webhook_event_type import WebhookEventType

__all__ = ["MessageEditedWebhookEvent", "Data", "DataChat", "DataPart"]


class DataChat(BaseModel):
    """Chat context"""

    id: str
    """Chat identifier"""

    is_group: bool
    """Whether this is a group chat"""

    owner_handle: ChatHandle
    """The handle that owns this chat (your phone number)"""


class DataPart(BaseModel):
    """The edited part"""

    index: int
    """Zero-based index of the edited part within the message"""

    text: str
    """New text content of the part"""


class Data(BaseModel):
    """Payload for `message.edited` events (2026-02-03 format).

    Describes which part of a message was edited and when. Only text parts can be edited.
    Only available for subscriptions using `webhook_version: "2026-02-03"`.
    """

    id: str
    """Message identifier"""

    chat: DataChat
    """Chat context"""

    direction: Literal["outbound", "inbound"]
    """\"outbound" if you sent the original message, "inbound" if you received it"""

    edited_at: datetime
    """When the edit occurred"""

    part: DataPart
    """The edited part"""

    sender_handle: ChatHandle
    """The handle that sent (and edited) this message"""


class MessageEditedWebhookEvent(BaseModel):
    """Complete webhook payload for message.edited events (2026-02-03 format only)"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """Payload for `message.edited` events (2026-02-03 format).

    Describes which part of a message was edited and when. Only text parts can be
    edited. Only available for subscriptions using `webhook_version: "2026-02-03"`.
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
