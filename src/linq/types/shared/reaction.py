# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .chat_handle import ChatHandle
from .reaction_type import ReactionType

__all__ = ["Reaction", "Sticker"]


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


class Reaction(BaseModel):
    handle: ChatHandle

    is_me: bool
    """Whether this reaction is from the current user"""

    type: ReactionType
    """Type of reaction.

    Standard iMessage tapbacks are love, like, dislike, laugh, emphasize, question.
    Custom emoji reactions have type "custom" with the actual emoji in the
    custom_emoji field. Sticker reactions have type "sticker" with sticker
    attachment details in the sticker field.
    """

    custom_emoji: Optional[str] = None
    """Custom emoji if type is "custom", null otherwise"""

    sticker: Optional[Sticker] = None
    """Sticker attachment details when reaction_type is "sticker".

    Null for non-sticker reactions.
    """
