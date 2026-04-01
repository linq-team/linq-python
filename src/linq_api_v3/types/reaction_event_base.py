# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.chat_handle import ChatHandle
from .shared.service_type import ServiceType
from .shared.reaction_type import ReactionType

__all__ = ["ReactionEventBase", "Sticker"]


class Sticker(BaseModel):
    """Sticker attachment details when reaction_type is "sticker".

    Null for non-sticker reactions.
    """

    file_name: Optional[str] = None
    """Filename of the sticker"""

    height: Optional[int] = None
    """Sticker image height in pixels"""

    mime_type: Optional[str] = None
    """MIME type of the sticker image"""

    url: Optional[str] = None
    """Presigned URL for downloading the sticker image (expires in 1 hour)."""

    width: Optional[int] = None
    """Sticker image width in pixels"""


class ReactionEventBase(BaseModel):
    is_from_me: bool
    """
    Whether this reaction was from the owner of the phone number (true) or from
    someone else (false)
    """

    reaction_type: ReactionType
    """Type of reaction.

    Standard iMessage tapbacks are love, like, dislike, laugh, emphasize, question.
    Custom emoji reactions have type "custom" with the actual emoji in the
    custom_emoji field. Sticker reactions have type "sticker" with sticker
    attachment details in the sticker field.
    """

    chat_id: Optional[str] = None
    """Chat identifier (UUID)"""

    custom_emoji: Optional[str] = None
    """The actual emoji when reaction_type is "custom". Null for standard tapbacks."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """DEPRECATED: Use from_handle instead.

    Phone number or email address of the person who added/removed the reaction.
    """

    from_handle: Optional[ChatHandle] = None
    """The person who added/removed the reaction as a full handle object"""

    message_id: Optional[str] = None
    """Message identifier (UUID) that the reaction was added to or removed from"""

    part_index: Optional[int] = None
    """Index of the message part that was reacted to (0-based)"""

    reacted_at: Optional[datetime] = None
    """When the reaction was added or removed"""

    service: Optional[ServiceType] = None
    """Messaging service type"""

    sticker: Optional[Sticker] = None
    """Sticker attachment details when reaction_type is "sticker".

    Null for non-sticker reactions.
    """
