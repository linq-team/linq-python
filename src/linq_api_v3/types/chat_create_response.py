# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .chats.sent_message import SentMessage
from .shared.chat_handle import ChatHandle
from .shared.service_type import ServiceType

__all__ = ["ChatCreateResponse", "Chat"]


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

    is_group: bool
    """Whether this is a group chat"""

    message: SentMessage
    """A message that was sent (used in CreateChat and SendMessage responses)"""

    service: ServiceType
    """Messaging service type"""


class ChatCreateResponse(BaseModel):
    """Response for creating a new chat with an initial message"""

    chat: Chat
