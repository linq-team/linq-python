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

    Every field is independent and optional — omit the object entirely, or any field
    within it, to keep the default (centred, default size, unrotated).
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
