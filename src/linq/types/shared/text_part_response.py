# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .reaction import Reaction
from ..._models import BaseModel
from .text_decoration import TextDecoration

__all__ = ["TextPartResponse", "Mention"]


class Mention(BaseModel):
    """
    One mention on a text part — who was mentioned, and which characters of `value` are
    the mention. A part carries one of these per mention, in the order they appear in the
    text, so a message naming two people has two entries.
    """

    handle: str
    """
    Address of the mentioned participant, exactly as the device recorded it — an
    E.164 phone number or an email address.
    """

    is_me: bool
    """Whether the mentioned participant is this line."""

    range: List[int]
    """
    Character range `[start, end)` in `value` highlighted as this mention.
    _Characters are measured as UTF-16 code units. Most characters count as 1; some
    emoji count as 2._
    """


class TextPartResponse(BaseModel):
    """A text message part"""

    reactions: Optional[List[Reaction]] = None
    """Reactions on this message part"""

    type: Literal["text"]
    """Indicates this is a text message part"""

    value: str
    """The text content"""

    mention: Optional[str] = None
    """DEPRECATED: Use `mentions` instead.

    Handle (E.164 phone number or Apple ID email) of the **first** mention on this
    part. A part may carry several mentions; this field shows only the first in
    `value` order, so it cannot be used to determine whether a given participant was
    mentioned. `null` when the part carries no mention.
    """

    mention_range: Optional[List[int]] = None
    """DEPRECATED: Use `mentions[].range` instead.

    Character range `[start, end)` in `value` highlighted as the **first** mention
    only. `null` when the range was omitted (the whole `value` is highlighted) or
    the part carries no mention. _Characters are measured as UTF-16 code units. Most
    characters count as 1; some emoji count as 2._
    """

    mentions: Optional[List[Mention]] = None
    """Every mention on this part, in the order they appear in `value`.

    `null` when the part carries no mention. A part can carry several mentions of
    different people — check `is_me` to tell whether this line was one of them.

    Only iMessage carries mentions. On a received message this is populated when the
    sender was on iMessage; SMS and RCS have no way to mark a mention, so a message
    from an SMS or RCS participant arrives as plain text with `mentions` null, even
    in a group where other participants are on iMessage.
    """

    text_decorations: Optional[List[TextDecoration]] = None
    """Text decorations applied to character ranges in the value"""
