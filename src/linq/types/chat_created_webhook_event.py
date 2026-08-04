# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.chat_handle import ChatHandle
from .webhook_event_type import WebhookEventType
from .shared.service_type import ServiceType

__all__ = ["ChatCreatedWebhookEvent", "Data", "DataHealthStatus"]


class DataHealthStatus(BaseModel):
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

    `OPTED_OUT` is terminal — the recipient sent `STOP`, `UNSUBSCRIBE`, `OPTOUT`,
    `CANCEL`, `END`, or `QUIT`. The keyword must be the whole trimmed message, never
    part of a longer one: `STOP` counts, `please stop` does not. Most keywords must
    match exactly, including case. `OPT OUT` is the exception — it matches in any
    casing, with or without the space or a hyphen, so `opt out`, `Opt-Out` and
    `optout` all count. It clears if they later send `START`, `OPTIN`, or `UNSTOP`,
    or if they keep replying on the chat — sustained two-way conversation is treated
    as a sign the stop keyword was a false positive.

    Linq enforces this: while a recipient is opted out, every send to them is
    rejected with `403` (error code `2024`) before the message is queued, across
    every chat and every line on your account. Nothing is delivered, including a
    final courtesy message — to send one, set `override_optout: true` on that single
    request.
    """

    updated_at: datetime
    """When this status last changed."""


class Data(BaseModel):
    """Payload for chat.created webhook events.

    Matches GET /v3/chats/{chatId} response.
    """

    id: str
    """Unique identifier for the chat"""

    created_at: datetime
    """When the chat was created"""

    display_name: Optional[str] = None
    """Display name for the chat.

    Defaults to a comma-separated list of recipient handles. Can be updated for
    group chats.
    """

    handles: List[ChatHandle]
    """List of chat participants with full handle details.

    Always contains at least two handles (your phone number and the other
    participant).
    """

    health_status: DataHealthStatus
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

    updated_at: datetime
    """When the chat was last updated"""

    service: Optional[ServiceType] = None
    """Messaging service type"""


class ChatCreatedWebhookEvent(BaseModel):
    """Complete webhook payload for chat.created events"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """Payload for chat.created webhook events.

    Matches GET /v3/chats/{chatId} response.
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
