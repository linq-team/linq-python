# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.chat_handle import ChatHandle
from .shared.service_type import ServiceType

__all__ = ["Chat", "HealthStatus"]


class HealthStatus(BaseModel):
    """**[BETA]** Current health for a chat.

    Always present — chats start at `HEALTHY` and may shift based on engagement and delivery signals on the conversation. Many `AT_RISK` or `CRITICAL` chats on a single line increase the risk of line flagging.

    Switch on `status` to surface chat and line health in your UI — the enum is the long-term contract. Each status carries a `doc_url` that deep-links to the relevant section of the Chat Health guide. To gate a send, act on the response rather than the status: a `403` is the authoritative answer.

    See the [Chat Health guide](/channel/imessage/guides/chats/chat-health) for what each status means and how to react.
    """

    doc_url: str
    """Deep-link to the relevant section of the Chat Health guide for this status."""

    status: Literal["HEALTHY", "AT_RISK", "CRITICAL", "OPTED_OUT"]
    """Current health bucket for the chat.

    See the [Chat Health guide](/channel/imessage/guides/chats/chat-health) for what
    each value means and how to react. `doc_url` deep-links to the relevant section.

    `OPTED_OUT` — the recipient sent `STOP`, `UNSUBSCRIBE`, `OPTOUT`, `CANCEL`,
    `END`, or `QUIT`. The keyword must be the whole trimmed message, never part of a
    longer one: `STOP` counts, `please stop` does not. Most keywords must match
    exactly, including case. `OPT OUT` is the exception — it matches in any casing,
    with or without the space or a hyphen, so `opt out`, `Opt-Out` and `optout` all
    count. It clears as soon as they reply again: any later message from them that
    is not itself an opt-out keyword opts them back in immediately — a reply in any
    conversation with you counts, the same way the block does.

    `OPTED_OUT` marks only the conversation the keyword arrived in. The block below
    is wider than the mark, so a conversation still reading `HEALTHY` can be blocked
    as well — gate on the `403`, not on the status. Group threads are never marked
    and are never blocked.

    Linq enforces this: while a recipient is opted out, every send to them is
    rejected with `403` (error code `2024`) before the message is queued, across
    every chat and every line on your account. Nothing is delivered, including a
    final courtesy message — to send one, set `override_optout: true` on that single
    request.
    """

    updated_at: datetime
    """When this status last changed."""


class Chat(BaseModel):
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

    health_status: HealthStatus
    """**[BETA]** Current health for a chat.

    Always present — chats start at `HEALTHY` and may shift based on engagement and
    delivery signals on the conversation. Many `AT_RISK` or `CRITICAL` chats on a
    single line increase the risk of line flagging.

    Switch on `status` to surface chat and line health in your UI — the enum is the
    long-term contract. Each status carries a `doc_url` that deep-links to the
    relevant section of the Chat Health guide. To gate a send, act on the response
    rather than the status: a `403` is the authoritative answer.

    See the [Chat Health guide](/channel/imessage/guides/chats/chat-health) for what
    each status means and how to react.
    """

    is_archived: bool
    """
    **DEPRECATED:** This field is deprecated and will be removed in a future API
    version.
    """

    is_group: bool
    """Whether this is a group chat"""

    updated_at: datetime
    """When the chat was last updated"""

    group_chat_icon: Optional[str] = None
    """URL of the group chat icon.

    Only set for group chats that have an icon; `null` otherwise.
    """

    service: Optional[ServiceType] = None
    """Messaging service type"""
