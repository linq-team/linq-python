# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.chat_handle import ChatHandle
from .webhook_event_type import WebhookEventType

__all__ = ["MessageEditedWebhookEvent", "Data", "DataChat", "DataChatHealthStatus", "DataPart"]


class DataChatHealthStatus(BaseModel):
    """**[BETA]** Current health for a chat.

    Always present — chats start at `HEALTHY` and may shift based on engagement and delivery signals on the conversation. Many `AT_RISK` or `CRITICAL` chats on a single line increase the risk of line flagging.

    Switch on `status` to gate sends or surface line health in your UI — the enum is the long-term contract. Each status carries a `doc_url` that deep-links to the relevant section of the Chat Health guide.

    See the [Chat Health guide](/guides/chats/chat-health) for what each status means and how to react.
    """

    doc_url: str
    """Deep-link to the relevant section of the Chat Health guide for this status."""

    status: Literal["HEALTHY", "AT_RISK", "CRITICAL", "OPTED_OUT"]
    """Current health bucket for the chat.

    See the [Chat Health guide](/guides/chats/chat-health) for what each value means
    and how to react. `doc_url` deep-links to the relevant section.

    `OPTED_OUT` — the recipient sent `STOP`, `UNSUBSCRIBE`, `OPTOUT`, `CANCEL`,
    `END`, or `QUIT`. The keyword must be the whole trimmed message, never part of a
    longer one: `STOP` counts, `please stop` does not. Most keywords must match
    exactly, including case. `OPT OUT` is the exception — it matches in any casing,
    with or without the space or a hyphen, so `opt out`, `Opt-Out` and `optout` all
    count. It clears as soon as they reply again: any later message from them that
    is not itself an opt-out keyword opts them back in immediately — a reply in any
    conversation with you counts, the same way the block does.

    Linq enforces this: while a recipient is opted out, every send to them is
    rejected with `403` (error code `2024`) before the message is queued, across
    every chat and every line on your account. Nothing is delivered, including a
    final courtesy message — to send one, set `override_optout: true` on that single
    request.
    """

    updated_at: datetime
    """When this status last changed."""


class DataChat(BaseModel):
    """Chat context"""

    id: str
    """Chat identifier"""

    health_status: DataChatHealthStatus
    """**[BETA]** Current health for a chat.

    Always present — chats start at `HEALTHY` and may shift based on engagement and
    delivery signals on the conversation. Many `AT_RISK` or `CRITICAL` chats on a
    single line increase the risk of line flagging.

    Switch on `status` to gate sends or surface line health in your UI — the enum is
    the long-term contract. Each status carries a `doc_url` that deep-links to the
    relevant section of the Chat Health guide.

    See the [Chat Health guide](/guides/chats/chat-health) for what each status
    means and how to react.
    """

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
