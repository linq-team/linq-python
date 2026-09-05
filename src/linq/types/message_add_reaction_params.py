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

    Either `url` or `attachment_id` must be provided when type is "sticker", but not
    both.
    """

    custom_emoji: str
    """Custom emoji string. Required when type is "custom"."""

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

    Unlike a media part, this does **not** accept an arbitrary host: reactions have
    no download step, so the image must already be stored. To send a sticker from
    elsewhere, upload it with `POST /v3/attachments` first and pass `attachment_id`.

    Either `url` or `attachment_id` must be provided when type is "sticker", but not
    both.
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
    """Size relative to the default, where 1 matches the size a sticker gets natively.

    Values outside 0.5–1.5 are clamped rather than rejected. The upper bound keeps a
    sticker within the size range iMessage itself displays: its own limit is larger,
    but that allowance assumes the transparent padding Apple's stickers carry, which
    a full-bleed image does not have.

    Scale is linear, so 1.5 is a little over twice the area.
    """

    x: float
    """Horizontal position on the target bubble, from -1 (far left) to 1 (far right).

    0 is centred.
    """

    y: float
    """Vertical position on the target bubble, from -1 (top) to 1 (bottom).

    0 is centred.
    """
