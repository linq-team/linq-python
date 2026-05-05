# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .chats.sent_message import SentMessage
from .shared.chat_handle import ChatHandle
from .shared.service_type import ServiceType

__all__ = ["ChatCreateResponse", "Chat", "ChatHealthStatus", "ChatHealthScore"]


class ChatHealthStatus(BaseModel):
    """**[BETA]** Current health for a chat.

    Always present — chats start at `healthy` and may shift based on engagement and delivery signals on the conversation. Many `at_risk` or `critical` chats on a single line increase the risk of line flagging.

    Switch on `status` to gate sends or surface line health in your UI — the enum is the long-term contract. Each status carries a `doc_url` that deep-links to the relevant section of the Chat Health guide.

    See the [Chat Health guide](/guides/chats/chat-health) for what each status means and how to react.
    """

    doc_url: str
    """Deep-link to the relevant section of the Chat Health guide for this status."""

    status: Literal["healthy", "at_risk", "critical", "opted_out"]
    """Current health bucket for the chat.

    See the [Chat Health guide](/guides/chats/chat-health) for what each value means
    and how to react. `doc_url` deep-links to the relevant section.
    """

    updated_at: datetime
    """When this status last changed."""


class ChatHealthScore(BaseModel):
    """**[BETA — DEPRECATED]** Legacy health assessment for a chat.

    Use `health_status` instead — it's the long-term contract.

    Higher `score` is healthier. `null` when a score isn't available yet. Low health scores across multiple chats increase risk of line flagging. Scoring model may change during beta. This field will be removed in a future release; partners on new integrations should switch on `health_status.status`.

    See the [Chat Health guide](/guides/chats/chat-health) for what we score on and how it relates to line health.
    """

    reason: str
    """Short summary of what's affecting the score. Empty when the score is 100."""

    score: int
    """Health score from 0 to 100. Higher is healthier."""

    updated_at: datetime
    """When this health score was last computed."""


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

    Always present — chats start at `healthy` and may shift based on engagement and
    delivery signals on the conversation. Many `at_risk` or `critical` chats on a
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

    health_score: Optional[ChatHealthScore] = None
    """**[BETA — DEPRECATED]** Legacy health assessment for a chat.

    Use `health_status` instead — it's the long-term contract.

    Higher `score` is healthier. `null` when a score isn't available yet. Low health
    scores across multiple chats increase risk of line flagging. Scoring model may
    change during beta. This field will be removed in a future release; partners on
    new integrations should switch on `health_status.status`.

    See the [Chat Health guide](/guides/chats/chat-health) for what we score on and
    how it relates to line health.
    """


class ChatCreateResponse(BaseModel):
    """Response for creating a new chat with an initial message"""

    chat: Chat
