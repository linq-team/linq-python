# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .reply_to import ReplyTo
from .message_effect import MessageEffect
from .shared.reaction import Reaction
from .shared.chat_handle import ChatHandle
from .shared.service_type import ServiceType
from .shared.text_part_response import TextPartResponse
from .shared.media_part_response import MediaPartResponse

__all__ = ["Message", "Part", "PartLinkPartResponse"]


class PartLinkPartResponse(BaseModel):
    """A rich link preview part"""

    reactions: Optional[List[Reaction]] = None
    """Reactions on this message part"""

    type: Literal["link"]
    """Indicates this is a rich link preview part"""

    value: str
    """The URL"""


Part: TypeAlias = Union[TextPartResponse, MediaPartResponse, PartLinkPartResponse]


class Message(BaseModel):
    id: str
    """Unique identifier for the message"""

    chat_id: str
    """ID of the chat this message belongs to"""

    created_at: datetime
    """When the message was created"""

    is_delivered: bool
    """Whether the message has been delivered"""

    is_from_me: bool
    """Whether this message was sent by the authenticated user"""

    is_read: bool
    """Whether the message has been read"""

    updated_at: datetime
    """When the message was last updated"""

    delivered_at: Optional[datetime] = None
    """When the message was delivered"""

    effect: Optional[MessageEffect] = None
    """iMessage effect applied to a message (screen or bubble effect)"""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """DEPRECATED: Use from_handle instead. Phone number of the message sender."""

    from_handle: Optional[ChatHandle] = None
    """The sender of this message as a full handle object"""

    parts: Optional[List[Part]] = None
    """Message parts in order (text, media, and link)"""

    preferred_service: Optional[ServiceType] = None
    """Messaging service type"""

    read_at: Optional[datetime] = None
    """When the message was read"""

    reply_to: Optional[ReplyTo] = None
    """Indicates this message is a threaded reply to another message"""

    sent_at: Optional[datetime] = None
    """When the message was sent"""

    service: Optional[ServiceType] = None
    """Messaging service type"""
