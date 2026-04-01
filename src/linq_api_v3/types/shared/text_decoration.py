# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TextDecoration"]


class TextDecoration(BaseModel):
    range: List[int]
    """
    Character range `[start, end)` in the `value` string where the decoration
    applies. `start` is inclusive, `end` is exclusive. _Characters are measured as
    UTF-16 code units. Most characters count as 1; some emoji count as 2._
    """

    animation: Optional[Literal["big", "small", "shake", "nod", "explode", "ripple", "bloom", "jitter"]] = None
    """Animated text effect to apply. Mutually exclusive with `style`."""

    style: Optional[Literal["bold", "italic", "strikethrough", "underline"]] = None
    """Text style to apply. Mutually exclusive with `animation`."""
