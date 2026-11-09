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
    Custom tapbacks have type "custom": an emoji tapback carries the emoji in the
    custom_emoji field, and an image tapback carries the image in the sticker field.
    Sticker reactions have type "sticker" with sticker attachment details in the
    sticker field.
    """

    attachment_id: str
    """
    Reference to an image pre-uploaded via `POST /v3/attachments`. Valid when type
    is "sticker", or when adding a type "custom" reaction to make it an image
    tapback.

    Exactly one of `emoji`, `url` or `attachment_id` is required when type is
    "sticker".
    """

    custom_emoji: str
    """Custom emoji string.

    When adding a type "custom" reaction, provide exactly one of `custom_emoji`,
    `url` or `attachment_id`. To remove an emoji reaction, pass the same
    `custom_emoji`.

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

    `x` and `y` set where the sticker's centre lands, as a fraction of the target
    bubble's width and height:

    | Position            | `x` | `y` |
    | ------------------- | --- | --- |
    | Top-left corner     | 0   | 0   |
    | Top-right corner    | 1   | 0   |
    | Centre              | 0.5 | 0.5 |
    | Bottom-left corner  | 0   | 1   |
    | Bottom-right corner | 1   | 1   |

    Every field is independent and optional. Omit `x` and `y` and the sticker lands
    on the top-left corner.

    Position and size are relative to the target bubble, so a sticker keeps its
    place on the bubble on every device. Its size follows the bubble's width: the
    same sticker is drawn smaller on a bubble that a recipient's screen renders
    narrower than the sender's.
    """

    url: str
    """
    Linq attachment URL of the image — the `download_url` returned by
    `POST /v3/attachments`. Valid when type is "sticker", or when adding a type
    "custom" reaction to make it an image tapback.

    The image must already be stored with us. To use an image from elsewhere, upload
    it with `POST /v3/attachments` first and pass `attachment_id`.

    Exactly one of `emoji`, `url` or `attachment_id` is required when type is
    "sticker".
    """


class Placement(TypedDict, total=False):
    """Optional position, size and rotation of a sticker on the target
    bubble.

    Only valid when type is "sticker".

    `x` and `y` set where the sticker's centre lands, as a fraction of
    the target bubble's width and height:

    | Position | `x` | `y` |
    |---|---|---|
    | Top-left corner | 0 | 0 |
    | Top-right corner | 1 | 0 |
    | Centre | 0.5 | 0.5 |
    | Bottom-left corner | 0 | 1 |
    | Bottom-right corner | 1 | 1 |

    Every field is independent and optional. Omit `x` and `y` and the
    sticker lands on the top-left corner.

    Position and size are relative to the target bubble, so a sticker
    keeps its place on the bubble on every device. Its size follows the
    bubble's width: the same sticker is drawn smaller on a bubble that a
    recipient's screen renders narrower than the sender's.
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
    """
    Where the sticker's centre sits horizontally, as a fraction of the target
    bubble's width: 0 is its left edge, 0.5 its centre and 1 its right edge. Values
    outside -1–1 are clamped.

    Avoid negative values: a sticker left of a received bubble makes the recipient's
    device shift the whole message to fit it.
    """

    y: float
    """
    Where the sticker's centre sits vertically, as a fraction of the target bubble's
    height: 0 is its top edge, 0.5 its centre and 1 its bottom edge. Negative values
    place it above the bubble; `-0.3` sits just above the top edge. Values outside
    -1–1 are clamped.
    """
