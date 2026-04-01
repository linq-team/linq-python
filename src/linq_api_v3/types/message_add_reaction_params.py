# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .shared.reaction_type import ReactionType

__all__ = ["MessageAddReactionParams"]


class MessageAddReactionParams(TypedDict, total=False):
    operation: Required[Literal["add", "remove"]]
    """Whether to add or remove the reaction"""

    type: Required[ReactionType]
    """Type of reaction.

    Standard iMessage tapbacks are love, like, dislike, laugh, emphasize, question.
    Custom emoji reactions have type "custom" with the actual emoji in the
    custom_emoji field. Sticker reactions have type "sticker" with sticker
    attachment details in the sticker field.
    """

    custom_emoji: str
    """Custom emoji string. Required when type is "custom"."""

    part_index: int
    """
    Optional index of the message part to react to. If not provided, reacts to the
    entire message (part 0).
    """
