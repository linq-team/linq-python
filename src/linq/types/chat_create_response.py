# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .chats.sent_message import SentMessage
from .shared.chat_handle import ChatHandle
from .shared.service_type import ServiceType

__all__ = ["ChatCreateResponse", "Chat", "ChatHealthStatus"]


class ChatHealthStatus(BaseModel):
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


class Chat(BaseModel):
    id: str
    """Unique identifier for the created chat (UUID)"""

    display_name: Optional[str] = None
    """Display name for the chat.

    Defaults to a comma-separated list of recipient handles. Can be updated for
    group chats.
    """

    handles: List[ChatHandle]
    """List of participants in the chat.

    Always contains at least two handles (your phone number and the other
    participant).
    """

    health_status: ChatHealthStatus
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

    message: SentMessage
    """A message that was sent (used in CreateChat and SendMessage responses)"""

    service: ServiceType
    """Messaging service type"""


class ChatCreateResponse(BaseModel):
    """Response for creating a new chat with an initial message"""

    chat: Chat
