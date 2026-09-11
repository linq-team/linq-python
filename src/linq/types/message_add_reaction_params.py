# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .shared.reaction_type import ReactionType

__all__ = ["MessageAddReactionParams", "Placement"]


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

    attachment_id: str
    """
    Reference to a sticker image pre-uploaded via `POST /v3/attachments`. Only valid
    when type is "sticker".

    Exactly one of `emoji`, `url` or `attachment_id` is required when type is
    "sticker".
    """

    custom_emoji: str
    """Custom emoji string. Required when type is "custom".

    This is a **tapback** — the emoji sits in the tapback bubble on the corner of
    the message. To peel an emoji onto the message as a draggable sticker instead,
    use type "sticker" with `emoji`.
    """

    emoji: str
    """A single emoji to peel onto the message as a sticker.

    Only valid when type is "sticker".

    Exactly one of `emoji`, `url` or `attachment_id` is required when type is
    "sticker".

    Not to be confused with `custom_emoji`, which produces a tapback.
    """

    part_index: int
    """
    Optional index of the message part to react to. If not provided, reacts to the
    entire message (part 0).
    """

    placement: Placement
    """Optional position, size and rotation of a sticker on the target bubble.

    Only valid when type is "sticker".

    Every field is independent and optional — omit the object entirely, or any field
    within it, to keep the default (centred, default size, unrotated).
    """

    url: str
    """
    Linq attachment URL of the sticker image — the `download_url` returned by
    `POST /v3/attachments`. Only valid when type is "sticker".

    The image must already be stored with us. To send a sticker from elsewhere,
    upload it with `POST /v3/attachments` first and pass `attachment_id`.

    Exactly one of `emoji`, `url` or `attachment_id` is required when type is
    "sticker".
    """


class Placement(TypedDict, total=False):
    """Optional position, size and rotation of a sticker on the target
    bubble.

    Only valid when type is "sticker".

    Every field is independent and optional — omit the object entirely,
    or any field within it, to keep the default (centred, default size,
    unrotated).
    """

    rotation: float
    """Clockwise rotation in degrees."""

    scale: float
    """How large the sticker is drawn.

    Omit it for the default size — equivalent to `1` for an image, or `0.5` for an
    emoji.

    Values outside 0.05–2.5 are clamped rather than rejected.

    Scale is linear, so 2.5 is a little over six times the area.
    """

    x: float
    """Horizontal position on the target bubble, from -1 (far left) to 1 (far right).

    0 is centred.
    """

    y: float
    """Vertical position on the target bubble, from -1 (top) to 1 (bottom).

    0 is centred.
    """
