# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..reply_to import ReplyTo
from ..message_effect import MessageEffect
from ..shared.reaction import Reaction
from ..shared.chat_handle import ChatHandle
from ..shared.service_type import ServiceType
from ..shared.text_part_response import TextPartResponse
from ..shared.media_part_response import MediaPartResponse

__all__ = ["SentMessage", "Part", "PartLinkPartResponse"]


class PartLinkPartResponse(BaseModel):
    """A rich link preview part"""

    reactions: Optional[List[Reaction]] = None
    """Reactions on this message part"""

    type: Literal["link"]
    """Indicates this is a rich link preview part"""

    value: str
    """The URL"""


Part: TypeAlias = Union[TextPartResponse, MediaPartResponse, PartLinkPartResponse]


class SentMessage(BaseModel):
    """A message that was sent (used in CreateChat and SendMessage responses)"""

    id: str
    """Message identifier (UUID)"""

    delivery_status: Literal["pending", "queued", "sent", "delivered", "failed"]
    """Current delivery status of a message"""

    is_read: bool
    """Whether the message has been read"""

    parts: List[Part]
    """Message parts in order (text, media, and link)"""

    sent_at: datetime
    """When the message was sent"""

    delivered_at: Optional[datetime] = None
    """When the message was delivered"""

    effect: Optional[MessageEffect] = None
    """iMessage effect applied to a message (screen or bubble effect)"""

    from_handle: Optional[ChatHandle] = None
    """The sender of this message as a full handle object"""

    preferred_service: Optional[ServiceType] = None
    """Messaging service type"""

    reply_to: Optional[ReplyTo] = None
    """Indicates this message is a threaded reply to another message"""

    service: Optional[ServiceType] = None
    """Messaging service type"""
