# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.chat_handle import ChatHandle
from .shared.service_type import ServiceType

__all__ = ["ChatSendVoicememoResponse", "VoiceMemo", "VoiceMemoChat", "VoiceMemoVoiceMemo"]


class VoiceMemoChat(BaseModel):
    id: str
    """Chat identifier"""

    handles: List[ChatHandle]
    """Chat participants"""

    is_active: bool
    """Whether the chat is active"""

    is_group: bool
    """Whether this is a group chat"""

    service: ServiceType
    """Messaging service type"""


class VoiceMemoVoiceMemo(BaseModel):
    id: str
    """Attachment identifier"""

    filename: str
    """Original filename"""

    mime_type: str
    """Audio MIME type"""

    size_bytes: int
    """File size in bytes"""

    url: str
    """CDN URL for downloading the voice memo"""

    duration_ms: Optional[int] = None
    """Duration in milliseconds"""


class VoiceMemo(BaseModel):
    id: str
    """Message identifier"""

    chat: VoiceMemoChat

    created_at: datetime
    """When the voice memo was created"""

    from_: str = FieldInfo(alias="from")
    """Sender phone number"""

    status: str
    """Current delivery status"""

    to: List[str]
    """Recipient handles (phone numbers or email addresses)"""

    voice_memo: VoiceMemoVoiceMemo

    service: Optional[ServiceType] = None
    """Messaging service type"""


class ChatSendVoicememoResponse(BaseModel):
    """Response for sending a voice memo to a chat"""

    voice_memo: VoiceMemo
