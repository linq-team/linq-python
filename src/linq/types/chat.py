# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.chat_handle import ChatHandle
from .shared.service_type import ServiceType

__all__ = ["Chat"]


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

    is_archived: bool
    """Whether the chat is archived"""

    is_group: bool
    """Whether this is a group chat"""

    updated_at: datetime
    """When the chat was last updated"""

    service: Optional[ServiceType] = None
    """Messaging service type"""
