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
    """
    The image when reaction_type is "sticker", or when reaction_type is "custom" and
    the tapback is an image. Null otherwise.
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
    Custom tapbacks have type "custom": an emoji tapback carries the emoji in the
    custom_emoji field, and an image tapback carries the image in the sticker field.
    Sticker reactions have type "sticker" with sticker attachment details in the
    sticker field.
    """

    chat_id: Optional[str] = None
    """Chat identifier (UUID)"""

    custom_emoji: Optional[str] = None
    """The actual emoji when reaction_type is "custom" and the tapback is an emoji.

    Null otherwise.
    """

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

    reaction_id: Optional[str] = None
    """
    Identifier for this reaction, matching `id` on the message's `reactions`.
    Changing a tapback keeps the same id, and `reaction.removed` carries the id of
    the reaction it removed. Pass it to
    `PATCH /v3/messages/{messageId}/reactions/{reactionId}` to move a sticker.
    Stickers stack, so this is what distinguishes one sticker from another on the
    same message.
    """

    service: Optional[ServiceType] = None
    """Messaging service type.

    Where this names the transport a message used, it is per-message: a chat's own
    `service` can differ from a message in it, and Apple can downgrade an individual
    message.
    """

    sticker: Optional[Sticker] = None
    """
    The image when reaction_type is "sticker", or when reaction_type is "custom" and
    the tapback is an image. Null otherwise.
    """
