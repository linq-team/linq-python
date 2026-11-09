# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageUpdateStickerPlacementParams", "Placement"]


class MessageUpdateStickerPlacementParams(TypedDict, total=False):
    message_id: Required[Annotated[str, PropertyInfo(alias="messageId")]]

    placement: Required[Placement]
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
