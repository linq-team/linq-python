# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TextDecoration"]


class TextDecoration(TypedDict, total=False):
    range: Required[Iterable[int]]
    """
    Character range `[start, end)` in the `value` string where the decoration
    applies. `start` is inclusive, `end` is exclusive. _Characters are measured as
    UTF-16 code units. Most characters count as 1; some emoji count as 2._
    """

    animation: Literal["big", "small", "shake", "nod", "explode", "ripple", "bloom", "jitter"]
    """Animated text effect to apply. Mutually exclusive with `style`."""

    style: Literal["bold", "italic", "strikethrough", "underline"]
    """Text style to apply. Mutually exclusive with `animation`."""
