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

    **Note:** Text decorations only render for iMessage recipients. For SMS/RCS,
    text decorations are not applied.
    """
