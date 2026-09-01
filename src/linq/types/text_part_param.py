# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .shared_params.text_decoration import TextDecoration

__all__ = ["TextPartParam"]


class TextPartParam(TypedDict, total=False):
    type: Required[Literal["text"]]
    """Indicates this is a text message part"""

    value: Required[str]
    """The text content of the message.

    This value is sent as-is with no parsing or transformation — Markdown syntax
    will be delivered as plain text. Use `text_decorations` to apply inline
    formatting and animations (iMessage only).
    """

    mention: str
    """Mention a chat participant.

    Group chats only — sending a mention to a direct chat is rejected with `409` /
    `2023`. The chat's service is not a constraint: a mention is accepted in any
    group, including one with SMS/RCS participants.

    Set to their handle — E.164 phone number or Apple ID email. `value` is the
    display text; use the bare name (`"Juan"`, not `"@Juan"`). By default the entire
    `value` renders as the mention; use `mention_range` to highlight only part of
    it.

    Rendering is per recipient, not per message. iMessage recipients see the mention
    highlighted and are notified even if they have muted the chat. SMS and RCS
    recipients receive the same message as plain text — no highlight, and no mute
    override. One send, two experiences.
    """

    mention_range: Iterable[int]
    """
    Optional character range `[start, end)` in `value` that renders as the `mention`
    highlight (e.g. just the name in `"Hey Kevin, can you look at this?"`). Requires
    `mention`. Without it, the entire `value` is highlighted. `start` is inclusive,
    `end` is exclusive. _Characters are measured as UTF-16 code units. Most
    characters count as 1; some emoji count as 2._

    Applies to iMessage recipients only, matching `mention` — SMS and RCS recipients
    receive the text with no highlight.
    """

    text_decorations: Iterable[TextDecoration]
    """
    Optional array of text decorations applied to character ranges in the `value`
    field (iMessage only).

    Each decoration specifies a character range `[start, end)` and exactly one of
    `style` or `animation`.

    **Styles:** `bold`, `italic`, `strikethrough`, `underline` **Animations:**
    `big`, `small`, `shake`, `nod`, `explode`, `ripple`, `bloom`, `jitter`

    Style ranges may overlap (e.g. bold + italic on the same text), but animation
    ranges must not overlap with other animations or styles.

    _Characters are measured as UTF-16 code units. Most characters count as 1; some
    emoji count as 2._

    **Note:** decorations render per recipient, not per message. In a group
    containing both iMessage and SMS/RCS participants, iMessage recipients see the
    decorations and SMS/RCS recipients receive the same message as plain text.
    """
