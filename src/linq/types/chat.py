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

    Always present — chats start at `healthy` and may shift based on engagement and
    delivery signals on the conversation. Many `at_risk` or `critical` chats on a
    single line increase the risk of line flagging.

    Switch on `status` to gate sends or surface line health in your UI — the enum is
    the long-term contract. Each status carries a `doc_url` that deep-links to the
    relevant section of the Chat Health guide.

    See the [Chat Health guide](/guides/chats/chat-health) for what each status
    means and how to react.
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

    service: Optional[ServiceType] = None
    """Messaging service type"""
